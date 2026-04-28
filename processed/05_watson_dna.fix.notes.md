# 05_watson_dna.tex Fix Notes

- Source used: `chunks/05_watson_dna.md`.
- Target repaired: `processed/05_watson_dna.tex`.
- Root cause: the TeX file contained valid UTF-8 Chinese but lacked a UTF-8 BOM, so default Windows/GBK readers displayed the Chinese as mojibake such as `閬椾紶瀛︾殑寮€绔`, `涓枃銆倉`, and `鎴戠殑`.
- Repair made: re-saved `processed/05_watson_dna.tex` as UTF-8 with BOM. This preserves the English originals, image references, and LaTeX structure while making the Chinese headings, labels, captions, and paragraphs read as proper Chinese in default Windows tooling.
- Terminology verified in the repaired TeX: 遗传学, 基因, 等位基因, 染色体, 显性/隐性, 突变, 优生学, 双螺旋, 核苷酸, 脱氧核糖核酸.
- Broad mojibake scan over the repaired UTF-8 text found zero matches for: `閬`, `銆`, `鎴`, `鍦`, `鐨`, `鍏`, `鍥`, `绗`, `�`.
