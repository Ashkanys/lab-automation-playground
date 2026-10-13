# Lesson 01 — Job market

**Goal:** read 10 real job postings and find out which skills employers ask for most. In week 12 you'll come back to the tally at the bottom and mark what this repo now shows.

**How to do it:**

1. Find a posting (see "Where to look" below).
2. Paste the whole posting into `postings_private.md`, which stays on your computer (see the note at the bottom).
3. Fill in its block below with a few words per line. You're looking for patterns, not copying the ad.
4. After all 10, fill in the skills tally and the last three sections.

**Where to look:** LinkedIn Jobs, Indeed, company career pages, and the Job Postings board on [labautomation.io](https://labautomation.io/). Useful search terms: "automation scientist", "lab automation", "liquid handling", "high-throughput screening", "Hamilton", "Tecan", "Biomek".

**Tips:**

- Company type is one of: pharma, biotech, CRO (contract research organisation), academic, or instrument vendor.
- Mark anything listed as "preferred" or "nice to have" with *(nice)*, so you can tell it apart from the requirements.

---

## The postings

### 1
- **Job title:** Bioprocess / Automation Engineer II
- **Company type:** biotech (proteomics platform, R&D + manufacturing)
- **Degree and years asked for:** BS/MS in engineering + 4 years
- **Robots and instruments:** Hamilton STAR (preferred), Opentrons, Agilent Bravo, Tecan; the company's own instrument
- **Software:** not named
- **Coding / data:** Python or C#; modular, maintainable, traceable code; data analysis
- **Assays and science:** NGS, PCR/qPCR, proteomics, immunoassays; debugging fluidics + robotics + chemistry; V&V, SOPs, transfer to manufacturing

### 2
- **Job title:** AI Lab Automation Scientist (1-year contract)
- **Company type:** tech company R&D lab
- **Degree and years asked for:** PhD + 3 years
- **Robots and instruments:** microcontrollers (Arduino, ESP32, Raspberry Pi), sensors, SPI/I2C/UART; Hamilton, Tecan, Bravo *(nice)*
- **Software:** GitHub, AI agent harnesses; PyLabRobot *(nice)*
- **Coding / data:** strong Python; drivers/APIs; data pipelines for machine learning; closed-loop "AI runs the experiment" systems
- **Assays and science:** molecular biology, assay development, cell/tissue culture, synthetic biology; protein engineering *(nice)*

### 3
- **Job title:** Senior Lab Process Automation Engineer
- **Company type:** biotech (clinical cancer diagnostics)
- **Degree and years asked for:** BS + 5 years, or MS/PhD + 3 years as an NGS automation programmer
- **Robots and instruments:** liquid handlers, lab robotics
- **Software:** Hamilton VENUS 4 or 6 (**required**)
- **Coding / data:** deploying methods with GitHub/GitLab; data analysis
- **Assays and science:** NGS; user requirements, IQ/OQ/PQ, SOPs, vendor management, mentoring

### 4
- **Job title:** Automation Engineer
- **Company type:** biotech (ML-driven antibody engineering)
- **Degree and years asked for:** no degree stated; 3+ years of industry liquid-handling experience
- **Robots and instruments:** Hamilton STAR/Vantage (strongly preferred), Tecan, Beckman Biomek, Agilent Bravo, Analytik Jena
- **Software:** VENUS, FluentControl, Biomek software, VWorks, Composer
- **Coding / data:** experimental design, data analysis; working with the in-house software team
- **Assays and science:** high-throughput antibody production and characterisation *(nice)*; maintaining instruments, supporting lab users, SOPs

### 5
- **Job title:** Lab Automation Software Engineer
- **Company type:** biotech (sequencing service)
- **Degree and years asked for:** BS/MS/PhD (CS, robotics, biology); 3+ years Python, 1+ year lab work, 1+ year liquid handlers
- **Robots and instruments:** Opentrons, Hamilton, a fleet of lab robots; 3D printing / CAD *(nice)*
- **Software:** Flask/Django, Docker, Ansible, AWS, Terraform, Linux, OpenCV, in-house LIMS; C#/.NET *(nice)*
- **Coding / data:** production-quality Python, AI agent tools, monitoring and telemetry for many devices
- **Assays and science:** molecular biology protocols, DNA and RNA sequencing

### 6
- **Job title:** Automation Engineer III
- **Company type:** biotech (molecular testing lab)
- **Degree and years asked for:** BS + 8 years
- **Robots and instruments:** Tecan, Beckman, PerkinElmer
- **Software:** not named
- **Coding / data:** advanced Excel
- **Assays and science:** nucleic acid extraction, NGS, molecular assays; precision and accuracy, Six Sigma; leading a team

### 7
- **Job title:** Automation Engineer (Protein Sciences)
- **Company type:** pharma
- **Degree and years asked for:** BS + 10, MS + 8, or PhD + 2–5 years
- **Robots and instruments:** integrated workcells, liquid handlers, lab robotics
- **Software:** scheduling software, LIMS, SharePoint, Smartsheet
- **Coding / data:** Python/Java/C++ *(nice)*; structured data capture for data science
- **Assays and science:** antibody discovery, protein expression and purification *(nice)*; qualification, root cause analysis; people manager

### 8
- **Job title:** Automation Engineer III (Manufacturing)
- **Company type:** instrument / reagent maker (manufacturing site)
- **Degree and years asked for:** BS + 5 or MS + 3 years, including 3+ years of Hamilton VENUS
- **Robots and instruments:** Hamilton STAR/STARlet/Vantage, sealers, labelers, pumps; CO-RE 96 head, iSWAP, plate readers, HPLC, PLCs *(nice)*
- **Software:** VENUS + HSL (Hamilton's scripting language); Git, SolidWorks, Arena PLM, Oracle *(nice)*
- **Coding / data:** statistics (gage R&R, capability, DOE); daily AI tools; Python *(nice)*
- **Assays and science:** liquid classes, carry-over, volume accuracy and precision, liquid-handling QC methods; TADM, cLLD/pLLD *(nice)*; ISO 9001, IQ/OQ/PQ, FMEA, change control

### 9
- **Job title:** Senior Automation Service Engineer
- **Company type:** biotech (clinical cancer diagnostics)
- **Degree and years asked for:** BS + 5–8 years of service / instrument support
- **Robots and instruments:** Hamilton, QIAsymphony, TapeStation, Illumina sequencers
- **Software:** asset management system; liquid handler programming *(nice)*
- **Coding / data:** equipment performance trends
- **Assays and science:** NGS workflow; CLIA, GMP, IQ/OQ/PQ, preventive maintenance, root cause, Lean/Six Sigma; on-call

### 10
- **Job title:**
- **Company type:**
- **Degree and years asked for:**
- **Robots and instruments:**
- **Software:**
- **Coding / data:**
- **Assays and science:**

---

## Skills tally

After all 10 postings, count how many mention each skill. Add rows for anything that keeps coming up and isn't listed. Leave the last column empty until week 12.

Counted over postings 1–9 (*(nice)* mentions included); add posting 10 when it's in.

| Skill | Postings (out of 10) | Shown in this repo? |
|---|---|---|
| Hamilton (VENUS) | 7 (VENUS named in 3) | |
| Tecan (FluentControl / EVOware) | 4 | |
| Beckman (Biomek) | 2 | |
| Echo acoustic dispensing | 0 | |
| Other robots: Agilent Bravo 3, Opentrons 2, PerkinElmer 1, Analytik Jena 1, QIAsymphony 1 | | |
| Python | 5 | |
| Excel / data handling | 5 | |
| Sample sheets / worklists | 0 | |
| Assay development or optimisation | 3 | |
| Cell-based assays | 1 | |
| Liquid classes / pipetting optimisation | 2 | |
| Pipetting QC (gravimetric / photometric) | 2 | |
| Plate readers | 1 | |
| Scheduling software (Green Button Go, Cellario, Momentum) | 1 | |
| LIMS / ELN | 3 | |
| Troubleshooting and instrument maintenance | 7 | |
| GLP / GMP / method validation | 6 | |
| Writing SOPs and documentation | 7 | |
| Training other scientists | 5 | |
| NGS / PCR / molecular biology | 6 | |
| Root cause analysis | 6 | |
| Git / GitHub | 4 | |
| Using AI tools | 4 | |
| Statistics / Six Sigma / DOE | 3 | |
| Antibody / protein work | 3 | |
| Electronics / PLC / CAD | 3 | |

## Words I didn't know

Write them down as you go; we'll go through them together.

- FMEA
- CO-RE
- 

## What I learned

- Hamilton is the dominent platfrom when it comes to liquid handling, and many job posting require Venus. It would be also good to update my knowledge on the biological assays needed (qPCR) or NGS. and in the relm of biopharma lab operation, small-volume pipetting is very important.

## Interview talking point

One sentence about what employers want and how you're preparing for it:

- I am actively improving my skill sets to prepare myself for more lab automation roles.

---

**Why the full postings live in a separate file:** this repo is public on GitHub, so anyone can read what's committed here, including a current employer who might notice which companies you're looking at. The posting text also belongs to the company that wrote it. `postings_private.md` matches a rule in `.gitignore`, the file that tells git which files to never track or upload.
