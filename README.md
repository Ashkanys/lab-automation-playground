# Lab Automation Playground

Liquid-handling protocols written in Python with [PyLabRobot](https://github.com/PyLabRobot/pylabrobot) and run on a simulated Hamilton STARlet. Each lesson starts from a bench protocol, turns it into code, breaks it on purpose, and ends with notes on what I learned.

Everything runs in software. The simulation backend logs each command instead of moving a robot. PyLabRobot reaches real hardware by swapping that backend, but nothing in this repo has run on a physical instrument yet.

## About me

I'm a PhD-trained engineer and scientist with hands-on experience in mammalian cell culture, bioreactor development, and high-throughput laboratory workflows. I'm pursuing laboratory automation roles, as a scientist or engineer, because I'm interested in making complex biological workflows more efficient, reproducible, and scalable.

This repository is my self-directed project to translate that lab experience into Python-based automation. I use PyLabRobot and simulated liquid-handling systems to learn robot programming, workflow design, and troubleshooting.

[LinkedIn](https://www.linkedin.com/in/ashkan-yekrang/)

## Lessons so far

| Lesson | What it does | Key result |
|---|---|---|
| [01](lessons/01_job_market/) · [02](lessons/02_git_basics/) · [03](lessons/03_reorganise_repo/) Groundwork | Tallied the skills asked for in 9 automation job postings; git basics; moved a script without losing its history (`git mv`) | Hamilton came up in 7 of 9 postings and NGS/PCR in 6, so the roadmap gained a qPCR plate-setup lesson |
| [04 First transfer](lessons/04_first_transfer/) | One 150 µL plate-to-plate transfer, line by line: deck, carriers, rails, backend, `async`/`await` | 300 µL tips: the smallest Hamilton size (10, 50, 300, 1000 µL) that holds 150 µL |
| [05 Python warm-up](lessons/05_python_warmup/) | Well names A1–H12, a plate map, a C1V1 function, a serial dilution table. No robot yet | The C1V1 function raises an error instead of returning an impossible volume. 1 µM from a 10 mM stock goes through a 100 µM intermediate, because 0.1 µL is too small to pipette |
| [06 Deck and labware](lessons/06_deck_and_labware/) | Dead volume from well shape, ANSI/SLAS plate footprints, and a STARlet deck laid out clean-left, dirty-right | With the tip 2 mm above the bottom, 60.1 µL stays behind in a flat-bottom well, 6.1 µL in a V-bottom PCR well and 454.5 µL in a 60 mL trough |
| [07 Channels and tips](lessons/07_channels_and_tips/) | 1 channel vs 8 channels, and when to change tips, as a `tips_touch_liquid` setting | 6 sample columns use 48 tips if the tips touch the samples, 8 if they dispense from above and stay clean |
| [08 Reagent to plate](lessons/08_reagent_to_plate/) *(in progress)* | 50 µL into all 96 wells: one aspiration per column vs multi-dispense (one aspiration, several dispenses) | 12 aspirations become 3 per plate. Each aspiration takes extra liquid (20 µL in the example) so the first and last dispenses stay accurate, and the extra goes back to the trough |

## What the simulator doesn't check

A run with no errors isn't proof that a protocol is safe. Each of these runs without complaint in PyLabRobot 0.2.2; I found them in the lessons by breaking things on purpose.

| Situation | What PyLabRobot does | What I do about it |
|---|---|---|
| Aspirating 320 µL into a 300 µL tip | Runs. Only the tip's physical maximum (360 µL) is enforced; 370 µL raises `TooLittleVolumeError` | A guardrail on the tip's nominal volume, checked before the robot moves ([08](lessons/08_reagent_to_plate/)) |
| Aspirating all 200 µL from a flat-bottom well | Runs. The volume tracker checks the total, not the ~60 µL a tip held 2 mm above the bottom can't reach | Work out each container's dead volume and plan fill volumes around it ([06](lessons/06_deck_and_labware/)) |
| A 6-rail plate carrier at rail 27, covering the deck's waste block | Runs. The overlap check only asks whether the new carrier's edges land inside something, so a carrier wide enough to cover the whole block slips through. At rail 26 it's caught | Print `deck.summary()` and check the layout before a run, like checking a real deck before pressing Start ([06](lessons/06_deck_and_labware/)) |
| Tips that touched samples going back into the reagent trough | Runs. The code is the same as with clean tips; PyLabRobot defines a `CrossContaminationError` but never raises it | Tip changes are an explicit setting (`tips_touch_liquid`), and leftover reagent goes back to the trough only if the tips touched nothing else ([07](lessons/07_channels_and_tips/), [08](lessons/08_reagent_to_plate/)) |

The tip guardrail, from [`multi_dispense.py`](lessons/08_reagent_to_plate/multi_dispense.py). It runs before `main()`, so a bad setting stops the script before any tip is picked up:

```python
tip_nominal_volume_ul = 300

for group in column_groups:
    # One aspiration for every column in the group, plus the extra.
    aspirate_volume_ul = len(group) * reagent_volume_ul + extra_volume_ul
    if aspirate_volume_ul > tip_nominal_volume_ul:
        raise ValueError(f"Cannot aspirate {aspirate_volume_ul} uL into a {tip_nominal_volume_ul} uL tip.")
```

## How each lesson works

1. Write the protocol in plain English, the way I'd explain it to a colleague at the bench.
2. Plan the deck: what goes where, volumes, tips, dead volume.
3. Small, commented code, walked through line by line: why each part is there, not just what it does.
4. Run it in the simulator.
5. Break it on purpose and read the error.
6. Change one thing myself.
7. Write what I learned in the lesson's `NOTES.md`, and commit.

I use [Claude Code](https://claude.com/claude-code) as a tutor: it drafts and explains small scripts; I plan the protocols, run and break the code, make my own changes and write the notes.

## Roadmap

The full 12-week plan, with lessons ticked off as I finish them, is in [LEARNING_PLAN.md](LEARNING_PLAN.md).

- **Pipetting basics (lessons 06–13):** serial dilution and carry-over, liquid classes, liquid-level detection and the 96-channel head, handling errors, and the same protocol on a Tecan EVO deck.
- **Protocols driven by data files (14–19):** plate maps, normalisation, cell seeding, hit-picking onto 384-well plates, qPCR plate setup, and worklists for Tecan, Hamilton VENUS, Biomek and Echo, with pytest checks.
- **Several instruments (20–25):** plate reader, heater-shaker, gripper moves, incubator, running two things at once, and timestamped run logs.
- **Pipetting QC (26–29):** volume checks by weight and by dye, tuning a liquid class, plate effects and Z′.
- **Opentrons (30–32):** the serial dilution again, with the Opentrons API and simulator.
- **Final project (33):** an automated cell-viability dose-response assay, from cell seeding to IC50 and Z′.

## Run it yourself

No robot needed. Tested with Python 3.14 on macOS.

```bash
git clone https://github.com/Ashkanys/lab-automation-playground.git
cd lab-automation-playground
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python lessons/08_reagent_to_plate/multi_dispense.py
```

The script prints each command the simulated robot receives, then a summary:

```
Plate 1 aspirations: 12
Plate 2 aspirations: 3
Reagent left in the trough: 1400.0 uL
```

[`first_transfer.py`](lessons/04_first_transfer/first_transfer.py) also opens PyLabRobot's deck Visualizer at http://127.0.0.1:1337 and waits for Enter before it closes.

## Repository layout

```
lab-automation-playground/
├── README.md
├── LEARNING_PLAN.md          ← the 12-week roadmap
├── CLAUDE.md                 ← instructions for Claude Code
├── requirements.txt          ← pylabrobot==0.2.2
└── lessons/                  ← one folder per lesson; each script runs on its own
    ├── 01_job_market/
    ├── ...
    ├── 07_channels_and_tips/
    │   ├── one_vs_eight_channels.py
    │   ├── tip_changes.py
    │   └── NOTES.md          ← what I learned, in my own words
    └── 08_reagent_to_plate/
```
