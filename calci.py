#This file contains code for the conversion caluculator


class time:
    items = {1:"Hours", 2:"Minutes", 3:"Seconds"}
    def main_time(self):
        items = {1:"hr", 2:"min", 3:"sec"}
        from_time_list = time.ask_from(self)
        from_time = from_time_list[1]
        from_value = from_time_list[2]
        to_time = time.ask_to(self)
        to_time = to_time[1]
        str_temp = str(from_time) + str(to_time)
        dictionary_of_units = {"12":time.hr_to_min(time, from_value), "13":time.hr_to_sec(time, from_value), "21":time.min_to_hr(time, from_value), "23":time.min_to_sec(time, from_value), "31":time.sec_to_hr(time, from_value), "32":time.sec_to_min(time, from_value)}
        print(dictionary_of_units[str_temp], items[to_time])

        
    
    def ask_from(self):
        while True:
            try:
                from_input = int(input(("Do you want to change the time from?\n1. Hours\n2. Minutes\n3. Seconds\n"))) 
            except ValueError:
                print("That is not a number")
            else:
                if from_input in [1,2,3]:
                    from_value = int(input("Enter the value in {}".format(time.items[from_input])))
                    return [True, from_input, from_value]
                else:
                    print("You have to select only from range of 1 to 3")
    

    def ask_to(self):
        while True:
            try:
                to_input = int(input(("Do you want to change the time to?\n1. Hours\n2. Minutes\n3. Seconds\n")))
            except ValueError:
                print("That is not a number")
            else:
                if to_input in [1,2,3]:
                    return [True, to_input]
                else:
                    print("You have to select only from range of 1 to 3")
    

        
    def hr_to_min(self, hr):
        return hr*60

    def hr_to_sec(self, hr):
        return hr*60*60
    
    def min_to_hr(self, hr):
        return hr/60

    def min_to_sec(self, min):
        return min*60

    def sec_to_min(self, sec):
        return sec/60

    def sec_to_hr(self, sec):
        return sec/3600

#decimeter, light year, millimeter, km, cm, m
class length:
    items = { 1:"Kilometer", 2:"Centimeter", 3:"Meter"}
    def main_length(self):
        
        items = {1:"km", 2:"cm", 3:"mt"}
        from_length_list = length.ask_from(self)
        from_length = from_length_list[1]
        from_value = from_length_list[2]
        to_length = length.ask_to(self)
        to_length = to_length[1]
        str_temp = str(from_length) + str(to_length)
        dictionary_of_units = {"12":length.km_to_cm(length, from_value), "13":length.km_to_mt(length, from_value), "21":length.cm_to_km(length, from_value), "23":length.cm_to_mt(length, from_value), "31":length.mt_to_km(length, from_value), "32":length.mt_to_cm(length, from_value)}
        print(dictionary_of_units[str_temp],items[to_length])
        
        

        
    
    def ask_from(self):
        while True:
            try:
                from_input = int(input(("Do you want to change the length from?\n1. Kilometer\n2. Centimeter\n3. Meter\n")))
            except ValueError:
                print("That is not a number")
            else:
                if from_input in [1,2,3]:
                    from_value = int(input("Enter the value in {}".format(length.items[from_input])))

                    return [True, from_input, from_value]
                else:
                    print("You have to select only from range of 1 to 3")
    

    def ask_to(self):
        while True:
            try:
                to_input = int(input(("Do you want to change the length to?\n1. Kilometer\n2. Centimeter\n3. Meter\n")))
            except ValueError:
                print("That is not a number")
            else:
                if to_input in [1,2,3]:
                    return [True, to_input]
                else:
                    print("You have to select only from range of 1 to 3")

    
    

    def km_to_cm(self, km):
        return km*100000

    def km_to_mt(self, km):
        return km*1000

    def cm_to_km(self, cm):
        return cm/100000
    
    def cm_to_mt(self, cm):
        return cm/100

    def mt_to_km(self, mt):
        return mt/1000
    
    def mt_to_cm(self, mt):
        return mt*100

    


