# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Purpose

A learning and prototyping playground for hardware-agnostic lab automation with [PyLabRobot](https://github.com/PyLabRobot/pylabrobot). Scripts run entirely in software — no physical instruments are attached.

## Working in this repo

This is a learning repo, and `LEARNING_PLAN.md` is the roadmap. Lessons are numbered folders under `lessons/`, added as the owner reaches them, each with its own `NOTES.md`. The original root-level `plr_demo.py` was moved (lesson 03) to `lessons/04_first_transfer/first_transfer.py`, where lesson 04 walked through it and switched it to 300 µL tips. Files matching `*_private.md` are git-ignored on purpose (e.g. full job postings) — keep personal material in them, never in committed files, because the GitHub repo is public.

- Follow the lesson routine in `LEARNING_PLAN.md` §5: plain-English protocol first, then small code, then a walkthrough of *why* each part exists.
- Code must be readable by a Python beginner: one new concept per lesson, scripts under ~80 lines, plain functions/lists/dicts (classes only with an explanation), units in variable names (`volume_ul`), comments that give the lab reason.
- Don't use a Python feature or library the plan hasn't reached yet without explaining it first.
- Don't restructure the repo, install packages, or commit unless asked — those steps are lessons the owner does alongside you.
- Opentrons work (lesson 30+) needs a separate Python 3.12 venv: `opentrons` 10.x pins `numpy<2`, which has no wheels for 3.13+, and `opentrons_simulate` crashes on 3.11 (pydantic `TypedDict` error).

## Setup and running

```bash
python -m venv .venv && source .venv/bin/activate   # existing .venv uses Python 3.14
pip install -r requirements.txt                      # pins pylabrobot==0.2.2
python lessons/04_first_transfer/first_transfer.py
```

`first_transfer.py` starts the PyLabRobot browser Visualizer at http://127.0.0.1:1337, waits 5 s so you can open it, runs one simulated transfer, then blocks on `input()` until Enter is pressed. It is interactive — don't run it in a context that can't send Enter (or pipe `echo |` into it).

There is no test suite, linter, or build step.

## How the scripts are structured

PyLabRobot scripts follow a fixed pattern (see `lessons/04_first_transfer/first_transfer.py`):

1. **Enable state tracking** (`set_tip_tracking(True)`, `set_volume_tracking(True)`) *before* creating resources, so the Visualizer and PLR's internal checks follow tips and liquid volumes.
2. **Deck + backend**: a deck definition (e.g. `STARLetDeck`) plus a backend passed to `LiquidHandler`. `LiquidHandlerChatterboxBackend` is the simulation backend — it just logs commands. Swapping the backend is how a script would target real hardware; the rest of the protocol stays the same.
3. **Resources**: carriers (`TIP_CAR_480_A00`, `PLT_CAR_L5AC_A00`) are assigned to the deck by `rails=`; tip racks and plates are slotted into carriers by index (`carrier[0] = plate`). Initial state is set via `tip_rack.fill()` and `plate.set_well_volumes(...)`.
4. **Operations** are async (`await lh.pick_up_tips(...)`, `aspirate`, `dispense`, `return_tips`), so everything runs inside `asyncio.run(main())`. Both `lh.setup()` and `Visualizer.setup()` must be awaited before use, and `vis.stop()` at the end.

PyLabRobot's API changes between releases; check against the pinned 0.2.2 (installed in `.venv/lib/.../pylabrobot`) rather than upstream docs when an import or signature doesn't match.
