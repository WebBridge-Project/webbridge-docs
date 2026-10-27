project = "webbridge"
copyright = "2026 F&S Bondtec Semiconductor GmbH"
author = "F&S Bondtec Semiconductor GmbH"
release = "0.1.0"

extensions = [
    "myst_parser",
    "breathe",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.intersphinx",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = ["fieldlist", "deflist"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "webbridge"

# -- Breathe (C++ API, from webbridge-runtime headers via Doxygen) ----------
breathe_projects = {"webbridge": "../doxygen/xml"}
breathe_default_project = "webbridge"

# -- Autodoc (Python API, from the installed webbridge-tools package) ------
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}
