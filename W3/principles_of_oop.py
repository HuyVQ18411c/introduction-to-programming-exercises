# In the scope of this example, I will only focus on the concepts of OOP instead of programming syntax
# Instead of explaining syntaxes in details.
# Kế thừa - Inheritance
# Đa hình - Polymorphism
# Bao đóng - Encapsulation
# Trừu tượng - Abstraction
from abc import abstractmethod

class Human:
    def __init__(self, job: str = None, name: str = '', weight:int = 40) -> None:
        self.job: str = job
        self.name: str = name

        # This attribute has underscore prefix, it should not be accessed from outsider🧐
        self._weight: int = weight

    # If you're curious about what the heck is `property` here, 
    # you can read more about getter/setter/delleter in Python: 
    # TODO: read https://www.programiz.com/python-programming/property
    # TODO: read https://www.geeksforgeeks.org/getter-and-setter-in-python/
    @property
    def weight(self):
        return self._weight

    def hangout(self):
        print(f'{self.name} (the {self.job}) is hanging out!')
    
    @abstractmethod
    def go_to_work(self):
        # This method has been marked as abstract
        # Child class will have this method, but it has to implement it if they want to access it
        # Raise error if child class is trying to access this method without override it.
        raise NotImplementedError('Not implemented')
    

class Student(Human): # Inheritance
    def __init__(self, name: str = '') -> None:
        super().__init__('student', name)


class Teacher(Human):
    def __init__(self, name: str = '') -> None:
        super().__init__('teacher', name)

    def go_to_work(self):
        print(f'{self.name} (the {self.job}) is going to school.')

    @property
    def weight(self):
        print('This is a huge secret. You don\'t have permission to view this😠.')


class Developer(Human):
    def __init__(self, name: str = '') -> None:
        super().__init__('developer', name)

    def go_to_work(self):
        print(f'{self.name} (the {self.job}) is going a software company.')

if __name__ == '__main__':
    student = Student('Huy')
    teacher = Teacher('Anh')
    developer = Developer('Huythuhai')

    # Inheritance
    # We do not need to re-implement `hangout` anymore
    # Since it has been `inherited` from `Human`` class
    student.hangout()
    teacher.hangout()

    # Polymorphism/Abstraction
    # Everyone will have to go to work
    # But definition of `go_to_work` can vary depends on their job.
    teacher.go_to_work()
    developer.go_to_work()

    # This call will raise `NotImplementedError` 
    # because it hasn't been implemented in Student class
    # TODO: go to student class and implement this method, and re-run
    student.go_to_work() 

    # Encapsulation
    # Nothing is really `private` in Python
    # However you can have some work around
    # Let try to access it first from a student
    print(student.weight) # It should not raise any exception

    # Let try to access from a teacher
    print(teacher.weight) # It should give you a threat 😈
    # Since we added a wrapper around `weight` property in `Teacher` class
    # As the result, you can not view the weight of that teacher.
