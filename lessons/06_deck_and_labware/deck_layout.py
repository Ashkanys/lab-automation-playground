# Lesson 06, part 3: carriers and rails, planning the deck.
#
# Deck plan, left to right, using the hood rule (clean on the left, work in
# the middle, trash on the right):
#   rails 12-17: tip carrier    (clean tips)
#   rail  18:    trough carrier (diluent)
#   rails 19-24: plate carrier  (the plate we pipette into)
#   rail  32:    trash          (built into the deck)
# A used tip travels left to right, plate -> trash, and never passes over clean tips.

from pylabrobot.resources.hamilton import STARLetDeck
from pylabrobot.resources import (
    TIP_CAR_480_A00,
    Trough_CAR_5R60_A00,
    PLT_CAR_L5AC_A00,
    hamilton_96_tiprack_300uL_filter,
    hamilton_1_trough_60mL_Vb,
    cor_96_wellplate_360uL_Fb,
)

deck = STARLetDeck()

# Tips: one rack in the carrier's first position (position 0 is the front-most slot).
tip_carrier = TIP_CAR_480_A00(name="tip_carrier")
tip_carrier[0] = hamilton_96_tiprack_300uL_filter(name="tips_01")
deck.assign_child_resource(tip_carrier, rails=12)  # 6 rails wide: covers 12-17

# Diluent: the 60 mL V-bottom trough from part 1, in a 1-rail carrier.
trough_carrier = Trough_CAR_5R60_A00(name="trough_carrier")
trough_carrier[0] = hamilton_1_trough_60mL_Vb(name="diluent_trough")
deck.assign_child_resource(trough_carrier, rails=18)  # 1 rail wide: covers 18 

# The plate we will dilute into.
plate_carrier = PLT_CAR_L5AC_A00(name="plate_carrier")
plate_carrier[0] = cor_96_wellplate_360uL_Fb(name="dilution_plate")
deck.assign_child_resource(plate_carrier, rails=19)  # 6 rails wide: covers 19-24

# Print the deck as a table, like checking the deck before you press Start.
print(deck.summary())
