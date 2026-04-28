# Notes for `07_poincare_kandel`

- Source processed: `chunks/07_poincare_kandel.md` only.
- Output written as bilingual LaTeX with paired original/Chinese blocks.
- Removed OCR structure noise: standalone page numbers, repeated `Chapter 1`, `Chapter 3`, `Chapter 4`, `Chapter 28` running headers, `Text 8/from` wrappers, and the OCR-only `<details><summary>text_image</summary>` transcription under figure 4-1.
- Preserved both Kandel image references as LaTeX figures using the original image filenames. The LaTeX `\graphicspath` searches `../images/`, `../chunks/images/`, and `images/`.
  - `a9b9ebf53506e9e0115c3e0ac3176d4a0e011804b72ed5e036c409bbfb033975.jpg`
  - `983d9daa0542de65f607fe473e33e0b93324598b87b96544aac66a41c60daf77.jpg`
- The referenced image files were not present in the workspace during verification, so image rendering/LaTeX compile was not verified.
- Repaired visible OCR/mojibake issues, including names and accents (`Poincaré`, `mathématique`, `Mont-Valérien`, `René`, `naive`), curly-quote artifacts, em-dash artifacts, `Crick's`, `don't`, `readiness potential`, `free won't`, `Nietzsche`, and `conscious being`.
- Standardized requested terminology: `事实的选择`, `数学发现`, `潜意识/无意识`, `意识`, `神经科学`, `还原论`, `面部表情`.
- Retained explicit ellipsis markers `[\dots]` where the source chunk marks omitted material.
- Excluded the trailing `Text 9` / Joseph Needham fragment at the end of the OCR chunk as spillover beyond the requested Poincaré/Kandel scope for this output.
