def generate_multiplication_table(number, up_to):

    print(f"Multiplication Table for {number} (up to {up_to}):\n")
    for i in range(1, up_to  + 1):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        num = int(input("Enter the number for which you want the multiplication table: "))
        limit = int(input("Enter the range up to which you want the table: "))

        generate_multiplication_table(num, limit)
    except ValueError:
        print("Please enter valid integer values!")
