# Lab Automation Learning Plan

**Goal:** get ready to apply for **automation scientist** jobs in pharma and large biotech, where Hamilton, Tecan and Beckman robots are standard, and build some automation engineering skills along the way.
**Time:** about 10 hours a week for 12 weeks.
**Hardware:** none. Everything runs on your laptop in simulation.

Tick lessons off as you finish them by changing `- [ ]` to `- [x]`. GitHub shows these as checkboxes, so your progress is visible.

---

## 1. The strategy

**Your wet-lab experience is the hard part, and you already have it.** Plenty of applicants can write Python. Far fewer know why serum foams when it's dispensed fast, why you aspirate slowly and high above adherent cells, or how much reagent a trough's dead volume wastes. Automation scientists are hired to make robots run assays *well*, and that judgment comes from the bench. This plan turns what you already know into code and write-ups an employer can look at.

**You don't need the vendors' software to get hired.** Hamilton VENUS, Tecan FluentControl/EVOware and Beckman Biomek only come with a license, usually through an employer, and employers expect to train new staff on them. What interviewers check is whether you understand the ideas underneath, and you can practise every one of them here:

- **Deck layout:** where labware sits on the robot's work surface (the "deck").
- **Labware:** plate types, well shapes, usable volumes.
- **Liquid classes:** the pipetting settings for each kind of liquid.
- **Worklists:** files that tell a robot which transfers to do.
- **Error handling:** what happens when something goes wrong mid-run.
- **Pipetting QC:** proving the robot dispenses what it should.

**Three tools do the work:**

1. **PyLabRobot** (already installed) simulates Hamilton and Tecan robots and other lab instruments, and shows the deck live in your browser. This is your main "lab".
2. **Plain Python** writes the worklist files that Hamilton, Tecan, Biomek and Echo software read. This is one of the most common Python tasks in real automation jobs.
3. **Opentrons** has a free, official simulator. Opentrons robots are less common in pharma, but it's the only vendor whose real protocol software you can run for free.

---

## 2. Your free toolbox

