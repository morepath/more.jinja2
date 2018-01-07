import os

from webtest import TestApp as Client
from .fixtures import (
    template, template_inheritance, override_template,
    override_template_inheritance, template_autoreload)


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


def test_autoreload_template():
    templates_path = os.path.join(
        os.path.dirname(__file__), 'fixtures', 'templates')
    with open(os.path.join(templates_path, 'person.jinja2')) as template:
        template_lines = template.readlines()

    autoreload_path = os.path.join(templates_path, 'person_autoreload.jinja2')
    with open(autoreload_path, mode='w') as template:
        template.writelines(template_lines)
    timestamp = os.path.getmtime(autoreload_path)

    c = Client(template_autoreload.App())

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
</body>
</html>'''

    with open(autoreload_path, mode='w') as template:
        for line in template_lines:
            if 'Hello' in line:
                line += '<p>Autoreload Test</p>\n'
            template.write(line)

    # alter modification time as required by the jinja2 FileSystemLoader
    # https://github.com/pallets/jinja/blob/master/jinja2/loaders.py#L179-L187
    os.utime(autoreload_path, (timestamp, timestamp + 1))

    response = c.get('/persons/world')
    assert response.body == b'''\
<html>
<body>
<p>Hello world!</p>
<p>Autoreload Test</p>
</body>
</html>'''

    os.unlink(autoreload_path)
