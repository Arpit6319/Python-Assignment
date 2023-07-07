# User-defined marks for three variables
n1 = float(input("Enter the marks for n1: "))
n2 = float(input("Enter the marks for n2: "))
n3 = float(input("Enter the marks for n3: "))

# Calculate the average
average = (n1 + n2 + n3) / 3

# Display the average in the desired format
print("The average of {}, {}, and {} is {:.2f}".format(n1, n2, n3, average))