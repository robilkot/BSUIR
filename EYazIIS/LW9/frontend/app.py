import flet as ft
from frontend.models.app_state import AppState
from frontend.views.input_view import InputView
from frontend.views.result_view import ResultView
from frontend.views.help_view import HelpView


class AbstractApp:

    def __init__(self):
        self.app_state = AppState()
        self.page = None
        self.views = {}

    def main(self, page: ft.Page):
        self.page = page
        self._setup_page()
        self._setup_views()
        self._setup_routing()

        page.go("/")

    def _setup_page(self):
        self.page.title = "Система автоматического реферирования"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 0
        self.page.scroll = ft.ScrollMode.AUTO

    def _setup_views(self):
        input_view = InputView(self.page, self.app_state)
        result_view = ResultView(self.page, self.app_state)
        help_view = HelpView(self.page, self.app_state)

        file_pickers = []
        file_pickers.append(input_view.get_file_picker())
        file_pickers.append(result_view.get_save_dialog())

        for picker in file_pickers:
            if picker not in self.page.overlay:
                self.page.overlay.append(picker)

        self.views = {
            "/": input_view,
            "/results": result_view,
            "/help": help_view
        }

    def _setup_routing(self):

        def route_change(route):
            self.page.views.clear()

            view = self.views.get(self.page.route, self.views["/"])

            if hasattr(view, 'refresh'):
                view.refresh()

            self.page.views.append(
                ft.View(
                    self.page.route,
                    [view.get_content()],
                    padding=0
                )
            )
            self.page.update()

        def view_pop(view):
            self.page.views.pop()
            top_view = self.page.views[-1]
            self.page.go(top_view.route)

        self.page.on_route_change = route_change
        self.page.on_view_pop = view_pop