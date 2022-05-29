import morepath
import jinja2


class Jinja2App(morepath.App):
    pass


@Jinja2App.setting_section(section="jinja2")
def get_setting_section():
    return {
        "auto_reload": False,
    }


@Jinja2App.template_loader(extension=".jinja2")
def get_jinja2_loader(template_directories, settings):
    config = settings.jinja2.__dict__.copy()

    # we always want to use autoescape as this is about
    # HTML templating
    config.update({"autoescape": True})

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directories), **config
    )


@Jinja2App.template_render(extension=".jinja2")
def get_jinja2_render(loader, name, original_render):
    template = loader.get_template(name)

    def render(content, request):
        variables = {"request": request}
        variables.update(content)
        return original_render(template.render(**variables), request)

    return render
