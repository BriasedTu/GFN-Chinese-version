# 02_lindberg_beginnings repair notes

- Scope: inspected `processed/02_lindberg_beginnings.tex` against `chunks/02_lindberg_beginnings.md`.
- Finding: the TeX file's Chinese text is valid UTF-8 on disk. The bad sample strings in the request are produced when the UTF-8 file is decoded through the Windows default ANSI code page.
- Repair applied: added an explicit TeX UTF-8 encoding directive beside the existing XeLaTeX directive, and saved the TeX as UTF-8 with a BOM for Windows tools that rely on BOM-based encoding detection. The existing Chinese headings, captions, and translation blocks already contain proper Chinese terms such as `西方科学的起源`, `希腊人与宇宙`, `柏拉图的形式世界`, `形式/理念`, `质料`, `四因`, `目的因`, `天球`, and `第一推动者`.
- Preservation: no English originals, image paths, figure environments, formulas, or LaTeX document structure were changed.
