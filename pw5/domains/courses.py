class courses:
    def __init__(self,id,name,credit):
        self.id = id
        self.name = name
        self.credit = credit
    def __str__(self):
        return f"id: {self.id}\nname: {self.name}\ncredit: {self.credit}" 