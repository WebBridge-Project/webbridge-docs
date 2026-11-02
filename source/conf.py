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
    "sphinx_design",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = ["fieldlist", "deflist", "colon_fence"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "pydata_sphinx_theme"
html_title = "webbridge"

# -- pydata-sphinx-theme: top navbar tabs come from the top-level entries of
# -- the root toctree in index.md (each nested toctree becomes a dropdown) --
html_theme_options = {
    "navigation_with_keys": True,
    "show_toc_level": 2,
    "navbar_align": "left",
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "icon_links": [
        {
            "name": "webbridge-runtime (C++)",
            "url": "https://github.com/WebBridge-Project/webbridge-runtime",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "webbridge-tools (Python)",
            "url": "https://github.com/WebBridge-Project/webbridge-tools",
            "icon": "fa-brands fa-python",
        },
    ],
}

# -- Breathe (C++ API, from webbridge-runtime headers via Doxygen) ----------
breathe_projects = {"webbridge": "../doxygen/xml"}
breathe_default_project = "webbridge"

# -- Autodoc (Python API, from the installed webbridge-tools package) ------
autodoc_member_order = "bysource"
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
}
