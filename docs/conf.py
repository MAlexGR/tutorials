# υπόδειγμα conf.py https://sublime-and-sphinx-guide.readthedocs.io/en/latest/create_project.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

"""
Imports the system and the theme, the project
is using to the project.
"""

import sys, os
import sphinx_bootstrap_theme
sys.path.insert(0, os.path.abspath('.'))


################ PROJECT INFORMATION ##############################

"""
The project name, copyright, and author.
"""

project = u'Generic Tutorials'
copyright = '2020, Alex M.'
author = 'Alex M.'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

################################################################



################### GENERAL CONFIGURATION ######################
# Add any Sphinx extension module names here, as strings. They
# can be extensions coming with Sphinx (named 'sphinx.ext.*') or
# your custom ones.

extensions = [ 
              'sphinx.ext.intersphinx',
              'sphinx.ext.extlinks',
              'rinoh.frontend.sphinx',
              'recommonmark',
              'sphinxcontrib.mermaid',
              'sphinx.ext.graphviz',
              'sphinx.ext.todo',
              'sphinx.ext.autosectionlabel',
              'nbsphinx',
              'sphinx.ext.mathjax',
              'sphinx_copybutton',
              ]
#################################################################



############## EXTENSIONS CONFIGURATION #########################


# Που να "βλέπει" (mapping) το intersphinx extension
intersphinx_mapping = {
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'python': ('https://docs.python.org/3', None),
                      }


# Ποιές ιστοσελίδες να "βλέπει" το extlinks. Aυτή τη ρύθμιση τη
# βρήκα στο https://github.com/sphinx-doc/sphinx/blob/3.x/doc/conf.py
# από το ίδιο το sphinx
extlinks = {
            'duref': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'restructuredtext.html#%s', ''),
            'durole': ('http://docutils.sourceforge.net/docs/ref/rst/'
                       'roles.html#%s', ''),
            'dudir': ('http://docutils.sourceforge.net/docs/ref/rst/'
                      'directives.html#%s', ''),
            'wiki': ('https://en.wikipedia.org/wiki/%s', ''),
            'pywiki': ('https://wiki.python.org/moin/%s', ''),
            'pyorg': ('https://docs.python.org/3/%s', ''),
            }


# Ενεργοποίηση του "todo" extension
todo_include_todos = True


# το χρειάζομαι????
autosectionlabel_prefix_document = True


# το χρειάζομαι????
mermaide_output_format = 'png'
######################################################################


# Add any paths that contain templates here, relative to this directory.
"""
Tells the project where to look for theme templates and css
overrides.
"""

templates_path = ['_templates']
html_static_path = ["_static"]



# The master toctree document.

"""
Tells the project the name of the home page.
"""

master_doc = 'index'

numfig = True


# The language for content autogenerated by Sphinx. Refer to
# documentation for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'el'


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    '.git',
    '_static'
    'Thumbs.db',
    '.DS_Store',
    'requirements.txt'
                   ]


#The file extensions of source files. Sphinx considers the files with
# this suffix as sources. The value can be a dictionary mapping file
# extensions to file types.

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'restructuredtext',
    '.md': 'markdown',
                 }


# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = ['css/custom.css',]

##---- HTML OUTPUT ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the
# documentation for a list of builtin themes.

# Theme 'bootstrap'. More at 
# info https://ryan-roemer.github.io/sphinx-bootstrap-theme/index.html

html_theme = 'bootstrap' #'sphinx_material'

# Add any paths that contain custom themes here, relative to this
# directory. ``get_html_theme_path`` returns a list, so you can
# concatenate with any other theme directories you would like.

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()


nitpicjy = True

##---- HTML SETTINGS -------------------------------------------------

html_theme_options = {
    'navbar_title': 'Athena Docs',      # Ο βασικός τίτλος στο
                                        # navication bar
                                          
    'navbar_site_name': 'Ιστοχώρος',         # Tab name for entire site.
                                        # (Default: "Site")

    'navbar_pagenav_name': "Σελίδα",      # Tab name for the current
                                        # pages TOC. (Default: "Page")
                                          
    'navbar_sidebarrel': True,          # Render the next and previous
                                        # page links in navbar
                                        # (Default: true).
                                             
    'bootstrap_version': "3",           # Choose Bootstrap version.
                                        # Values: "3" (default) or
                                        # "2" (σε εισαγωγικά)

# Bootswatch (http://bootswatch.com/) theme. Η επόμενη επιλογή καθορίζει
# αν θελουμε κάποιο συγκεκριμένο θέμα. Αν δεν την  χρησιμοποιήσουμε,
# (προεπιλογή), θα χρησιμοποιηθεί το προεπιλεγμένο θέμα. Εναλλακτικά
# μπορούμε να δώσουμε το όνομα ενός έγκυρου θέματος. όπως "cosmo" ή 
# "sandstone".
# Τα έγκυρα ονόματα θεμάτων εξαρτώνται από την έκδοση του Bootstrap
# που χρησιμοποιείται (εδώ χρησιμοποιήσαμε το "3" (δες παραπάνω).
# Τα υποστηριζόμενα θέματα μπορούμε να τα βρούμε στις διευθύνσεις:
# Bootstrap 2: https://bootswatch.com/2
# Bootstrap 3: https://bootswatch.com/3
    'bootswatch_theme': "cerulean",
}

html_sidebars = {
    "**": [
           "globaltoc.html",
           "localtoc.html",
          ]
                }



html_domain_indices = True

html_compact_lists = True


##---------------PDF OUTPUT ------------------------------------------
# δες https://rinohtype.readthedocs.io/en/latest/index.html

# latex_additional_files = ["mystyle.sty"]
latex_engine = 'xelatex'
latex_show_urls = 'no' # εναλλακτικά 'footnote', 'inline'
latex_toplevel_sectioning = 'part'
latex_additional_files = ["mystyle.tex.txt"]
latex_appendices = ["temp"]
latex_elements = {

    'papersize': 'a4paper',

    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': r'\usepackage{mystyle}',

    'footer': r"""  """,

    'maketitle': r'''\pagenumbering{arabic}''',


    'fncychap': r'\usepackage[Sonny]{fncychap}', # εναλλακτικά:
                                                 # Bjornstrup
                                                 # Lenny
                                                 # Glenn
                                                 # Conny
                                                 # Renje

    'preamble': r'\input{mystyle.tex.txt}',

    'printindex': r'\footnotesize\raggedright\printindex',

    'sphinxsetup': 'hmargin={2cm, 2cm}, vmargin={2.5cm, 2.5cm}, verbatimwithframe=false', 

                }
