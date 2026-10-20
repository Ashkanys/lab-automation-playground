import asyncio

from pylabrobot.liquid_handling import LiquidHandler
from pylabrobot.liquid_handling.backends import LiquidHandlerChatterboxBackend
from pylabrobot.visualizer.visualizer import Visualizer

from pylabrobot.resources.hamilton import STARLetDeck
from pylabrobot.resources import (
    TIP_CAR_480_A00,
    PLT_CAR_L5AC_A00,
    cor_96_wellplate_360uL_Fb,
    hamilton_96_tiprack_300uL_filter,
    set_tip_tracking,
    set_volume_tracking,
)


async def main():
    # Turn on state tracking so the Visualizer can follow tips/liquid.
    set_tip_tracking(True)
    set_volume_tracking(True)

    # Software-only Hamilton STARlet setup.
    deck = STARLetDeck()

    lh = LiquidHandler(
        backend=LiquidHandlerChatterboxBackend(),
        deck=deck,
    )

    await lh.setup()

    # Start browser Visualizer.
    vis = Visualizer(resource=lh)
    await vis.setup()

    # Add a tip carrier and rack.
    tip_carrier = TIP_CAR_480_A00(name="tip_carrier")

    tip_rack = hamilton_96_tiprack_300uL_filter(
        name="tips_01",
        with_tips=False,
    )

    tip_carrier[0] = tip_rack
    deck.assign_child_resource(tip_carrier, rails=15)

    tip_rack.fill()

    # Add two plates.
    plate_carrier = PLT_CAR_L5AC_A00(name="plate_carrier")

    source_plate = cor_96_wellplate_360uL_Fb(name="source_plate")
    destination_plate = cor_96_wellplate_360uL_Fb(name="destination_plate")

    plate_carrier[0] = source_plate
    plate_carrier[1] = destination_plate

    deck.assign_child_resource(plate_carrier, rails=8)

    # Give the source plate some liquid.
    source_plate.set_well_volumes([200] * 96)
    destination_plate.set_well_volumes([0] * 96)

    print("\nOpen this in your browser:")
    print("http://127.0.0.1:1337\n")

    # Give yourself a few seconds to open the browser.
    await asyncio.sleep(5)

    # Simulate one transfer.
    transfer_volume_ul = 150
    
    await lh.pick_up_tips(tip_rack["A2"])
    await asyncio.sleep(1)

    await lh.aspirate(source_plate["A2"], vols=[transfer_volume_ul])
    await asyncio.sleep(1)

    await lh.dispense(destination_plate["A2"], vols=[transfer_volume_ul])
    await asyncio.sleep(1)

    await lh.return_tips()
    await asyncio.sleep(1)

    # Keep the visualizer alive until you are finished looking at it.
    await asyncio.to_thread(
        input,
        "\nTransfer finished. Press Enter to close the Visualizer..."
    )

    await vis.stop()


asyncio.run(main())