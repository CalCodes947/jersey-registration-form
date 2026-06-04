import os

file_name = "jersey_data.csv"

# Create file with headers if it doesn't exist
if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        file.write("Full Name, Jersey Size, Jersey Name, Jersey Number\n")

while True: # Loop for all person

    valid_sizes = ["S", "M", "L", "XL", "XXL", "XXXL"]

    # Collecting details
    name = input("Enter Your Full Name: ")
    while True:
        size = input("Enter Your Jersey Size (S/M/L/XL/XXL/XXXL): ").upper()
        if size in valid_sizes:
            break
        print("invalid size")

    jersey_name = input("Enter The Name You Want On Your Jersey: ")

    while True:
        try:
            jersey_num = int(input("Enter The Number You Want On Your Jersey (in figures): "))
            break
        except ValueError:
            print("Enter valid number")

    # Showing details
    print("\n---------- Details ---------")
    print(f"Full name = {name}")
    print(f"Jersey Size = {size}")
    print(f"Jersey Name = {jersey_name}")
    print(f"Jersey Number = {jersey_num}")

    ask_remaining = True

    while True: # Confirmation Loop
        
        # confirmation to save the data
        confirmation = input("\nAre the above details correct? (y/n): ").strip().lower()
        if confirmation == "y":
            with open("Jersey_data.csv", "a") as file:
                file.write(f"{name}, {size}, {jersey_name}, {jersey_num}\n")

            print("\nDetails saved successfully!\n")
            break # Exit confirmation loop

        elif confirmation == "n":
            print("\nRe-enter your details below\n")
            ask_remaining = False
            break # Exit confirmation loop

        else:
            print("Wrong input! Please type 'y' or 'n'")

    if not ask_remaining:
        continue
            
    while True:
        remaining = input("Another player? (y/n): ").strip().lower()
        if remaining in ["y", "n"]:
            break
        print("Invalid input! Please Enter only 'y' or 'n' ")

    if remaining == "n":
        print("\nAll details captured! Form closed...")
        break
    