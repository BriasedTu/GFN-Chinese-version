# Chinese Mojibake Audit Notes

Scope: `processed/00_*.tex` through `processed/10_*.tex`

Date: 2026-04-27

## Result

No Chinese mojibake requiring repair was found in the scoped fragments.

Must repair before final assembly: none.

## Method

- Scanned all 11 scoped `.tex` fragments: `00_front_intro.tex` through `10_dunham_euclid.tex`.
- Checked all CJK-bearing lines, with emphasis on Chinese headings, `中文`/`译文` blocks, `\zh` blocks, and `zhtranslation` environments.
- Searched for exact and broad mojibake-shaped sequences including `銆`, `鏌`, `鑻`, `鎴`, `鍦`, `鐨`, `鍏`, `鍥`, `绗`, `閬`, `寮€`, `涓`, `璇`, `濂`, `鏄`, plus broader GBK/UTF-8 artifact-style tokens.
- Checked for malformed text markers: U+FFFD replacement characters and private-use characters.
- Verified scoped files decode as valid UTF-8.

## Coverage

| Fragment | CJK-bearing lines | Severity | Notes |
|---|---:|---|---|
| `00_front_intro.tex` | 52 | None | Chinese title/front matter appears normal. |
| `01_plato_republic.tex` | 83 | None | Simplified Chinese headings/dialogue appear normal. |
| `02_lindberg_beginnings.tex` | 73 | None | One broad-token false positive; see below. |
| `03_cohen_newton.tex` | 88 | None | Chinese translation paragraphs appear normal. |
| `04_darwin.tex` | 53 | None | One broad-token false positive; see below. |
| `05_watson_dna.tex` | 151 | None | Chinese translation paragraphs/captions appear normal. |
| `06_carson.tex` | 60 | None | Chinese translation paragraphs appear normal. |
| `07_poincare_kandel.tex` | 132 | None | One broad-token false positive; see below. |
| `08_needham_sivin.tex` | 190 | None | Chinese headings/tables/translation material appear normal. |
| `09_shen_brush_talks.tex` | 33 | None | Traditional/classical Chinese appears intentional and normal. |
| `10_dunham_euclid.tex` | 206 | None | Chinese translation paragraphs/captions appear normal. |

## Suspicious-Looking But Benign Samples

These were caught by broad scanning only because isolated legitimate characters can overlap with mojibake artifact lists.

- `02_lindberg_beginnings.tex:149` - `勾勒出的知识理论`
  - Severity: none. `勾勒` is normal Chinese usage here.
- `04_darwin.tex:100` - `绛三叶草（Trifolium pratense 和 incarnatum）`
  - Severity: none. `绛三叶草` is the correct plant name context.
- `07_poincare_kandel.tex:757` - `开始勾勒一种情绪`
  - Severity: none. `勾勒` is normal Chinese usage here.

## Negative Findings

- No hits for the user-specified seed sequences in mojibake-like clusters.
- No U+FFFD replacement characters found.
- No private-use mojibake remnants found.
- No scoped file failed strict UTF-8 decoding.

## Final Assembly Blockers

None from Chinese mojibake.
