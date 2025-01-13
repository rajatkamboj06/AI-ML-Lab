loop_type = input("Enter the loop type ('for' or 'while'): ").strip().lower()

if loop_type == "for":
    print("Using for loop:")
    for i in range(1, 11):
        print(i)

elif loop_type == "while":
    print("Using while loop:")
    counter = 1
    while counter <= 10:
        print(counter)
        counter += 1

else:
    print("Invalid input. Please enter 'for' or 'while'.")
