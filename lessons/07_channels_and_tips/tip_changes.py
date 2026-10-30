# Lesson 07, part 2: when to change tips.
#
# The job: columns 1-3 hold 24 different samples, 50 uL each. Add 100 uL of the
# same diluent from the trough to every sample: 8 channels, one column per move.
# The rule: a tip that touched a sample must not go into anything else, including
# the trough that every column shares. PyLabRobot doesn't check for contamination,
# so the rule only exists if you write it in the code.

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

sample_volume_ul = 50
diluent_volume_ul = 100
tips_touch_liquid = False  # False = the tips dispense from above and stay clean
num_sample_columns = 6
trough_volume_ul = 5500  # (should change based on the number of columns) 6 columns * 8 channels * 100 uL + some extra

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
    trough = hamilton_1_trough_60mL_Vb(name="diluent_trough")
    trough_carrier[0] = trough
    deck.assign_child_resource(trough_carrier, rails=18)

    plate_carrier = PLT_CAR_L5AC_A00(name="plate_carrier")
    plate = cor_96_wellplate_360uL_Fb(name="sample_plate")
    plate_carrier[0] = plate
    deck.assign_child_resource(plate_carrier, rails=19)

    trough.tracker.set_volume(trough_volume_ul)
    for well in plate["A1:H"+str(num_sample_columns)]:  # the 48 samples; the rest of the plate stays empty
        well.tracker.set_volume(sample_volume_ul)

    tips_used = 0
    if tips_touch_liquid:
        # Your protocol 1: fresh tips for each column, discarded before they can go back to the trough.
        for column in range(1, num_sample_columns + 1):
            column_range = "A" + str(column) + ":H" + str(column)  # e.g. "A2:H2"
            await lh.pick_up_tips(tip_rack[column_range])  # tip column 1 for plate column 1, and so on
            tips_used = tips_used + 8
            await lh.aspirate([trough] * 8, vols=[diluent_volume_ul] * 8)
            await lh.dispense(plate[column_range], vols=[diluent_volume_ul] * 8)
            await lh.discard_tips()
    else:
        # Your protocol 2: the tips never touch a sample, so one set does all 3 columns.
        await lh.pick_up_tips(tip_rack["A1:H1"])
        tips_used = tips_used + 8
        for column in range(1, num_sample_columns + 1):
            column_range = "A" + str(column) + ":H" + str(column)
            await lh.aspirate([trough] * 8, vols=[diluent_volume_ul] * 8)
            await lh.dispense(plate[column_range], vols=[diluent_volume_ul] * 8)
        await lh.discard_tips()

    print("\nTips used:", tips_used)
    print("Diluent left in the trough:", trough.tracker.get_used_volume(), "uL")


asyncio.run(main())
