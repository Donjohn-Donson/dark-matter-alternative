# ---------------------------------------------------------------------------
# Build this thesis against the CU Boulder graduate-thesis template that lives
# in a SEPARATE repository, without vendoring any of its files into this repo.
#
# Primary mechanism: `thesis.cls` in this directory is a symlink into the
# template checkout (see `ls -l thesis.cls`). That makes `pdflatex main.tex`
# work in any editor with no configuration.
#
# This file is a backstop: it also puts the template checkout on TEXINPUTS so
# the build works when run from a different working directory or if the symlink
# is missing (e.g. a Windows checkout without symlink support).
#
# Default template location: a sibling checkout next to this repo, i.e.
#   <parent>/Research/cu-boulder-thesis-template-main
# Override with an env var, e.g.
#   DMA_THESIS_TEMPLATE=/path/to/cu-boulder-thesis-template latexmk
# ---------------------------------------------------------------------------
use Cwd qw(getcwd);

my $template = $ENV{'DMA_THESIS_TEMPLATE'}
    || getcwd() . '/../../../cu-boulder-thesis-template-main';

if (-e "$template/thesis.cls") {
    # '//' lets kpathsea recurse into the template folder.
    $ENV{'TEXINPUTS'} = "$template//:" . ($ENV{'TEXINPUTS'} // '');
    $ENV{'BIBINPUTS'} = "$template//:" . ($ENV{'BIBINPUTS'} // '');
} elsif (! -e 'thesis.cls') {
    warn "\n[.latexmkrc] CU Boulder thesis template not found at:\n"
       . "    $template\n"
       . "  and ./thesis.cls symlink is missing. Clone the template (or point\n"
       . "  DMA_THESIS_TEMPLATE at your checkout):\n"
       . "    https://github.com/GiacoCorsiglia/cu-boulder-thesis-template\n\n";
}

@default_files = ('main.tex');

$pdf_mode = 1;      # pdflatex
$bibtex_use = 2;    # run biber/bibtex as needed, clean its output
