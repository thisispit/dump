
with open('test.text') as f:
    lines = f.readlines()

currencyDict = {}
for line in lines:
    parsed = line.strip().split("\t")  # Strip any leading/trailing whitespace and split by tab
    currencyDict[parsed[0]] = float(parsed[1])  # Convert the rate to float for calculations

try:
    amount = float(input("Enter the amount in INR:\n"))
except ValueError:
    print("Invalid amount entered. Please enter a numerical value.")
    exit(1)


print("Enter the name of the currency you want to convert this amount to. Available Options:")
for item in currencyDict.keys():
    print(item)

currency = input("Please enter one of these values: \n")


if currency in currencyDict:
    converted_amount = amount * currencyDict[currency]
    print(f"{amount} INR is equal to {converted_amount} {currency}")
else:
    print("Invalid currency entered. Please enter a valid currency from the available options.")