| Tool | What you'll use it for | When |
|---|---|---|
| [PyLabRobot](https://docs.pylabrobot.org/) 0.2.2 | Simulated Hamilton STAR/STARlet and Tecan EVO decks, plus a simulated plate reader, heater-shaker, shaker, incubator, scale, centrifuge, temperature controller, thermocycler, pump and tilt module. Live browser view of the deck. | Already installed |
| pandas, matplotlib, pytest | Data tables, plots, and automatic checks of your calculations | Phase 2 |
| [Opentrons Python API](https://docs.opentrons.com/python-api/tutorial/) + `opentrons_simulate` | Write a real Opentrons protocol and simulate it step by step | Phase 5 |
| [Opentrons Protocol Designer](https://designer.opentrons.com/) | Build a protocol by clicking (in Chrome), export it as Python, then read the code it wrote | Phase 5 |
| [Opentrons App](https://docs.opentrons.com/ot-2/opentrons-app/protocol-import/) | Import a protocol to see its deck layout and errors, with no robot connected | Phase 5 |
| [OneLab](https://onelab.andrewalliance.com/) (Waters / Andrew Alliance) | Optional: design protocols by dragging pipettes around a virtual bench | Any time |
| Git + [GitHub](https://github.com/Ashkanys/lab-automation-playground) | Version history now, portfolio later | From week 1 |

Everything above is free. Three things to know up front:

- **Simulated instruments return placeholder numbers.** PyLabRobot's simulated plate reader returns all zeros unless you give it data, and the simulated scale always reports the same weight. You'll make realistic fake data yourself (for example, a dose-response curve with some noise). That turns out to be useful: it teaches you what real instrument data looks like.
- **The PyLabRobot website documents the newest version.** This repo is pinned to 0.2.2. If an example from the website doesn't work here, trust the installed version.
- **Opentrons needs its own Python.** Its tutorial asks for Python 3.12, and it means it: I tried the Python 3.11 already on your Mac and the simulator crashes, and one of its dependencies (an older numpy) has no ready-made installer for Python 3.13 or newer. Your main environment uses Python 3.14, so in Phase 5 you'll install Python 3.12 with Homebrew and make a second environment just for Opentrons.

---

## 3. Real hands-on time and "online labs": the honest picture

- **Cloud labs aren't realistic for one person.** Remote-controlled labs such as [Emerald Cloud Lab](https://www.emeraldcloudlab.com/) don't publish prices; they negotiate contracts with companies and universities.
- **Vendor software needs a license.** VENUS, FluentControl and Biomek all have simulation modes, but access comes through an employer or institution, not a free download.
- **The cheapest real hands-on option** is the [SLAS Applied Liquid Handling Boot Camp](https://www.slas.org/events-calendar/applied-liquid-handling-boot-camp/). SLAS (Society for Laboratory Automation and Screening) is the main professional society in this field.
  - Self-paced online prep, then 2 hands-on days on real liquid handlers in San Diego, hosted at Eli Lilly, on **November 17–18, 2026**.
  - It covers protocol development, comparing liquid classes and dye-based accuracy checks: Phase 4 of this plan, on real robots.
  - The student/unemployed rate is **$425 if you register by October 19**, then $500. Academic rates are $1,700/$2,000 and industry rates $2,125/$2,500. Travel is extra.
- **Other ways to get near a real robot:** university core facilities and community biolabs (ask about training or volunteering), and the automation group at any lab you've worked with (ask to shadow a run).
- **Where people in the field talk:** [labautomation.io](https://labautomation.io/) has forums for Hamilton, Tecan, Beckman Coulter, Opentrons and PyLabRobot, plus a Job Postings board. [SLAS](https://www.slas.org/) runs webinars and has career resources.

---

## 4. Folder structure

This is where the repo is heading. We'll build it up bit by bit as you reach each lesson.

```
lab-automation-playground/
├── README.md              ← portfolio front page: what's here, screenshots, how to run
├── LEARNING_PLAN.md       ← this file
├── CLAUDE.md              ← instructions for Claude Code
├── requirements.txt       ← Python packages this repo needs
├── lessons/
│   ├── 01_job_market/
│   │   └── NOTES.md
│   ├── 04_first_transfer/
│   │   ├── first_transfer.py   ← the original plr_demo.py, moved here in lesson 03
│   │   └── NOTES.md
│   ├── 18_worklists/
│   │   ├── make_worklists.py
│   │   ├── NOTES.md
│   │   └── output/             ← files the script creates
│   └── ...
├── data/                  ← input files shared by several lessons
├── labtools/              ← reusable functions (from lesson 19)
├── tests/                 ← automatic checks for labtools (from lesson 19)
└── opentrons/             ← Opentrons protocols, run with Python 3.12 (from lesson 30)
```

Why this shape:

- **One numbered folder per lesson.** The numbers match the roadmap below, so you always know where things are. Each lesson runs on its own, so breaking lesson 12 can't break lesson 9.
- **A `NOTES.md` in every lesson.** A few lines on what you learned, what confused you, and one sentence you could say in an interview. Writing it is also practice for writing SOPs, which is part of the job.
- **Files a lesson creates go in its own `output/` folder**, and input files go in `data/`. Keeping them apart means you never confuse "what I was given" with "what my script made".
- **`labtools/` arrives in lesson 19, on purpose.** First you'll copy the same deck setup into a few lessons. When that gets annoying, we move it into one shared file. That's how real code grows, and you'll know exactly why the shared file exists.
- **`tests/` holds automatic checks of your calculations.** A wrong dilution calculation ruins a plate; a test catches it before any robot moves.
- **`opentrons/` is separate** because it uses a different Python (see section 2).

---

## 5. How each lesson works

1. **Protocol in plain English.** Write the steps as you would for a colleague at the bench. You're the expert here.
2. **Plan the deck.** What goes where, the volumes, how many tips, how much dead volume.
3. **Code, with a walkthrough.** Small, commented code, and I explain each part: *why* it's there, not just *what* it does. Ask "why?" as often as you like.
4. **Run it in the simulator.** Watch the browser view or read the printed log.
5. **Break it on purpose.** Ask for more liquid than a well holds, then learn to read the error.
6. **Your turn.** Make one change yourself: different volumes, an extra replicate column.
7. **Write `NOTES.md` and commit** (save a version in git).

**How the code is written:**

- One new idea per lesson; scripts stay under about 80 lines.
- Plain functions, lists and dictionaries. Classes only when there's a clear reason, explained the first time they appear.
- Units in names: `volume_ul`, `conc_ng_per_ul`, `cells_per_ml`.
- Comments give the lab reason (`# aspirate 2 mm above the bottom so we don't disturb the cells`), not just what the line does.
- Readable beats short: no clever one-liners.
- **About `async` and `await`:** PyLabRobot needs these because the computer must wait for each robot step to finish before starting the next. Lesson 04 explains them once; after that, they're a pattern you copy.

---

## 6. The 12-week roadmap

### Phase 0 — Week 1: Foundations

- [x] **01 Job market.** Collect 10 postings that mention Hamilton, Tecan or Beckman. List the skills they ask for in `NOTES.md`. You'll come back to this list in week 12.
- [x] **02 Git basics.** Saving a version (*commit*), uploading it to GitHub (*push*), and viewing your history.
- [x] **03 Reorganise the repo.** Create the folders from section 4 together, and move `plr_demo.py` into lesson 04.
- [x] **04 First transfer, line by line.** What the deck, carriers, rails and *backend* (the part that talks to the robot, or pretends to) are, and what `async`/`await` do.
- [x] **05 Python warm-up, lab edition.** Generate well names A1–H12 with loops, store a plate map in a dictionary, write a C1V1 = C2V2 function, and print a serial dilution table. No robot yet.

### Phase 1 — Weeks 2–4: Pipetting basics on a simulated Hamilton STARlet

- [ ] **06 Deck and labware.** Carriers and rails, the standard plate footprint (ANSI/SLAS), well shapes, and dead volume.
- [ ] **07 Channels and tips.** One channel vs 8 channels, and when to change tips (contamination risk vs cost and time).
- [ ] **08 Adding a reagent to a plate.** From a trough to all 96 wells, including multi-dispensing (one aspiration, several dispenses) and why it needs a little extra liquid to stay accurate.
- [ ] **09 Serial dilution.** Across a row, with mixing, and the carry-over problem.
- [ ] **10 Liquid classes.** Compare PyLabRobot's Hamilton settings for water, glycerin, ethanol, serum and DMSO. Connect each setting (flow rate, air gap, blow-out, settling time, over-aspirate, clot retract) to bench habits you already have: reverse pipetting, pre-wetting, avoiding foam.
- [ ] **11 Heights and the 96-channel head.** Pipetting at a fixed height vs liquid-level detection (the robot sensing the liquid surface); a media exchange that leaves adherent cells undisturbed; pipetting a whole plate at once.
- [ ] **12 Errors on purpose.** Too little liquid, a tip already on, no tip. Catch them with `try`/`except`, and decide what a real operator would do next.
- [ ] **13 Same protocol, Tecan deck.** Run lesson 09 on a simulated Tecan EVO. The logic stays the same; only the layout changes. That makes a good interview story.

### Phase 2 — Weeks 5–6: Protocols driven by data files

This is the most common kind of task in real jobs: a scientist gives you a spreadsheet, and the robot does what it says.

- [ ] **14 Plate maps.** Read a sample sheet with pandas and print it as a plate layout.
- [ ] **15 Normalisation.** Work out sample and diluent volumes to bring DNA or protein samples to the same concentration. Handle volumes below the smallest the robot can pipette (intermediate dilution) and above what fits in a well.
- [ ] **16 Cell seeding.** From a cell-counter export, work out the volume per well to seed a set number of cells, skipping samples with low viability.
- [ ] **17 Hit-picking and 384-well plates.** Pick selected wells from a list; map four 96-well plates onto one 384-well plate.
- [ ] **17b qPCR plate setup.** From a sample sheet (samples × primer sets × triplicates), lay out a 384-well qPCR plate with a standard curve and no-template controls (NTCs). Work out master mix with overage for dead volume, then dispense in the order that protects the plate: master mix to every well, then NTC water, then samples, then standards from lowest to highest concentration. Small volumes (2–5 µL) and tip-change rules come back here, because an extra 0.2 µL of template shifts the Ct value. Optional: run the cycling on PyLabRobot's simulated thermocycler. PCR and NGS showed up in 6 of the 9 postings in lesson 01.
- [ ] **18 Worklists.** Turn one list of transfers into four files: a Tecan worklist (`.gwl`), a CSV for a Hamilton VENUS method, a CSV for Biomek's "Transfer From File" step, and a picklist for Beckman's Echo acoustic dispenser (volumes in nanolitres).
- [ ] **19 Shared code and tests.** Move repeated code into `labtools/`, write pytest checks for your volume math, and learn how Python finds your own files.

### Phase 3 — Weeks 7–8: Connecting several instruments

- [ ] **20 Plate reader.** Read a plate with the simulated reader, feeding it realistic fake data such as a dose-response curve plus noise.
- [ ] **21 Heating and shaking.** Incubation steps on a heater-shaker and a temperature controller.
- [ ] **22 Moving plates.** Use the robot's gripper to move plates and lids between positions.
- [ ] **23 Incubator.** Store and fetch plates, including steps that must happen within a time window.
- [ ] **24 Two things at once.** Shake plate A while pipetting plate B. This is what scheduling software (Green Button Go, Cellario, Momentum) does in real labs.
- [ ] **25 Run logs.** Record every step, volume and error with a timestamp: the audit trail regulated labs require.

### Phase 4 — Weeks 9–10: Pipetting QC and assay quality

This is the core of an automation scientist's job.

- [ ] **26 Checking volumes by weight.** Dispense replicates onto a simulated balance, then calculate accuracy (% of target) and precision (CV%) and compare them with pass/fail limits.
- [ ] **27 Checking volumes with dye.** Convert dye absorbance to volume with a standard curve. In industry, systems such as Artel MVS do this.
- [ ] **28 Tuning a liquid class.** For glycerol, change one setting at a time, compare the results, and pick the best.
- [ ] **29 Plate effects and Z′.** Spot edge effects and row/column bias on heatmaps, and calculate Z′, the standard score for whether an assay can tell positives from negatives.

### Phase 5 — Week 11: Opentrons

- [ ] **30 Opentrons setup.** Install Python 3.12, make the Opentrons environment, and simulate a first protocol with `opentrons_simulate`.
- [ ] **31 Protocol Designer.** Click together a serial dilution, export it as Python, then read and change the code it generated.
- [ ] **32 Serial dilution, Opentrons version.** Rewrite lesson 09 with the Opentrons API and compare the two.

### Phase 6 — Week 12 and onwards: Final project and job preparation

- [ ] **33 Final project: automated cell-viability dose-response assay.**
  1. Seed cells from a cell-counter export (lesson 16).
  2. Make a compound serial dilution in DMSO, then an intermediate dilution in media so the cells see no more than 0.5% DMSO.
  3. Add the compounds to the cells.
  4. Incubate in the simulated incubator (72 hours shortened to seconds).
  5. Add a viability reagent, shake, and read luminescence.
  6. Fit a dose-response curve (4-parameter logistic) and report IC50 and Z′.
  7. Bonus: write the compound addition as an Echo picklist instead.

  Write it up in the README with a screenshot of the browser view and your plots. This is the project you'll walk interviewers through.

**Job preparation checklist:**

- [ ] Polish the README, pin the repo on your GitHub profile, and add it to LinkedIn.
- [ ] Revisit your skills list from lesson 01 and mark what you can now show.
- [ ] Practise explaining three decisions you made: a liquid class choice, a tip strategy, and how you handled an error.
- [ ] Do a timed 3-hour practice take-home: turn a written SOP into a protocol, a deck layout and a reagent list.
- [ ] Check the Job Postings board on labautomation.io every week.

### After week 12: more engineering

If the coding parts turn out to be the most fun, these go further:

- **Contribute to PyLabRobot.** Adding a labware definition or fixing documentation gives you a public contribution to an open-source lab automation project.
- **SiLA 2**, an open standard for how lab instruments talk to software. The `sila2` Python package lets you wrap a simulated instrument as a SiLA 2 server.
- **A small scheduler.** Extend lesson 24 so it plans a whole day of plates around incubation times.

---

## 7. Bench ↔ robot vocabulary

| At the bench | On a liquid handler |
|---|---|
| Tip box | Tip rack |
| Multichannel pipette | 8-channel head, or a 96-channel head for a whole plate at once |
| Your pipetting technique (speed, depth, pre-wetting, reverse pipetting) | Liquid class |
| The plate layout in your notebook | Plate map / sample sheet (CSV) |
| How you lay out your bench | Deck layout |
| Pipette calibration | Volume checks by weight (gravimetric) or dye (photometric) |
| Watching the tip touch the liquid | Liquid-level detection: capacitive (cLLD) or pressure-based (pLLD) |
| Carrying a plate to the incubator | Gripper or robot-arm move, timed by scheduling software |
| Your SOP | Method / protocol script |

---

## 8. Changing the plan

Treat this as a draft. If an interview comes up at an Opentrons lab, do Phase 5 early. If a posting asks for something missing here, add a lesson for it. Keep the checkboxes up to date so this file stays an honest record of where you are.
