#Taking user input

city= input("Enter your city's name.")
temp= float(input("Enter your city's temperature."))

#Conditional Statements
#1.If-statements
if temp > 35:
    print("It is very hot today! Stay home or take an umbrella if you are going out.")

    # 2. If-else statements
if temp > 25:
    print("Great day to have fun outside! Enjoy your day.")
else:
    print("Get a jacket or a heavy clothes  before you go somewhere!")

    #3.if-else-elif statements
if temp > 35:
    print("Weather: Hot and scorching")
elif temp > 25:
       print("Weather: Warm and sunny")
elif temp > 15:
     print(" Weather:Cool and breezy")
else:
     print("Weather:Cold: Stay warm")

     #datemoulde
import datetime
import calendar
now = datetime.datetime.now()
print("City :",city )
print("Time now:",now)

print(calendar.calendar(now.year))