@echo off
REM WayneIA ArXiv Paper Compilation Script
REM Requires MiKTeX or TeX Live installed
REM Install via: choco install miktex

echo Compiling WayneIA PutnamBench ArXiv Paper...

pdflatex -interaction=nonstopmode wayneia_putnam_arxiv.tex
bibtex wayneia_putnam_arxiv
pdflatex -interaction=nonstopmode wayneia_putnam_arxiv.tex
pdflatex -interaction=nonstopmode wayneia_putnam_arxiv.tex

echo.
echo Compilation complete!
echo Output: wayneia_putnam_arxiv.pdf
pause
