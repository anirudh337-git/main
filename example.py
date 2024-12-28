# Program to calculate factorial using iterative and recursive methods

def factorial_iterative(n):
    """Calculate factorial iteratively."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """Calculate factorial recursively."""
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("Factorial Calculator")
    number = int(input("Enter a positive integer: "))
    
    if number < 0:
        print("Factorial is not defined for negative numbers.")
        return
    
    print("\nChoose method:")
    print("1. Iterative")
    print("2. Recursive")
    print("anirudh")
    print("anirudh2")
    choice = int(input("Enter choice (1/2): "))

    if choice == 1:
        print(f"Factorial (Iterative) of {number}: {factorial_iterative(number)}")
    elif choice == 2:
        print(f"Factorial (Recursive) of {number}: {factorial_recursive(number)}")
    else:
        print("Invalid choice. Please run the program again.")

if __name__ == "__main__":
    main()
