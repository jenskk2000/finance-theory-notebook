# Finance Theory I · local course

This local-first learning interface for MIT OpenCourseWare 15.401 Finance Theory I (Fall 2008) provides the full 12-module source map, a complete authored Introduction lesson, an authored Present Value learning pilot, and concise guided overviews for modules 03–12. The overviews are not claimed as complete authored lessons.

The Present Value pilot currently includes one substantive authored lesson with six navigable sections: an interactive cash-flow timeline, derivations, the MIT lighting-system exercise with progressive hints, annuity/perpetuity and real/nominal explanations, saved browser progress, notes, search, a source drawer, local lecture/recitation/transcript PDFs, captions, and exact access to all 35 original problems and solutions in their PDF spans. It is a quality milestone, not an exhaustive conversion of the module.

## Run

```bash
./start-course.sh
```

Then open <http://127.0.0.1:4173>. The launcher builds the app and serves the production output locally. Stop it with `Ctrl+C`.

For development:

```bash
pnpm run dev
```

## Coverage state

- 12 of 12 modules: source-mapped in navigation
- Introduction: complete authored notebook lesson with six sections, interaction, comprehension feedback, original recording, and source anchors
- Present Value: first authored pilot lesson and interactive model complete; six sections are navigable within the lesson
- Modules 03–12: guided overviews with core explanations, worked examples, self-check prompts and original source links; full lesson and exercise conversion remains open
- Original Present Value problems 1–35: accessible at exact question pages 7–14 and solution pages 42–48; not all converted into native exercises yet
- Videos: all 20 lectures plus the instructor interview are present locally (21 ready recordings, approximately 3.55 GB). Transfer, duration, hashes and decode sampling are recorded in `public/media/manifest.json`; official online fallbacks remain linked.
- Offline tutor/API: intentionally absent from this milestone; authored content is stored locally

Progress and notes are stored in browser `localStorage`. Clearing site data removes them.

On macOS, `Start Course.command` provides a one-click launcher for the same local server.

## Validation

```bash
npm test
npm run build
```

The tests cover lecture-grounded PV/FV, NPV, annuity, compounding, perpetuity, and real-rate calculations.

Detailed Introduction source coverage is recorded in `INTRO-COVERAGE.md`.

## Attribution

Original course materials are from MIT OpenCourseWare 15.401 Finance Theory I, Fall 2008, taught by Andrew W. Lo. Authored explanations and interactions here are adaptations for local study. MIT source files retain their published credits and CC BY-NC-SA 4.0 license metadata. This package does not attribute the material to Khan Academy.
