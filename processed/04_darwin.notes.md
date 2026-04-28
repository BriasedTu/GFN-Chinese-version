# Notes for `04_darwin`

- Scope kept to `chunks/04_darwin.md` and the requested output paths.
- Removed OCR/navigation artifacts: `Text 4`, `from`, isolated page numbers, HTML `<details>` wrapper, and the `Text 5 / DNA: The Secret of Life` spillover with mojibake Chinese note.
- Repaired common mojibake punctuation in the English text, including em dashes, apostrophes, curly quotes, and broken quote marks.
- Joined paragraphs split by page breaks and preserved intentional excerpt gaps as `[\ldots]`.
- Preserved the three front image references before the Darwin title and the central divergence diagram reference in LaTeX. The trailing three image references were treated as belonging to the next text boundary and omitted.
- Image files referenced in the Markdown were not present at the checked workspace paths, so the LaTeX preserves references with `\IfFileExists` fallbacks instead of copying assets.
- Translated the English into Chinese paragraph by paragraph, using Darwin terminology consistently: 自然选择, 生存斗争, 变异, 有利变异, 适应, 性状, 种/品种, 性选择, 性状分歧.
