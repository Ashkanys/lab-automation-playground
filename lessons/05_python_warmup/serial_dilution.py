# Lesson 05, part 4: a serial dilution table, built from parts 1-3.
#
# The bench protocol for row A:
#   0. Make 200 uL of 100 uM top concentration from the 10 mM stock.
#   1. Put that 200 uL in A1, and 100 uL of diluent in each of A2-A12.
#   2. Move 100 uL from A1 to A2 and mix, then A2 to A3, and so on up to A11.
#   3. Take 100 uL out of A11 and discard it, so every well ends at 100 uL.
#   A12 never gets sample: it is the blank.


# From part 3, copied here so this script runs on its own.
def calc_stock_volume_ul(stock_conc_um, final_conc_um, final_volume_ul):
    # C1 x V1 = C2 x V2, solved for V1: how much stock goes in the tube.
    stock_volume_ul = final_conc_um * final_volume_ul / stock_conc_um
    if stock_volume_ul > final_volume_ul:
        raise ValueError(
            f"Stock volume {stock_volume_ul} uL exceeds final volume {final_volume_ul} uL"
        )
    return stock_volume_ul


drug_stock_um = 10000  # the 10 mM stock, written in uM
top_conc_um = 100  # what A1 should hold
a1_volume_ul = 200  # 100 uL stays in A1, 100 uL moves on to A2
dilution_factor = 2  # 2-fold: each well is 1/2 the concentration of the one before


# Step 0: make the top concentration (part 3's function).
stock_ul = calc_stock_volume_ul(drug_stock_um, top_conc_um, a1_volume_ul)
print("A1 prep:", stock_ul, "uL stock +", a1_volume_ul - stock_ul, "uL diluent")

# Steps 1-3 as a plate map (part 2), filled in by a loop (part 1).
plate_map = {}  # empty map: well name -> concentration in uM
conc_um = top_conc_um

for column in range(1, 12):  # A1 to A11 get sample; A12 is the blank
    well_name = "A" + str(column)
    plate_map[well_name] = conc_um
    conc_um = conc_um / dilution_factor  # each well is fraction of the one before

plate_map["A12"] = 0  # blank: diluent only, no sample

for well_name, well_conc_um in plate_map.items():
    print(well_name, "->", well_conc_um, "uM")

# Check against the hand calculation: A11 should be about 97.7 nM.
print("A11 in nM:", plate_map["A11"] * 1000)
print("Wells mapped:", len(plate_map))
