while True:
    print("\n this is a program to know your horoscope\n")
    date = int(input("enter your birth date"))
    if date>31:
        print("\n plese enter the correct date.the date should not exceed 31\n")
        continue
    month =int (input("\enter the birth month in number format(for example 1 for junuary 12 for december):\n"))
    if month>12:
        print("\n please enter the correct month. the month should not exceed 12\n")
        continue
    if month==12:
        if(date<22):
            sign="Sagittarious"
        else:"Capricorn"
    elif month==1:
        if(date<20):
            sign="Capricorn"
        else:'Aquarius'
    elif  month==2:
        if (date<19): 
            sign="Aquarius"
        else:"Pisces"
    elif month==3:
        if(date<21):
            sign="Pisces"
        else:"Aries"
    elif month==4:
        if(date<20): 
            sign="Aries"
        else:"Gemini"
    elif month==6:
        if(date<21): 
            sign="Gemini"
        else:"Cancer"
    elif month==7:
        if(date<23): 
            sign="Cancer"
        else:"Leo"
    elif month==8:
        if (date<23): 
            sign="Leo"
        else:"Virgo"
    elif month==9:
        if (date<23): 
            sign="Virgo"
        else:"Libra"
    elif month==10:
        if(date<23): 
            sign="Libra"
        else:"Scorpio"
    elif month==11:
        if(date<22): 
            sign="Scorpio"
        else:"Sagittarius"

    print("\n your astrological sign is:")

    user=(input("\n do you want to read  your horoscope?\n Enter yes to read your scope and no to exit\n"))
    if user=="yes":
        print("\nhere is your horoscope!!!!")
        if sign=="Sagittarius":
            print("\n you will have a good day today .new massage will come from your friend")
        elif sign=="capricorn":
            print(" \n we will get the asupicious result of our hard work in the last month of year")
            break
        elif sign=="Aquarius":
            print("\nyour little carelessness can cause big problemse\n")
            break
        elif sign=="Pisces":
            print("\n Pisces is symbolized by a pair of fish. All the people are selfless and focus on the sprain")
        elif sign=="Aries":
            print("\n people make their point in a powerfull way.\n")
        elif sign=="Taurus":
            print("\n there will we progress in your life.\n")
        elif sign=="Gemini":
            print("\n today work is very good.\n")
        elif sign=="Cancer":
            print("\n you need to stop crying about way that waiter gave you cold food \n")
        elif sign=="Leo":
            print("\n you miss all your deadlines this work \n")
        elif sign=="Virgo":
            print("\n you get the job coming the month \n")
        elif sign=="Libra":
            print("\n tolking your way out of problems.\n")
        elif sign=="Scorpeo":
            print("\n there is one think that you love more than your reflection\n")
            break
        elif sign=="N":
            print ('\n thank you for your time\n')
            break
        else:
            print('invalid ,plese enter the correct input')
