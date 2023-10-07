CHANGES
*******

0.4 (unreleased)
================

- Add support for Python 3.11 and PyPy 3.9-

- Drop support for Python 3.6 and use `pyupgrade --py37-plus`.

- Remove buildout.

- Add development setup.

- Sort imports with isort.


0.3 (2022-05-29)
================

- Apply `pyupgrade --py36-plus`.

- Use black code formatter.

- Add support for Python 3.6, 3.7, 3.8, 3.9 and 3.10.

- Fix test collection.

- Drop support for Python 2.7, 3.4, 3.5.

- Updated the test suite to work with Morepath 0.15.

- Added Tox environments for Python 3.6, PyPy 3, PEP8.

- Clean up meta data.

- Use GitHub Actions for CI.

- Fix Jinja2 integration - the ``autoescape`` extension was removed as now it
  is built-in.


0.2 (2015-04-09)
================

- Actual release to PyPI.


0.1 (2015-04-09)
================

- Initial public release.
