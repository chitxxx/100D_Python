print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = float(input("How much tip would you like to give? (%)"))
people = int(input("How many people to split the bill?"))
bill_with_tip = bill * (1 + tip / 100)
per_person_bill = bill_with_tip / people
print(f"Each person should pay ${round(per_person_bill, 2)}.")
