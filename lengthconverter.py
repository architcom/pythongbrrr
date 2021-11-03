first_unit=input("Type the unit which u want to convert - [K]ilometer,[H]ectometer,[D]ecameter,[M]eter,[De]cimeter,[C]entimeter,[Mi]llimeter ")
second_unit=input("Type the unit which u want to convert to - [K]ilometer,[H]ectometer,[D]ecameter,[M]eter,[De]cimeter,[C]entimeter,[Mi]llimeter ")
mag1=int(input("type the magnitude  "))
ans=""


#killometer

if first_unit=="K" and second_unit=="K":

    

    print(str(mag1)+"km")
else:
    print("bruh")

    


if first_unit=="K" and second_unit=="K":

    ans=(mag1*10)

    print(str(ans)+"hm")
    



if first_unit=="K" and second_unit=="D":

    ans=(mag1*100)

    print(str(ans)+"dam")


if first_unit=="K" and second_unit=="M":

    ans=(mag1*1000)

    print(str(ans)+"m")



if first_unit=="K" and second_unit=="De":

    ans=(mag1*10000)

    
    print(str(ans)+"dm")


if first_unit=="K" and second_unit=="C":

    ans=(mag1*100000)


    print(str(ans)+"cm")


if first_unit=="K" and second_unit=="Mi":

    ans=(mag1*1000000)

    print(str(ans)+"mm")



#Hectameter

if first_unit=="H" and second_unit=="K":

    ans=(mag1/10)

    

    print(str(ans)+"km")


if first_unit=="H" and second_unit=="H":

    

    print(str(mag1)+"hm")


if first_unit=="H" and second_unit=="D":

    ans=(mag1*10)

    print(str(ans)+"dam")


if first_unit=="H" and second_unit=="M":

    ans=(mag1*100)

    print(str(ans)+"m")



if first_unit=="H" and second_unit=="De":

    ans=(mag1*1000)

    
    print(str(ans)+"dm")


if first_unit=="H" and second_unit=="C":

    ans=(mag1*10000)


    print(str(ans)+"cm")

if first_unit=="H" and second_unit=="Mi":

    ans=(mag1*100000)

    print(str(ans)+"mm")


#decameter

if first_unit=="D" and second_unit=="K":

    ans=(mag1/100)

    

    print(str(ans)+"km")





if first_unit=="D" and second_unit=="D":

    

    print(str(mag1)+"dam")




if first_unit=="D" and second_unit=="H":

    ans=(mag1/10)

    print(str(ans)+"hm")



if first_unit=="D" and second_unit=="M":

    ans=(mag1*10)

    print(str(ans)+"m")




if first_unit=="D" and second_unit=="De":

    ans=(mag1*100)

    
    print(str(ans)+"dm")



if first_unit=="D" and second_unit=="C":

    ans=(mag1*1000)


    print(str(ans)+"cm")


if first_unit=="D" and second_unit=="Mi":

    ans=(mag1*10000)

    print(str(ans)+"mm")



#Meter


if first_unit=="M" and second_unit=="K":

    ans=(mag1/1000)

    

    print(str(ans)+"km")


if first_unit=="M" and second_unit=="M":

    

    print(str(mag1)+"m")




if first_unit=="M" and second_unit=="H":

    ans=(mag1/100)

    print(str(ans)+"hm")
elif first_unit==""and second_unit=="":
    print("bruh")



if first_unit=="M" and second_unit=="D":

    ans=(mag1/10)

    print(str(ans)+"dam")




if first_unit=="M" and second_unit=="De":

    ans=(mag1*10)

    
    print(str(ans)+"dm")



if first_unit=="M" and second_unit=="C":

    ans=(mag1*100)


    print(str(ans)+"cm")


if first_unit=="M" and second_unit=="Mi":

    ans=(mag1*1000)

    print(str(ans)+"mm")






#decimeter


if first_unit=="De" and second_unit=="K":

    ans=(mag1/10000)

    

    print(str(ans)+"km")


if first_unit=="De" and second_unit=="De":

    

    print(str(mag1)+"dm")



if first_unit=="De" and second_unit=="H":

    ans=(mag1/1000)

    print(str(ans)+"hm")


if first_unit=="De" and second_unit=="D":

    ans=(mag1/100)

    print(str(ans)+"dam")



if first_unit=="De" and second_unit=="M":

    ans=(mag1*10)

    
    print(str(ans)+"m")




if first_unit=="De" and second_unit=="C":

    ans=(mag1*10)






    print(str(ans)+"cm")
if first_unit=="De" and second_unit=="Mi":

    ans=(mag1*100)

    print(str(ans)+"mm")


#Centimeter



if first_unit=="C" and second_unit=="K":

    ans=(mag1/100000)

    

    print(str(ans)+"km")


if first_unit=="C" and second_unit=="C":

    

    print(str(mag1)+"cm")



if first_unit=="C" and second_unit=="H":

    ans=(mag1/10000)

    print(str(ans)+"hm")


if first_unit=="C" and second_unit=="D":

    ans=(mag1/1000)

    print(str(ans)+"dam")



if first_unit=="C" and second_unit=="M":

    ans=(mag1*100)

    
    print(str(ans)+"m")




if first_unit=="C" and second_unit=="De":

    ans=(mag1*10)






    print(str(ans)+"d")
if first_unit=="C" and second_unit=="Mi":

    ans=(mag1/10)

    print(str(ans)+"mm")



























