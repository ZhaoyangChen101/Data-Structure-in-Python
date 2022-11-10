# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
#​‌​​​​​‌‌‌​‌​​​ Class to describe a car object
#​‌​​​​​‌‌‌​‌​​​ A car has the following attributes: max_tank, tank, consumption, mileage and id

class Car:

    def __init__(self, consumption, name = "unregistered vehicle"):
        self.max_tank = 40
        self.tank = self.max_tank # tank is full when delivered from factory
        self.consumption = consumption
        self.mileage = 0.0
        self.id = name

    #​‌​​​​​‌‌‌​‌​​​ Return mileage
    def get_mileage(self):
        return self.mileage

    #​‌​​​​​‌‌‌​‌​​​ Return tank
    def get_tank_level(self):
        return self.tank

    #​‌​​​​​‌‌‌​‌​​​ Drive the wanted distance
    def drive(self, distance):
        max_distance = self.tank / self.consumption * 100
        if max_distance < distance:
            self.mileage += max_distance
            self.tank = 0
            return max_distance
        else:
            self.mileage += distance
            self.tank -= distance * self.consumption / 100
            return distance

    #​‌​​​​​‌‌‌​‌​​​ Refuels the car
    def refuel(self, amount):
        self.tank += min(amount, self.max_tank - self.tank)
        return self.tank


#​‌​​​​​‌‌‌​‌​​​ Class to describe a car track
#​‌​​​​​‌‌‌​‌​​​ A car track has the following attributes: name, distance, cars and nof_cars
#​‌​​​​​‌‌‌​‌​​​ Fill in the missing methods

class CarTrack:

    def __init__(self, name, distance):
        self.name = name
        self.distance = distance    # distance of the car track
        self.cars = []              # cars driving on the track (Car-objects)
        self.nof_cars = 0

    #​‌​​​​​‌‌‌​‌​​​ Returns the distance of the car track
    def get_distance(self):
        return self.distance

    #​‌​​​​​‌‌‌​‌​​​ Returns the list containing the cars in the car track
    def get_cars(self):
        return self.cars

    #​‌​​​​​‌‌‌​‌​​​ Returns the number of cars in the car track
    def get_nof_cars(self):
        return self.nof_cars


    def add_car(self, car):
        """ Add a car to the car track and return the number of cars in the track """
        #raise NotImplementedError("Fix me!") #Remove this line
        self.cars.append(car)
        self.nof_cars += 1
        return self.nof_cars


    def count_avg_consumption(self):
        """ Count and return the average consumption of the race cars """
        #raise NotImplementedError("Fix me!") #Remove this line
        totalConsumption = 0.0
        if self.nof_cars == 0:
            return 0.0
        else:
            for singleCar in self.cars:
                totalConsumption += singleCar.consumption
            return totalConsumption/self.nof_cars

    def get_winner(self):
        """ Return the car with the biggest mileage """
        """ Use of built-in functions such as max() is prohibited """
        #raise NotImplementedError("Fix me!") #Remove this line
        if self.nof_cars == 0:
            return None
        else:
            winner = self.cars[0]
            for singleCar in self.cars:
                if singleCar.mileage <= winner.mileage:
                    continue
                else:
                    winner = singleCar
            return winner


    def count_rounds(self, car):
        """ Count how many rounds a car drove, round down to the nearest integer """
        #raise NotImplementedError("Fix me!") #Remove this line
        driveDistance = car.mileage
        rounds = driveDistance * 1.0 / self.distance
        return int(rounds)



def main():
    '''my_fiat = Car(5.0, "ZZZ-123")
    neighbours_ferrari = Car(12.5, "ITA-1")

    print(my_fiat.drive(20))
    print(my_fiat.refuel(10))

    print(neighbours_ferrari.drive(450))
    '''
    track = CarTrack("Sunrise", 30)
    car1 = Car(10.6, "ZZZ-123")
    car2 = Car(8.1, "ABC-245")
    car3 = Car(13.8, "FOO-634")
    car4 = Car(14.2, "JKL-375")
    track.add_car(car1)
    track.add_car(car2)
    track.add_car(car3)
    track.add_car(car4)
    car1.drive(479)
    car2.drive(472)
    car3.drive(531)
    car4.drive(317)
    print("Which car drove the longest distance (mileage)\n", track.get_winner().id)
    print("What was the mileage of the winner?\n", track.get_winner().mileage)
    print("How many whole laps the winner drove?\n", track.count_rounds(track.get_winner()))
    print("What was the mean consumption of the cars?\n", track.count_avg_consumption())
if __name__ == "__main__":
    main()