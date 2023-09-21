
## This is a simple makefile to build tex files in this directory
## to build from a file called project.tex you can type `make project.pdf` on the command line
## if you just type `make`, by default ('all' rule) it will build the example.tex file into example.pdf

%.pdf : %.tex
	pdflatex $<
	## it's a good idea to run pdflatex twice, as sometimes referencing needs it.
	pdflatex $<
	biber $*
	pdflatex $<
	pdflatex $<

all : example.pdf

## clean target gets rid of the compiled pdfs (in this directory) and the auxiliary files pdflatex makes
clean :
	rm -f *.pdf *.aux *.out *.log
