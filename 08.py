#Nazmul Zaman Bsc in IT
print("This is task no:8")


num_of_checks = int(input("Enter the number of checks: "))
for _ in range(num_of_checks):
    char = input("Enter a character: ").lower()
    if char.isalpha():
        result = "vowel" if char in 'aeiou' else "consonant"
        print(f"The character '{char}' is a {result}.")
    else:
        print("Invalid input. Please enter a valid alphabet character.")

