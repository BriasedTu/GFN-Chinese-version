# Notes for `10_dunham_euclid`

- Scope respected: only `chunks/10_dunham_euclid.md` was used as source, and outputs were written to the two requested `processed` paths.
- Removed page-number-only lines and false OCR headings such as numbered case lines promoted with `#`.
- Repaired obvious OCR/mojibake artifacts in prose: curly quote mojibake, em-dash mojibake, Greek labels `伪`/`尾`/`未` interpreted as `\alpha`/`\beta`/`\delta`, `postulate l` corrected to `postulate 1`, `[1. 10]` corrected to `[I. 10]`, and broken line wraps rejoined.
- Cleaned the Euclid portrait caption conservatively: `Brafi` to `brass`, `Queen Christian` to Queen Christina, `Laught` to taught, `PtolemyLagus` to Ptolemy Lagus, and `Hypficles` to Hypsicles.
- Preserved all Markdown image references as LaTeX `\includegraphics` calls using the original `images/...` paths.
- Translated all retained English into Chinese in bilingual LaTeX, using standard terms including 定义, 公设, 公理/共同概念, 命题, 等边三角形, 角平分线, 垂线, 全等.
- Kept the excerpt markers `[...]` as bilingual omission markers because they indicate intentional omissions in the source excerpt rather than OCR noise.
