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
# N = int(input())

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

# # Read the floating point value
# N_float = float(input("write a number: "))

# # Convert to total cents. Add a small epsilon (e.g., 1e-9)
# # before int() conversion to handle potential floating point inaccuracies.
# # For example, 576.73 * 100 might be 57672.99999999999.
# # int(57672.99999999999) would be 57672.
# # Adding a small epsilon (1e-9) makes it 57673.00000000009, and int() correctly gives 57673.
# total_cents = int(N_float * 100 + 1e-9)

# print("NOTAS:")
# # Denominations for notes: [display_value_in_reais, value_in_cents]
# notes = [
#     (100.00, 10000),
#     (50.00, 5000),
#     (20.00, 2000),
#     (10.00, 1000),
#     (5.00, 500),
#     (2.00, 200)
# ]

# # Use total_cents for note calculation, this variable will be modified.
# amount_to_decompose_cents = total_cents
# print(f"amount_to_decompose_cents: {amount_to_decompose_cents}")
# for display_val, cent_val in notes:
#     count = amount_to_decompose_cents // cent_val
#     print(f"{count} nota(s) de R$ {display_val:.2f}") # .2f ensures two decimal places
#     amount_to_decompose_cents %= cent_val
#     print(f"amount_to_decompose_cents: {amount_to_decompose_cents}")
# print("MOEDAS:")
# # Denominations for coins: [display_value_in_reais, value_in_cents]
# coins = [
#     (1.00, 100),
#     (0.50, 50),
#     (0.25, 25),
#     (0.10, 10),
#     (0.05, 5),
#     (0.01, 1)
# ]

# # The amount_to_decompose_cents now holds the remainder after notes,
# # which is the total amount for coins.
# for display_val, cent_val in coins:
#     count = amount_to_decompose_cents // cent_val
#     print(f"{count} moeda(s) de R$ {display_val:.2f}")
#     amount_to_decompose_cents %= cent_val
#     print(f"**********: {amount_to_decompose_cents}")

# beecrowd | 1035
# A , B , C , D = map(int, input().split())
# if B > C and D > A and   C + D > A + B and c > 0 and D > 0 and A % 2 == 0:
#     print("Valores aceitos")
# else:
#     print("Valores nao aceitos")


# beecrowd | 1036
# Bhaskara's Formula

# import math # Import the math module for square root

# # Read the three floating-point numbers A, B, C
# # Assume they are space-separated on a single line
# line = input().split()
# A = float(line[0])
# B = float(line[1])
# C = float(line[2])

# # Alternative using map:
# # A, B, C = map(float, input().split())

# # Check the first condition for impossibility: A == 0
# if A == 0.0:
#     print("Impossivel calcular")
# else:
#     # Calculate the discriminant (delta)
#     delta = (B**2) - (4 * A * C)

#     # Check the second condition for impossibility: delta < 0
#     if delta < 0.0:
#         print("Impossivel calcular")
#     else:
#         # If we reach here, A != 0 and delta >= 0, so roots can be calculated
#         sqrt_delta = math.sqrt(delta) # or delta**0.5

#         # Calculate R1 and R2
#         R1 = (-B + sqrt_delta) / (2 * A)
#         R2 = (-B - sqrt_delta) / (2 * A)

#         # Print the results formatted to 5 decimal places
#         print(f"R1 = {R1:.5f}")
#         print(f"R2 = {R2:.5f}")



# beecrowd | 1037
# Interval
# Read the floating-point number
# num = float(input())

# # Check the intervals using if-elif-else
# if 0 <= num <= 25:
#     print("Intervalo [0,25]")
# elif 25 < num <= 50: # num > 25 is implied if the first 'if' was false
#     print("Intervalo (25,50]")
# elif 50 < num <= 75: # num > 50 is implied if the previous conditions were false
#     print("Intervalo (50,75]")
# elif 75 < num <= 100: # num > 75 is implied if the previous conditions were false
#     print("Intervalo (75,100]")
# else:
#     # This 'else' block catches any number not fitting the above conditions,
#     # which means it's either < 0 or > 100.
#     print("Fora de intervalo")

# beecrowd | 1038
# Salary
# # Read the input values
# x = int(input('enter a x'))
# y = int(input('enter a y'))

# menu = {
#     1: 4.00,
#     2: 4.50,
#     3: 5.00,
#     4: 2.00,
#     5: 1.50
# }
# # Calculate the total price
# total_price = menu[x] * y

# # Print the result
# print(f"Total: R$ {total_price:.2f}")

# Read the input line and split it into two parts
# input_line = input().split()
# code = int(input_line[0])
# quantity = int(input_line[1])

# # Alternatively, using map:
# # code, quantity = map(int, input().split())

# price = 0.0

# if code == 1:
#     price = 4.00
# elif code == 2:
#     price = 4.50
# elif code == 3:
#     price = 5.00
# elif code == 4:
#     price = 2.00
# elif code == 5:
#     price = 1.50
# # No else needed if we assume valid input codes as per problem context

