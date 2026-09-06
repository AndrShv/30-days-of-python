from abc import ABC, abstractmethod


class AbstractButton(ABC):
    @abstractmethod
    def set_button_colour(self):
        pass

class AbstractInputLine(ABC):
    @abstractmethod
    def set_input_colour(self):
        pass


class AbstractThemeFactory(ABC):
    @abstractmethod
    def create_button(self) -> AbstractButton:
        pass

    @abstractmethod
    def create_input(self) -> AbstractInputLine:
        pass


class LightButton(AbstractButton):
    def set_button_colour(self):
        return "⚪ Светлая кнопка"


class LightInputLine(AbstractInputLine):
    def set_input_colour(self):
        return "⬜ Светлое поле ввода"

class DarkButton(AbstractButton):
    def set_button_colour(self):
        return "⬛ Тёмная кнопка"


class DarkInputLine(AbstractInputLine):
    def set_input_colour(self):
        return "🔳 Тёмное поле ввода"




class LightThemeFactory(AbstractThemeFactory):
    def create_button(self) -> AbstractButton:
        return LightButton()

    def create_input(self) -> AbstractInputLine:
        return LightInputLine()

class DarkThemeFactory(AbstractThemeFactory):
    def create_button(self) -> AbstractButton:
        return DarkButton()

    def create_input(self) -> AbstractInputLine:
        return DarkInputLine()

def render_ui(factory):
    new_button = factory.create_button()
    new_input = factory.create_input()
    print(f"Отрисовка: {new_button.set_button_colour()} и {new_input.set_input_colour()}")

render_ui(LightThemeFactory())
render_ui(DarkThemeFactory())