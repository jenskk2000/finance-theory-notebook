# Finance Theory Notebook

A local visual course built from MIT OpenCourseWare **15.401 Finance Theory I (Fall 2008)**, taught by Andrew W. Lo.

## Start

With Node.js and pnpm installed:

```sh
cd local-course
pnpm install --frozen-lockfile
./start-course.sh
```

Open http://127.0.0.1:4173/. Introduction and a Present Value pilot are authored notebook lessons. The remaining modules currently provide source materials.

## Contents

- `local-course/`: interactive course, source library, lesson coverage and review notes.
- `course-audit/`: inventory, extracted text, original-course audit, build plan and design references.
- `static_resources/`, `pages/`, `resources/`, and related root files: preserved OCW course materials/site.

## Lecture videos

Large MP4 recordings, build output and installed dependencies are intentionally excluded from Git. The media manifest and downloader are included. To restore videos after cloning, from the repository root:

```sh
python3 -m venv local-course/.tools/venv
local-course/.tools/venv/bin/pip install imageio-ffmpeg
local-course/.tools/venv/bin/python local-course/scripts/download_media.py
```

The full download is approximately 3.55 GB. PDFs and captions are included. See `local-course/public/media/README.md` for provenance and validation limits.

## Attribution

Original MIT materials retain their published credits and license notices. Authored explanations and interactions are adaptations for local study. This repository does not claim MIT endorsement or completion of every modernized lesson.
