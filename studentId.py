studentid = input("Input ID: ").strip().upper()
letters = studentid[0:2]
numbers = studentid[2:8]

if len(studentid) != 8:
    print("Invalid ID - ID must be exactly 8 characters")
elif not letters.isalpha():
    print("Invalid ID - First 2 characters must be letters")
elif not numbers.isdigit():
    print("Invalid ID - Last 6 characters must be numbers")
else:
    print(f"Valid ID - Masked ID: {letters}****{(numbers[4:6])}")