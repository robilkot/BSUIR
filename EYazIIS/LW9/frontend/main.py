import flet as ft
from frontend.app import AbstractApp

def main(page: ft.Page):
    app = AbstractApp()
    app.main(page)

def start_app():
    ft.app(target=main)

if __name__ == "__main__":
    ft.app(target=main)