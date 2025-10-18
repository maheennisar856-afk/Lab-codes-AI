# Function to show first 'n' even numbers
def even_numbers(n):
    evens = []  # list to store even numbers
    for i in range(1, n+1):
        evens.append(2 * i)
    print("First", n, "even numbers:", evens)
    return evens  # return the list

# Take input from user
n = int(input("Enter how many even numbers you want: "))

# Call the function
even_list = even_numbers(n)

# Calculate sum and product outside the function
sum_evens = sum(even_list)

product = 1
for num in even_list:
    product *= num

print("Sum of even numbers:", sum_evens)
print("Product of even numbers:", product)
