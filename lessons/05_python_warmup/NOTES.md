# Lesson 05 — python warmup

**Goal:** understand how to generate all the
  well names with a loop, and how PyLabRobot orders wells


**what I learned**: 
1. PyLabRobot orders the wells, column-wise, meaning A1,B1,C1,... H1, A2, B2, ... H2, A3, ...
2. an int and a str cannot be added together and it will throw a TypeError, we need to make sure we use "row+str(column)" to add attach them like two strings together
3. Sometimes not finding the error is worst. for expample, if I had used range(1, 12), and forget that using this would miss column 12, then I am only using 11 columns and 88 wells, and it won't throw an error. so it will be harder to catch it.