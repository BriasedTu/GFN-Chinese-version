from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent
PROCESSED = ROOT / "processed"
OUT = ROOT / "in_dialogue_with_nature_bilingual.tex"


ORDER = [
    "00_front_intro.tex",
    "01_plato_republic.tex",
    "02_lindberg_beginnings.tex",
    "03_cohen_newton.tex",
    "04_darwin.tex",
    "05_watson_dna.tex",
    "06_carson.tex",
    "07_poincare_kandel.tex",
    "08_needham_sivin.tex",
    "09_shen_brush_talks.tex",
    "10_dunham_euclid.tex",
]


PREAMBLE_PATTERNS = [
    r"^% !TeX.*$",
    r"^\\documentclass.*$",
    r"^\\usepackage.*$",
    r"^\\graphicspath.*$",
    r"^\\setlength.*$",
    r"^\\title.*$",
    r"^\\author.*$",
    r"^\\date.*$",
    r"^\\maketitle\s*$",
]


def strip_document_shell(text: str) -> str:
    text = text.replace("\r\n", "\n")
    begin = text.find(r"\begin{document}")
    end = text.rfind(r"\end{document}")
    if begin != -1 and end != -1 and begin < end:
        text = text[begin + len(r"\begin{document}") : end]
    lines = []
    skipping_macro = False
    brace_balance = 0
    for line in text.splitlines():
        if skipping_macro:
            brace_balance += line.count("{") - line.count("}")
            if brace_balance <= 0:
                skipping_macro = False
            continue
        if any(re.match(p, line.strip()) for p in PREAMBLE_PATTERNS):
            continue
        stripped = line.strip()
        if (
            stripped.startswith(r"\newcommand")
            or stripped.startswith(r"\providecommand")
            or stripped.startswith(r"\renewcommand")
            or stripped.startswith(r"\newenvironment")
            or stripped.startswith(r"\renewenvironment")
        ):
            brace_balance = line.count("{") - line.count("}")
            skipping_macro = brace_balance > 0
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def normalize_body(text: str) -> str:
    replacements = {
        r"\begin{english}": r"\begin{enblock}",
        r"\end{english}": r"\end{enblock}",
        r"\begin{zhtranslation}": r"\begin{zhblock}",
        r"\end{zhtranslation}": r"\end{zhblock}",
        r"\begin{translation}": r"\begin{zhblock}",
        r"\end{translation}": r"\end{zhblock}",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace("・", "·")
    label_replacements = {
        r"\textbf{English.}": r"\textbf{原文}",
        r"\textbf{English}": r"\textbf{原文}",
        r"\textbf{Original.}": r"\textbf{原文}",
        r"\textbf{Original}": r"\textbf{原文}",
        r"\textbf{中文。}": r"\textbf{译文}",
        r"\textbf{中文}": r"\textbf{译文}",
        r"\textbf{中}": r"\textbf{译文}",
        r"\textbf{Translation.}": r"\textbf{译文}",
        r"\textbf{Translation}": r"\textbf{译文}",
    }
    for old, new in label_replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"\\chapter\{([^{}]+)\}", r"\\section*{\1}", text)
    text = re.sub(r"(?m)^\\zh\s+(.+)$", r"\\zhline{\1}", text)
    text = re.sub(r"\\darwinpair\s*\{(.+?)\}\s*\{(.+?)\}", r"\\pair{\1}{\2}", text, flags=re.S)
    text = re.sub(r"\\darwinimage(?:\[[^\]]*\])?\{(?:images/)?([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(r"\\ocrimage(?:\[[^\]]*\])?\{(?:images/)?([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(r"\\preserveimage\{(?:images/)?([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(r"\\gapnote\{([^{}]*)\}", r"\\editorialnote{\1}", text)
    text = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{(?:\.\./)?images/([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{(?:\.\./chunks/)?images/([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{chunks/images/([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(r"\\includegraphics(?:\[[^\]]*\])?\{([^}/\\]+\.jpe?g|[^}/\\]+\.png)\}", r"\\safeincludeimage{\1}", text, flags=re.I)
    text = re.sub(r"\\preservedimage\{(?:images/)?([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(r"\\safeincludeimage\{(?:images/)?([^}]+)\}", r"\\safeincludeimage{\1}", text)
    text = re.sub(
        r"\\safeincludeimage\{([^}]+)\}\s*\\(?:quad|hfill)\s*\\safeincludeimage\{([^}]+)\}",
        r"\\safeincludeimagepair{\1}{\2}",
        text,
    )
    return text


def main() -> None:
    parts = []
    for name in ORDER:
        path = PROCESSED / name
        text = path.read_text(encoding="utf-8-sig", errors="replace")
        body = normalize_body(strip_document_shell(text))
        parts.append(f"% ===== {name} =====\n{body}\n")

    preamble = r"""\documentclass[UTF8,zihao=-4]{ctexart}
\usepackage[a4paper,margin=2.35cm]{geometry}
\usepackage{fontspec}
\usepackage{xeCJK}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{float}
\usepackage{longtable}
\usepackage{booktabs}
\usepackage{array}
\usepackage{amsmath,amssymb}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{etoolbox}
\usepackage{fancyhdr}

\setmainfont{Times New Roman}
\IfFontExistsTF{SimSun}{\setCJKmainfont{SimSun}}{\setCJKmainfont{Noto Serif CJK SC}}
\graphicspath{{images/}{E:/大学/书/与自然对话/vlm/images/}}
\linespread{1.12}
\setlength{\parindent}{2em}
\setlength{\parskip}{0.45em}
\hypersetup{colorlinks=true,linkcolor=black,urlcolor=blue}
\pagestyle{fancy}
\fancyhf{}
\fancyfoot[C]{\scriptsize 译者：智乃的脚小小的}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[C]{\scriptsize 译者：智乃的脚小小的}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
}

\newcommand{\BodyFont}{\fontsize{10.5pt}{15.5pt}\selectfont}
\newcommand{\origlabel}{\textbf{原文}\quad}
\newcommand{\translabel}{\textbf{译文}\quad}
\newenvironment{enblock}{\par\noindent\begingroup\BodyFont\origlabel}{\par\endgroup}
\newenvironment{zhblock}{\par\noindent\begingroup\BodyFont\translabel}{\par\endgroup\vspace{0.35em}}
\renewenvironment{quote}{\par\noindent\begingroup\BodyFont}{\par\endgroup}
\newcommand{\en}[1]{\begin{enblock}#1\end{enblock}}
\newcommand{\zh}[1]{\begin{zhblock}#1\end{zhblock}}
\newcommand{\pair}[2]{\begin{enblock}#1\end{enblock}\begin{zhblock}#2\end{zhblock}}
\newcommand{\speaker}[2]{\par\medskip\noindent\textbf{#1 / #2}\par}
\newcommand{\safegraphics}[3]{%
  \IfFileExists{images/#1}{\includegraphics[width=#2,height=#3,keepaspectratio]{images/#1}}{%
  \IfFileExists{E:/大学/书/与自然对话/vlm/images/#1}{\includegraphics[width=#2,height=#3,keepaspectratio]{E:/大学/书/与自然对话/vlm/images/#1}}{%
    \fbox{\parbox{0.72\linewidth}{\centering 图片引用保留：\texttt{\detokenize{#1}}}}%
  }}%
}
\newcommand{\safeincludeimage}[1]{\begin{center}\safegraphics{#1}{0.86\linewidth}{0.46\textheight}\end{center}}
\newcommand{\safeincludeimagepair}[2]{\begin{center}\safegraphics{#1}{0.45\linewidth}{0.34\textheight}\hfill\safegraphics{#2}{0.45\linewidth}{0.34\textheight}\end{center}}
\newcommand{\preservedimage}[1]{\safeincludeimage{#1}}
\newcommand{\preserveimage}[1]{\safeincludeimage{#1}}
\newcommand{\editorialnote}[1]{\par\smallskip\noindent{\footnotesize\color{gray}\textbf{编者按：}#1}\par\smallskip}
\newcommand{\orig}{\par\noindent\begingroup\BodyFont\origlabel}
\newcommand{\zhline}[1]{\par\endgroup\noindent\begingroup\BodyFont\translabel #1\par\endgroup\vspace{0.35em}}

\begin{document}
\sloppy
\BodyFont
"""
    ending = "\n\\end{document}\n"
    OUT.write_text(preamble + "\n\n".join(parts) + ending, encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
