'''from car import Car, Autopark
from rental import Rental, Timetable_booking, Booking, Payments
from people import Staff, Client'''

import sqlite3

conn = sqlite3.connect('car_rental.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS cars(
    carid INT PRIMARY KEY,
    brand TEXT,
    module TEXT,
    transmission TEXT,
    year INT,
    body_type TEXT,
    class_car TEXT,
    category_license TEXT,
    status TEXT,
    cost REAL);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS staffs(
    staffid INT PRIMARY KEY,
    fio TEXT,
    post TEXT,
    phone_number TEXT,
    email TEXT);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS clients(
    clientid INT PRIMARY KEY,
    fio TEXT,
    phone_number TEXT,
    email TEXT,
    drivers_license TEXT);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS autopark(
    carid INT,
    staffid INT,
    date_technical_inspection TEXT,
    mileage REAL,
    status TEXT);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS rental(
    rentalid INT PRIMARY KEY,
    carid INT,
    clientid INT
    start_date TEXT,
    finish_date TEXT,
    cost REAL);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS booking(
    bookingid INT PRIMARY KEY,
    carid INT,
    clientid INT,
    start_date TEXT,
    finish_date TEXT,
    status TEXT
    cost REAL);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS payments(
    paymentsid INT PRIMARY KEY,
    rentalid INT,
    date_payment TEXT,
    summ_payment REAL);
    """)

cursor.execute("""CREATE TABLE IF NOT EXISTS timetable_booking(
    timetableid INT PRIMARY KEY,
    carid INT,
    date_booking TEXT,
    start_time TEXT,
    finish_time TEXT,
    clientid INT);
    """)
conn.commit()

car1 = ('1','BMV','X6','auto',2018,'hatchback','premium','B','Free',3000)
staff1 = ('1', 'Петров И.И.', 'mng', '89324378287','example@primer.ru')
client1 = ('1','Иванов П.П.','+79283218811','choto@bk.com','B')

try:
    cursor.execute('INSERT INTO cars VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);', car1)
    cursor.execute('INSERT INTO staffs VALUES(?, ?, ?, ?, ?);',staff1)
    cursor.execute('INSERT INTO clients VALUES(?, ?, ?, ?, ?);',client1)
    conn.commit()
except sqlite3.IntegrityError:
    ...
