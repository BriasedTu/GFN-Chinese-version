# 07_poincare_kandel Fix Notes

Scope:
- Inspected only `chunks/07_poincare_kandel.md` and `processed/07_poincare_kandel.tex`.
- Modified `processed/07_poincare_kandel.tex` and this notes file.

Repairs:
- Repaired corrupted Chinese title/heading text for Kandel chapter headings:
  - `第四章 一次研究一个细胞`
  - `第二十八章 意识`
- Restored U+FFFD-damaged Chinese paragraph-final punctuation throughout the TeX.
- Restored inline corrupted Chinese fragments:
  - `1923年至1933年`
  - `2004年7月28日`
  - `医学博士/哲学博士项目学生`
  - `此前200毫秒`
  - `前200毫秒内`
- Preserved the readable English blocks, with only minimal repair of U+FFFD-damaged quotation marks.
- Preserved image references:
  - `a9b9ebf53506e9e0115c3e0ac3176d4a0e011804b72ed5e036c409bbfb033975.jpg`
  - `983d9daa0542de65f607fe473e33e0b93324598b87b96544aac66a41c60daf77.jpg`

Final static check on target TeX:
- `鈥`: 0
- `茅`: 0
- `浜`: 0
- `鎵`: 0
- `绉戝`: 0
- `�`: 0
- `english` environments: 122 begin / 122 end
- `zhtranslation` environments: 122 begin / 122 end
- `includegraphics`: 2
- `caption`: 2