# total_value = price * quantity

# # Print the output formatted to 2 decimal places
# print(f"Total: R$ {total_value:.2f}")

# beecrowd | 1040
# Average 3
# N1, N2, N3, N4 = map(float,input().split())

# # Calculate the average
# average = (N1 + N2 + N3 + N4) / 4
# if average >= 4.0:
#     print("Media: %.1f" % average)
# elif average < 7.0:
#     print("Media: %.1f" % average)
#     print("Aluno reprovado.")
# elif average >= 5 and average < 7:
#     print("Media: %.1f" % average)
#     print("Aluno em exame.")
# N5 = float(input("enter a number: N5"))
# average_final = (average + N5) / 2
# if average_final >= 5.0:
#     print("Aluno aprovado.")
#     print("Media final: %.1f" % average_final)
# else:
#     print("Aluno reprovado.")
#     print("Media final: %.1f" % average_final)

# beecrowd | 1041
# Coordinates of a Point# Read the two floating-point numbers
# line = input().split()
# x = float(line[0])
# y = float(line[1])

# # Alternatively, using map:
# # x, y = map(float, input().split())

# if x == 0.0 and y == 0.0:
#     print("Origem")
# elif x == 0.0:  # If x is 0 and not origin, it must be on Y-axis
#     print("Eixo Y")
# elif y == 0.0:  # If y is 0 and not origin, it must be on X-axis
#     print("Eixo X")
# elif x > 0.0 and y > 0.0:
#     print("Q1")
# elif x < 0.0 and y > 0.0:
#     print("Q2")
# elif x < 0.0 and y < 0.0:
#     print("Q3")
# elif x > 0.0 and y < 0.0: # This could also be an 'else' if all prior are mutually exclusive
#     print("Q4")

# beecrowd / 1042
# Sort the Numbers
# Read the three integers
# Read the line and convert space-separated input strings to integers
# The map function applies int() to each element returned by input().split()
# # list() converts the map object into a list
# original_numbers = list(map(int, input().split()))

# # Create a new list containing the sorted elements of the original list
# # The sorted() function does not modify the original list.
# sorted_numbers = sorted(original_numbers)

# # Print the sorted numbers, each on a new line
# for number in sorted_numbers:
#     print(number)

# # Print a blank line (an empty print call prints a newline)
# print() 

# # Print the original numbers in their input order, each on a new line
# for number in original_numbers:
#     print(number)

# beecrowd | 1043
# Triangle

# Read the three floating-point numbers
# A,B,C = map(float, input().split())
# is_triangle = False
# if A + B > C and A + C > B and B + C > A:
#     is_triangle = True
# if is_triangle:
#     print(f"Perimetro = {A + B + C:.1f}")
# else:
#     print(f"Area = {((A + B) * C) / 2:.1f}")
# Read the three floating-point numbers
# line = input().split()
# A = float(line[0])
# B = float(line[1])
# C = float(line[2])

# # Alternatively, using map:
# # A, B, C = map(float, input().split())

# # Check the triangle inequality theorem
# # All three conditions must be true
# if (A + B > C) and (A + C > B) and (B + C > A):
#     # It's a triangle
#     perimeter = A + B + C
#     print(f"Perimetro = {perimeter:.1f}")
# else:
#     # It's not a triangle, calculate area of trapezium
#     area_trapezium = ((A + B) * C) / 2.0
#     print(f"Area = {area_trapezium:.1f}")

# beecrowd | 1044
# Multiples
# x = int(input("x = "))
# y = int(input("y = "))
# if x % y == 0 or y % x == 0:
#     print("Sao Multiplos")
    
# else:
#     print("Nao sao Multiplos")

# beecrowd | 1045
# Triangle types 
# A,B,C = map(float, input().split())
# if A >= B + C :
#     print("NAO FORMA TRIANGULO")
# elif A**2 == B**2 + C**2:
#     print("TRIANGULO RETANGULO")
# elif A**2 > B**2 + C**2:
#     print("TRIANGULO OBTUSANGULO")
# elif A**2 < B**2 + C**2:
#     print("TRIANGULO ACUTANGULO")
# if A == B == C:
#     print("TRIANGULO EQUILATERO")
# elif A == B or B == C or A == C:
#     print("TRIANGULO ISOSCELES")

# beecrowd | 1046
# Game Time
# Read the input values
# starting_hour,finnishing_hour  = map(int, input().split())
# print(f"starting_hour finnishing_hour: {starting_hour, finnishing_hour}")
# # # Calculate the total time played in secondsif starting 
# if starting_hour == finnishing_hour:
#     duration = 24
#     print(f"duration: {duration}")
# elif starting_hour > finnishing_hour:
#     duration = (24 -starting_hour) + finnishing_hour
#     print(f"duration: {duration}")
# else:
#     duration = finnishing_hour - starting_hour
#     print(f"duration: {duration}")
# # # Print the result
# print(f"Time played: {duration} hours")

