# Lesson 06, part 1: well shapes and dead volume.
#
# At the bench: the tip can't reach the very bottom of a well or trough, so
# whatever sits below its lowest point stays behind. How much that is depends
# on the shape of the bottom.
#
# PyLabRobot stores a height -> volume curve for each container (measured by
# whoever defined that labware), so we can ask the labware directly.

from pylabrobot.resources import (
    cor_96_wellplate_360uL_Fb,
    thermo_AB_96_wellplate_300ul_Vb_MicroAmp,
    hamilton_1_trough_60mL_Vb,
)

tip_clearance_mm = 2  # the tip stops this far above the bottom, so it never hits the plastic

# One container of each kind. For the plates we only need one well, A1.
flat_well = cor_96_wellplate_360uL_Fb(name="cell_plate").get_well("A1")
v_well = thermo_AB_96_wellplate_300ul_Vb_MicroAmp(name="pcr_plate").get_well("A1")
trough = hamilton_1_trough_60mL_Vb(name="reagent_trough")

containers = {
    "flat-bottom well (Corning 360 uL)": flat_well,
    "V-bottom well (MicroAmp PCR plate)": v_well,
    "V-bottom trough (Hamilton 60 mL)": trough,
}

for label, container in containers.items():
    # Ask the labware: how much liquid fills it up to the tip's lowest point?
    dead_volume_ul = container.compute_volume_from_height(tip_clearance_mm)
    print(label, "->", round(dead_volume_ul, 1), "uL left below the tip")

usable_volume_ul = 200 - flat_well.compute_volume_from_height(tip_clearance_mm)
print("Usable volume in flat well if we had 200uL to start with:", round(usable_volume_ul, 1), "uL")
