class students:
    def __init__(self,id,name,DoB):
        self.id = id
        self.name = name
        self.DoB = DoB
        self.GPA = 0
    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\nDoB: {self.DoB}\nGPA: {self.GPA}"