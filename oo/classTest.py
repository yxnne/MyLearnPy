class Student():
    def __init__(self):
        self.name = "yxnne"
        self.age = 29

    def __init__(self, name="yxnne", age=29):
        self.name = name
        self.age = age

    def my_info(self):
        info = "my name is :" + self.name + " age is " + str(self.age)
        print(info)


stu = Student()
stu.my_info()

other = Student("jerk", 40)

other.my_info()


def test_import():
    print("this is just a test")
