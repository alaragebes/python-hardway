class Person(object):
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.age = age

    def __str__ (self):
        return self.first_name + " " + self.last_name + " " + str(self.age)

class Lecture (Person):
    def __init__(self, first, last, age, lec_num):
        super(Lecture, self).__init__(first, last, age)
        self.lec_num = lec_num

    def __str__ (self):
        return super(Lecture, self).__str__() + ", " + str(self.lec_num)


x = Person ("Rocky", "Balboa", 30)
y = Lecture ("Frank", "Sinatra", 35, "Music")

print x
print y
