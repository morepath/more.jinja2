import os
import morepath
import jinja2


class Jinja2App(morepath.App):
    pass


@Jinja2App.setting_section(section='jinja2')
def get_setting_section():
    return {
        'auto_reload': False,
        'autoescape': True,
        'extensions': ['jinja2.ext.autoescape']
    }


@Jinja2App.template_engine(extension='.jinja2')
def get_jinja2_render(path, original_render, settings):
    config = settings.jinja2.__dict__
    # XXX creates a new environment and loader each time,
    # which could slow startup somewhat
    dirpath, filename = os.path.split(path)
    environment = jinja2.Environment(
        loader=jinja2.FileSystemLoader(dirpath),
        **config)
    template = environment.get_template(filename)
    def render(content, request):
        variables = {'request': request}
        variables.update(content)
        return original_render(template.render(**variables), request)
    return render
