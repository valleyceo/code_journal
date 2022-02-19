class Student(object):
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def __lt__(self, other):
        return self.gpa < other.gpa

students = [Student('A', 4.0), Student('B', 3.0), Student('C', 2.0), Student('D', 1.0)]

# Sort by gpa
sorted_by_name = sorted(students)

# Sort by student name
students.sort(key = lambda x : x.name)
