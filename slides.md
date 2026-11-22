<!--
HOW THIS FILE WORKS
Edit the wording below, save, and the slides rebuild (automatically on GitHub, or run `python3 build.py` locally).

- Slides are separated by a line containing only ---
- Each slide starts with a few "key: value" lines (id, layout, theme, eyebrow, title), then a blank line, then the content.
- "Notes:" starts the speaker notes. They are never shown on the published page.
- Placeholders like [Your name] are reported by the build so you don't forget to fill them in.

LAYOUTS (keep the layout line as it is; just change the words)
  cover     title + one paragraph
  split     "### Files" and "### Pains" with bullet lists
  cards     "### Heading" blocks, optional "icon:" or "tag:" line under a heading
  numbered  like cards, with 01 02 03 04 numbers added automatically
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
title: Git & GitHub: a safety net for collaborative work
meta: [Your name] · [Date]

What they are, why they matter, and how anyone on the team can use them. No coding experience needed.

Notes: Timing: 0:00–1:00. Welcome everyone and set expectations: this session is for everyone, technical or not. We will use plain English and a live demo in the browser, with no terminal. A separate recorded session goes deeper for technical people. Ask the audience to keep their questions for the chat or the Q&A near the end.

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
- Report_final_v2_FINAL_JM-edits.docx
- Report_final_v2_FINAL_JM-edits_USE-THIS-ONE.docx

### Pains
- Whose changes are in this one?
- Did my edit get overwritten?
- Which version is the real one?

Notes: Timing: 1:00–3:00. Start with the relatable pain. Ask: has anyone ever had a file like this? The same thing happens with AI-generated code, only faster: an assistant can change ten files in a minute, and without history it is hard to know what changed or how to go back. Keep this light and quick.

---
id: want
layout: cards
theme: dark2
eyebrow: What we want instead
title: One shared history, with a safety net

### Track
icon: Book
Every change is saved with who made it and why.

### Collaborate
icon: Users
Many people can work at once without overwriting each other.

### Undo
icon: Clock
Go back to any earlier version, at any time.

Notes: Timing: 3:00 (end of the opening). These three ideas are the whole value of version control. Everything else in the session is a way of getting these three things. For the AI-savvy audience: this is exactly what you want around AI-written code. You can let the assistant try things because you can always see what it did and roll it back.

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

> Think of it as Track Changes for any kind of file, plus a shared space to review and agree changes.

Notes: Timing: 3:00–5:00. Keep the distinction simple. Git is the engine that records history. GitHub is the website where that history lives and where people collaborate. People often say "Git" when they mean either. Most of what we use today happens on GitHub, in the browser.

---
id: concepts
layout: numbered
theme: dark
eyebrow: Core ideas
title: Four ideas cover most of it

### Repository
A project folder that remembers its whole history.

### Commit
A saved snapshot, with a short note saying what changed.

### Branch
A safe copy where you can try changes without affecting the original.

### Merge
Bringing finished changes back into the main version.

Notes: Timing: 5:00–7:00. Walk through the four ideas with one analogy each. Repository: a project folder with a memory. Commit: a save point with a note, like a labelled snapshot. Branch: a safe copy to experiment in, which is the single most useful idea for anyone working with AI. Let the assistant try things on a branch and the main version stays safe. Merge: combining the work once you are happy.

---
id: jargon
layout: table
theme: light
eyebrow: Cheat sheet
title: The jargon translator
widths: 32/68

| Term | In plain English |
|---|---|
| Repository (repo) | A project folder with its full history |
| Commit | A saved snapshot with a note |
| Branch | A safe copy for trying out changes |
| Pull request | A proposal: “please review my changes” |
| Merge | Combining approved changes back in |
| Issue | A tracked task, bug or idea |

Notes: Timing: 7:00–8:00. This is the slide people will screenshot, and it becomes the one-page glossary at the end. Do not read every row. Pull request is the one to dwell on: despite the name it is simply a proposal to add your changes, with a place for discussion and review. It is the heart of good practice.

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

Notes: Timing: 8:00–10:00. This is the picture to keep in mind during the demo. Point at each step in order. The key message: nothing reaches the main version until somebody has looked at it. That one habit is what makes collaborative work, with people or with AI, safe.

---
id: demo
layout: demo
theme: mint
eyebrow: Live demo · about 10 minutes
title: GitHub in the browser

