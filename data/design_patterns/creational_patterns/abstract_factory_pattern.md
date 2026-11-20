# Abstract Factory Pattern

- It provides interface for creating families of. related or dependent objects without specifying their concrete classes.

> **Example:** A UI theme system supports Light and Dark themes, where each theme provides its own set of components like Button and TextBox. The application uses a factory to create these components, allowing it to switch between themes without changing the main code.

![abstract_factory_pattern](../../assets/images/design_patterns/creational_pattern/uicomponentfactory.webp)

```python
from abc import ABC, abstractmethod

# Abstract Product A
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

# Concrete Product A1
class WindowsButton(Button):
    def click(self):
        print("Windows button clicked")

# Concrete Product A2
class MacOSButton(Button):
    def click(self):
        print("MacOS button clicked")

# Abstract Product B
class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Concrete Product B1
class WindowsCheckbox(Checkbox):
    def check(self):
        print("Windows checkbox checked")

# Concrete Product B2
class MacOSCheckbox(Checkbox):
    def check(self):
        print("MacOS checkbox checked")

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factory 1
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Concrete Factory 2
class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()


# Client code
def create_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    return button, checkbox


# factory based on user preference
def read_factory() -> GUIFactory:
    factory = {
        "windows": WindowsFactory(),
        "macos": MacOSFactory()
    }
    return factory.get(input("Enter the type of GUI you want to create: "), None)


# Usage
if __name__ == "__main__":
    gui_factory = read_factory()
    if gui_factory:
        print(f"{gui_factory.__class__.__name__}GUI:")
        button, checkbox = create_gui(gui_factory)
        button.click()
        checkbox.check()
    else:
        print("Invalid input")
```

![code explanation](../../assets/images/design_patterns/creational_pattern/abstractFactoryCode.webp)
