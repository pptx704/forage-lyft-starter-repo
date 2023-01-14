from battery import NubbinBattery, SpindlerBattery
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from tire import CarriganTire, OctoprimeTire
from car import Car

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage), 
            SpindlerBattery(last_service_date, current_date),
            CarriganTire(tires)
        )

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            SpindlerBattery(last_service_date, current_date),
            OctoprimeTire(tires)
        )

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        return Car(
            SternmanEngine(warning_light_is_on),
            SpindlerBattery(last_service_date, current_date),
            CarriganTire(tires)
        )

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            WilloughbyEngine(current_mileage, last_service_mileage),
            NubbinBattery(last_service_date, current_date),
            OctoprimeTire(tires)
        )

    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        return Car(
            CapuletEngine(current_mileage, last_service_mileage), 
            NubbinBattery(last_service_date, current_date),
            CarriganTire(tires)
        )