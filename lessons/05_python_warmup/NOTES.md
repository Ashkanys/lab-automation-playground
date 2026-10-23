# Lesson 05 — python warmup
## Part 1

**Goal:** understand how to generate all the
  well names with a loop, and how PyLabRobot orders wells


**what I learned**: 
1. PyLabRobot orders the wells, column-wise, meaning A1,B1,C1,... H1, A2, B2, ... H2, A3, ...
2. an int and a str cannot be added together and it will throw a TypeError, we need to make sure we use "row+str(column)" to add attach them like two strings together
3. Sometimes not finding the error is worst. for expample, if I had used range(1, 12), and forget that using this would miss column 12, then I am only using 11 columns and 88 wells, and it won't throw an error. so it will be harder to catch it.
## Part 2
**Goal:** To learn about dictionary and how we save plate map in dictionary.

**what I learned:**
1. It is important the order of the wells that are being written into dictionary. Python saves the same order as they are introduced.
2. If I ask for a well that isn't on the map (B2), Python stops with a KeyError that names the missing well. A loud error like this is safer than a silent one.
3. During the well assignment, if a name is repeated, Python overrides its content without warning. The only way I was able to figure out was through paying attention to the total count