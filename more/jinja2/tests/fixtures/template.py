from more.jinja2 import Jinja2App


class App(Jinja2App):
    pass


@App.path(path='persons/{name}')
class Person(object):
    def __init__(self, name):
        self.name = name


@App.html(model=Person, template='templates/person.jinja2')
def person_default(self, request):
    return {'name': self.name}
