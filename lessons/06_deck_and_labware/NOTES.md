# Lesson 06 — deck and labware
## Part 1 - dead volume

**Goal:** understanding the dead volumes for each container, and how PyLabRobot stores the shape of each container type

**what I learned**: 
1. V-shape containers will have significantly less dead volume compare to flat bottom containers.
2. Dead volume for containers are fixed values that could be calculated using the data stored in pylabrobot library
3. PyLabRobot only checks that the well holds at least the requested volume. It doesn't check how much the tip can actually reach (the dead volume), so that guardrail is up to the programmer.

## Part 2 - Standard and spacing

**Goal:** understanding why standards matters for our automation system, and how to calcualte the spacing between wells

**what I learned**: 
1. The ANSI/SLAS standards fixes the outside size and well positions, which helps switching between plates of different venders if they produce it based on the standard and helps with the aligning the plates to the holder or the spacing between the multichannel pipettes
2. if a plate has the standard well position, but the outter size is not standard, an adaptor can be used to place it on the carier.
3. X direction is from left to right (getting larger),y direction is from front to back (getting larger), so row A, at the back, has a higher y than row B, and z direction is from bottom to top

## Part 3 - introducing decks and carriers

**Goal:** How to introduce deck, add carriers and labware to your PyLabRobot environment.

**what I learned**: 
1. it is important to pay attention to the layout of your deck. Dedicate clean area (ideally on the left) working area, and dispose area (usually on the right)
2. While planning the layout, pay attention to the movement of the arm and which path it will take and consider possible drop from filled pipette tip that is moving.
3. PyLabRobot do have some checks to make sure the labware are not overlapping, but it is not comprehensive (for example it only checks the ends of the labware and whether it collide with any existing labware. So putting a 1-rail trough first and then a 6-rail carrier over it, might get missed in its check.)
4. putting labware on the carrier and carrier on decks, are known to pylabrobot as assigning children. and when you assign carrier on deck, you especify rails position. rails= gives the carrier's leftmost rail. (first rail start from x=100mm and each rail gap is 22.5 mm)
5. deck.summary() will print out the layout