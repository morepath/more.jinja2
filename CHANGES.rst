CHANGES
*******

1.0.0 (unreleased)
------------------

- Add type annotations and integrate ``mypy`` and ``pyright``.

- Switch to ``pyproject.toml`` based project setup.

- Switch to ``src-layout`` based file structure.

- Switch to native namespace package defined in PEP 420.

- Add support for Python 3.12 - 3.15.

- Drop support for Python below 3.11.

- Support Pypy 3.12.

- Switch from black, flake8, isort and pyupgrade to Ruff_ linter and formatter.

  .. _Ruff: https://docs.astral.sh/ruff

- Replace ``pre-commit`` integration with our custom tracked
  pre-commit git hook for Ruff checks on staged Python files.

- Update ``README.rst`` and rename ``CHANGES.txt`` to ``CHANGES.rst``.

- Remove coveralls integration.

- Update CI workflow.

- Adjust the deployment strategy:
  
  * Move the Pypi upload from ``zest.release`` to ``gh-actions``.

  * Use ``v`` + version as release tags like ``v1.0.0``.

  * So we still use ``zest.release`` but without publishing to Pypi.
    The Pypi upload is triggered by pushing the new release tag to GitHub.
    This happens in the Release workflow in ``.github/workflows/release.yml``.
    With this workflow we get Trusted Publishing with short-lived OIDC tokens
    that PyPI issues to one specific repository, workflow file and environment (``pypi``).
    We also get PEP 740 provenance and can set required reviewers for the environment
    and a ruleset who can create release tags and trigger releases.

- Make an overall cleanup.


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
