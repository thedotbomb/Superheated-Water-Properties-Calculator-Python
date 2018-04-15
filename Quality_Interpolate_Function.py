# 5/30/2017
# quality interpolate function


def quality_interpolate (Pressure_higher,Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vH, vL, uH , uL ,hH, hL , sH, sL):

  # This function is if pressure needs to be read from two different file
    # At lower pressure finds x and Vlow
    
    xlow =  (vl - vh) /( Temp_higher - Temp_lower)
    VL = vh + xlow*(temperature - Temp_lower)

    # AT higher pressure finds x and Vhigh

    xhigh =  (vL - vH) /( Temp_higher - Temp_lower)
    VH = vH+ xhigh*(temperature - Temp_lower)

    # final  volume interpolation
    xfinal =  (VH - VL) /( Pressure_higher - Pressure_lower)
    finalV = VL + xfinal*(pressure - Pressure_lower)
   


#######################################################################
    # At lower pressure finds x and Ulow

    xlow =  (ul- uh) /( Temp_higher - Temp_lower)
    UL = uh + xlow*(temperature - Temp_lower)

    # AT higher pressure finds x and Uhigh

    xhigh =  (uL - uH) /( Temp_higher - Temp_lower)
    UH = uH + xhigh*(temperature - Temp_lower)


    # final internal energy interpolation

    xfinal =  (UH - UL) /( Pressure_higher - Pressure_lower)
    finalU = UL + xfinal*(pressure - Pressure_lower)

    
##########################################################################
    # At lower pressure finds x and Elow

    xlow =  (hl-hh) /( Temp_higher - Temp_lower)
    HL = hh + xlow*(temperature - Temp_lower)

    # AT higher pressure finds x and Ehigh

    xhigh =  (hL-hH) /( Temp_higher - Temp_lower)
    HH = hH + xhigh*(temperature - Temp_lower)


    # final entropy interpolation

    xfinal =  (HH - HL) /( Pressure_higher - Pressure_lower)
    finalH = HL + xfinal*(pressure - Pressure_lower)
    
######################################################################
    # At lower pressure finds x and Elow

    xlow =  (sl - sh) /( Temp_higher - Temp_lower)
    SL = sh + xlow*(temperature - Temp_lower)

    # AT higher pressure finds x and Ehigh

    xhigh =  (sL - sH) /( Temp_higher - Temp_lower)
    SH = sH + xhigh*(temperature - Temp_lower)


    # final entropy interpolation

    xfinal =  (SH - SL) /( Pressure_higher - Pressure_lower)
    finalE = SL + xfinal*(pressure - Pressure_lower)
    
    #print(finalV , finalE , finalU , finalH)
   
    return finalV , finalE , finalU , finalH
 
def quality_interpolate_pressure(Pressure_higher,Pressure_lower, pressure, Temp_higher, Temp_lower, temperature, vh, uh, hh, sh, vl, ul, hl, sl , vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2 ):
    # this function is if pressure is exact vh2, uh2, hh2, sh2, vl2, ul2, hl2, sl2



    xlow =  (vl - vh) /( Temp_higher - Temp_lower)
    VL = vh + xlow*(temperature - Temp_lower)
    #print( xlow , VL )
    # AT higher pressure finds x and Vhigh

    xhigh =  (vl2 - vh2) /( Temp_higher - Temp_lower)
    VH = vh2+ xhigh*(temperature - Temp_lower)
    #print( xhigh , VH )
    # final  volume interpolation
    xfinal =  (VH - VL) /( Pressure_higher - Pressure_lower)
    finalV = VL + xfinal*(pressure - Pressure_lower)
    
    
##########################################################

    
    xlow =  (ul- uh) /( Temp_higher - Temp_lower)
    UL = uh + xlow*(temperature - Temp_lower)

    
    # AT higher pressure finds x and Uhigh

    xhigh =  (ul2 - uh2) /( Temp_higher - Temp_lower)
    UH = uh2 + xhigh*(temperature - Temp_lower)


    # final internal energy interpolation

    xfinal =  (UH - UL) /( Pressure_higher - Pressure_lower)
    finalU = UL + xfinal*(pressure - Pressure_lower)


###########################################################


    xlow =  (hl-hh) /( Temp_higher - Temp_lower)
    HL = hh + xlow*(temperature - Temp_lower)

    xhigh =  (hl2-hh2) /( Temp_higher - Temp_lower)
    HH = hh2 + xhigh*(temperature - Temp_lower)


    # final entropy interpolation

    xfinal =  (HH - HL) /( Pressure_higher - Pressure_lower)
    finalH = HL + xfinal*(pressure - Pressure_lower)



###########################################################


    xlow =  (sl - sh) /( Temp_higher - Temp_lower)
    SL = sh + xlow*(temperature - Temp_lower)

    # AT higher pressure finds x and Ehigh

    xhigh =  (sl2 - sh2) /( Temp_higher - Temp_lower)
    SH = sh2 + xhigh*(temperature - Temp_lower)


    # final entropy interpolation

    xfinal =  (SH - SL) /( Pressure_higher - Pressure_lower)
    finalE = SL + xfinal*(pressure - Pressure_lower)
    #print(VL , SL , UL , HL)
    return finalV , finalE , finalU , finalH
    
