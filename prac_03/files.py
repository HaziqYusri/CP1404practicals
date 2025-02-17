#TODO: 1. Write a name to name.txt
name = input("Enter your name: ")

file = open("name.txt", "w")
file.write(name)
file.close()

#TODO: 2. Read and print the name from name.txt
file = open("name.txt", "r")
name = file.readline().strip()  #read
file.close()

print(f"Hi {name}!")  #print

#TODO: 3. Read first two numbers on numbers.txt and print the sum
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())

print(f"Sum of first two numbers: {num1 + num2}")

#TODO: 4. Sum of all no.s in numbers.txt
total = 0

with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())

print(f"Total sum of all numbers: {total}")