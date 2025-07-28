from abc import ABC, abstractmethod


class Vericles:
    def __init__(self, vehicle_type, model, rate_per_day):
        self.vehicle_type = vehicle_type
        self.model = model
        self.rate_per_day = rate_per_day

    @abstractmethod
    def total_rent(self):
        pass


class Car(Vericles):
    def __init__(self, vehicle_type, model, rate_per_day, isac, day):
        Vericles.__init__(self, vehicle_type, model, rate_per_day)
        self.isac = isac
        self.day = day

    def total_rent(self):
        if self.isac:
            total_rent = (self.rate_per_day * self.day) + 5
        else:
            total_rent = self.rate_per_day * self.day

        print("total rent is ", total_rent)


ob = Car('Maruti','s1 pro',10, False,3)
ob.total_rent()