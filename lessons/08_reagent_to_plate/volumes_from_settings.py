# Lesson 08, part 2: every volume worked out from a few settings.
#
# The job: part 1's multi-dispense on 2 plates, with one set of tips for both
# (the tips only touch clean reagent, so they can stay on).
# The extra is now split by what it fixes (part 1 NOTES, point 2):
#   pre-dispense: back to the trough straight after aspirating, so the first well isn't short
#   residual:     stays in the tips so the last well isn't short, then goes back too
# Two checks run before the robot moves: the tip volume and the trough volume.

import asyncio

from pylabrobot.visualizer.visualizer import Visualizer
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

# Settings: the only numbers you type. Everything else is worked out from them.
num_plates = 2
reagent_volume_ul = 50  # per well
columns_per_aspiration = 5
pre_dispense_ul = 10  # example values: together they are part 1's 20 uL extra
residual_ul = 10
tip_nominal_volume_ul = 300
trough_dead_volume_ul = 455  # 60 mL trough, tip 2 mm above the bottom (lesson 06)
trough_volume_ul = 11000  # what the operator pours in
pause_per_column_s = 0.5  # delay between columns

# Split the 12 columns into groups: [1-5], [6-10], [11, 12] for 5 per aspiration.
column_groups = []
current_group = []
for column in range(1, 13):
    current_group.append(column)
    if len(current_group) == columns_per_aspiration:  # full: start the next group
        column_groups.append(current_group)
        current_group = []
if len(current_group) > 0:  # the last group can be shorter
    column_groups.append(current_group)

# Check 1 (from part 1): every aspiration fits in the tip.
extra_ul = pre_dispense_ul + residual_ul
for group in column_groups:
    aspirate_volume_ul = len(group) * reagent_volume_ul + extra_ul
    if aspirate_volume_ul > tip_nominal_volume_ul:
        raise ValueError(f"Cannot aspirate {aspirate_volume_ul} uL into a {tip_nominal_volume_ul} uL tip.")

# Check 2: enough reagent in the trough. The extra comes back after every aspiration,
# so it counts once, but for all 8 tips: at the last aspiration they hold it at the same time.
trough_needed_ul = num_plates * 96 * reagent_volume_ul + 8 * extra_ul + trough_dead_volume_ul
if trough_volume_ul < trough_needed_ul:
    raise ValueError(f"The trough needs at least {trough_needed_ul} uL but has {trough_volume_ul} uL.")


async def main():
    set_tip_tracking(True)
    set_volume_tracking(True)

    deck = STARLetDeck()
    lh = LiquidHandler(backend=LiquidHandlerChatterboxBackend(), deck=deck)
    await lh.setup()

    # Dark blue: 50 uL fills only 14% of a well, too pale to see in the GIF in the default amber.
    vis = Visualizer(resource=lh, liquid_color="000080")
    await vis.setup()

    tip_carrier = TIP_CAR_480_A00(name="tip_carrier")
    tip_rack = hamilton_96_tiprack_300uL_filter(name="tips_01")
    tip_carrier[0] = tip_rack
    deck.assign_child_resource(tip_carrier, rails=12)

    trough_carrier = Trough_CAR_5R60_A00(name="trough_carrier")
    trough = hamilton_1_trough_60mL_Vb(name="reagent_trough")
    trough_carrier[0] = trough
    deck.assign_child_resource(trough_carrier, rails=18)
    trough.tracker.set_volume(trough_volume_ul)

    plate_carrier = PLT_CAR_L5AC_A00(name="plate_carrier")
    plates = []
    for slot in range(num_plates):  # slot 0 is the front slot
        plate = cor_96_wellplate_360uL_Fb(name="plate_" + str(slot + 1))
        plate_carrier[slot] = plate
        plates.append(plate)
    deck.assign_child_resource(plate_carrier, rails=19)

    await asyncio.to_thread(input,
        "\nOpen http://127.0.0.1:1337 and start recording, then press Enter to run..."
    )

    await lh.pick_up_tips(tip_rack["A1:H1"])
    await asyncio.sleep(pause_per_column_s)
    for plate in plates:
        for group in column_groups:
            aspirate_volume_ul = len(group) * reagent_volume_ul + extra_ul
            await lh.aspirate([trough] * 8, vols=[aspirate_volume_ul] * 8)
            await lh.dispense([trough] * 8, vols=[pre_dispense_ul] * 8)  # pre-dispense
            await asyncio.sleep(pause_per_column_s)
            for column in group:
                column_range = "A" + str(column) + ":H" + str(column)
                await lh.dispense(plate[column_range], vols=[reagent_volume_ul] * 8)
                await asyncio.sleep(pause_per_column_s)
            await lh.dispense([trough] * 8, vols=[residual_ul] * 8)  # residual goes back
            await asyncio.sleep(pause_per_column_s)
    await lh.discard_tips()

    # Summary last, so it isn't buried under the robot's command log.
    print("\nColumn groups:", column_groups)
    print("Trough needs", trough_needed_ul, "uL, has", trough_volume_ul, "uL")
    print("Aspirations:", num_plates * len(column_groups))
    print("Reagent left in the trough:", trough.tracker.get_used_volume(), "uL")

    # Keep the Visualizer's server running: the browser needs it to build the GIF.
    await asyncio.to_thread(input,
          "\nRun finished. Save the GIF and PNG, then press Enter to close..."
    )
    await vis.stop()

asyncio.run(main())
