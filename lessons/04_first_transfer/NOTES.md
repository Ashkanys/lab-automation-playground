# Lesson 04 — First transfer, line by line

**Goal:** understand every part of `first_transfer.py`: the deck, carriers and rails, the backend, and what `async`/`await` do. Then run it, break it on purpose, and change one thing.

---

## 1. Protocol in plain English

### Draft 1 (bench version)

1. Move the arm over location C (pipette tips) and pick up a 200 µL tip.
2. Move the arm over location A.
3. Lower the arm, mix the reagent and aspirate 150 µL.
4. Move the arm to location B.
5. Lower the arm and dispense 150 µL.
6. Move the arm to location C and discard the tip back into its place.

### Bench decisions

- **Return or discard the tip:** returning risks contamination; only reuse a tip for the same liquid. Anything biological goes to waste.
- **Tip size:** a 1000 µL tip is too big for 150 µL; the smallest tip that fits is more accurate. On a Hamilton the sizes are 10, 50, 300 and 1000 µL, so 150 µL → 300 µL tip.
- **Mixing:** depends on the liquid. PBS or media: no. Cell suspension: yes. Beads: let them settle and take the supernatant without disturbing them.

### Draft 2 (robot-ready: every well, volume, tip and decision written down)
Plate A: 200 µL PBS in every well. Plate B: empty. Tip rack full.

1. grab a 300ul pipette tip from position A2 in tip rack
2. Since the content is PBS, no need to mix. Collect 150uL from plate A well A2
3. dispense 150uL into plate B well A2
4. return the tip back to the tip rack, position A2 (since the content is PBS and we are not worried about cross contamination)

Plate A well A2: 50 µL. Plate B well A2: 150 µL. Tip back in position A2.

## 2. Deck plan
1. Tip carrier on rail 15, tip rack on position 0
2. plate carrier on rail 8, plate A (source_plate) on position 0 and plate B (destination_plate) on position 1

## 3. Code walkthrough: words in my own words

- **Deck:** The working station (type of machine) you are working on 
- **Carrier / rails:** rails are the slots in an empty working station, you put carriers on them (like plate carriers, or tip carriers) tp support adding additional tools on your workstation.
- **Backend:** where you are sending your commands to, it can be the chatterbox, or the actual machine
- **`async` / `await`:** it is necassary when you are dealing with steps which takes time and you need to wait for each step before run the next command. it means run this step and wait until it's done

## What confused me

- The await command is necessary to run the command, it is not just the matter of waiting. It is running and waiting

## What I learned

- you need to read the error from bottom up, and the place where error happens doesn't necessarily mean the place there is an issue. The issue might have started earlier but it didn't trigger an error until later

## Interview talking point

- When I left out await on the aspirate step, I was expecting the aspirate to still run. instead the error appeared on dispense, which confused me at first. Then I realised the aspirate never ran at all: await doesn't just wait for a command, it is what makes the command run. This taught me that if a similar error happens on a real setup, I should read back through the earlier steps to find where the problem actually started.
