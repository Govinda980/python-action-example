class Birds:

    def intro(self):
        print("ASK ME ANYTHING....")

    def fly(self):
        print("Depends on birds")


class Crow(Birds):
    def fly(self):
        print("Yes fly....")


ob1 = Crow()

ob1.intro()
ob1.fly()

