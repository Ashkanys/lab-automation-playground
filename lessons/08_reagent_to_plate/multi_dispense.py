# Lesson 08, part 1: one aspiration per column vs multi-dispense.
#
# The job: 50 uL of reagent from the trough into all 96 wells, 8 channels, 300 uL tips.
#   Plate 1: one aspiration per column -> 12 aspirations.
#   Plate 2: aspirate for 5 columns + extra, dispense 5 times, extra back to the trough
#            -> 3 aspirations (5 + 5 + 2 columns).
# Empty wells, dispensed from above: the tips only touch clean reagent (lesson 07).

import asyncio

from pylabrobot.liquid_handling import LiquidHandler
from pylabrobot.liquid_handling.backends import LiquidHandlerChatterboxBackend
from pylabrobot.resources.hamilton import STARLetDeck
from pylabrobot.resources import (
    TIP_CAR_480_A00,
    Trough_CAR_5R60_A00,
    PLT_CAR_L5AC_A00,
    hamilton_96_tiprack_300uL_filter,
    hamilton_1_trough_60mL_Vb,
    cor_96_wellplate_360uL_Fb,
    set_tip_tracking,
    set_volume_tracking,
)

reagent_volume_ul = 50  # per well
extra_volume_ul = 20  # aspirated on top and never dispensed into a well (example value)
trough_volume_ul = 11000  # 2 plates x 96 x 50 uL = 9600 uL + ~455 uL dead volume + margin
# Multi-dispense: the columns each aspiration fills. 5 x 50 + 20 = 270 uL, under the 300 uL tip.
column_groups = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12]]
tip_nominal_volume_ul = 300

for group in column_groups:
    # One aspiration for every column in the group, plus the extra.
    aspirate_volume_ul = len(group) * reagent_volume_ul + extra_volume_ul
    if aspirate_volume_ul > tip_nominal_volume_ul:
        raise ValueError(f"Cannot aspirate {aspirate_volume_ul} uL into a {tip_nominal_volume_ul} uL tip.")


async def main():
    set_tip_tracking(True)
    set_volume_tracking(True)

    deck = STARLetDeck()
    lh = LiquidHandler(backend=LiquidHandlerChatterboxBackend(), deck=deck)
    await lh.setup()

    tip_carrier = TIP_CAR_480_A00(name="tip_carrier")
    tip_rack = hamilton_96_tiprack_300uL_filter(name="tips_01")
    tip_carrier[0] = tip_rack
    deck.assign_child_resource(tip_carrier, rails=12)

    trough_carrier = Trough_CAR_5R60_A00(name="trough_carrier")
    trough = hamilton_1_trough_60mL_Vb(name="reagent_trough")
    trough_carrier[0] = trough
    deck.assign_child_resource(trough_carrier, rails=18)

    plate_carrier = PLT_CAR_L5AC_A00(name="plate_carrier")
    plate_1 = cor_96_wellplate_360uL_Fb(name="plate_1")
    plate_2 = cor_96_wellplate_360uL_Fb(name="plate_2")
    plate_carrier[0] = plate_1  # front slot
    plate_carrier[1] = plate_2  # the slot behind it
    deck.assign_child_resource(plate_carrier, rails=19)

    trough.tracker.set_volume(trough_volume_ul)


    print("\n===== Plate 1: one aspiration per column =====")
    plate_1_aspirations = 0
    await lh.pick_up_tips(tip_rack["A1:H1"])
    for column in range(1, 13):
        column_range = "A" + str(column) + ":H" + str(column)
        await lh.aspirate([trough] * 8, vols=[reagent_volume_ul] * 8)
        plate_1_aspirations = plate_1_aspirations + 1
        await lh.dispense(plate_1[column_range], vols=[reagent_volume_ul] * 8)
    await lh.discard_tips()

    print("\n===== Plate 2: multi-dispense =====")
    plate_2_aspirations = 0
    await lh.pick_up_tips(tip_rack["A2:H2"])
    for group in column_groups:
        # One aspiration for every column in the group, plus the extra.
        aspirate_volume_ul = len(group) * reagent_volume_ul + extra_volume_ul
        await lh.aspirate([trough] * 8, vols=[aspirate_volume_ul] * 8)
        plate_2_aspirations = plate_2_aspirations + 1
        for column in group:  # several dispenses from that one aspiration
            column_range = "A" + str(column) + ":H" + str(column)
            await lh.dispense(plate_2[column_range], vols=[reagent_volume_ul] * 8)
        await lh.dispense([trough] * 8, vols=[extra_volume_ul] * 8)  # the extra goes back
    await lh.discard_tips()

    print("\nPlate 1 aspirations:", plate_1_aspirations)
    print("Plate 2 aspirations:", plate_2_aspirations)
    print("Reagent left in the trough:", trough.tracker.get_used_volume(), "uL")


asyncio.run(main())
