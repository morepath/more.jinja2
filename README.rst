.. image:: https://github.com/morepath/more.jinja2/workflows/CI/badge.svg?branch=master
   :target: https://github.com/morepath/more.jinja2/actions?workflow=CI
   :alt: CI Status

.. image:: https://coveralls.io/repos/github/morepath/more.jinja2/badge.svg?branch=master
    :target: https://coveralls.io/github/morepath/more.jinja2?branch=master

.. image:: https://img.shields.io/pypi/v/more.jinja2.svg
  :target: https://pypi.org/project/more.jinja2/

.. image:: https://img.shields.io/pypi/pyversions/more.jinja2.svg
  :target: https://pypi.org/project/more.jinja2/


more.jinja2: Jinja2 template integration for Morepath
=====================================================

``more.jinja2`` is an extension for Morepath_ that adds Jinja2_
template support when you use the ``.jinja2`` extension.

For details on the Jinja2 template language see the `Jinja2
template designer documentation`_.

Example usage::

  from more.jinja2 import Jinja2App

  class App(Jinja2App):
      pass

  @App.path(path='persons/{name}')
  class Person(object):
       def __init__(self, name):
           self.name = name

  @App.template_directory()
  def get_template_directory():
      return 'templates'

  @App.html(model=Person, template='person.jinja2')
  def person_default(self, request):
      return {'name': self.name}

and then in ``person.jinja2`` (in the ``templates`` subdirectory)::

  <html>
  <body>
  <p>Hello {{name}}!</p>
  </body>
  </html>

Note that the Jinja2 documentation uses the ``.html`` extension for
Jinja2 templates, whereas this extension uses ``.jinja2`` instead.

To control Jinja2 behavior you can define a ``jinja2`` setting section
in your app. For instance::

  @App.setting_section(section='jinja2')
  def get_setting_section():
      return {
        'auto_reload': False,
        'autoescape': True,
      }

For details on Jinja2 configuration options, consult the `Jinja2 API
documentation`_.

.. _Morepath: http://morepath.readthedocs.org

.. _Jinja2: http://jinja.pocoo.org/

.. _`Jinja2 template designer documentation`: http://jinja.pocoo.org/docs/dev/templates/

.. _`Jinja2 API documentation`: http://jinja.pocoo.org/docs/dev/api/#jinja2.Environment
