class Vehicle:
    def __init__(self, seat_capacity):
        self.seat_capacity = seat_capacity

    def fare(self):
        return self.seat_capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance_charge = total_fare * 10 / 100
        final_amount = total_fare + maintenance_charge
        return final_amount


bus = Bus(50)

print("Bus seat capacity:", bus.seat_capacity)
print("Total fare:", bus.fare())