# Builder design Pattern

- It provides a step-by-step approach to constructing complex objects. It separates the construction process from the object’s representation, enabling the same method to create different variations of an object.

> **Example:** Consider building an SQL query in a database application. A query can have different parts like select fields, conditions, sorting, and limits.

![Builder Pattern](../../assets/images/design_patterns/creational_pattern/bilderPatter.webp)

The final complex object that is created using the Builder pattern.

```python
""" Product """
class Computer:

    def __init__(self):
        self.cpu_ = ""
        self.ram_ = ""
        self.storage_ = ""

    def setCPU(self, cpu):
        self.cpu_ = cpu

    def setRAM(self, ram):
        self.ram_ = ram

    def setStorage(self, storage):
        self.storage_ = storage

    def displayInfo(self):
        print(f'Computer Configuration:\nCPU: {self.cpu_}\nRAM: {self.ram_}\nStorage: {self.storage_}\n\n')
```
