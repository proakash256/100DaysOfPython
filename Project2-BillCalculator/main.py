print("Welcome to the Bill Calculator....\n\n")

total = float(input("What is the Total Bill in Rupees : "))
tip = int(input("What Percentage of Tip would you like to give : "))
n = int(input("Number of People to Split the Bill : "))

total += ((tip / 100) * total)
head = "{:.2f}".format(total / n)
print(f"\nBill per head is {head} Rupees.")
