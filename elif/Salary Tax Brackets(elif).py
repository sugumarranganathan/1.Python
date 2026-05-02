salary = int(input("Enter salary: "))

if salary <= 250000:
    print("No Tax")
elif salary <= 500000:
    print("5% Tax")
elif salary <= 1000000:
    print("20% Tax")
else:
    print("30% Tax")
