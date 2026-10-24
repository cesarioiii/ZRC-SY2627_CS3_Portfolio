# Single Inheritance

```python
class Parent:
    def __init__(self, msg="This function is in parent class."):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def func1(self):
        print(self._msg)

class Child(Parent):
    def func2(self):
        print("This function is in child class.")

obj = Child()
obj.func1()
obj.func2()
```


# Multilevel Inheritance
```python
class Grandfather:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class Father(Grandfather):
    def __init__(self, father_name, grandfather_name):
        super().__init__(grandfather_name)
        self._father_name = father_name

    @property
    def father_name(self):
        return self._father_name

    @father_name.setter
    def father_name(self, value):
        self._father_name = value

class Son(Father):
    def __init__(self, son_name, father_name, grandfather_name):
        super().__init__(father_name, grandfather_name)
        self._son_name = son_name

    @property
    def son_name(self):
        return self._son_name

    @son_name.setter
    def son_name(self, value):
        self._son_name = value

    def print_name(self):
        print("Grandfather name :", self.name)
        print("Father name :", self.father_name)
        print("Son name :", self.son_name)

s1 = Son('Prince', 'Rampal', 'Lal mani')
s1.print_name()
```


# Heirarchical Inheritance
```python
class Parent:
    def __init__(self, msg="This function is in parent class."):
        self._msg = msg

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    def func1(self):
        print(self._msg)

class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")

class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")

# Testing the code
object1 = Child1()
object2 = Child2()

object1.func1()
object1.func2()

object2.func1()
object2.func3()
```