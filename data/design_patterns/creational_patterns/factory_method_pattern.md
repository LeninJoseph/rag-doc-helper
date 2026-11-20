# Factory Method

- It defines an interface for creating objects but lets subclasses decide which object to instantiate.

> **Example:** Consider a Notification System where you need to send different types of notifications like Email, SMS, or Push notifications. Instead of creating objects directly, you use a Factory Method to decide which notification to create.

![Factory Method](../../assets/images/design_patterns/creational_pattern/notificationfactory.webp)

```python
from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def save(self):
        pass

class TextDocument(Document):
    def open(self):
        print("Opening Text Document")

    def save(self):
        print("Saving Text Document")

class SpreadsheetDocument(Document):
    def open(self):
        print("Opening Spreadsheet Document")

    def save(self):
        print("Saving Spreadsheet Document")


if __name__ == "__main__":

    # Taking input from the user to create a document
    doc_type = input("Enter the type of document you want to create: ")

    # Creating the document based on the user input
    if doc_type == "text":
        doc = TextDocument()
    elif doc_type == "spreadsheet":
        doc = SpreadsheetDocument()
    else:
        print("Invalid document type")

    # Using the document
    doc.open()
    doc.save()
```
