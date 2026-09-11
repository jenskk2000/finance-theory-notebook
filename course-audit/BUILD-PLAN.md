# A complete local, visual Finance Theory I course

Status: implementation plan, 9 September 2026. Based on the verified [source audit](REPORT.md), [course map](index.html) and [machine-readable inventory](inventory.json). The modern course is not yet built.

## 1. The finished experience

Build an English-language course that teaches the full substance of the published MIT course through detailed written explanations, interactive visual models, worked examples and practice. All original lectures, slides, transcripts, recitations, problems and exams remain accessible locally.

A learner can finish the course without an internet connection, a subscription, a working AI service or having to buy the referenced textbook. AI helps author the course; the finished explanations, hints and solutions are saved as course content. An optional conversational tutor can be added without becoming a dependency.

The course opens through one local launcher. The home screen has a course outline and a Continue button. Lessons combine text, figures, mathematics, exercises and relevant video excerpts. A source drawer opens the original slide, PDF page or recording timestamp. A library provides the complete original materials.

Use two views of the same content: the modern module-based learning path, and the original 20-session sequence. Progress belongs to the shared lesson objects, so switching views does not create duplicate work.

## 2. What “complete” means

The verified baseline includes 12 topic modules, 20 lecture recordings represented by 28 topic segments, 20 distinct lecture transcripts, 12 lecture decks, 8 recitation decks, 136 numbered problems with solutions, 2 practice exams, 2 exam solutions, 2 exam review decks, a course outline and the supplementary instructor interview. Include the syllabus, calendar and bibliography in the library.

Preserve all substantive definitions, assumptions, derivations, examples, counterexamples, applications, limitations, classroom explanations and exercises appearing in these published materials. Repetition may be consolidated, but every occurrence remains traceable to the corresponding lesson. Retain complete original recordings so the teacher's delivery and context remain available.

Do not equate linking a PDF with teaching its contents. Each substantive source item must map to an implemented lesson, worked example, visual explanation or exercise. Detailed derivations can be expandable, but must actually be written and included.

The referenced commercial books and a standalone Acid Rain case handout are not present. The course cannot claim to reproduce those unseen materials. During gap analysis, identify concepts required by the published lessons that would otherwise rely on them, then write self-contained supplementary explanations and a clearly labeled replacement case. Seek accessible primary or educational sources where needed. Record unresolved dependencies explicitly; do not call the complete course finished while a required learning dependency remains unresolved.

## 3. Preserve the sources and obtain the videos

Keep the existing download unchanged. Put the modern course in a new `local-course/` directory alongside it. Use the existing `course-audit/` inventory rather than making a competing catalogue.

1. Check all 20 official archive download URLs and the interview URL. The first lecture's MP4 endpoint has already returned HTTP 200; the other downloads still need verification.
2. Download each unique lecture once with resumable transfers, temporary filenames and completion checks. The recorded size estimate is approximately 3.5 GB for the 20 lectures; verify actual disk requirements before transfer. Keep room for originals, the self-contained package and temporary media processing.
3. Verify each completed video by inspecting duration, audio/video streams and decodability. Compare its duration with caption endpoints and review the start, end and each topic boundary. Record hashes and download provenance.
4. Play topic and concept clips as time ranges of the original local video. A clip has a session ID, start time and end time; it does not require a second video file. Make the player stop at the clip boundary and offer Continue full lecture.
5. Define finer concept boundaries using the transcript and then check them against the recording. Do not cut through a derivation, a question or its answer. Use variable clip lengths appropriate to the explanation.
6. Export physical clips only when useful for portability. Preserve originals; retime subtitles and use accurate encoding where keyframe-only cuts would miss the intended boundary. Verify exported clips for audio/video synchronization and caption alignment.

Download the interview as supplementary material if its official file is available. A failed source remains visible as a gap; transcripts are a fallback, not evidence of a successful video download. A media-processing tool such as FFmpeg will be needed for validation and optional exports; it was not found on the current shell PATH.

## 4. Build a coverage model before rewriting

Create stable records for sources, sessions, segments, concepts, lessons, examples, exercises and assessments. Every source reference includes the original filename/hash and either a physical PDF page plus printed slide/page number, or a video time range.

Read every distinct PDF and the full transcripts. The existing text extraction is a starting point: equations, tables and figures require visual checking. Examine video/board content where the transcript and slides do not capture what is being taught.

For every substantive source span, record:

- What is taught: concept, argument, derivation, example, question, limitation or application.
- Where it appears: document/page and recording/timestamp.
- Where it will be taught in the new course.
- Status: identified, drafted, checked or included in the finished course.
- Whether it repeats another item; keep all source references when consolidating.

Mark administrative remarks and genuine repetition explicitly rather than silently dropping them. Reconcile the inventory in both directions: each source item has a destination, and each new factual claim has supporting evidence or a clear label as a new example. A second review pass uses the original material to look for omissions rather than reviewing only the rewritten lesson.

## 5. Course structure and visual treatment

