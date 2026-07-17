from models import GreenHouse

greenHouse_db = list[GreenHouse] = []


def add_green_house(greenHouse):
    print("Saving new GreenHouse with", greenHouse.sensor_id)
    greenHouse_db.append(greenHouse)


def get_all_green_houses():
    print("Getting all GreenHouses")
    return greenHouse_db


def get_dry_zones() -> list[GreenHouse]:
    dry_zones = []
    if GreenHouse.needs_water(greenHouse_db) == True:
        dry_zones.append(greenHouse_db)
    return dry_zones