1. Browse a repository and read its history
2. Open an issue to describe a task
3. Edit a file, saving it on a new branch
4. Open a pull request
5. Review the changes, then merge

No terminal and no installs, just a web browser.

Notes: Timing: 10:00–20:00 (the demo). Use the prepared sandbox repository with a ready-made issue and a document to edit. Keep every step visible: show the history first so people see the "memory", then make a one-line change, then show the pull request page with the highlighted differences. Backup plan: a short screen recording of the same flow in case the connection fails.

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

Notes: Timing: 20:00–21:30. This is the bridge for the technical audience, who are experienced with AI but new to Git. The question they will recognise: how do I trust what the AI produced? Answer: you do not have to trust it blindly. A branch contains the damage, the history shows what changed, and the pull request is the moment where you or a colleague check the work before it goes live.

---
id: habits
layout: table
theme: light
eyebrow: Good practice
title: Habits that make products reliable
widths: 46/54

| Habit | Why it helps |
|---|---|
| Work on a branch, not on main | Experiments can’t break what works |
| Keep changes small | Easier to review, test and undo |
| Write a clear description | Reviewers see what changed and why |
| Run tests automatically | Problems are caught before merging |
| Get a review before merging | A second pair of eyes, human or AI |
| Protect the main branch | Nothing merges without passing checks |

Notes: Timing: 21:30–23:00. These six habits are the practical takeaway for anyone building software, including with AI. If people remember only one: one task, one branch, one pull request. Small, reviewable changes with automatic tests are what turn a quick AI prototype into a product people can rely on.

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

Notes: Timing: 23:00–24:00. For the non-technical audience this is the reassurance: anything made of text can live on GitHub. Many teams run their documentation, policies and websites this way, because the review step gives them an approval trail for free.

---
id: tryit
layout: cards
theme: light
eyebrow: Take-away
title: Three things to try this week

### Publish a web page
icon: Globe
GitHub Pages turns a repository into a live website, free for public repositories.

### Propose a change
icon: Check
Edit a file in the browser, open a pull request and watch the review flow.

### Track work with issues
icon: Activity
Turn tasks into issues and organise them on a project board.

Notes: Timing: 24:00–25:00. Make this the "I could try that" moment for the non-technical audience. All three can be done in a browser with a free GitHub account, no installation. The sandbox repository in the next steps is the safe place to practise the second one.

---
id: safeguards
layout: grid
theme: dark2
eyebrow: For AI-assisted builders
title: Safeguards worth switching on

### Automatic tests
GitHub Actions runs your tests whenever someone proposes a change.

### Protected main branch
Nothing merges without a review and passing checks.

### Secret scanning
Blocks passwords and API keys before upload. Free on public repos.

### Copilot coding agent
Assign an issue and it opens a pull request for you to review.

Notes: Timing: 25:00–27:00. This is the "new feature to be interested in" moment for the technical audience. Pick two to dwell on. Protected branches plus automatic tests mean AI-written changes cannot reach the main version without passing checks and a review. Secret scanning matters because AI-generated code sometimes includes keys and passwords, and push protection blocks them before they are uploaded (free on public repositories; private repositories need the paid add-on). The Copilot coding agent turns an issue into a pull request, which you review like any colleague’s work. Also worth a mention: Codespaces gives a ready-to-use coding environment in the browser, with a monthly free allowance on personal accounts, so nothing needs installing.

---
id: yourturn
layout: prompts
theme: light
eyebrow: Your turn
title: Where could this help your team?

Put one idea in the chat. For example:

- A document that exists in too many versions
- A process that needs sign-off before it changes
- Something several people edit at once

Notes: Timing: 27:00–29:00. Invite answers in the chat and read out two or three. Link each one back to the idea it fits: tracking, review, or undo. This also tells you what to cover in the follow-up session. Leave a minute for questions.

---
id: next
layout: rows
theme: dark
eyebrow: Next steps
title: Keep going
foot: Thank you · [Your name / contact]

### Try it yourself
Practise in the sandbox repository: [sandbox repo link]

### Keep the glossary
A one-page jargon translator: [glossary link]

### Go deeper (optional)
Recorded technical session with a live demo: [recording link or date]

Notes: Timing: 29:00–30:00. Finish with three clear actions. Everyone can do the first two. The third is for people who want to see Git in action with AI assistance. Thank the audience and share the links in the chat before closing.
