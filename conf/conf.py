# -*- coding: utf-8 -*-
#
# Fess documentation build configuration file, created by
# sphinx-quickstart on Sat Aug 16 11:40:54 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
#import sphinx_bootstrap_theme

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'rst2pdf.pdfbuilder',
    'sphinxjp.themes.basicstrap',
    'ext',
    'ogtag',
]

[extensions]
todo_include_todos=True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Fess'
if 'SPHINX_PROJECT' in os.environ:
    project = os.environ['SPHINX_PROJECT']

copyright = u'2020 CodeLibs Project'

# Document title
title = 'Fess'
if 'SPHINX_TITLE' in os.environ:
    title = unicode(os.environ['SPHINX_TITLE'], "utf-8")

# Document author
author = 'CodeLibs'
if 'SPHINX_AUTHOR' in os.environ:
    author = unicode(os.environ['SPHINX_AUTHOR'], "utf-8")

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = '1.0'
if 'SPHINX_RELEASE' in os.environ:
    release = os.environ['SPHINX_RELEASE']

# The short X.Y version.
if 'SPHINX_VERSION' in os.environ:
    version = os.environ['SPHINX_VERSION']
else:
    version = release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = None
if 'SPHINX_LANG' in os.environ:
    language = os.environ['SPHINX_LANG']

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'
today_fmt = '%Y-%m-%d'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
sys.path.append(os.path.abspath('_themes'))
html_theme_path = ["_themes", ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = None
#html_logo = '../resources/images/fess-logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {
    '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'blanksearchbox.html'],
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'transition': '',
    'extraclassoptions': ',openany,oneside',
    'babel': '\usepackage[japanese]{babel}',
#    'figure_align': 'here',
#    'preamble': '',
}

#latex_elements['preamble'] = r'''
#\usepackage[export]{adjustbox}
#\usepackage{letltxmacro}
#\LetLtxMacro{\origincludegraphics}{\includegraphics}
#\renewcommand*\includegraphics[2][clip,scale=0.5,max width=\textwidth,max height=\textheight,keepaspectratio]{%
#\begin{minipage}{\columnwidth}
#\begin{wrapfigure}{r}{\columnwidth}
#\origincludegraphics[#1]{#2}
#\end{wrapfigure}
#\end{minipage}
#}
#\let\OrigVerbatim\OriginalVerbatim
#\renewcommand{\OriginalVerbatim}[1][1]{\OrigVerbatim[#1,frame=single]}
#'''

latex_elements['preamble'] = r'''
\usepackage{here}
\usepackage[export]{adjustbox}
\usepackage{letltxmacro}
\LetLtxMacro{\origincludegraphics}{\includegraphics}
\renewcommand*\includegraphics[2][clip,scale=0.6,max width=\textwidth,max height=\textheight,keepaspectratio]{%
\begin{figure}[H]
\origincludegraphics[#1]{#2}
\end{figure}
}
\let\OrigVerbatim\OriginalVerbatim
\renewcommand{\OriginalVerbatim}[1][1]{\OrigVerbatim[#1,frame=single]}
'''

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', project+'.tex', title,
   author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None
#latex_logo = '../resources/images/fess-logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

latex_docclass = {'manual': 'jsbook'}

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', project, title,
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', project, title,
   author, project, 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for PDF output --------------------------------------------------

# Grouping the document tree into PDF files. List of tuples
# (source start file, target name, title, author, options).
#
# If there is more than one author, separate them with \\.
# For example: r'Guido van Rossum\\Fred L. Drake, Jr., editor'
#
# The options element is a dictionary that lets you override
# this config per-document.
# For example,
# ('index', u'MyProject', u'My Project', u'Author Name',
#  dict(pdf_compressed = True))
# would mean that specific document would be compressed
# regardless of the global pdf_compressed setting.

pdf_documents = [
    ('index', project, title, author),
]

# A comma-separated list of custom stylesheets. Example:
pdf_stylesheets = ['sphinx','kerning','a4','ja']

# Create a compressed PDF
# Use True/False or 1/0
# Example: compressed=True
#pdf_compressed = False

# A colon-separated list of folders to search for fonts. Example:
pdf_font_path = ['/Library/Fonts']

# Language to be used for hyphenation support
pdf_language = language

# Mode for literal blocks wider than the frame. Can be
# overflow, shrink or truncate
#pdf_fit_mode = "shrink"

# Section level that forces a break page.
# For example: 1 means top-level sections start in a new page
# 0 means disabled
#pdf_break_level = 0

# When a section starts in a new page, force it to be 'even', 'odd',
# or just use 'any'
#pdf_breakside = 'any'

# Insert footnotes where they are defined instead of
# at the end.
#pdf_inline_footnotes = True

# verbosity level. 0 1 or 2
#pdf_verbosity = 0

# If false, no index is generated.
#pdf_use_index = True

# If false, no modindex is generated.
#pdf_use_modindex = True

# If false, no coverpage is generated.
#pdf_use_coverpage = True

# Documents to append as an appendix to all manuals.
#pdf_appendices = []

# Enable experimental feature to split table cells. Use it
# if you get "DelayedTable too big" errors
#pdf_splittables = False

# Set the default DPI for images
#pdf_default_dpi = 72
#pdf_default_dpi = 94
#pdf_default_dpi = 50

# -- HTML theme options for `sphinx_rtd_theme` style -------

html_theme_options = {
    'collapse_navigation': False,
    'display_version': False,
#    'navigation_depth': 3,
}

html_context = {
#    "context_path": "",
    "display_github": True,
#    "last_updated": True,
    "commit": False,
    "github_user": "codelibs",
    "github_repo": "fess-docs",
    "github_version": "master",
}

og_site_url = 'https://fess.codelibs.org/'
og_twitter_site = ''
