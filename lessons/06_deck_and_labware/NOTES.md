# Lesson 06 — deck and labware
## Part 1 - dead volume

**Goal:** understanding the dead volumes for each container, and how PyLabRobot stores the shape of each container type

**what I learned**: 
1. V-shape containers will have significantly less dead volume compare to flat bottom containers.
2. Dead volume for containers are fixed values that could be calculated using the data stored in pylabrobot library
3. PyLabRobot only checks that the well holds at least the requested volume. It doesn't check how much the tip can actually reach (the dead volume), so that guardrail is up to the programmer.
