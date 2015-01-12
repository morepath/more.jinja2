import morepath
import more.jinja2
from webtest import TestApp as Client
import pytest
from .fixtures import (
    template, template_inheritance, override_template,
    override_template_inheritance)


def setup_module(module):
    morepath.disable_implicit()


def test_template():
    config = morepath.setup()
    config.scan(more.jinja2, ignore=['.tests'])
    config.scan(template)
    config.commit()
    c = Client(template.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''


def test_override_template():
    config = morepath.setup()
    config.scan(more.jinja2, ignore=['.tests'])
    config.scan(override_template)
    config.commit()

    c = Client(override_template.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''

    c = Client(override_template.SubApp())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hi world!</p>
</body>
</html>'''


def test_template_inheritance():
    config = morepath.setup()
    config.scan(more.jinja2, ignore=['.tests'])
    config.scan(template_inheritance)
    config.commit()
    c = Client(template_inheritance.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>'''


def test_override_template_inheritance():
    config = morepath.setup()
    config.scan(more.jinja2, ignore=['.tests'])
    config.scan(override_template_inheritance)
    config.commit()
    c = Client(override_template_inheritance.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>'''

    c = Client(override_template_inheritance.SubApp())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<head>
</head>
<body>
<div id="content2">
<p>Hello world!</p>
</div>
</body>
</html>'''
