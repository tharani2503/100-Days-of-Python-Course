## Day2 { Type casting or conversion, type error,value error & Type Checking}

print("Welcome to the tip calculator")
bill=int(input("What was the total bill?"))
tip=int(input("How much tip would you like to give? 10, 12 or 15?"))
sharing=int(input("How many People to split the bill?"))
a=round((bill*(1+(0.01*tip)))/sharing)
print("Each person should pay"+f"{a}")
