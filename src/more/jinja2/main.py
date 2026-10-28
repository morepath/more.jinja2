from __future__ import annotations

from typing import TYPE_CHECKING, Any

import jinja2
import morepath

if TYPE_CHECKING:
    from collections.abc import Sequence
    from os import PathLike

    from webob import Response as BaseResponse

    from morepath import Request
    from morepath.settings import SettingRegistry
    from morepath.types import Render


class Jinja2App(morepath.App):
    pass


@Jinja2App.setting_section(section="jinja2")
def get_setting_section() -> dict[str, Any]:
    return {
        "auto_reload": False,
    }


@Jinja2App.template_loader(extension=".jinja2")
def get_jinja2_loader(
    template_directories: str | PathLike[str] | Sequence[str | PathLike[str]],
    settings: SettingRegistry,
) -> jinja2.Environment:
    config = settings.jinja2.__dict__.copy()

    # we always want to use autoescape as this is about
    # HTML templating
    config.update({"autoescape": True})

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directories), **config
    )


@Jinja2App.template_render(extension=".jinja2")
def get_jinja2_render(
    loader: jinja2.Environment, name: str, original_render: Render
) -> Render:
    template = loader.get_template(name)

    def render(content: Any, request: Request[Jinja2App]) -> BaseResponse:
        variables: dict[str, Any] = {"request": request}
        variables.update(content)
        return original_render(template.render(**variables), request)

    return render
