from car import Car, Autopark
from people import Staff, Client


class Rental:

    def __init__(self, rentalid, car, client, start_date, finish_date, cost):
        """Конструктор

        Args:
            rentalid (int): id проката
            car (class): автомобиль
            client (class): клиент
            start_date (str): дата начала проката
            finish_date (str): дата окончания проката
            cost (float): стоимость проката
        """
        self.rentalid = rentalid
        self.carid = car.get_carid()  # Передаём id автомобиля
        self.clientid = client.get_cleintid()  # Передаём id клиента
        self.start_date = start_date
        self.finish_date = finish_date
        self.cost = cost

    def get_rentalid(self):
        return self.rentalid


class Booking:

    def __init__(self, bookingid, car, client, start_date, finish_date, status, cost):
        """Конструктор

        Args:
            bookingid (int): Бронь
            car (class): автомобиль
            client (class): клиент
            start_date (str): дата начала брони
            finish_date (str): дата окончания брони
            status (str): статус (подтверждено или на рассмотрении)
            cost (float): стоимость брони
        """
        self.bookingid = bookingid
        self.carid = car.get_carid()  # Передаём id автомобиля
        self.clientid = client.get_cleintid()  # Передаём id клиента
        self.start_date = start_date
        self.finish_date = finish_date
        self.status = status
        self.cost = cost


class Payments:

    def __init__(self, paymentsid, rental, date_payment, summ_payment):
        """Конструктор

        Args:
            paymentsid (int): id платежа
            rental (class): прокат
            date_payment (str): дата платежа
            summ_payment (float): суммо платежа
        """
        self.paymentsid = paymentsid
        self.rentalid = rental.get_rentalid()  # Передаём id проката
        self.date_payment = date_payment
        self.summ_payment = summ_payment


class Timetable_booking:

    def __init__(self, timetableid, car, date_booking, start_time, finish_time, client):
        """Конструктор

        Args:
            timetableid (int): id рассписания брони
            car (class): автомобиль
            date_booking (str): дата брони
            start_time (str): начало брони
            finish_time (str): окончание брони
            client (class): клиент
        """
        self.timetableid = timetableid
        self.carid = car.get_carid()  # Передаём id автомобиля
        self.date_booking = date_booking
        self.start_time = start_time
        self.finish_time = finish_time
        self.clientid = client.get_clientid()  # Передаём id клиента
