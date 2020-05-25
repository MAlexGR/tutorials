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


################ Project information ############################

"""
The project name, copyright, and author.
"""

project = u'Generic Tutorials'
copyright = '2020, Alex M.'
author = 'Alex M.'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

##################################################################


################### General configuration ########################

#---- Add any Sphinx extension module names here, as strings.
#---- They can be extensions coming with Sphinx (named
#---- 'sphinx.ext.*') or your custom ones.

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'rinoh.frontend.sphinx',
    'recommonmark'
]

# Που να "βλέπει" το intersphinx extension

intersphinx_mapping = {
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
    'python': ('https://docs.python.org/3', None),
}

# Που να "βλέπει" το extlinks extension (δες https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html)

# extlinks = {
#     'issue': ('https://github.com/sphinx-doc/sphinx/issues/%s', 'issue ')
#             }



# Add any paths that contain templates here, relative to this directory.

"""
Tells the project where to look for theme templates and css overrides.
"""

templates_path = ['_templates']
html_static_path = ["_static"]



# The master toctree document.

"""
Tells the project the name of the home page.
"""

master_doc = 'index'



# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'el'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
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
html_css_files = [
    'css/custom.css',
]

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


##---- HTML SETTINGS -------------------------------------------------

# for material
#html_theme_options = {
#    'nav_title': 'Οδηγοί Επιβίωσης',
#    'globaltoc_depth': 2,
#    'globaltoc_collapse': False,
#    'globaltoc_includehidden': False
#}

html_theme_options = {
    'navbar_title': 'Οδηγοί Επιβίωσης', # Ο βασικός τίτλος στο
                                        # navication bar
                                          
    'navbar_site_name': 'Site',         # Tab name for entire site.
                                        # (Default: "Site")

    'navbar_pagenav_name': "Page",      # Tab name for the current
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
    'bootswatch_theme': "sandstone",
}

html_sidebars = {
    "**": [
           "globaltoc.html",
           "localtoc.html",
          ]
                }

# html_sidebars = {
#     'sidebar': [
#                 'globaltoc.html',
#                 'localtoc.html',
#                 'sourcelink.html',
#                 'searchbox.html',
#                ]
#                 }

# Add any paths that contain custom static files (such as style
# sheets) here, relative to this directory. They are copied after the
# builtin static files, so a file named "default.css" will overwrite
# the builtin "default.css".
html_static_path = ['_static']


##---------------PDF OUTPUT ------------------------------------------
# δες https://rinohtype.readthedocs.io/en/latest/index.html