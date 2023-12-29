class CAR:
    def __init__(self, colour:str, max_spd:int, acceleration:float, tyre_frec:int, is_eng_started:bool):
        self.colour = colour
        self.max_spd = max_spd
        self.acceleration = acceleration
        self.tyre_frec = tyre_frec
        self.is_eng_started = is_eng_started
        self.current_speed = 0

    def car_start(self):
        
        if(self.is_eng_started):
            print("car is already in start mode")
        else:
            self.is_eng_started = True

    def car_stop(self):
        if(self.is_eng_started):
            self.is_eng_started=False
        else:
            print("car is already stop mode")
    
    def car_break(self):
        
        if car.is_eng_started:
            car_decr = self.current_speed - self.tyre_frec
            if  car_decr >= 0:
                self.current_speed=car_decr
                print(f"The car decreased the speed to {self.current_speed} kmph")
            else:
                self.current_speed=0
                print("The car has stopped")
        else:
            print("The car is not started")

    def car_acceletarion(self): 
        if self.is_eng_started:
            carincr= self.current_speed+self.acceleration
            if  carincr > self.max_spd:
                self.current_speed==self.max_spd
                print(f"The car reached maximum speed{self.max_spd}  kmph")
            else:
                self.current_speed=carincr
                print(f"The car speed is increased to {self.current_speed} kmph")
        else:
            print("car is not started")

    def car_horn(self):
        if self.is_eng_started:
           print("car horn is blow")
        else:
            print("car is not started")
    
class Truck(CAR):
    def __init__(self, colour, max_spd, acceleration, tyre_frec, is_eng_started, max_cargo):
        super().__init__(colour, max_spd, acceleration, tyre_frec, is_eng_started)
        self.max_cargo = max_cargo
        self.cargo_weight=100
        self.cargo = 0
        self.car_go=100

    def Truck_load(self,load):
        if not car.is_eng_started:
            if self.car_go>= load:
                self.cargo =self.cargo + load
                if self.cargo>=self.cargo_weight:
                    self.cargo=self.cargo_weight
                    print(f"The truck reached maximum weight {self.cargo_weight} kgs") 
                else:
                    self.car_go=self.car_go-load
                    print(f"After Load The truck contain {self.cargo} kgs")
            else:
                print(f"The capacity of the load is {self.car_go} kgs only")
        else:
            print("we can't load bcz the truck in motion")

    def Truck_unload(self,unload):
        if not car.is_eng_started:
            if self.cargo >= unload:
                self.cargo =self.cargo-unload
                if self.cargo_weight >= self.cargo:
                    print(f"After unload the truck contain {self.cargo}kgs")
                # else:
                #     print(f"The truck contain only car weight")
            else:
                print(f"the truck contain {self.cargo} kgs only" )
        else:
            print("we can't unload bcz the truck in motion")          
# Instantiate the object before calling the method
            

car = Truck("Blue",160,10,5,True,500)
car.car_start()
car.car_acceletarion()
car.car_break()
car.car_horn()
car.car_stop()
car.Truck_load(1)
car.Truck_load(91)
car.Truck_load(19)
car.Truck_unload(52)
car.Truck_unload(20)
car.Truck_unload(20)