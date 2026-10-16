from more.jinja2 import Jinja2App


class App(Jinja2App):
    pass


@App.path(path="persons/{name}")
class Person:
    def __init__(self, name):
        self.name = name


@App.template_directory()
def get_template_dir():
    return "templates"


@App.html(model=Person, template="person_inherit.jinja2")
def person_default(self, request):
    return {"name": self.name}
