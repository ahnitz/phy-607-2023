\ProvidesClass{project}
\LoadClass{article}

% The following are standard packages in most latex distributions

%% Formatting
\RequirePackage[utf8]{inputenc} %text encoding
\RequirePackage{graphicx} % including graphics
\RequirePackage{xcolor} % color stuff
\RequirePackage{titling} % expands on title page
\RequirePackage{booktabs} % nice looking table lines
\RequirePackage{subcaption} % subfigures, captions, references

%% For citations, biblatex is a reimplementation of the default bibliography commands with extended capabilities
%% Biber is a "backend" that replaces bibtex during compilation (the backend reads your .bib file and produces something for your main document to use)
\RequirePackage[backend=biber]{biblatex}

%% Physics and math stuff
\RequirePackage{amsmath} %% AMS packages are the gold standard
\RequirePackage{amssymb}
\RequirePackage{amsthm}
\RequirePackage{physics} % i like physics for derivative syntax, as well as braket notation and some other things
\RequirePackage{siunitx} % control formatting for units
\sisetup{per-mode=symbol,separate-uncertainty=true} % setup format now, can change it later without rewriting

%% hyperref does internal and external linking. it redefines a lot and should be last except in special cases (cleveref is one)
\RequirePackage[pdfpagelabels]{hyperref}
%% cleveref is great because it automatically creates the "Fig." in "Fig. 1", and the style can be adjusted globally for the document.
\RequirePackage{cleveref}

\endinput
