import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = "Моё первое приложение на Flet"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Hello world")

    greeting_history = []
    history_text = ft.Text(value='История приветствий:')

    name_input = ft.TextField(label="Введите имя")
    greet_button = ft.ElevatedButton(text="Поздороваться")

    def on_button_click(_):
        name = name_input.value.strip()
        if name:
            # Форматируем время
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # Приветствие
            greeting_text.value = f"Hello, {name}! ({now})"
            # Добавляем в историю
            greeting_history.append(f"{name} — {now}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            # Обновляем страницу
            page.update()

    greet_button.on_click = on_button_click

    page.add(
        name_input,
        greet_button,
        greeting_text,
        history_text
    )


ft.app(target=main)
