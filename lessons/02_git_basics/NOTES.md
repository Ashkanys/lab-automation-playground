# Lesson 02 — Git basics

**Goal:** save a version of this repo (*commit*), upload it to GitHub (*push*), and read your history (*log*). From now on, every lesson ends with a commit.

**The lab analogy:** git is a lab notebook for files. A commit is a dated, signed notebook entry: what changed, and a sentence on why. You never tear out pages; you can always look back at what a protocol said on any day. GitHub is the copy kept in the archive down the hall.

---

## The words, in my own words

Fill these in as we go.

- **Repository (repo):** is my working folder/project  + all the hidden files and previous commits
- **Working folder vs. staged vs. committed:** working: my current files I am working with locally. Stagged, the files I dimmed ready to be commited. Commited: taking a snapshot of the staged station and stamping them with time and date
- **Commit:** taking the snapshot and stamping it with time and date
- **Commit message:** a short message summarizing the change in the commit
- **`.gitignore`:** files that should be ignored for tracking/stamping/uploading
- **Remote / `origin`:** a copy of the files that are stored in a different place (cloud)
- **Push:** filing your stamped snapshops (saving online)

## Commands I used

| Command | What it does | When I'd use it |
|---|---|---|
| `git status` |shows you what is and is not in the working staged | to check if the files I want are ready to be commited |
| `git diff` |shows the difference between your uncommited changes and compare it to the las commit | |
| `git add <file>` |adds files to the staging area | |
| `git commit -m "..."` |stamping the working stage with a message | |
| `git log --oneline` |shows the entries of your commits  | |
| `git push` |sending your stamped snapshots to GitHub | |

## What confused me

-

## What I learned

- for git diff: before staging, to review exactly what I changed
- it is OK to commit as many changes as you want. breaking part commits to smaller edits, helps troubleshooting and moving back to a previous step easier, rather than waiting for a big change before you commit

## Interview talking point

One sentence on why version control matters for automation methods (hint: posting 8 in lesson 01 asks for code "managed under version control" and "change control"):

- Every change to a method is a reviewed, dated commit with a reason, so when a run fails I can see exactly what changed since the last good run and roll back. That's the same idea as change control in a regulated lab.

