"""
Sphinx Ansible theme.

From https://github.com/ryan-roemer/sphinx-bootstrap-theme.
"""

from __future__ import absolute_import, division
from os import path
import sphinx

__metaclass__ = type


try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("sphinx_ansible_theme").version
except Exception:
    __version__ = "unknown"


__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = path.abspath(path.dirname(path.dirname(__file__)))
    return cur_dir


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    """Sphinx entry point."""
    if sphinx.version_info >= (1, 6, 0):
        # Register the theme that can be referenced without adding a theme path
        app.add_html_theme("sphinx_ansible_theme", path.abspath(path.dirname(__file__)))

    if sphinx.version_info >= (1, 8, 0):
        # Add Sphinx message catalog for newer versions of Sphinx
        # See http://www.sphinx-doc.org/en/master/extdev/appapi.html#sphinx.application.Sphinx.add_message_catalog
        rtd_locale_path = path.join(path.abspath(path.dirname(__file__)), "locale")
        app.add_message_catalog("sphinx", rtd_locale_path)

    return {"parallel_read_safe": True, "parallel_write_safe": True}