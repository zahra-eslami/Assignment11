
# 11th Assignments in Python

# Classes in Phyton

In Python, a class is a blueprint for creating objects. Objects are instances of classes and can have attributes (characteristics) and methods (functions) associated with them. Classes provide a way to structure and organize code in a modular and reusable manner, making it a fundamental concept in object-oriented programming (OOP).

---

## Defining a Class
To define a class in Python, use the class keyword followed by the class name. The class body contains attributes and methods.

```
class MyClass:
    # class body
    pass
```
---
## Constructor (init)
The __init__ method is a special method called a constructor. It is executed when an object is created and allows you to initialize instance variables.

```
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```
---
## Inheritance
Inheritance allows a class to inherit attributes and methods from another class. This promotes code reuse and helps create a hierarchy of classes.

```
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"
```
---

## Example
Here's a simple example combining the concepts discussed above:

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.make} {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Accessing attributes and calling a method
print(my_car.display_info())  # Output: Toyota Camry
```

## Benefits of Using Classes

- **Modularity :** Classes facilitate modular and organized code.
- **Reusability :** Objects created from classes promote code reuse.
- **Encapsulation**: Attributes and methods are encapsulated within objects.

---
You can alse see more example of using classes in this repository.