from webtest import TestApp as Client
from .fixtures import (
    template,
    template_inheritance,
    override_template,
    override_template_inheritance,
)


def test_template():
    c = Client(template.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<p>Hello world!</p>
</body>
</html>"""
    )


def test_override_template():
    c = Client(override_template.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<p>Hello world!</p>
</body>
</html>"""
    )

    c = Client(override_template.SubApp())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<body>
<p>Hi world!</p>
</body>
</html>"""
    )


def test_template_inheritance():
    c = Client(template_inheritance.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>"""
    )


def test_override_template_inheritance():
    c = Client(override_template_inheritance.App())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<head>
</head>
<body>
<div id="content">
<p>Hello world!</p>
</div>
</body>
</html>"""
    )

    c = Client(override_template_inheritance.SubApp())

    response = c.get("/persons/world")
    assert (
        response.body
        == b"""\
<html>
<head>
</head>
<body>
<div id="content2">
<p>Hello world!</p>
</div>
</body>
</html>"""
    )
