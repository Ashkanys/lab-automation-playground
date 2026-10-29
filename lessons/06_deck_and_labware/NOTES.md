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
3. X direction is from left to right (getting larger), y direction is from back to front (row A has higher y than row B) and z direction is from bottom to top
