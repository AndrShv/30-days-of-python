from models import GreenHouse

greenHouse_db: list[GreenHouse] = []


def add_green_house(greenHouse):
    print("Saving new GreenHouse with", greenHouse.sensor_id)
    greenHouse_db.append(greenHouse)


def get_all_green_houses():
    print("Getting all GreenHouses")
    return greenHouse_db


def get_dry_zones() -> list[GreenHouse]:
    dry_zones = []
    for greenHouse in greenHouse_db:
        if greenHouse.needs_water():
           dry_zones.append(greenHouse)
    return dry_zones

def get_fix_zones()-> list[GreenHouse]:
    fix_zones = []
    for greenHouse in greenHouse_db:
        if greenHouse.need_to_fix():
            fix_zones.append(greenHouse)
    return fix_zones


def fix_green_house(sensor_id):
    for greenHouse in greenHouse_db:
        if greenHouse.sensor_id == sensor_id:
           greenHouse.status = "inactive"
        else:
            print("GreenHouse not found")