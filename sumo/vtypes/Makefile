PDFLATEX=pdflatex
LATEX=latex
BIBTEX=bibtex
MAIN=$(shell ls *.tex | cut -d'.' -f1)
VIEWER=evince

all: pdf

view: $(MAIN).pdf
	$(VIEWER) $(MAIN).pdf

clean: 
	/bin/rm -f *~ .*~ *.out *.idx *.bbl *.blg *.aux *.log *.toc *.nav *.snm *.vrb *.upa *.upb *.ini _region_.* \#*\# *.cut *.pdf *-blx.bib *run.xml

.SUFFIXES: .tex .pdf



pdf: $(MAIN).tex
	$(PDFLATEX) $(MAIN).tex
	$(PDFLATEX) $(MAIN).tex
