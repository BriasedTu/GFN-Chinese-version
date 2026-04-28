# Assembly audit notes

Scope: `processed/00_*.tex` through `processed/10_*.tex` only. No `.tex` rewrites were performed as part of this audit. Note: this folder is not a git repo, and initial vs final filesystem inventories showed `07_poincare_kandel.tex` and `10_dunham_euclid.tex` changing during the audit; findings below reflect the final on-disk versions after a second scan of those files.

## High-priority assembly blockers

### Embedded document wrappers

These fragments are full standalone documents. Concatenating them raw inside a main document will break XeLaTeX at the nested `\documentclass`, `\begin{document}`, or `\end{document}`.

- `01_plato_republic.tex`: preamble/wrapper at lines 1-6, title metadata at 22-24, `\begin{document}` at 26, `\maketitle` at 27, `\end{document}` at 199.
- `02_lindberg_beginnings.tex`: preamble/wrapper at lines 3-7, `\begin{document}` at 14, `\end{document}` at 307.
- `07_poincare_kandel.tex`: preamble/wrapper at lines 2-8, `\begin{document}` at 15, `\end{document}` at 790.
- `08_needham_sivin.tex`: preamble/wrapper at lines 1-9, title metadata at 30-32, `\begin{document}` at 34, `\maketitle` at 35, `\end{document}` at 955.

Suggested assembler rule: extract only body content from wrapped fragments, but hoist any required local macro/environment definitions before stripping them.

### Local macros/environments that can become undefined

If wrapper/preamble content is stripped without hoisting definitions, these body commands become undefined:

- `01_plato_republic.tex`: `\speaker` defined line 8, used 31-187; `\en` defined line 9, used 32-188; `\zh` defined line 10, used 33-189; `\preserveimage` defined line 11, used 195-197.
- `02_lindberg_beginnings.tex`: `\orig` defined line 11, used 23-303; `\zh` defined line 12, used 25-305.
- `04_darwin.tex`: `\darwinpair` defined line 3, used 30-238; `\darwinimage` defined line 7, used 18-20.
- `05_watson_dna.tex`: `\ocrimage` defined line 5, used 37-1062; also uses `\chapter` at lines 9 and 369, which requires a book/report-like class or conversion to `\section*`.
- `07_poincare_kandel.tex`: environment `english` defined line 12, used 21-784; environment `zhtranslation` defined line 13, used 24-787.
- `08_needham_sivin.tex`: environments `enblock` and `zhblock` defined lines 15 and 18, used 81-933; `\gapnote` defined line 21, used 39, 95, 476; `\preservedimage` defined line 22, used 365, 939, 945, 951.
- `09_shen_brush_talks.tex`: `\preservedimage` defined line 4, used 70-75.

Important collision: `01_plato_republic.tex` and `02_lindberg_beginnings.tex` both define `\zh`, but with incompatible signatures. Do not blindly hoist both `\newcommand{\zh...}` definitions. Normalize to namespaced macros or expand them during assembly.

Package/class needs to consolidate in the main preamble: `graphicx`, `caption`, `hyperref`, `array`, `booktabs`, `longtable`, `amsmath`/math support, and a CJK-capable class or package. `08_needham_sivin.tex` uses `longtable`, `booktabs`, `arraybackslash`, `LTpre`, and `LTpost`; `10_dunham_euclid.tex` uses math `array` environments.

### Mojibake/remnant characters

- Current UTF-8 scan found no U+FFFD hits and no obvious mojibake remnants in 00-10. The only literal hit from the requested token list is `10_dunham_euclid.tex:26`, where the character is part of the normal Chinese word for "omission" and is not mojibake.

Suggested assembler rule: fail fast or warn on U+FFFD and the known mojibake token list before final assembly, because these can appear transiently in regenerated fragments.

### Image references and missing files

No `images/`, `chunks/images/`, or `processed/images/` directory is present under the workspace, and every image-like reference found in the fragments is currently unresolved. If images are optional, the assembler needs a single fallback macro; otherwise materialize/copy images to one canonical root and rewrite paths.

