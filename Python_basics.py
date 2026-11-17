#Print the details of a student
name = "Diksha"
branch = "Artificial Intelligence and Machine Learning"

print("Name:", name)
print("Branch:", branch)

#Check even or odd number
num= int(input("Enter the Number:"))
if num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

#Print numbers using a loop
for i in range(1, 11):
    print(i)

#Function to add two numbers
def add_numbers(a, b):
    return a + b
print(add_numbers(10, 20))

# working with lists
numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))




