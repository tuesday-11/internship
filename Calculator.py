
def show_menu():
    print("\n--- CALCULATOR MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", num1 + num2)
            elif choice == "2":
                print("Result:", num1 - num2)
            elif choice == "3":
                print("Result:", num1 * num2)
            elif choice == "4":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                else:
                    print("Result:", num1 / num2)

        except ValueError:
            print("Invalid input! Please enter numbers.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")