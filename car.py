from datetime import date
class car:
    def __init__(self,weight,maxspeed,no_of_wheels,service_dates):
        self.weight=weight
        self.maxspeed=maxspeed
        self.no_of_wheels=no_of_wheels
        self.service_dates=service_dates

    def get_max_speed(self):
        print("maxspeed:{}km/hr".format(self.maxspeed))
    def get_service_dates(self):
        print("service_dates:",self.service_dates)
    def add_service_dates(self,service_dates1):
        self.service_dates1=service_dates1
        print("add service_date:",self.service_dates1)
    def update_maxspeed(self,maxspeed):
        self.maxspeed=maxspeed
        print("max_speed after updation:{} km/hr".format(self.maxspeed))
dt=date(2022,2,4)
c=car(1500,50,4,dt)
dot=date(2022,3,5)
c.get_max_speed()
c.get_service_dates()
c.add_service_dates(dot)
c.update_maxspeed(80)
