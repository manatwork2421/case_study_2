class Student:
    def __init__(self, name, marks=[]):
        self.name = name
        self.marks = marks or []

    def add_mark(self, mark):
        self.marks.append(mark)

    def average(self):
        if not self.marks:
            return 0
        else:
            return sum(self.marks)/len(self.marks)
        
    def has_passed(self, threshold=40):
        return self.average() >= threshold
        
