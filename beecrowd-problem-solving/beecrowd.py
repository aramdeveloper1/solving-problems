# “I Solve to Learn, Not to Impress”
#  Spaced Repetition (Anki / Review List)
# Re-attempt failed or complex problems:
# 1 day later
# 3 days later
# 7 days later



# beecrowd | 1011
# Sphere
# PI = 3.14159
# # r = float(input())
# volume = (4/3) * PI * (r** 3)
# print(f"VOLUME = {volume:.3f}")


# beecrowd | 1012
# Simple Arithmetic Operations
# Area
# a = float(input("wirte a number: "))
# b = float(input("wirte a number: "))
# c = float(input("wirte a number: "))
# pi= 3.14159
# # Area of a rectangle triangle
# area = (a * c) / 2
# # Area of a circle
# area_circle = pi * (c**2)
# # Area of a trapezium
# area_trapezium = ((a + b) * c) / 2
# # Area of a square
# square_area = b**2
# # Area of a rectangle
# rectangle_area = a * b
# print(f"TRIANGULO: {area:.3f}")
# print(f"CIRCULO: {area_circle:.3f}")
# print(f"TRAPEZIO: {area_trapezium:.3f}")
# print(f"QUADRADO: {square_area:.3f}")
# print(f"RETANGULO: {rectangle_area:.3f}")

# beecrowd | 1013
# The Greatest
# Read the input values from a single line
# input_line = input().split()  # Reads "7 14 106" into ['7', '14', '106']

# # Convert the string values to integers
# val1 = int(input_line[0])
# val2 = int(input_line[1])
# val3 = int(input_line[2])

# # --- Calculations ---

# # Step 1: Find the greater of val1 and val2 using the formula
# # In Python, abs() is the absolute value function.
# # We use // for integer division to ensure the result is an integer.
# temp_maior = (val1 + val2 + abs(val1 - val2)) // 2
# print(f"temp_maior: {temp_maior}")
# # Step 2: Find the greater of temp_maior and val3 using the formula
# maior_final = (temp_maior + val3 + abs(temp_maior - val3)) // 2

# # --- Output ---
# # Using an f-string for formatted output
# print(f"{maior_final} eh o maior")


# beecrowd | 1014
# x_km = float(input())
# y_liters = float(input())
# find_consumption = x_km / y_liters
# print(f"{find_consumption:.3f} km/l")

# beecrowd | 1015
# Distance Between Two Points
# import math
# # # Read the input values from a single line
# input_line = input().split()  # Reads "1 2 3 4" into ['1', '2', '3', '4']
# print(f"input_line: {input_line}")
# # # Convert the string values to integers
# x1 = int(input_line[0])
# y1 = int(input_line[1])
# x2 = int(input_line[2])
# y2 = int(input_line[3])

# # # Calculate the distance using the formula
# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# # # Output the result using an f-string for formatted output
# print(f"{distance:.4f}")

# # beecrowd | 1016
# Distance Between Two Points
# Step 1: Get the input
# The input is a single integer value.
# desired_distance_km = int(input())

# # Step 2: Perform the calculation
# # For every kilometer of distance Y needs to gain, it takes 2 minutes.
# time_taken_minutes = desired_distance_km * 2

# # Step 3: Print the output
# # We need to print the integer result followed by " minutos".
# # An f-string is a good way to format this.
# print(f"{time_taken_minutes} minutos")

# beecrowd | 1017
# Consumption of Fuel
# Step 1: Get the input values
# The first input is the total time spent in hours.
# The second input is the distance travelled in kilometers.
# total_time_hours = int(input())
# distance_travelled_km = float(input())
# distance = total_time_hours * distance_travelled_km
# # Step 2: Perform the calculation
# # The fuel consumption is the distance travelled divided by the total time spent.
# litters_per_km = distance / 12
# print(f"{litters_per_km:.3f}")


# beecrowd | 1018
# Banknotes
# Read the integer value


# Read the integer value
N = int(input())

# Print the read value (as per output requirement)
# print(N)

# # List of possible banknote denominations, from largest to smallest
# banknote_values = [100, 50, 25, 10, 5, 2, 1]

# # Keep track of the amount we still need to decompose
# amount_remaining = N 

# # Iterate through each banknote denomination
# for value in banknote_values:
#     # Calculate how many notes of the current 'value' can be used
#     # Integer division (//) gives the whole number of notes
#     count = amount_remaining // value
    
#     # Print the result for this banknote value in the specified format
#     # The format string R$ {value},00 is literal for the value part.
#     print(f"{count} nota(s) de R$ {value},00")
    
#     # Update the amount remaining
#     # The modulo operator (%) gives the remainder after division
#     amount_remaining = amount_remaining % value
#     print(f"amount_remaining: {amount_remaining}")
#     # Alternatively: amount_remaining = amount_remaining - (count * value)


# beecrowd | 1019
# Time Conversion
# Read the input string
# seconds = int(input("write a number: "))
# # seconds = int(input())
# print(f"seconds: {seconds}")
# # Calculate the hours, minutes and seconds
# hours = seconds // 3600
# minutes = (seconds % 3600) // 60
# remaining_seconds = seconds % 60

# # Print the result in the specified format
# print(f"{hours}:{minutes}:{remaining_seconds}")