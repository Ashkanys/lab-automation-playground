# Lesson 06, part 2: the standard plate footprint (ANSI/SLAS).
#
# At the bench: almost any plate fits any plate reader, incubator stacker or
# plate holder, whatever the brand. That's thanks to a standard (ANSI/SLAS,
# once called SBS) that fixes the outside size of a plate: 127.76 x 85.48 mm.
# A robot depends on it too: it doesn't look at the plate, it moves the tip to
# coordinates worked out from the labware definition.

from pylabrobot.resources import (
    cor_96_wellplate_360uL_Fb,
    biorad_384_wellplate_50uL_Vb,
    thermo_AB_96_wellplate_300ul_Vb_MicroAmp,
)

slas_length_mm = 127.76  # left to right (x)
slas_width_mm = 85.48  # front to back (y)

plates = {
    "Corning 96 (cell plate)": cor_96_wellplate_360uL_Fb(name="cell_plate"),
    "Bio-Rad 384 (V-bottom)": biorad_384_wellplate_50uL_Vb(name="plate_384"),
    "MicroAmp 96 (PCR plate)": thermo_AB_96_wellplate_300ul_Vb_MicroAmp(name="pcr_plate"),
}

for label, plate in plates.items():
    # How far is this plate from the standard footprint, in each direction?
    off_x_mm = plate.get_size_x() - slas_length_mm
    off_y_mm = plate.get_size_y() - slas_width_mm

    # Well spacing ("pitch"): the distance from A1 to A2, like measuring with a ruler.
    # .location is where a well sits on the plate, in mm from the plate's corner.
    pitch_mm = plate.get_well("A2").location.x - plate.get_well("A1").location.x
    pitch_y_mm = plate.get_well("A1").location.y - plate.get_well("B1").location.y # row A is at the back (larger y), so A1 - B1

    print(label)
    print("  wells:", plate.num_items, "| pitch:", round(pitch_mm, 2), "mm and, pitch_y:", round(pitch_y_mm, 2), "mm")
    print("  size:", plate.get_size_x(), "x", plate.get_size_y(), "mm")
    print("  off the standard by:", round(off_x_mm, 2), "x", round(off_y_mm, 2), "mm")
