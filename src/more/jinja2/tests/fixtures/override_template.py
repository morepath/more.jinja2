from __future__ import annotations

from typing import TYPE_CHECKING, Any

from more.jinja2 import Jinja2App

if TYPE_CHECKING:
    from morepath import Request


class App(Jinja2App):
    pass


@App.path(path="persons/{name}")
class Person:
    def __init__(self, name: str) -> None:
        self.name = name


@App.template_directory()
def get_template_dir() -> str:
    return "templates"


@App.html(model=Person, template="person.jinja2")
def person_default(self: Person, request: Request[App]) -> dict[str, Any]:
    return {"name": self.name}


class SubApp(App):
    pass


@SubApp.template_directory()
def get_template_dir_override() -> str:
    return "templates_override"
