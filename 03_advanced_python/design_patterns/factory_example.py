from enum import Enum


class DeliveryType(Enum):
    TRUCK = "truck"
    SHIP = "ship"


class Truck:
    def __str__(self) -> str:
        return "Deliver With Truck"

class Ship:
    def __str__(self) -> str:
        return "Deliver With Ship"

class Logistics:
    def create_transport(self, transport_type: DeliveryType):
        if transport_type == DeliveryType.TRUCK:
            return Truck()
        elif transport_type == DeliveryType.SHIP:
            return Ship()
        else:
            raise ValueError("Unknown transport type")


fst_transport = Logistics().create_transport(DeliveryType.TRUCK)
print(fst_transport)

snd_transport = Logistics().create_transport(DeliveryType.SHIP)
print(snd_transport)