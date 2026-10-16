# Lesson 03 — Reorganise the repo

**Goal:** move `plr_demo.py` into its lesson folder as `lessons/04_first_transfer/first_transfer.py` without losing its history, find every file that still mentions the old name, and check the script still runs.

**The lab analogy:** this is relocating a validated method. You move it unchanged, update every SOP that points to it, and re-check that it still works in the new place before anyone uses it. (Lab instruments get the same treatment: relocation is followed by requalification.)

---

## Steps I did

1. make a directory for lesson 4 through the terminal  
2. move the plr_demo into the new folder and rename it using git mv
3. using git grep to identify where plr_demo was mentioned and make changes to thos files if necessary

## The words, in my own words

- **`git mv`:** moves a file to a new location, and stages it
- **Rename-only commit:** helps making sure we are doing 1 step at a time in case something doesn't work, we know where it came from
- **`git grep`:** identifies where in your project, the name you typed has been mentioned, allowing you to edit files that have mentions of the old name. this search is only limited to the files that are being tracked by git
- **Why git ignores empty folders:** git only tracks files. since an empty folder doesn't have any files, git won't track it,

## What confused me

- git grep, but searching what it does make it clear

## What I learned

- using git mv instead of mv make the process easier for future commits

## Interview talking point

One sentence on how you'd move or rename a method that other people depend on:

- I first move the file with git mv, without editing it, and commit that move on its own so the history follows the file. Then I update everything that depends on it (other files, SOPs, and the people who run it), and run it in the new location to prove it still works before I start editing.
