from enum import Enum as PythonEnum

class IncidentCategory(PythonEnum):
    FIRE = "fire"
    ACCIDENT = "accident"
    EMERGENCY = "emergency"
    HAZARDOUS_MATTER = "hazardous_matter"

class LawBreakingCategory(PythonEnum):
    SPEED_VIOLATION = "speed_violation"
    WANTED_VEHICLE = "wanted_vehicle"
    STOLEN_PLATE = "stolen_plate"
    STH_ELSE = "sth_else"


class UserRole(PythonEnum):
    USER = "user",
    OFFICER = "officer"