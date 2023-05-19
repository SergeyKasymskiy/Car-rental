from people import Staff


class Car:

    def __init__(self, carid, brand, module, transmission, year, body_type, class_car, category_license, status, cost):
        self.carid = carid
        self.brand = brand
        self.module = module
        self.transmission = transmission
        self.year = year
        self.body_type = body_type
        self.class_car = class_car
        self.category_license = category_license
        self.status = status
        self.cost = cost

    def get_carid(self):
        return self.carid


class Autopark:

    def __init__(self, car, staff, date_technical_inspection, mileage, status):
        self.carid = car.get_carid()
        self.staffid = staff.get_staffid()
        self.date_technical_inspection = date_technical_inspection
        self.mileage = mileage
        self.status = status