Keep MIT's 12-topic order. Determine the number of individual lessons after coverage mapping; do not force the material into an arbitrary lesson count. Target a manageable main lesson, with full derivations and additional examples available immediately alongside it.

| Module | Detailed teaching to retain | Interactive treatment | Original practice |
|---|---|---|---|
| Introduction | Financial decisions, assets/liabilities, valuation principles, markets and opportunity cost | Household/company balance sheet and a financial decision map | Lecture examples; new checks labeled as additions |
| Present value | PV/NPV, discounting, compounding, annuities, perpetuities, real/nominal quantities | Move cash flows along a timeline; vary rates, growth and timing | Recitation 1; all 35 problems |
| Fixed income | Bond cash flows, term structure, spot/forward rates, yields, duration, convexity and hedging | Yield-curve and bond-price explorer; construct an immunized position | Recitation 2; all 65 problems |
| Equities | DCF/dividend models, earnings, payout, reinvestment and growth opportunities | Trace earnings into dividends and reinvestment; valuation sensitivity | Recitation 3; all 36 problems |
| Forwards and futures | Contracts, carry, arbitrage relations, marking to market and hedging | Cash-and-carry trade and daily margin-account simulation | Recitation 4; mapped lecture/exam examples |
| Options | Payoffs, strategies, replication, binomial pricing and pricing assumptions | Combine calls/puts; expand a binomial tree; reveal replication step by step | Recitation 5; mapped lecture/exam examples |
| Risk and return | Return measurement, uncertainty, expected return, risk measures and horizons | Distributions and simulated paths with explicit assumptions | Mapped lecture/review/exam questions |
| Portfolio theory | Covariance, correlation, diversification, optimization and efficient trade-offs | Change weights/correlation and see the opportunity set and frontier | Recitation 6; mapped lecture/exam examples |
| CAPM and APT | Beta, systematic risk, pricing relations, assumptions, evidence and factor models | Security market line and factor exposure explorer | Recitation 7; mapped lecture/exam examples |
| Capital budgeting | Incremental cash flows, decision criteria, NPV/IRR, interactions and real options | Project builder, NPV profile and investment decision tree | Recitation 8; clearly labeled replacement case if needed |
| Efficient markets | Forms of efficiency, implications, tests, evidence and limitations | Information arrival and prediction experiments; examine misleading evidence | Mapped lecture/review/exam questions |
| Summary | Connections across valuation, uncertainty and corporate decisions | Linked concept map and an integrated decision case | Both review decks and final assessment |

The table sets the design direction, not a substitute for the exhaustive concept inventory. Preserve any source topic beyond this table, including formula derivations or pricing models identified during the full review.

Add a short optional foundations section: algebra, exponents/logarithms, summation, probability, expectation, variance/covariance, reading charts and the calculus needed for particular derivations. Link to a prerequisite explanation exactly where it becomes necessary. Definitions and notation must be available without leaving the course.

## 6. The lesson template

Each lesson should contain:

1. A concrete question or decision, learning objectives and prerequisite links.
2. A prediction prompt that gives the visual exploration a purpose.
3. An interactive diagram or model, with sensible defaults, reset controls, units and accessible alternatives.
4. A detailed explanation connecting intuition to the formal mathematics. Define every symbol and state assumptions and validity conditions.
5. A derivation that can be revealed step by step, including why each step follows.
6. At least one fully worked source example where available, retaining its original numbers and assumptions.
7. Common mistakes, edge cases and a contrasting example that tests the distinction.
8. Original practice with progressive hints, followed by full reasoning and the original solution reference.
9. A short retrieval check and a meaningful transfer question.
10. Source links to every relevant original page and timestamp, plus the full recording.

Not every explanation needs animation. Use motion or controls when changing an assumption reveals a relationship. Render plots and equations from deterministic code; do not use generated illustrations as mathematical evidence. Simulations identify their assumptions and use reproducible seeds when needed.

Example: for an annuity lesson, predict how payment timing changes value, move payments on a timeline, derive the geometric-series result, reproduce a source problem, compare beginning/end-of-period payments and solve a changed scenario. Keep the full original derivation and relevant video passage accessible.

## 7. Practice and assessment

Import all 136 numbered problems with every subpart, preserving numbering and source anchors. Map every recitation example and every exam question/subpart; count those during ingestion rather than estimating from page totals. Retain all original solutions and review material.

Use separate learning and exam modes. Learning mode offers hints and explanations. Exam mode hides solutions and tutoring during the attempt, then offers review. Preserve the original midterm placement after session 11 in the original-session view; label any revised checkpoint placement in the modern path.

Numeric answers use explicit units, rounding rules and tolerances checked against reference calculations. Symbolic answers need equivalent-form handling or a transparent self-check rubric. Written reasoning receives a rubric and model answer; optional AI feedback is advisory, not an authoritative grade.

Keep newly generated variants clearly separate from MIT originals. Validate their solvability and solutions before inclusion. Preserve historical numerical assumptions; do not quietly replace them with contemporary values.

