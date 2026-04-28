# 09_shen_brush_talks notes

- Scope observed: only `chunks/09_shen_brush_talks.md` was read as chunk input; no unrelated chunks were opened.
- The source Markdown was mojibake from a UTF-8/GB18030-style decoding path. I used that recovery only as a guide, then normalized the relevant 《夢溪筆談》 text by context.
- Removed OCR/page noise: `Text 10b`, `from`, `Brush Talks from Dream Brook`, author/source headings, page header `252 與自然對話 In Dialogue with Nature`, the duplicated `卷二十四 雜誌一` mid-paragraph header, stray page numbers, and all of `Text 11a` / William Dunham / Greek geometry bleed-through.
- Preserved the six image references from the chunk as LaTeX image placeholders with the original `images/...jpg` paths. A workspace search did not find the actual image files, so the paths are retained verbatim rather than rewritten.
- English-only passages for “Total Number of Possible Situations in Chess” and “Moveable Type Printing” were translated into Chinese as 補譯 because they add content not otherwise present in the Chinese OCR block.
- The English renderings of “The Rainbow,” “Transformation of the Land and the Sea,” and “The Compass” were used only to align/repair the existing Chinese passages; their duplicated English body was not kept in the TeX.

## OCR/text repairs

- `異事異疾附` normalized to `卷二十一　異事（異疾附）`.
- `虹`: restored terms including `黑水境`, `永安山`, `卓帳`, `扣澗`, `綃縠`, `日所鑠`, `孫彥先`; rendered the optical explanation as `雨中日影`.
- `海陸變遷`: restored `遵太行而北`, `螺蚌殼`, `橫亙石壁如帶`, `濁泥所湮`, `堯殛鯀於羽山`, and the silt-bearing rivers `大河、漳水、滹沱、涿水、桑乾`.
- `指南針`: restored `磁石磨針鋒`, `微偏東`, `指爪`, `盌唇`, `縷懸`, `新纊中獨繭縷`, and `芥子許蠟`.
- Chess-number passage: corrected the OCR/English `10,000^{52}` sense to `「萬」字連書四十三次`, which matches the classical calculation for a 19-by-19 board order of magnitude.

## Terminology choices

- Movable type: `活版印刷`, `泥活字`, `字模`, `鐵範`, `印版`, `排字`.
- Rainbow: `虹` / `彩虹`; `雨中日影` rendered as sunlight/rain optical image.
- Geomorphology: `海陸變遷`, `帶狀地層`, `泥沙沉積`, `淤塞`, `地貌變遷`, `泥沙搬運`.
- Compass: `指南針`, `磁針`, `磁石`, `磁針的偏角現象`, `獨繭絲`.

## Reference checks

- Public-domain classical text was checked against online editions/search snippets for 《夢溪筆談》, including [ADBDB《夢溪筆談》](https://adbdb.com/cn/mengxibitan/) and [Project Gutenberg eBook 7317](https://www.gutenberg.org/ebooks/7317.html.images).
