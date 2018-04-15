# 5/28/17
# Main Program ###
# super_heated_water_program "function" 

from Column_Selection_Function import*
from Quality_Interpolate_Function import*




    

#temperature = 423
#pressure = .055

def super_heated_water_program(temperature, pressure):

    if 45.81 <= temperature <= 1300 and .01 <= pressure < .05:

        Pressure_lower = .01
        Pressure_higher = .05
        file = "first.txt"
        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        
        ######################################
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 81.32 <= temperature <= 1300 and .05 <=pressure < .10:

        Pressure_lower = .05
        Pressure_higher = .10
        file = "first.txt"
        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2

        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)
        

    #### First double file reader 
    elif 99.61 <= temperature <= 1300 and .10 <= pressure <.20:

        
        Pressure_lower = .10
        Pressure_higher = .20
        move = 9

        file = "first.txt"
        f = "second.txt"
        
        Temp_lower, Temp_higher, data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL ) 
        print( VL ,SL ,UL ,HL )

     
        
    ################################### END OF FIRST ROW ##########################    
    elif 120.21 <= temperature <= 1300 and .20 <= pressure <.30:

        Pressure_lower = .20
        Pressure_higher = .30
        file = "second.txt"
        

        move= 1
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move , file)
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2

        ######################################
        
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 133.52 <= temperature <= 1300 and .30 <= pressure < .40:

        Pressure_lower = .30
        Pressure_higher = .40
        file = "second.txt"
        
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 143.61 <= temperature <= 1300 and .40 <= pressure <.50:

        Pressure_lower = .40
        Pressure_higher = .50
        file = "second.txt"
        f = "third.txt"
        move = 9
        
        Temp_lower, Temp_higher,data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ################################### END OF SECOND ROW #######################
        
    elif 151.83 <= temperature <= 1300 and .50 <= pressure < .60:

        Pressure_lower = .50
        Pressure_higher = .60
        file = "third.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher  = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 158.83 <= temperature <= 1300 and .60 <= pressure < .80:

        Pressure_lower = .60
        Pressure_higher = .80
        file = "third.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 170.41 <= temperature <= 1300 and .80 <= pressure <1.00:

        Pressure_lower = .80
        Pressure_higher = 1.00
        file = "third.txt"
        
        f = "fourth.txt"
        move = 9
        
        Temp_lower, Temp_higher,data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF THIRD ROW #####################
        
    elif 179.88 <= temperature <= 1300 and 1.00 <= pressure < 1.20:

        Pressure_lower = 1.00
        Pressure_higher = 1.20
        file = "fourth.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher  = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 187.96 <= temperature <= 1300 and 1.20 <= pressure < 1.40:

        Pressure_lower = 1.20
        Pressure_higher = 1.40
        file = "fourth.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 195.04 <= temperature <= 1300 and 1.40 <= pressure <1.60:

        Pressure_lower = 1.40
        Pressure_higher = 1.60
        file = "fourth.txt"
        
        f = "fifth.txt"
        move = 9
        
        Temp_lower, Temp_higher, data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL =  quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF fourth ROW #####################

        


    elif 201.37 <= temperature <= 1300 and 1.60 <= pressure < 1.80:

        Pressure_lower = 1.60
        Pressure_higher = 1.80
        file = "fifth.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 207.11 <= temperature <= 1300 and 1.80 <= pressure < 2.00:

        Pressure_lower = 1.80
        Pressure_higher = 2.00
        file = "fifth.txt"
       

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 212.38 <= temperature <= 1300 and 2.00 <= pressure <2.50:

        Pressure_lower = 2.00
        Pressure_higher = 2.50
        file = "fifth.txt"
      
        f = "sixth.txt"
        move = 9
        
        Temp_lower, Temp_higher, data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF fifth ROW #####################

    elif 223.95 <= temperature <= 1300 and 2.50 <= pressure < 3.00:

        Pressure_lower = 2.50
        Pressure_higher = 3.00
        file = "sixth.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 233.85 <= temperature <= 1300 and 3.00 <= pressure < 3.50:

        Pressure_lower = 3.00
        Pressure_higher = 3.50
        file = "sixth.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 242.56 <= temperature <= 1300 and 3.50 <= pressure <4.00:

        Pressure_lower = 3.50
        Pressure_higher = 4.00
        file = "sixth.txt"
        
        f = "seventh.txt"
        move = 9
        
        Temp_lower, Temp_higher,data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF sixth ROW #####################

    elif 250.35 <= temperature <= 1300 and 4.00 <= pressure < 4.50:

        Pressure_lower = 4.00
        Pressure_higher = 4.50
        file = "seventh.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher  = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 257.44 <= temperature <= 1300 and 4.50 <= pressure < 5.00:

        Pressure_lower = 4.5
        Pressure_higher = 5.00
        file = "seventh.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 263.94 <= temperature <= 1300 and 5.0 <= pressure <6.00:

        Pressure_lower = 5.0
        Pressure_higher = 6.00
        file = "seventh.txt"
        
        f = "eigth.txt"
        move = 9
        
        Temp_lower, Temp_higher,data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF seventh ROW #####################



    elif 275.59 <= temperature <= 1300 and 6.00 <= pressure < 7.0:

        Pressure_lower = 6.00
        Pressure_higher = 7.00
        file = "eigth.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 285.83 <= temperature <= 1300 and 7.0 <= pressure < 8.00:

        Pressure_lower = 7.00
        Pressure_higher = 8.00
        file = "eigth.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)


    elif 295.01 <= temperature <= 1300 and 8.00 <= pressure <9.00:

        Pressure_lower = 8.00
        Pressure_higher = 9.00
        file = "eigth.txt"
        
        f = "ninth.txt"
        move = 9
        
        Temp_lower, Temp_higher, data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF seventh ROW #####################  

    elif 303.35 <= temperature <= 1300 and 9.00 <= pressure < 10.0:

        Pressure_lower = 9.00
        Pressure_higher = 10.00
        file = "ninth.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher  = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 311.00 <= temperature <= 1300 and 10.0 <= pressure < 12.50:

        Pressure_lower = 10.0
        Pressure_higher = 12.50
        file = "ninth.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 327.81 <= temperature <= 1300 and 12.50 <= pressure <15.00:

        Pressure_lower = 12.50
        Pressure_higher = 15.0
        file = "ninth.txt"
        
        f = "tenth.txt"
        move = 9
        
        Temp_lower, Temp_higher,data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF e ROW #####################

    elif 342.16 <= temperature <= 1300 and 15.0 <= pressure < 17.50:

        Pressure_lower = 15.0
        Pressure_higher = 17.50
        file = "tenth.txt"
        
        
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher  = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 354.67 <= temperature <= 1300 and 17.5 <= pressure < 20.0:

        Pressure_lower = 17.5
        Pressure_higher = 20.0
        file = "tenth.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 365.7 <= temperature <= 1300 and 20.00 <= pressure <25.00:

        Pressure_lower = 20.00
        Pressure_higher = 25.00
        file = "tenth.txt"
        
        f = "eleven.txt"
        move = 9
        
        Temp_lower, Temp_higher, data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF  ROW #####################

    elif 375 <= temperature <= 1300 and 25.0 <= pressure < 30.0:

        Pressure_lower = 25.0
        Pressure_higher = 30.50
        file = "eleven.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher  = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 375 <= temperature <= 1300 and 30.0 <= pressure < 35.0:

        Pressure_lower = 30.0
        Pressure_higher = 35.00
        file = "eleven.txt"
        

        move= 5
        data_list1, data_list2,Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 375 <= temperature <= 1300 and 35.0 <= pressure <40.00:

        Pressure_lower = 35.0
        Pressure_higher = 40.00
        file = "eleven.txt"
        
        f = "twelfth.txt"
        move = 9
        
        Temp_lower, Temp_higher, data_list1, data_list2, data_list1_two , data_list2_two = column_selection_for_two(temperature,move, file , f)
        
        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        vH , uH , hH , sH = data_list1_two
        vL , uL , hL , sL = data_list2_two 
        
        VL , SL , UL , HL = quality_interpolate(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL, sH, sL )
        print( VL ,SL ,UL ,HL )
    ######################## END OF seventh ROW #####################

    elif 375 <= temperature <= 1300 and 40.0 <= pressure < 50.0:

        Pressure_lower = 40.0
        Pressure_higher = 50.0
        file = "twelfth.txt"
        

        move= 1
        data_list1, data_list2, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =5 
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)

    elif 375 <= temperature <= 1300 and 50.0 <= pressure < 60.0:

        Pressure_lower = 50.0
        Pressure_higher = 60.00
        file = "twelfth.txt"
        

        move= 5
        data_list1, data_list2, Temp_lower , Temp_higher  = column_selection(temperature , move, file)
        

        vh , uh , hh , sh = data_list1
        vl , ul , hl , sl = data_list2
        move =9
        data_list12, data_list22, Temp_lower , Temp_higher = column_selection(temperature , move , file)
        
        vh2 , uh2 , hh2 , sh2 = data_list12
        vl2 , ul2 , hl2 , sl2 = data_list22
        
        
        finalV , finalE , finalU , finalH = quality_interpolate_pressure(Pressure_higher, Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl, vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2) 
        print( finalV , finalE , finalU , finalH)
    else:
        print("Out of range")  
#super_heated_water_program(temperature, pressure)
