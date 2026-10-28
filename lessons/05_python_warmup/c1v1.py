# Lesson 05, part 3: C1V1 = C2V2 as a function.
#
# The bench steps:
#   1. Write both concentrations in the same unit (10 mM = 10000 uM).
#   2. Stock volume = final concentration x final volume / stock concentration.
#   3. Media volume = final volume - stock volume.


def calc_stock_volume_ul(stock_conc_um, final_conc_um, final_volume_ul):
    # C1 x V1 = C2 x V2, solved for V1: how much stock goes in the tube.
    stock_volume_ul = final_conc_um * final_volume_ul / stock_conc_um
    if stock_volume_ul > final_volume_ul:
        raise ValueError(
            f"Stock volume {stock_volume_ul} uL exceeds final volume {final_volume_ul} uL"
        )
        #print(f"Warning: Stock volume {stock_volume_ul} uL exceeds final volume {final_volume_ul} uL. Check your concentrations.")
    return stock_volume_ul


drug_stock_um = 10000  # the 10 mM stock, written in uM so it matches the final concentrations
tube_volume_ul = 1000  # every tube we make is 1 mL

# Question 1: 1 mL of 50 uM.
stock_ul = calc_stock_volume_ul(drug_stock_um, 50, tube_volume_ul)
print("50 uM:", stock_ul, "uL stock +", tube_volume_ul - stock_ul, "uL media")

# Question 2: 1 mL of 1 uM, straight from the stock.
# The answer is too small to pipette accurately by hand or by robot.
stock_ul = calc_stock_volume_ul(drug_stock_um, 1, tube_volume_ul)
print("1 uM, direct:", stock_ul, "uL stock")

# The fix: an intermediate tube at 100 uM, then dilute that to 1 uM.
# The same function, used twice: this is why we wrote it once.
intermediate_um = 100
step1_ul = calc_stock_volume_ul(drug_stock_um, intermediate_um, tube_volume_ul)
print("Step 1, 100 uM:", step1_ul, "uL stock +", tube_volume_ul - step1_ul, "uL media")

step2_ul = calc_stock_volume_ul(intermediate_um, 1, tube_volume_ul)
print("Step 2, 1 uM:", step2_ul, "uL of 100 uM +", tube_volume_ul - step2_ul, "uL media")
