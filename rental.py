from car import Car, Autopark
from people import Staff, Client


class Rental:

    def __init__(self, rentalid, car, client, start_date, finish_date, cost):
        self.rentalid = rentalid
        self.carid = car.get_carid()
        self.clientid = client.get_cleintid()
        self.start_date = start_date
        self.finish_date = finish_date
        self.cost = cost

    def get_rentalid(self):
        return self.rentalid


class Booking:

    def __init__(self, bookingid, car, client, start_date, finish_date, status, cost):
        self.bookingid = bookingid
        self.carid = car.get_carid()
        self.clientid = client.get_cleintid()
        self.start_date = start_date
        self.finish_date = finish_date
        self.status = status
        self.cost = cost


class Payments:

    def __init__(self, paymentsid, rental, date_payment, summ_payment):
        self.paymentsid = paymentsid
        self.rentalid = rental.get_rentalid()
        self.date_payment = date_payment
        self.summ_payment = summ_payment


class Timetable_booking:

    def __init__(self, timetableid, car, date_booking, start_time, finish_time, client):
        self.timetableid = timetableid
        self.carid = car.get_carid()
        self.date_booking = date_booking
        self.start_time = start_time
        self.finish_time = finish_time
        self.clientid = client.get_clientid()
