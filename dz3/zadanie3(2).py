import datetime


class AirPlane:
    __destination = ''
    __flightNumber = ''
    __planeNumber = ''
    __depart_time = ''
    __date = ''

    def __init__(self, destination, flight_number, plane_number, depart_time, day):
        self.__destination = destination
        self.__flightNumber = flight_number
        self.__planeNumber = plane_number
        self.__depart_time = depart_time
        self.__date = day
        print('New object created!')

    def get_destination(self):
        return self.__destination

    def get_flight_number(self):
        return self.__flightNumber

    def get_plane_number(self):
        return self.__planeNumber

    def get_depart_time(self):
        return self.__depart_time

    def get_day(self):
        return self.__date


def flight_info(i):
    print('Destination: ' + str(air_flight[i].get_flight_number()))
    print('Depart time: ' + str(air_flight[i].get_depart_time()))
    print('Plane number: ' + str(air_flight[i].get_plane_number()))
    print('Date: ' + str(air_flight[i].get_day()))
    print('---------------')


i = 0

air_flight = [AirPlane('Antalya', 'B2 8105', 'Boeing 737-800', '07:25', 'Monday'),
            AirPlane('Istanbul', 'Boeing 737-800', 'Boeing 737-800', '10:46', 'Friday'),
            AirPlane('Batumi', 'B2 731', 'Embraer 195-E2', '12:50', 'Saturday '),
            AirPlane('Moscow', 'B2 735', 'Boeing 737-800', '06:25', 'Sunday '),
            AirPlane('Sharm El Sheikh', 'B2 9303  ', 'Boeing 737-800', '20:05', 'Wednesday '),
            AirPlane('Antalya', 'B2 951', 'Boeing 737-800', '03:12', 'Thursday '),
            AirPlane('Batumi', 'B2 737', 'Boeing 737-300', '16:15', 'Friday'),
            AirPlane('Moscow', 'B2 977', 'Boeing 737-500', '01:23', 'Saturday '),
            AirPlane('Tbilisi', 'B2 8105', 'Embraer 195', '23:31', 'Monday')]


flight_num = str(input('Input destination:\n'))


while i < len(air_flight):
    if air_flight[i].get_destination() == flight_num:
        flight_info(i)
    i += 1
i = 0

day_of_week = str(input('Input date:\n'))
while i < len(air_flight):
    if air_flight[i].get_day() == day_of_week:
        flight_info(i)
    i += 1