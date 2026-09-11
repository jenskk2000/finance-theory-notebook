# Finance Theory I: source audit and modernization map

Checked 9 September 2026 against [MIT OpenCourseWare](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/).

**Start with the [clickable course map](index.html).** It links every topic to local slides, transcripts, captions, recitations and exercises, and shows the proposed visual activity for each module. This is the mapping and preparation stage; the new lessons and AI tutor have not been built.

## What is available

The downloaded course is a strong foundation for a complete visual adaptation of the materials MIT actually publishes. It is not a complete archive of everything used in the original classroom.

| Material | Available locally | Interpretation |
|---|---:|---|
| Lecture topics | 12 | All official topic pages present |
| Lecture recordings | 0 of 20 | Online URLs and metadata present; no MP4 files |
| Topic video segments | 28 | Views into 20 recordings, using start/end offsets |
| Lecture transcript PDFs | 28 files / 20 distinct documents | Eight identical pairs arise from sessions spanning topics |
| Instructor interview | 1 transcript PDF + captions | Video is online; keep as supplementary context |
| Lecture slide decks | 12 PDFs | Includes the course summary |
| Recitation decks | 8 PDFs | Worked applications across the main topics |
| Problem collection | 1 PDF, 73 physical pages | Three sets and solutions; 136 numbered problems in total |
| Practice exams | 2 PDFs | Midterm and final |
| Exam solutions | 2 PDFs | One for each practice exam |
| Exam review decks | 2 PDFs | Midterm and final reviews |
| Course outline | 1 PDF | Topic structure and textbook chapter references |
| Caption/subtitle files | 85 files | 56 VTT + 28 SRT + 1 WEBVTT; many duplicate representations |
| Administrative/support pages | Present | Syllabus, calendar, readings, instructor insights and resource indexes |
| Referenced books | Not present | Main textbook plus three supplementary books are bibliographic references |
| Acid Rain case handout | Not found as a standalone asset | Mentioned in the syllabus/outline; do not invent the missing handout |

There are **57 PDF files, representing 49 distinct PDFs and 1,356 physical pages after exact deduplication**. Lecture captions extend across approximately 25 hours of recordings; this is a caption-derived estimate, not a playback measurement. The interview is additional.

## What the live comparison established

- The live and local content maps both contain **185 identifiers**, with no added or removed identifiers.
- Fetched all **166 course JSON documents** identified by the live map, including root course metadata. Saved their current contents under `evidence/live/`.
- **135 matched after link normalization; 31 had field differences.** All 29 video records now use language-tagged arrays for transcripts/captions instead of the older single-file fields. All 29 still reference the same local transcript and caption filenames. The other differences are the instructor search URL, interview player markup and an added interview metadata tag. The interview's introductory prose is unchanged.
- Fetched and SHA-256 compared all **57 PDFs and 85 caption files: 142/142 matched exactly**. No missing locally referenced resource files were found.
- The four course image assets were inventoried but not compared byte for byte. Shared website scripts, styling and fonts were outside the teaching-content comparison.
- Online video playback and archive downloads were not tested. No videos or books were downloaded.

These results establish source coverage and file identity. They do not establish that extracted equations are correct, that every link outside MIT works, or that new lessons have full pedagogical coverage.

Evidence: [inventory.json](inventory.json), [metadata comparison](evidence/metadata-comparison.json), [file comparison](evidence/asset-comparison.json). Page-by-page text extraction of all 57 PDFs is under `extracted/`; formulas and figures still require visual inspection when authoring lessons.

## The course map

The sequence follows the [official lecture structure](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/video-lectures-and-slides/) and [calendar](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/calendar/). Every row has a local slide deck and the corresponding lecture transcripts. Visual activities below are proposed additions.

| Module | Sessions | Additional practice | Proposed visual treatment |
|---|---|---|---|
| 1. Introduction | 1 | Concept checks to author | Household/company balance sheet and financial decision map |
| 2. Present value | 2–4 | Recitation 1; problem set 1 | Cash-flow timeline; discounting, compounding and inflation controls |
| 3. Fixed income | 4–7 | Recitation 2; problem set 2 | Bond price/yield curves, duration and immunization experiments |
| 4. Equities | 8 | Recitation 3; problem set 3 | Dividend, reinvestment and growth valuation waterfall |
| 5. Forwards and futures | 9–10 | Recitation 4 | Carry/no-arbitrage model and daily margin simulation |
| 6. Options | 10–12 | Recitation 5 | Payoff builder, binomial tree and replicating portfolio |
| 7. Risk and return | 12–13 | Relevant exam/review questions to map | Return distributions and repeated-path experiments |
| 8. Portfolio theory | 13–15 | Recitation 6 | Correlation controls and an interactive efficient frontier |
| 9. CAPM and APT | 15–17 | Recitation 7 | Security market line, beta and factor exposures |
| 10. Capital budgeting | 17–18 | Recitation 8 | Project cash flows, NPV profiles and real-option trees |
| 11. Efficient markets | 18–20 | Relevant exam/review questions to map | Information arrival, prediction and backtesting experiments |
| 12. Course summary | 20 | Final exam and review | Integrated case and connected concept map |