Track lesson completion separately from demonstrated understanding. Offer a simple list of concepts to revisit based on attempted questions. Allow notes, bookmarks, reset and export/import of progress; avoid requiring a complex study dashboard.

## 8. AI and offline operation

Use AI primarily during production to propose lesson structure, explanations, comparisons, hints and practice variants from bounded source passages. Save accepted outputs into the course so they work offline. Review all mathematics and source coverage before marking content ready.

An optional tutor can use the selected lesson, original passages and the learner's question. Require citations to local pages/timestamps, incremental hints before full answers and an explicit statement when available sources do not support an answer. Keep assessment solutions out of its exam-mode context. Do not let model-generated text directly execute code.

The optional tutor can eventually support a local model or a hosted service. The default complete course does not need either. Hosted credentials belong in a local backend rather than browser code. If a hosted provider is configured later, make the transmitted content clear and send only the context required for the question.

Modern examples are supplements with dated sources. The original 2008 course stays identifiable, and its scientific/economic claims and historical context are preserved with any later commentary clearly distinguished.

## 9. Local architecture and packaging

Use a browser-based application with a small local launcher/server bound to localhost. Build the written course from structured lesson files; use reusable visual components and a tested calculation library. Finalize framework and dependency versions at implementation after inspecting the environment.

Proposed layout:

```text
local-course/
  app/                  application and reusable visual components
  content/              modules, lessons, glossary, questions and solutions
  sources/              packaged original PDFs, captions, videos and credits
  manifests/            source references, clip ranges and coverage records
  data/                 local search index and validated example datasets
  tests/                calculation, content, accessibility and offline checks
  dist/                 built course
  Start Course.command  one local entry point
  README.md             launch, backup, restore and update instructions
```

Development may reference the existing sources to save space. The final distribution must contain its own sources and runtime requirements, use relative paths and work after being moved to a different folder. Do not depend on `/Users/jenskristian/Downloads/15`, the audit preview server, external fonts, CDNs, remote video embeds or runtime package downloads.

Keep user progress independent of source content. Use export/import and a stable local origin or local progress file so a browser-origin change or course update does not lose work. Do not put a final package recursively inside itself when copying source assets.

Carry forward MIT attribution, original license metadata and individual credits. Mark adaptations clearly. A later public release would be a separate distribution task; this plan targets personal local use.

## 10. Implementation phases and completion gates

| Phase | Work | Required evidence before moving on |
|---|---|---|
| 1. Source acquisition | Preserve archive; obtain/verify recordings; canonicalize transcripts/captions | All published teaching assets accounted for; downloads readable; gaps explicit |
| 2. Curriculum extraction | Review all sources; map concepts, examples, problems, prerequisites and time ranges | Every substantive source span classified and assigned; missing prerequisites identified |
| 3. Course shell and pilot | Navigation, local reader/player/search; complete Present Value module | Full source coverage for PV; all 35 problems/subparts; checked visual models; offline use |
| 4. Valuation modules | Introduction, fixed income, equities, forwards/futures and options | Source reconciliation, original practice and validated calculations for each module |
| 5. Risk and synthesis | Risk/return, portfolio theory, CAPM/APT, capital budgeting, efficient markets and summary | All remaining substantive material taught; derivations/examples checked |
| 6. Assessment and completeness | Integrate both exams/reviews, recitations, foundations, interview and gap supplements | All questions/solutions accounted for; no unresolved required teaching dependency |
| 7. Offline release | Bundle sources/runtime, accessibility review, progress backup and installation test | Launch from a new folder with networking disabled; finish representative lessons and restore progress |

The pilot is a quality checkpoint, not the final scope. Review its visual style and level of detail before repeating the pattern, and carry the work through all modules. Estimate effort after source extraction and the pilot reveal the actual lesson count and authoring/review cost; a reliable full-course estimate is premature now.

## 11. Definition of done

- Every published lecture/session and distinct source document is available in the local library, including verified local video files.
- Every substantive source concept, derivation, example and limitation is represented in the course with an accurate source anchor; no unexplained omissions remain.
- All 136 original numbered problems and their subparts, all recitation examples, and all practice exam/review items are represented and checked.
- Required explanations and prerequisites are complete without mandatory textbook access or AI connectivity; unavoidable missing original materials are clearly distinguished from the new supplements that cover their learning dependency.
- Interactive mathematics passes reference and edge-case checks, and diagrams agree with the formulas and written explanations.
- Original and adapted solutions are checked; extraction errors and source inconsistencies are resolved or explicitly documented.
- Video boundaries and captions are synchronized. Full recordings are reachable from clips.
- Every lesson works with keyboard navigation and readable layouts; essential meaning is not conveyed by color or motion alone.
- The packaged course works with networking disabled, outside the development directory, with local search and no broken media/source links.
- Progress survives restart and export/import. The learner sees one obvious starting point and can resume easily.

The first implementation deliverable is a verified local source/video library and exhaustive curriculum inventory, followed by the course shell and a complete Present Value pilot. The final deliverable is the entire course, not a polished sample with placeholder modules.
