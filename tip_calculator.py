print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculate the total bill including the tip
total_with_tip =bill * (1 + tip / 100)

# Calculate the amount each person should pay
amount_per_person = total_with_tip / people

# Format the result to 2 decimal places
final_amount = f"{amount_per_person:.2f}"

print(f"Each person should pay: ${final_amount}")
