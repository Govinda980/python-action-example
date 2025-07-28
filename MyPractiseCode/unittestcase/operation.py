class opera:
    c = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def call_div_num(self):
        return self.div_num(self.a, self.b)

    def div_num(self, a, b):
        self.c = a / b  # Use a and b directly, not self.a or self.b
        return self.c


ob = opera(4, 2)
print(ob.call_div_num())
