from more.jinja2 import Jinja2App


class App(Jinja2App):
    pass


@App.path(path='persons/{name}')
class Person(object):
    def __init__(self, name):
        self.name = name


@App.template_directory()
def get_template_dir():
    return 'templates'


@App.setting_section(section='jinja2')
def get_setting_section():
    return {
        'auto_reload': True,
    }


# note "person_autoreload.jinja2" will be created (and deleted) by the test
@App.html(model=Person, template='person_autoreload.jinja2')
def person_default(self, request):
    return {'name': self.name}
