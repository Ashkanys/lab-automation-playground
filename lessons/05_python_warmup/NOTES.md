# Lesson 05 — python warmup
## Part 1 - well names

**Goal:** understand how to generate all the
  well names with a loop, and how PyLabRobot orders wells


**what I learned**: 
1. PyLabRobot orders the wells, column-wise, meaning A1,B1,C1,... H1, A2, B2, ... H2, A3, ...
2. an int and a str cannot be added together and it will throw a TypeError, we need to make sure we use "row+str(column)" to add attach them like two strings together
3. Sometimes not finding the error is worst. for expample, if I had used range(1, 12), and forget that using this would miss column 12, then I am only using 11 columns and 88 wells, and it won't throw an error. so it will be harder to catch it.
## Part 2 - Plate map
**Goal:** To learn about dictionary and how we save plate map in dictionary.

**what I learned:**
1. It is important the order of the wells that are being written into dictionary. Python saves the same order as they are introduced.
2. If I ask for a well that isn't on the map (B2), Python stops with a KeyError that names the missing well. A loud error like this is safer than a silent one.
3. During the well assignment, if a name is repeated, Python overrides its content without warning. The only way I was able to figure out was through paying attention to the total count

## Part 3 concentration calculation
**Goal:** to write functions that help with concentration calculations.

**what I learned:**
1.  A function does the C1V1 = C2V2 math the same way every time, so I don't make math slips when I redo it. It can't catch wrong inputs, though (see 2).
2. Although, extra attention should be paid into how the units are recorded. A simple unit slip can cause huge error in calculation, which Python itself could not detect or catch.
3. Certain guardrails should be placed to catch not-reasonable results.
4. "print" only warns and the script keeps going; "raise" stops it, so the bad volume never gets used. The traceback shows where it stopped (read it from the bottom up). Later, "try/except" can catch a specific error type and handle it, like pausing for a refill.

## Part 4 serial dilution
**Goal:** to combine a loop, a dictionary and the C1V1 function into a serial dilution table for row A of a 96-well plate

**what I learned:**
1. in writing a loop fuction, extra attention should be paid to the order of the steps. Is plate name is saved before the dilutaion calculation or after. without looking at the final print out, this type of error won't be cought.
2. adding "dilution_factor" to the code would make it easy to caluculate the final concentration, but don't forget to add it in your calculation for Media:drug mixing volume calculation