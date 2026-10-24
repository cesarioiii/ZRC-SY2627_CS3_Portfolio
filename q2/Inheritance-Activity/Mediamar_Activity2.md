# Single Inheritance
class Parent:
    def __init__(self, parent_message="This function is in parent class."):
        self._parent_message = parent_message  

    @property
    def parent_message(self):
        """Getter for parent_message"""
        return self._parent_message

    @parent_message.setter
    def parent_message(self, message):
        """Setter for parent_message"""
        self._parent_message = message

    def func1(self):
        print(self._parent_message)

class Child(Parent):
    def __init__(self, parent_message="This function is in parent class.", child_message="This function is in child class."):
        super().__init__(parent_message)
        self._child_message = child_message

    @property
    def child_message(self):
        """Getter for child_message"""
        return self._child_message

    @child_message.setter
    def child_message(self, message):
        """Setter for child_message"""
        self._child_message = message

    def func2(self):
        print(self._child_message)

obj = Child()
obj.parent_message = "Updated Parent Message via Property!"
obj.child_message = "Updated Child Message via Property!"

obj.func1()
obj.func2()



# Multilevel Inheritance
class Grandfather:
    def __init__(self, grandfathername):
        self._grandfathername = grandfathername

    @property
    def grandfathername(self):
        return self._grandfathername

    @grandfathername.setter
    def grandfathername(self, name):
        self._grandfathername = name


class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self._fathername = fathername
        super().__init__(grandfathername)

    @property
    def fathername(self):
        return self._fathername

    @fathername.setter
    def fathername(self, name):
        self._fathername = name


class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self._sonname = sonname
        super().__init__(fathername, grandfathername)

    @property
    def sonname(self):
        return self._sonname

    @sonname.setter
    def sonname(self, name):
        self._sonname = name

    def print_name(self):
        print("Grandfather name :", self._grandfathername)
        print("Father name :", self._fathername)
        print("Son name :", self._sonname)


s1 = Son('Prince', 'Rampal', 'Lal mani')

s1.sonname = 'Aryan'
s1.fathername = 'Vikram'

print("Grandfather name accessed via property:", s1.grandfathername)
s1.print_name()



# Heirarchical Inheritance
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
    def __init__(self, parent_msg, child1_msg="This function is in child 1."):
        super().__init__(parent_msg)
        self._child1_msg = child1_msg

    @property
    def child1_msg(self):
        return self._child1_msg

    @child1_msg.setter
    def child1_msg(self, value):
        self._child1_msg = value

    def func2(self):
        print(self._child1_msg)

class Child2(Parent):
    def __init__(self, parent_msg, child2_msg="This function is in child 2."):
        super().__init__(parent_msg)
        self._child2_msg = child2_msg

    @property
    def child2_msg(self):
        return self._child2_msg

    @child2_msg.setter
    def child2_msg(self, value):
        self._child2_msg = value

    def func3(self):
        print(self._child2_msg)

object1 = Child1("Parent shared with Child 1")
object2 = Child2("Parent shared with Child 2")

object1.child1_msg = "Modified Child 1 output string."
object2.msg = "Updated Parent message for Child 2."

object1.func1()
object1.func2()

object2.func1()
object2.func3()