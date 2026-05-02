age = int(input("Enter your age: "))

if age < 5:
    print("Free Ticket")
elif age <= 12:
    print("Child Ticket - 50 Rs")
elif age <= 60:
    print("Adult Ticket - 100 Rs")
else:
    print("Senior Ticket - 70 Rs")
