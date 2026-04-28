# Notes for `08_needham_sivin`

- Read only `chunks/08_needham_sivin.md`; did not inspect neighboring chunks.
- Wrote output only to:
  - `processed/08_needham_sivin.tex`
  - `processed/08_needham_sivin.notes.md`

## Cleanup Decisions

- Removed standalone OCR page numbers and broken running headers such as isolated `18`, `19`, `31`, `57`, etc.
- Removed the OCR `<details>` image-description block; preserved the actual image and replaced the incorrect alt text with a corrected bilingual caption.
- Removed structural source labels such as `Text 10a` from the main flow and promoted the real essay title to a LaTeX section.
- Kept explicit source-gap notices where the chunk itself has `[...]` or begins/ends mid-context, rather than filling missing book text from other chunks.
- Repaired common OCR mojibake in prose by normalizing quotes, apostrophes, dashes, names, and sinological terms in the cleaned English and Chinese translation.

## Translation and Terminology

- Used mainstream terms requested by the prompt: 阴阳, 五行, 气, 相关性思维, 科学革命, 历史推理谬误.
- Normalized key names and titles in Chinese: 李约瑟, 席文, 邹衍, 董仲舒, 王充, 沈括, 《墨经》, 《梦溪笔谈》, 《易经》/《周易》, 《春秋繁露》, 《大戴礼记》.
- Corrected the Sivin opening claim from OCR “eighteenth century” to “seventeenth century,” consistent with the later discussion of post-1600 Western astronomy in China.

## Tables and Images

- Converted the HTML tables into LaTeX `longtable` format.
- Table 8 was already partial and its ancient-character columns were badly corrupted; retained only high-confidence rows and marked the ancient-form column as unrecoverable in the LaTeX gap note.
- Table 9 was normalized into three smaller bilingual tables for readability.
- Preserved all substantive image references using paths relative to the processed file:
  - `../chunks/images/cd03d8e58d264dd5693c5d23747232e6341e7bbc70ec126811e0481af5645590.jpg`
  - `../chunks/images/ab8db89f822f852b2811695f7d04179e4928c24f1184703305320c6d28dbdfd8.jpg`
  - `../chunks/images/39fb42c881e228e97ba0885f8316c52c8fc1fac4d2aab457bf7362ce851e1440.jpg`
  - `../chunks/images/916233d2f39dd52cfca28f6dd4858c99111a70e4ad0a2e974036e9fc4873485b.jpg`
- Verification found that these image files are not currently present under the workspace. The LaTeX therefore uses a `\preservedimage{...}` macro that includes the image if it exists and otherwise prints a visible placeholder with the original OCR image filename.

## Exclusions and Uncertainties

- The final mojibake block beginning with `Text 10b` appears to be a separate Chinese source/translation section from `梦溪笔谈` rather than part of Needham/Sivin. Because the user specified this chunk as Needham/Sivin content and requested removal of false headings/page headers/Chinese-note noise, that tail block was not integrated into the bilingual LaTeX.
- Some OCR footnote fragments in the Sivin section were incomplete or displaced into the main text. I retained the substantive argument in the translated prose and omitted fragmentary bibliography strings whose placement could not be established from this isolated chunk.
- The output is a standalone XeLaTeX/ctex document. It should be compiled with XeLaTeX or LuaLaTeX; missing OCR image files will appear as placeholders rather than causing image-include failures.
