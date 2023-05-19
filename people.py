class Staff:

    def __init__(self, staffid, fio, post, phone_number, email):
        """Конструктор

        Args:
            staffid (int): id персонала
            fio (str): ФИО
            post (str): должность
            phone_number (str): номер телефона
            email (str): почта
        """
        self.staffid = staffid
        self.fio = fio
        self.post = post
        self.phone_number = phone_number
        self.email = email

    def get_staffid(self):
        return self.staffid


class Client:

    def __init__(self, clientid, fio, phone_number, email, drivers_license):
        """Конструктор

        Args:
            clientid (int):id клиента
            fio (str): ФИО
            phone_number (str): номер телефоно
            email (str): почта
            drivers_license (str): категория водительского удостоверения
        """
        self.clientid = clientid
        self.fio = fio
        self.phone_number = phone_number
        self.email = email
        self.drivers_license = drivers_license

    def get_clientid(self):
        return self.clientid
