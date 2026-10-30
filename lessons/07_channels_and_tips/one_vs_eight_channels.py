# Lesson 07, part 1: one channel vs 8 channels.
#
# The job: 100 uL of diluent from the trough into every well of one column.
#   Single channel (column 2): 1 tip, trough -> A2, trough -> B2, ... trough -> H2, discard.
#   8 channels     (column 3): 8 tips, trough -> A3-H3 in one move, discard.
# The wells start empty and all get the same diluent, so a tip never touches
# anything that could contaminate it: no tip change is needed within a column.
#
# Deck (same as lesson 06, part 3): tips at rail 12, trough at rail 18, plate at rail 19.

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

diluent_volume_ul = 100  # per well
# 2.5 columns x 8 wells x 100 uL = 2000 uL, plus about 455 uL the tips can't reach
# (trough dead volume, lesson 06 part 1), plus a margin.
trough_volume_ul = 5000


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
    plate = cor_96_wellplate_360uL_Fb(name="dilution_plate")
    plate_carrier[0] = plate
    deck.assign_child_resource(plate_carrier, rails=19)

    trough.tracker.set_volume(trough_volume_ul)  # pour the diluent in

    # Each command takes lists: one entry per channel. One channel -> lists of 1.
    print("\n===== Single channel: column 2 =====")
    await lh.pick_up_tips(tip_rack["A1"])
    for well in plate["A2:H2"]:  # one well at a time, back to the trough each time
        await lh.aspirate([trough], vols=[diluent_volume_ul])
        await lh.dispense([well], vols=[diluent_volume_ul])
    await lh.discard_tips()  # into the trash at rail 32, not back in the rack

    # Eight channels -> lists of 8. The channels are 9 mm apart, the same as
    # the row spacing, so 8 tips line up with one column (A-H).
    print("\n===== 8 channels: column 3 =====")
    await lh.pick_up_tips(tip_rack["A2:H2"])  # tip column 2: tip A1 is already used
    await lh.aspirate([trough] * 8, vols=[diluent_volume_ul] * 8)
    await lh.dispense(plate["A3:H3"], vols=[diluent_volume_ul] * 8)
    await lh.discard_tips()

    print("\n===== 4 channels: A4-D4 =====")
    await lh.pick_up_tips(tip_rack["A3:D3"])  # tip column 3: tip A1 and column 2 is already used 
    await lh.aspirate([trough] * 4, vols=[diluent_volume_ul] * 4)
    await lh.dispense(plate["A4:D4"], vols=[diluent_volume_ul] * 4)
    await lh.discard_tips()

    print("\nDiluent left in the trough:", trough.tracker.get_used_volume(), "uL")

asyncio.run(main())
