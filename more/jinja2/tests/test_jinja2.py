from webtest import TestApp as Client
from .fixtures import (
    template, template_inheritance, override_template,
    override_template_inheritance, inject_models, inject_globals)


def test_template():
    c = Client(template.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''


def test_override_template():
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


def test_inject_globals():
    c = Client(inject_globals.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
<p>This is fancy</p>
</body>
</html>'''


def test_inject_models():
    c = Client(inject_models.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
<p><a href="http://localhost/persons/mars">Mars</a></p>
</body>
</html>'''
