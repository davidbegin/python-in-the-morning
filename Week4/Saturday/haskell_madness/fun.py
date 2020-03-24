class Zach():
    longname = "Zachari"

    def __init__(self, last_name):
        self.last_name = last_name

    def name(self):
        print(self.__class__.longname + " " + self.longname)


Zach.longname
