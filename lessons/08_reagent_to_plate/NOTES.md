# Lesson 08 — Reagent to plate

## Part 1 - Multidispensing

**Goal:** How Multi-dispensing is different and what things we should keep in mind.

**what I learned**:  
1. Multi-dispensing can accelarate the experiment, but it comes with side effects that needs to be considered.
2. Extra volume should be aspirated to account for the air coushion effect in the first dispense and the film on the tip wall that might make the last dispense becoming short.
3. the extra volume in the tip at the end of multi-dispense can go back to the trough, but only if the tips touched nothing except the clean reagent.
4. PyLabRobot only enforces the tip's physical maximal limit, not the nominal one. It would be ideal to set guardrail for crossing the nominal limit too.
5. If possible, the guardrails should be placed before the machine is set or tips are picked up, that way the machine is not stuck in middle of a run with tips in the arm.

## Part 2 - separating pre-dispense and leftover at the end + visualization

**Goal:** separating pre-dispense and post dispense extras, dynamically grouping columns and adding visualization for gif

**what I learned**:  
- In calculating the trough volume, consider the last round of aspiration and dispense require 8x extra reagent volume, even though it is going back to the trough.
- PyLabRobot lets the trough run down to 0, and it is up to the user to consider the dead volume of the trough, hence the existence of the trough volume check before the run start
- visualizaer has gif recorder. The well color can be controlled during the Visualizer initiation. The well color is affected by the percentage of reagent volume to the capacity.