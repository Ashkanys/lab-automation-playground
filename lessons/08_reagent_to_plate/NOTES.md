# Lesson 08 — Reagent to plate

## Part 1 - Multidispensing

**Goal:** How Multi-dispensing is different and what things we should keep in mind.

**what I learned**:  
1. Multi-dispensing can accelarate the experiment, but it comes with side effects that needs to be considered.
2. Extra volume should be aspirated to account for the air coushion effect in the first dispense and the film on the tip wall that might make the last dispense becoming short.
3. the extra volume in the tip at the end of multi-dispense can go back to the trough, but only if the tips touched nothing except the clean reagent.
4. PyLabRobot only enforces the tip's physical maximal limit, not the nominal one. It would be ideal to set guardrail for crossing the nominal limit too.
5. If possible, the guardrails should be placed before the machine is set or tips are picked up, that way the machine is not stuck in middle of a run with tips in the arm.