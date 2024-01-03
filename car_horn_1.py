class CAR:
    def __init__(self, colour, max_spd, acceleration, tyre_frec, is_eng_started):
        self.colour = colour
        self.max_spd = max_spd
        self.acceleration = acceleration
        self.tyre_frec = tyre_frec
        self.is_eng_started = is_eng_started
        self.current_speed = 0

    def car_start(self):
        self.is_eng_started = True
        print(f"Hello user, your {self.colour} car is started")

    def car_stop(self):
        self.is_eng_started = False
        print("The car is stopped")

    def car_break(self):
        self.current_speed = self.current_speed - self.tyre_frec
        if self.current_speed > 0 :
            print(f"The car decreased the speed to {self.current_speed} kmph")
        else:
            self.current_speed < 0
            self.current_speed = 0
            print("The car has reach 0 kmph or car is stopped")
        
    def car_acceletarion(self): 
        self.current_speed= self.current_speed+self.acceleration
        if self.current_speed > self.max_spd:
             self.current_speed = self.max_spd
             print(f"The car reached maximum speed{self.max_spd}  kmph")
        else:
            print(f"The car speed is increased to {self.current_speed} kmph")

    def car_horn(self):
        if self.car_start():
           print("car horn is activeted")
        else:
            print("car is not started ")
# Instantiate the object before calling the method
car = CAR("Red", 160, 10, 5, "Started")

car.car_start()
car.car_stop()
car.car_acceletarion()
car.car_acceletarion()
car.car_break()
car.car_horn()