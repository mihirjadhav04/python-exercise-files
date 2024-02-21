userAge = int(input("Enter your age : "))
print("USER AGE:", userAge)
if userAge < 13:
    print("Child")
elif userAge < 19:
    print("Teenager")
elif userAge < 60:
    print("Adult")
elif userAge > 60:
    print("Senior")
else:
    print("something went wrong.")
