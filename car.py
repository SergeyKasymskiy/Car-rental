from people import Staff


class Car:

    def __init__(self, carid, brand, module, transmission, year, body_type, class_car, category_license, status, cost):
        """Конструктор

        Args:
            carid (int): id автомобиля
            brand (str): марка автомобиля
            module (str): модель автомобиля
            transmission (str): коробка передач (механика, автомат)
            year (int): год выпуска
            body_type (str): тип кузова (сидан, универсал, внедорожник и т.д.)
            class_car (str): класс автомобиля (эконом, стандарт, премиум и т.д.)
            category_license (str): категория автомобиля (B, C, D, и т.д.)
            status (str): статус (свободна, занята)
            cost (float): _стоимость за сутки
        """
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
        """Конструктор

        Args:
            car (class): автомобиль
            staff (class): персонал
            date_technical_inspection (str): дата последнего техосмотра
            mileage (float): пробег
            status (str): статус (свободна, занята)
        """
        self.carid = car.get_carid()  # Передаём id автомобиля
        self.staffid = staff.get_staffid()  # Передаём id персонала
        self.date_technical_inspection = date_technical_inspection
        self.mileage = mileage
        self.status = status
