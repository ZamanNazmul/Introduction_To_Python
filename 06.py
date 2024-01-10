#Nazmul Zaman Bsc in IT
print("This is task no:6")


num_of_checks = int(input("Enter the number of checks: "))


for _ in range(num_of_checks):
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")

