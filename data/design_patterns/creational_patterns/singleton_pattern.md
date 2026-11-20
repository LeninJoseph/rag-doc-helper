# _Singleton_:

- Ensures a class has only one instance and provides a global point of access to it.
- It is used when we wantcentralized control of resources, such as managing database connections, configuration settings or logging.

> **Example:** A Database Connection Manager uses a single shared instance instead of creating multiple connections. This ensures efficient resource usage and consistent access to the database across the application.

![Singleton](../../assets/images/design_patterns/creational_pattern/singleton.jpg)

```python
class Singleton:
    _instance = None

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            Singleton._instance = Singleton()
        return Singleton._instance

# Usage
singleton_instance = Singleton.get_instance()
```

## Thread-Safety in Singleton Design Pattern

- In a multi-threaded environment, the basic implementation of the Singleton Design Pattern may fail due to a problem known as a **race condition**.
- When multiple threads try to access the Singleton instance at the same time, it can lead to the creation of more than one instance, which violates the core principle of Singleton.

To make the singleton pattern thread-safe, we can use synchronization mechanisms such as locks to ensure that only one thread can create the instance at a time.

```python
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            with Singleton._lock:
                if Singleton._instance is None:
                    Singleton._instance = Singleton()
        return Singleton._instance

# Usage
singleton_instance = Singleton.get_instance()
```
