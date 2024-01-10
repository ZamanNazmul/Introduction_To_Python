#Nazmul Zaman Bsc in IT
print("This is task no:10")


numbers = []
for i in range(3):
    number = int(input(f"Enter the {i+1} number: "))
    numbers.append(number)
largest_number = max(numbers)
print(f"The largest number among the entered integers is: {largest_number}")