- `00_front_intro.tex`: 13 missing `\includegraphics` refs at lines 3, 27, 162, 167, 172, 206, 211, 216, 237, 242, 247, 286, 291. Basenames: `a6efff7140e16fd202e094f504efbaea737deea9ccb83d4abcff42c748ab01a2.jpg`, `8784b1a80b63978c6fc27b4602b394f6fdeabc934a2093867ec476486f1f88da.jpg`, `5a95f7933242031cdf7344c31ef7efcfcc6659edeca4b1d640d2787ab3da55ee.jpg`, `e46bf37999529a2a85624c7a05753348a21652c15fb110832234e25b1b1e9435.jpg`, `38a900aa2a3bead557129f54f70faecda13b9101dd57d9dd5cdb6a4553305375.jpg`, `5265f181dd0fe79129fa8aa065cac75e9ca7f4f99bb903ce0f90219f5794202e.jpg`, `e1c8979b6a5dce498d7e399e551e97dcc7c98202c23ad6576615adb69900dd5f.jpg`, `e89973539a1419965672c1f045ac56baaa69ada9dc08454add0b99eae625b100.jpg`, `e164458d709fca29a085e534aa501bdb3c5626375e966787db06f40681f85ae2.jpg`, `6009ea775e9606e425a1e59b1278ad9f5938885e80cf1409a9bc591b3ea7fc76.jpg`, `41665940a7220c3cfe9399263f99ec7c7f37f68b9c41c38f23d351ec2425484e.jpg`, `0f3226dc6469800784c93e5ebaa09727ee23625021c803313d88daef8ca01ec3.jpg`, `a7bdbab81e3c4ed51ae0467fd19042b20e3a5fd1f97c5b2fb71e2f1e2b191f32.jpg`.
- `01_plato_republic.tex`: 3 missing `\preserveimage` refs at lines 195-197 under `images/`.
- `02_lindberg_beginnings.tex`: 8 missing `\includegraphics` refs at lines 29, 39, 85, 86, 87, 105, 217, 239 under `../chunks/images/`.
- `03_cohen_newton.tex`: 5 missing `\includegraphics` refs at lines 94, 353, 365, 369, 373 under `chunks/images/`.
- `04_darwin.tex`: 5 missing image refs at lines 18, 19, 20 (`\darwinimage`) and 161, 164 (`\includegraphics` fallback paths).
- `05_watson_dna.tex`: 28 missing `\ocrimage` refs at lines 37, 92, 161, 188, 306, 365, 404, 431, 528, 562, 603, 623, 713, 715, 735, 769, 771, 777, 779, 854, 965, 985, 1005, 1018, 1038, 1058, 1060, 1062 under `images/`.
- `07_poincare_kandel.tex`: 2 missing `\includegraphics` refs at lines 458 and 707.
- `08_needham_sivin.tex`: 4 missing `\preservedimage` refs at lines 365, 939, 945, 951.
- `09_shen_brush_talks.tex`: 6 missing `\preservedimage` refs at lines 70-75 under `images/`.
- `10_dunham_euclid.tex`: 31 missing `\includegraphics` refs at lines 12, 38, 60, 126, 127, 141, 155, 189, 221, 267, 301, 322, 323, 324, 399, 415, 439, 459, 460, 492, 520, 548, 568, 588, 612, 636, 668, 696, 720, 740, 760 under `images/`.

Suggested assembler rule: convert all image calls to one wrapper such as `\safeincludegraphics[opts]{canonical/path}` that tests known roots, emits a visible placeholder on miss, and never leaves raw unresolved `\includegraphics` in final assembly.

### Source-boundary/spillover markers

These look intentional, but they are visible editorial/source-boundary notes and should be normalized if the final assembly should read as a clean anthology.

- `02_lindberg_beginnings.tex:88`: caption says image-only material is preserved from the OCR source between Chapter 2 and Chapter 3.
- `05_watson_dna.tex:1063`: caption says terminal image references were retained from the Watson/Berry source boundary.
- `08_needham_sivin.tex:39`, `95`, `476`: `\gapnote{...}` source-gap notes.

Suggested assembler rule: map source-gap and boundary notes to a consistent editorial-note style, or suppress them behind a build flag.

## Lower-priority checks

- Brace scan: no negative brace depth and final brace balance is zero for all 00-10 `.tex` fragments.
- Environment scan: all `\begin{...}` / `\end{...}` pairs balance in all 00-10 `.tex` fragments.
- No embedded `\input{...}`, `\include{...}`, bibliography commands, or merge-conflict markers were found.

## Main assembler normalization rules

1. Treat each fragment as either `standalone-doc` or `body-fragment`; for standalone docs, keep only content between `\begin{document}` and `\end{document}`.
2. Hoist or inline local definitions before body extraction. Namespace incompatible short macros, especially `\zh`.
3. Consolidate package/class requirements in one main preamble; do not keep fragment-level `\documentclass`, `\usepackage`, `\graphicspath`, title metadata, `\maketitle`, or `\end{document}`.
4. Normalize image paths through a single image resolver. Prefer copying assets into one canonical `images/` root, or use a safe placeholder macro for missing files.
5. Add a preflight text scan that rejects U+FFFD and the known mojibake token list before XeLaTeX.
6. Normalize editorial gap/source-boundary markers to a single macro or suppress them for final output.
7. If the main class is article-like, convert `\chapter` in `05_watson_dna.tex` to `\section*`; otherwise use a book/report-like CJK class.
