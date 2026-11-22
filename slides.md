<!--
HOW THIS FILE WORKS
Edit the wording below, save, and the slides rebuild (automatically on GitHub, or run `python3 build.py` locally).

- Slides are separated by a line containing only ---
- Each slide starts with a few "key: value" lines (id, layout, theme, eyebrow, title), then a blank line, then the content.
- Optional: "Notes:" starts speaker notes (never shown on the published page). Personal notes live in speaker-notes.md, which is git-ignored.
- Placeholders like [Your name] are reported by the build so you don't forget to fill them in.

LAYOUTS (keep the layout line as it is; just change the words)
  cover     title + one paragraph
  split     "### Files" and "### Pains" with bullet lists
  cards     "### Heading" blocks, optional "icon:" or "tag:" line under a heading
  numbered  like cards, with 01 02 03 04 numbers added automatically ("start: 5" begins at 05)
  grid      like cards, in a 2x2 grid
  table     a markdown table, "widths:" sets the column split
  flow      numbered list: "1. Step title | short description"
  demo      numbered list + a final plain line
  prompts   a lead paragraph + bullet list
  rows      "### Heading" blocks, numbered automatically

ICONS you can use: Book, Users, Clock, Lightning, Lock, Verified, Globe, Check, Activity
A line starting with > becomes the highlighted callout box.
-->

---
id: cover
layout: cover
theme: dark
eyebrow: Introduction · 30 minutes
title: Git & GitHub: a system for collaborative work
meta: Guy Roberts · Wed 25th Nov

What they are, why they matter, and how to use. No coding experience needed.

---
id: familiar
layout: split
theme: light
eyebrow: The problem
title: Sound familiar?

### Files
- Report_final.docx
- Report_final_v2.docx
- Report_final_v2_FINAL.docx
- Report_final_v2_FINAL_July-edits.docx
- Report_final_v2_FINAL_July-edits_USE-THIS-ONE.docx

### Pains
- Whose changes are in this one?
- Did my edit get overwritten?
- Which version is the real one?

---
id: want
layout: cards
theme: dark2
eyebrow: What we want instead
title: A shared history, with a safety net

### Track
icon: Book
Every change is saved with who made it and why.

### Collaborate
icon: Users
Many people can work at once without overwriting each other.

### Undo
icon: Clock
Go back to any earlier version, at any time.

---
id: gitgithub
layout: cards
theme: light
eyebrow: Core ideas
title: Git vs GitHub

### Git
tag: On your computer
The tool that records every change to your files, so you can see what changed and go back.

### GitHub
tag: Online
A shared home for that history, with reviews, task tracking and project boards for working together.

> In the same way that email exists independently of Gmail. Gmail is just the service built on top of email.

---
id: concepts
layout: numbered
theme: dark
eyebrow: Core ideas
title: Common Actions (1/2)

### Repository
A project folder that records its whole history.

### Commit
A saved snapshot, with a short note saying what changed.

### Branch
A safe copy where you can try changes without affecting the original.

### Merge
Bringing finished changes back into the main version.

---
id: concepts2
layout: numbered
theme: dark
start: 5
eyebrow: Core ideas
title: Common Actions (2/2)

### Issue
A tracked task, bug or idea, so nothing gets lost in an email thread.

### Pull request
A proposal: “please review my changes before they go in.”

### Review
Others read the changes, leave comments, and approve them.

### Diff
The before-and-after view that highlights exactly what changed.

---
id: flow
layout: flow
theme: dark2
eyebrow: How a change travels
title: A change, from start to finish

1. Make a branch | A safe copy to work in
2. Edit and commit | Save changes with a note
3. Open a pull request | Ask others to take a look
4. Get a review | Comments and approval
5. Merge | Join the main version

> The main version stays untouched until the very last step.

---
id: demo
layout: demo
theme: mint
eyebrow: Live demo
title: Let's see it in action

Over to GitHub, in the browser.

---
id: whyai
layout: cards
theme: dark
eyebrow: Why it matters
title: Even more so when AI writes the code

### AI works fast
icon: Lightning
An assistant can change many files in minutes. History shows exactly what it changed.

### Branches keep experiments safe
icon: Lock
Let the AI try things on a branch. The working version stays untouched.

### Pull requests give you the review
icon: Verified
You see every change side by side before anything is accepted.

---
id: habits
layout: table
theme: light
eyebrow: Good practice
title: Useful habits to adopt
widths: 46/54

| Habit | Why it helps |
|---|---|
| Work on a branch, not on main | Experiments can’t break what works |
| Keep changes small | Easier to review, test and undo |
| Write a clear description | Reviewers see what changed and why |
| Run tests automatically | Problems are caught before merging |
| Get a review before merging | A second pair of eyes, human (or AI) |
| Protect the main branch | Nothing merges without passing checks |

---
id: beyond
layout: grid
theme: dark
eyebrow: Beyond code
title: It’s not just for code

### Documentation
Guides and handbooks with a full edit history.

### Policies and processes
Changes are reviewed and approved before going live.

### Websites and content
Edit pages in the browser and publish via a pull request.

### Planning and tracking
Issues and boards keep tasks, owners and status together.

---
id: tryit
layout: cards
theme: light
eyebrow: Take-away
title: Things to try this week

### Publish a web page
icon: Globe
GitHub Pages turns a repository into a live website, free for public repositories.

### Propose a change
icon: Check
Edit a file in the browser, open a pull request and watch the review flow.

### Track work with issues
icon: Activity
Turn tasks into issues and organise them on a project board.

---
id: safeguards
layout: grid
theme: dark2
eyebrow: For AI-assisted developers
title: To explore

### Automatic tests
GitHub Actions runs your tests whenever someone proposes a change (e.g. custom WP plugins)

### Secret scanning
Blocks passwords and API keys before upload.

### Dependabot
Spots outdated or vulnerable libraries and opens a pull request to update them.

### AI coding agents
Copilot, Claude, Cursor and others can take an issue and hand back a pull request for you to review.

---
id: next
layout: rows
theme: dark
eyebrow: Next steps
title: Keep going
foot: Thank you · [Your name / contact]

### Go deeper (optional)
Recorded technical session with a live demo...