The original calendar places the midterm after session 11, before the last options segment. Preserve this if offering an original-course mode; a new module-based path can place its checkpoint after the entire options module, clearly labeled as a revised sequence.

## Practice material and source anchors

The [MIT problem sets page](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/problem-sets/) describes the collection added in December 2019. It covers the first three quantitative topics; it is not a problem set for every module.

| Set | Numbered problems | Physical PDF pages: questions | Physical PDF pages: solutions |
|---|---:|---|---|
| Present value | 35 | 7–14 | 42–48 |
| Fixed income | 65 | 15–33 | 49–63 |
| Common stock | 36 | 34–41 | 64–72 |

The PDF has front matter, so printed page numbers differ from physical page numbers. Store both. Split questions from solutions in the learner interface; retain their original identifiers and page anchors. Exact question-to-concept and exam-question mappings remain authoring work.

The [recitations](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/recitations/) and [exam materials](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/exams/) provide further applications. Preserve their attribution to Yichuan Liu and Amir Khandani respectively.

## How to turn this into the local course

**Build a source-backed learning experience around these materials.** Every original document stays accessible, while the new course explains its concepts through shorter lessons and manipulable models.

1. **Complete the source model.** Use session IDs and timestamps for recordings; topic IDs for modules; hashes for distinct files; physical pages and printed slide numbers for documents. The inventory already provides these file/session relationships and MIT's per-segment slide-coverage notes. Parse captions into timed passages, align slides and worked examples, and map every original problem. Keep the same full-session transcript attached to both topic segments without feeding duplicate copies to AI.
2. **Build one full pilot module: Present Value.** It has three lecture segments, a slide deck, a recitation and 35 original problems with solutions. Build short lessons with a cash-flow timeline, worked derivations, source links, original exercises and graded hints. Preserve all substantive source concepts and examples, even when some are placed in optional depth sections.
3. **Validate the pilot before applying its pattern to all 12 modules.** Audit concept/example coverage against the source pages and transcript intervals. Check calculators with deterministic reference calculations and original solutions. Visually check equations and charts. Ensure keyboard and small-screen use works, and that the full lesson remains useful without AI connectivity.
4. **Expand and integrate.** Apply the approved learning pattern across all topics, then bring in the recitations, both exams, reviews and interview. Add cumulative problems and spaced revisits. Keep a simple resume point and learning history rather than a large tracking dashboard.

Suggested lesson rhythm: **predict → explore a visual model → read/watch the relevant source → solve → receive feedback → revisit**. The original recordings remain an optional depth route alongside the new visual explanations.

## AI's role

- During authoring: identify concepts and misconceptions, draft explanations and new practice variants, and propose visuals. Each output must name the supporting original pages or timestamps and be reviewed before becoming course content.
- During learning: explain the selected passage or visual, give progressively stronger hints, compare reasoning with the original solution, and suggest a relevant prerequisite lesson.
- Calculations: use tested code for valuations, returns, payoffs and portfolio arithmetic. AI explains the calculation and its assumptions.
- Provenance: label original MIT text, AI-assisted adaptations and newly researched examples. Keep a source-coverage record so a polished summary cannot silently replace unrepresented material.
- Offline behavior: store lessons, sources, search, models and progress locally. A live AI tutor is a separate capability; a local interface alone does not make a hosted AI service work offline. The model/provider choice remains open.

## Meaning of “ALL” and “modern”

“All” should mean every distinct published teaching asset is mapped, accessible and accounted for, with substantive concepts, examples and original exercises carried into the new learning path. Website boilerplate and duplicate file encodings are preserved in the download but need not become separate lessons. Missing books and the case handout remain explicit gaps until supplied or replaced with clearly labeled new material.

The [reading list](https://ocw.mit.edu/courses/15-401-finance-theory-i-fall-2008/pages/readings/) references *Principles of Corporate Finance*, 9th edition, as the textbook. The bibliography is available; the book text is not. Do not imply AI has used it without obtaining and indexing it.

Modernize the teaching interface and explanations first. Preserve historical 2008 examples and assumptions as historical context. Add contemporary examples only with dated sources and explicit labels; changing tax rules, instruments or market evidence requires separate verification. Carry original license and credit metadata forward into derived lessons.

**Recommended next build:** the local course shell plus a complete Present Value pilot, using this map and inventory as its source layer. The rest of the course should remain visibly mapped but not marked as completed lessons until actually authored and checked.

## Map verification

The generated map was opened and visually inspected in the in-app browser. Topic filtering and expandable lecture details worked; all local file links resolved in a filesystem check. The map also opens directly from `index.html` without a build step. The temporary browser preview is served only on 127.0.0.1:8765.
