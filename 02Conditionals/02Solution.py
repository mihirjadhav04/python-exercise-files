from datetime import datetime
import calendar
print(datetime.day)

age = 10
today = datetime.today()
day = calendar.day_name[today.weekday()]
# print(today)
# print(day)

if age > 17:
    if day == "Wednesday":
        print("Adult : you will get extra $2 off as today is wednesday. Your final ticket price is $8.")
    else:
        print("Adult : your ticket price is $12.")

elif age < 18:
    if day == "Wednesday":
        print("Children : you will get extra $2 off as today is wednesday. Your final ticket price is $6.")
    else:
        print(" Children: your ticket price is $8")
else:
    print("something wrong.")
    