#g, mg, kg
class weight:
    items = {1:"Grams", 2:"Milligrams", 3:"Kilograms"}
    def main_weight(self):
        items = {1:"g", 2:"mg", 3:"kg"}
        from_weight_list = weight.ask_from(self)
        from_weight = from_weight_list[1]
        from_value = from_weight_list[2]
        to_weight = weight.ask_to(self)
        to_weight = to_weight[1]
        str_temp = str(from_weight) + str(to_weight)
        dictionary_of_units = {"12":weight.g_to_mg(weight, from_value), "13":weight.g_to_kg(weight, from_value), "21":weight.mg_to_g(weight, from_value), "23":weight.mg_to_kg(weight, from_value), "31":weight.kg_to_g(weight, from_value), "32":weight.kg_to_mg(weight, from_value)}
        print(dictionary_of_units[str_temp],items[to_weight])
        




    def ask_from(self):
        while True:
            try:
                from_input = int(input(("Do you want to change the weight from?\n1. Grams\n2. Milligrams\n3. Kilograms\n")))

            except ValueError:
                print("That is not a number")
            else:

                if from_input in [1,2,3]:
                    from_value = int(input("Enter the value in {}".format(weight.items[from_input])))
                    return [True, from_input, from_value]
                else:
                    print("You have to select only from range of 1 to 3")
    

    def ask_to(self):
        while True:
            try:
                to_input = int(input(("Do you want to change the weight to?\n1. Grams\n2. Milligrams\n3. Kilograms\n")))
            except ValueError:
                print("That is not a number")
            else:
                if to_input in [1,2,3]:
                    return [True, to_input]
                else:
                    print("You have to select only from range of 1 to 3")



    def g_to_mg(self, g):
        return  g*1000
    
    def g_to_kg(self, g):
        return g/1000

    def mg_to_g(self, mg):
        return mg/1000

    def mg_to_kg(self, mg):
        return mg/1000000

    def kg_to_g(self, kg):
        return kg*1000

    def kg_to_mg(self, kg):
        return kg*1000000

#F, C
class temparature:
    items = {1:"Celcius", 2:"Farenhit"}
    def main_temparature(self):
        items = {1:"C", 2:"F",}
        from_temparature_list = temparature.ask_from(self)
        from_temparature = from_temparature_list[1]
        from_value = from_temparature_list[2]
        to_temparature = temparature.ask_to(self)
        to_temparature = to_temparature[1]
        str_temp = str(from_temparature) + str(to_temparature)
        dictionary_of_units = {"12":temparature.c_to_f(temparature, from_value), "21":temparature.f_to_c(temparature, from_value)}
        print(dictionary_of_units[str_temp],items[to_temparature])

    

    def c_to_f(self, c):
        return (c*180/100)+32

    def f_to_c(self, f):
        return (f-32)*100/180
    

        




    def ask_from(self):
        while True:
            try:
                from_input = int(input(("Do you want to change the te,parature from?\n1. Celcius\n2. Farenhit\n")))
                from_value = int(input("Enter the value in {}".format(temparature.items[from_input])))
            except ValueError:
                print("That is not a number")
            else:
                if from_input in [1,2]:
                    return [True, from_input, from_value]
                else:
                    print("You have to select only from range of 1 to 2")
    

    def ask_to(self):
        while True:
            try:
                to_input = int(input(("Do you want to change the weight to?\n1. Celcius\n2. Farenhit\n")))
            except ValueError:
                print("That is not a number")
            else:
                if to_input in [1,2]:
                    return [True, to_input]
                else:
                    print("You have to select only from range of 1 to 2")



class speed:

    items = {1:"Kmph", 2:"Mph"}
    def main_speed(self):
        items = {1:"Kmph", 2:"mph"}
        from_speed_list = speed.ask_from(self)
        from_speed = from_speed_list[1]
        from_value = from_speed_list[2]
        to_speed = speed.ask_to(self)
        to_speed = to_speed[1]
        str_temp = str(from_speed) + str(to_speed)
        dictionary_of_units = {"12":speed.kmph_to_mph(speed, from_value), "21":speed.mph_to_kmph(speed, from_value)}
        print(dictionary_of_units[str_temp],items[to_speed])
        




    def ask_from(self):
        while True:
            try:
                from_input = int(input(("Do you want to change the speed  from?\n1. Km/h\n2. M/h\n")))

            except ValueError:
                print("That is not a number")
            else:
                if from_input in [1,2]:
                    from_value = int(input("Enter the value in {}".format(speed.items[from_input])))
                    return [True, from_input, from_value]
                else:
                    print("You have to select only from range of 1 to 2")
    

    def ask_to(self):
        while True:
            try:
                to_input = int(input(("Do you want to change the weight to?\n1. Km/h\n2. M/h\n")))
            except ValueError:
                print("That is not a number")
            else:
                if to_input in [1,2]:
                    
                    return [True, to_input]
                else:
                    print("You have to select only from range of 1 to 2")


    def kmph_to_mph(self, kmph):
        return kmph*0.621371
    
    def mph_to_kmph(self, mph):
        return mph*1.60934

#time, length, weight, temparatue, speed

class main:

    def main_check(self, inp):
        if inp == 1:
            time.main_time(time)
        elif inp == 2:
            length.main_length(length)
        elif inp == 3:
            weight.main_weight(weight)
        elif inp == 4:
            temparature.main_temparature(temparature)
        else:
            speed.main_speed(speed)
        return 

    def main(self):
        print("Hi there! I'm VICTOR. I can help you converting units from one to another. :)")
        print("I can do the followning conversions for you. Choose the right one from the following:")
        while True:
            try:
                inp = int(input("1. Time\n2. Length\n3. Weight\n4. Temparature\n5. Speed"))
            except ValueError:
                print("Must be a number")
            
            else:
                if inp in [1, 2, 3, 4, 5]:
                    main.main_check(main, inp)
                    return True
                else:
                    print("Must be in range 1 - 5")


