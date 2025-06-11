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

# Beecrowd | 1047
# Time Conversion
# Read the four integer inputs
# line = input().split()
# initial_hour = int(line[0])
# initial_minute = int(line[1])
# final_hour = int(line[2])
# final_minute = int(line[3])

# # Alternatively, using map:
# # initial_hour, initial_minute, final_hour, final_minute = map(int, input().split())

# # Convert start and end times to total minutes from 00:00
# start_total_minutes = initial_hour * 60 + initial_minute
# end_total_minutes = final_hour * 60 + final_minute

# duration_in_minutes = 0

# if start_total_minutes == end_total_minutes:
#     # This covers the case where start and end times are identical (e.g., 7:07 to 7:07)
#     # The problem states this means 24 hours.
#     duration_in_minutes = 24 * 60
# elif start_total_minutes < end_total_minutes:
#     # Game ends on the same day
#     duration_in_minutes = end_total_minutes - start_total_minutes
# else: # start_total_minutes > end_total_minutes (game crosses midnight)
#     # Add 24 hours worth of minutes to the end time and then subtract start time
#     duration_in_minutes = (end_total_minutes + 24 * 60) - start_total_minutes

# # Convert the total duration from minutes back to hours and minutes
# final_duration_hours = duration_in_minutes // 60
# final_duration_minutes = duration_in_minutes % 60

# # Print the result
# print(f"O JOGO DUROU {final_duration_hours} HORA(S) E {final_duration_minutes} MINUTO(S)")

# beecrowd | 1048

# ============================== 
# Read the employee's salary
# current_salary = float(input())

# readjustment_rate_percent = 0

# if current_salary >= 0 and current_salary <= 400.00:
#     readjustment_rate_percent = 15
# elif current_salary <= 800.00: # Implicitly > 400.00
#     readjustment_rate_percent = 12
# elif current_salary <= 1200.00: # Implicitly > 800.00
#     readjustment_rate_percent = 10
# elif current_salary <= 2000.00: # Implicitly > 1200.00
#     readjustment_rate_percent = 7
# else: # Implicitly current_salary > 2000.00
#     readjustment_rate_percent = 4

# # Calculate the money earned and the new salary
# money_earned = current_salary * (readjustment_rate_percent / 100.0)
# new_salary = current_salary + money_earned

# Print the results
# Use .2f for formatting to two decimal places for monetary values.
# The percentage is printed as an integer.
# print(f"Novo salario: {new_salary:.2f}")
# print(f"Reajuste ganho: {money_earned:.2f}")
# print(f"Em percentual: {readjustment_rate_percent} %")


# beecrowd | 1049
# # Animal
# animal1 = input("enter a animal 1: ")
# animal2 = input("enter a animal 2: ")
# animal3 = input("enter a animal 3: ")
# if animal1 == "vertebrado":
#     if animal2 == "ave":
#         if animal3 == "carnivoro":
#             print("aguia")
#         elif animal3 == "onivoro":
#             print("pomba")
#     elif animal2 == "mamifero":
#         if animal3 == "onivoro":
#             print("homem")
#         elif animal3 == "herbivoro":
#             print("vaca")
# elif animal1 == "invertebrado":
#     if animal2 == "inseto":
#         if animal3 == "hematofago":
#             print("pulga")
#         elif animal3 == "herbivoro":
#             print("lagarta")
#     elif animal2 == "anelideo":
#         if animal3 == "hematofago":
#             print("sanguessuga")
#         elif animal3 == "onivoro":
#             print("minhoca")
# beecrowd | 1050
# # DDD
# ddd = int(input())

# if ddd == 61:
#     print("Brasilia")
# elif ddd == 71:
#     print("Salvador")
# elif ddd == 11:
#     print("Sao Paulo")
# elif ddd == 21:
#     print("Rio de Janeiro")
# elif ddd == 32:
#     print("Juiz de Fora")
# elif ddd == 19:
#     print("Campinas")
# elif ddd == 27:
#     print("Vitoria")
# elif ddd == 31:
#     print("Belo Horizonte")
# else:
#     print("DDD nao cadastrado")

# beecrowd | 1051
# # Income Tax
# salary = float(input())
# # tax = 0.0
# if salary <= 2000.00 and salary >= 0:
#     print("Isento")
# elif salary > 2000.00 and salary <= 3000.00:
#     tax = (salary - 2000.00) * 0.08
#     print(f"R$ {tax:.2f}")
# elif salary > 3000.00 and salary <= 4500.00:
#     tax = (salary - 3000.00) * 0.08 + 100.00
#     print(f"R$ {tax:.2f}")
# elif salary > 4500.00:
#     tax = (salary - 4500.00) * 0.28 + 100.00 + 120.00
#     print(f"R$ {tax:.2f}")
# else:
#      print("Isento")

# beecrowd | 1052
# # Month
# month = int(input())
# months ={
#     1: "January",
#     2: "February",
#     3: "March",
#     4: "April",
#     5: "May",
#     6: "June",
#     7: "July",
#     8: "August",
#     9: "September",
#     10: "October",
#     11: "November",
#     12: "December"
# }
# if month in months:
#     print(months[month])
# else:
#     print("Invalid month")


# beecrowd | 1059
# # # Even Numbers
# for i in range(101):
#     if i % 2 == 0:
#         print(i)

# beecrowd | 1060
# # Positive Numbers
# num = map(float, input("enter a number: ").split())
# positive_count = 0
# for i in num:
#     if i > 0:
#         positive_count += 1
# print(f"{positive_count} valores positivos")

# Initialize a counter for positive numbers
# positive_count = 0

# # Loop 6 times because we need to read 6 numbers
# for _ in range(6): # The underscore '_' is used when the loop variable itself isn't needed
#     # Read a line of input (which will be a string)
#     # Convert it to a float to handle both integers and decimals
#     number = float(input()) 
    
#     # Check if the number is positive
#     if number > 0:
#         positive_count = positive_count + 1 # Increment the counter

# # Print the final count
# print(f"{positive_count} valores positivos")

# beecrowd | 1061
# # Event Time  
# --- Read Start Information ---
# start_day_line = input() # "Dia dd"
# start_day = int(start_day_line.split()[1]) # Get the 'dd' part

# start_time_line = input() # "hh : mm : ss"
# parts_start_time = start_time_line.split(" : ")
# start_hour = int(parts_start_time[0])
# start_minute = int(parts_start_time[1])
# start_second = int(parts_start_time[2])

# # --- Read End Information ---
# end_day_line = input() # "Dia dd"
# end_day = int(end_day_line.split()[1])

# end_time_line = input() # "hh : mm : ss"
# parts_end_time = end_time_line.split(" : ")
# end_hour = int(parts_end_time[0])
# end_minute = int(parts_end_time[1])
# end_second = int(parts_end_time[2])

# # --- Define time constants in seconds ---
# SECONDS_PER_MINUTE = 60
# SECONDS_PER_HOUR = 60 * SECONDS_PER_MINUTE
# SECONDS_PER_DAY = 24 * SECONDS_PER_HOUR

# # --- Convert start and end to total seconds from a reference point ---
# # (e.g., start of Day 1 of April, 00:00:00)
# # The problem says "within April month", so day 1 is our reference.
# start_total_seconds = (start_day - 1) * SECONDS_PER_DAY + \
#                       start_hour * SECONDS_PER_HOUR + \
#                       start_minute * SECONDS_PER_MINUTE + \
#                       start_second

# end_total_seconds = (end_day - 1) * SECONDS_PER_DAY + \
#                     end_hour * SECONDS_PER_HOUR + \
#                     end_minute * SECONDS_PER_MINUTE + \
#                     end_second

# # --- Calculate duration in seconds ---
# duration_seconds = end_total_seconds - start_total_seconds

# # --- Convert duration back to days, hours, minutes, seconds ---
# d_duration = duration_seconds // SECONDS_PER_DAY
# remainder_seconds = duration_seconds % SECONDS_PER_DAY

# h_duration = remainder_seconds // SECONDS_PER_HOUR
# remainder_seconds = remainder_seconds % SECONDS_PER_HOUR

# m_duration = remainder_seconds // SECONDS_PER_MINUTE
# s_duration = remainder_seconds % SECONDS_PER_MINUTE

# # --- Print the output ---
# print(f"{d_duration} dia(s)")
# print(f"{h_duration} hora(s)")
# print(f"{m_duration} minuto(s)")
# print(f"{s_duration} segundo(s)")




# beecrowd | 1064
# # # Positive and Average
# positive_count = 0
# positive_Sum = 0
# for i in range(6):
#     num = float(input())
#     if num >0:
#         print(f"num: {num}")
#         positive_count +=1
#         positive_Sum += num
# average = positive_Sum / positive_count
# print(f"{positive_count} valores positivos and average: {average:.1f}")

# beecrowd | 1065
# # Even Numbers
# Initialize a counter for even numbers
# even_count = 0

# # Loop 5 times because we need to read 5 integer numbers
# for _ in range(5):
#     # Read a line of input and convert it to an integer
#     number = int(input()) 
    
#     # Check if the number is even
#     if number % 2 == 0:
#         even_count += 1 # Increment the counter

# # Print the final count
# print(f"{even_count} valores pares")


# beecrowd | 
# # Even and Odd
# Initialize counters for even, odd, positive, and negative numbers
# # even_count = 0
# X = int(input())

# # Iterate from 1 to X (inclusive)
# for number in range(1, X + 1): # range(start, stop) goes up to stop-1, so X+1 for stop
#     # Check if the number is odd
#     if number % 2 != 0: # or number % 2 == 1 for positive odds
#         print(number)

# beecrowd | 1070
# # Six Odd Numbers
# X = int(input())

# starting_odd_number = 0

# # Determine the first odd number in the sequence
# if X % 2 != 0:  # If X is odd
#     starting_odd_number = X
# else:  # If X is even
#     starting_odd_number = X + 1

# # Print 6 consecutive odd numbers
# current_number_to_print = starting_odd_number
# for _ in range(6): # We need to print exactly 6 numbers
#     print(current_number_to_print)
#     current_number_to_print += 2 # Move to the next odd number

# beecrowd | 1071
# # Sum of Consecutive Odd Numbers
# Read the two integer inputs
# A,B = map(int,input().split())
# A = min(A,B)
# B = max(A,B)
# sum_of_consecutive_odds = 0
# for i in range(A+1, B):
#     if i % 2 != 0:
#         print(i)
#         sum_of_consecutive_odds += i
# print(sum_of_consecutive_odds)

# beecrowd | 1072
# # Interval 2
# Read the number of integers to be processed
# N = int(input())
# count_in_interval = 0
# for _ in range(N):
#      value = int(input())
#      if 10 <= value <= 20:
#          count_in_interval += 1
# print(f"{count_in_interval} in")
# print(f"{N - count_in_interval} out")



# Beecrowd | 1073
# # Even Square
# Read the integer input
# N = int(input())
# for i in range(1, N + 1):
#     if i % 2 == 0:
#         print(f"{i} the square of {i**2}")


# beecrowd | 1074
# # Even or Odd
# Read the number of integers to be processed
# N = int(input())
# for _ in range(N):
#     number = int(input())
#     if number == 0:
#         print("NULL")
#     elif number % 2 == 0 and number > 0:
#         print("EVEN POSITIVE")
#     elif number % 2 == 0 and number < 0:
#         print("EVEN NEGATIVE")
#     elif number % 2 != 0 and number > 0:
#         print("ODD POSITIVE")
#     elif number % 2 != 0 and number < 0:
#         print("ODD NEGATIVE")

# N = int(input()) # Number of test cases

# for _ in range(N):
#     X = int(input()) # Read the integer for the current test case
    
#     if X == 0:
#         print("NULL")
#     else:
#         # Determine if X is EVEN or ODD
#         if X % 2 == 0:
#             parity_part = "EVEN"
#         else:
#             parity_part = "ODD"
            
#         # Determine if X is POSITIVE or NEGATIVE
#         if X > 0:
#             sign_part = "POSITIVE"
#         else: # X must be < 0 since X != 0
#             sign_part = "NEGATIVE"
            
#         print(f"{parity_part} {sign_part}")

# beecrowd | 1075
# # Remainder 2
# N = int(input('enter a number: '))
# # Iterate from 1 up to 10000 (inclusive)
# # range(start, stop) goes up to stop-1, so we use 10001 for the stop value.
# for i in range(1, 40):
#     if i % N == 2:
#         print(i)

# beecrowd | 1078
# # Multiplication Table
# n = int(input("enter a number: "))
# for i in range(2,10):
#     s = n * i
#     print(f"{i} x {n} = {s}")



# beecrowd | 1079
# # Weighted Average
# n = int(input("enter a number: "))
# for i in range(n):
#     a,b,c = map(float,input().split())
#     weighted_average =(a * 2 + b *3 + c * 5)
#     weighted_average /= 10
#     print(f"{weighted_average:.1f}")

# beecrowd | 1080
# n = int(input("enter a number: "))
# max_value = 0
# for i in range(n):
#     current_number = int(input())
#     if current_number > max_value:
#         max_value = current_number
#         print(f"max_value: {max_value}")
# print(max_value)
# Read the first number to initialize
# highest_value = int(input())
# position_of_highest = 1 # The first number is at position 1

# # Loop 99 more times to read the remaining numbers (from 2nd to 100th)
# # The current_position will range from 2 to 100
# for current_position in range(2, 101): # range(2, 101) gives 2, 3, ..., 100
#     current_number = int(input())
    
#     if current_number > highest_value:
#         highest_value = current_number
#         position_of_highest = current_position

# # Print the results
# print(highest_value)
# print(position_of_highest)


# beecrowd | 1081
# Experiment

# n = int(input("enter a number: "))
# animal_a = 0
# animal_b = 0
# animal_c = 0

# for i in range(n):
#     animal = input("enter a animal: ")
#     quantity = int(input("enter a quantity: "))
#     if animal == "c":
#         animal_a += quantity
#     elif animal == "r":
#         animal_b += quantity
#     elif animal == "s":
#         animal_c += quantity
#     else:
#         print("Invalid animal type")
#         continue

# print(f"Total number of cats: {animal_a}")
# print(f"Total number of rats: {animal_b}")
# print(f"Total number of frogs: {animal_c}")
# print(f"Total number of animals: {animal_a + animal_b + animal_c}")
# print(f"Percentage of cats: {animal_a / (animal_a + animal_b + animal_c) * 100:.2f} %")
# print(f"Percentage of rats: {animal_b / (animal_a + animal_b + animal_c) * 100:.2f} %")
# print(f"Percentage of frogs: {animal_c / (animal_a + animal_b + animal_c) * 100:.2f} %")

# beecrowd | 1095
# # Sequence I
# j = 0
# for i in range(1, 80, 3):
#     print(f"I={i} J={60 - j}")
#     j +=5

# i =1
# j = 60
# while j >= 0:
#     print(f"I={i} J={j}")
#     i += 3
#     j -= 5

# beecrowd | 1096
# # Sequence II
# Outer loop for I: values are 1, 3, 5, 7, 9
# range(start, stop, step)
# for i_val in range(1, 10, 2): # Generates 1, 3, 5, 7, 9
#     # Inner loop for J: values are 7, 6, 5
#     # range(start, stop, step) where stop is exclusive
#     for j_val in range(7, 4, -1): # Generates 7, 6, 5
#         print(f"I={i_val} J={j_val}")

# beecrowd | 1097
# # Sequence III

# # Outer loop for I: values are 1, 3, 5, 7, 9
# # range(start, stop, step)
# for i_val in range(1, 10, 2): # Generates 1, 3, 5, 7, 9
    
#     # Determine the starting J value for the current i_val
#     j_start = i_val + 6
    
#     # Inner loop for J: J takes 3 values: j_start, j_start-1, j_start-2
#     # We can loop 3 times or use a range that counts down
#     for k in range(3): # k will be 0, 1, 2
#         j_val = j_start - k
#         print(f"I={i_val} J={j_val}")

# # Alternative for inner loop:
# # for i_val in range(1, 10, 2):
# #     j_start = i_val + 6
# #     for j_val in range(j_start, j_start - 3, -1): # Generates j_start, j_start-1, j_start-2
# #         print(f"I={i_val} J={j_val}")

# beecrowd | 1098
# # Sequence IV
# i = 0.0
# j = 1.0
# # Outer loop for I: values are 0.0, 0.2, 0.4, ..., 2.0
# # range(start, stop, step)
# my attempt

# for i in range(0, 2.0, 0.2):
#     for j in range(1, 4):
#         print(f"I={i:.1f} J={j + i:.1f}")


# for step in range(11):  # From 0 to 10 inclusive → 11 steps of 0.2
#     i = step * 0.2
#     for j in range(1, 4):
#         print(f"I={i:.1f} J={i + j:.1f}")


# import decimal # For more precise arithmetic if needed, but let's try without first

# # Outer loop for I's progression
# # i_counter goes from 0 to 10.
# # I = i_counter / 5.0  (which is i_counter * 0.2)
# for i_counter in range(11): # 0, 1, ..., 10
#     i_float = i_counter / 5.0 
#     # Example: i_counter=0 -> i_float=0.0
#     #          i_counter=1 -> i_float=0.2
#     #          i_counter=5 -> i_float=1.0
#     #          i_counter=10 -> i_float=2.0

#     # Inner loop for J's progression (J = I+1, I+2, I+3)
#     for j_offset in range(1, 4): # j_offset will be 1, 2, 3
#         j_float = i_float + j_offset
        
#         # Format I for printing
#         # float.is_integer() is a good way to check if a float has no fractional part
#         if i_float.is_integer():
#             i_str = str(int(i_float))
#         else:
#             i_str = f"{i_float:.1f}" # Or str(round(i_float, 1)) but .1f is better for formatting

#         # Format J for printing
#         if j_float.is_integer():
#             j_str = str(int(j_float))
#         else:
#             j_str = f"{j_float:.1f}"

#         print(f"I={i_str} J={j_str}")


# beecrowd | 1099
# # Sum of Consecutive Odd Numbers II
# my attempt
# n = int(input("enter a number: "))
# a,b = map(int,input("enter a and b ").split())
# sum_of_consecutive_odds = 0
# for i in range(n):
#     if a % 2 != 0 and b % 2 != 0:
#         print(f"a and b are odd: {a, b}")
#         sum_of_consecutive_odds += a + b
#         print(f"sum_of_consecutive_odds: {sum_of_consecutive_odds}")
#         a += 1
#         b -= 1
#     else:
#         print("a and b are not odd")
# print(sum_of_consecutive_odds)


# N = int(input()) # Read the number of test cases

# for _ in range(N):
#     # Read X and Y for the current test case
#     # Assume X and Y are space-separated on a single line
#     line_values = input().split()
#     X = int(line_values[0])
#     Y = int(line_values[1])
    
#     # Alternative using map:
#     # X, Y = map(int, input().split())

#     # Determine the smaller and larger values to define the range
#     lower_bound = min(X, Y)
#     upper_bound = max(X, Y)

#     current_sum_of_odds = 0

#     # Iterate through numbers strictly between lower_bound and upper_bound
#     # range(start, stop) goes from start up to stop-1.
#     # We need to iterate from lower_bound + 1 up to (but not including) upper_bound.
#     for number in range(lower_bound + 1, upper_bound):
#         # Check if the number is odd
#         if number % 2 != 0: # Python's % handles negative numbers correctly for this
#             current_sum_of_odds += number

#     # Print the sum for the current test case
#     print(current_sum_of_odds)


# beecrowd | 1101
# # Sequence of Numbers and Sum

# Input Sample	Output Sample
# 5 2
# 6 3
# 5 0

# 2 3 4 5 Sum=14
# 3 4 5 6 Sum=18
# my attempt
# n = int(input("enter a number: "))
# sum = 0
# a,b = map(int, input("enter a and b: ").split())
# start = min(a, b)
# end = max(a, b)
# for i in range(start, end+1):
#     sum += i
#     print(i, end=" ")
# print(f"Sum={sum}")

# while True:
#     try:
#         # Read M and N from a single line, space-separated
#         line_values = input().split()
#         M = int(line_values[0])
#         N = int(line_values[1])
#     except EOFError:
#         # This handles the case where input might end abruptly without the M<=0/N<=0 terminator.
#         # For Beecrowd, the problem usually guarantees the M<=0/N<=0 terminator.
#         break
#     except (ValueError, IndexError):
#         # This handles cases like empty lines or lines not containing two integers.
#         # Again, may not be strictly necessary if Beecrowd inputs are always well-formed
#         # until the M<=0 or N<=0 condition.
#         break # Or continue if you want to try reading next line

#     # Check the primary termination condition
#     if M <= 0 or N <= 0:
#         break

#     # Determine the smaller and larger values
#     if M < N:
#         min_val = M
#         max_val = N
#     else:
#         min_val = N
#         max_val = M
        
#     current_sum = 0
#     sequence_parts = [] # To store numbers as strings for the sequence output

#     # Iterate from min_val to max_val (inclusive)
#     for i in range(min_val, max_val + 1):
#         sequence_parts.append(str(i)) # Add the number (as a string) to the list
#         current_sum += i             # Add the number to the sum
        
#     # Join the sequence parts with spaces to form the sequence string
#     sequence_str = " ".join(sequence_parts)
    
#     # Print the sequence and the sum in the required format
    # print(f"{sequence_str} Sum={current_sum}")


# beecrowd | 1113
# #Ascending and Descending
# my attempt
# a, b = map(int, input("enter a and b: ").split())
# if a < b :
#     print("CRESCENTE")
# else:
#     print("DECRESCENTE")

# while True:
#     try:
#         # Read X and Y from a single line, space-separated
#         line_values = input().split()
#         X = int(line_values[0])
#         Y = int(line_values[1])
#     except EOFError: 
#         # Handle potential end of input if not terminated by X==Y
#         # Though problem specifies X==Y as the terminator.
#         break
#     except (ValueError, IndexError):
#         # Handle malformed lines, if necessary
#         break 

#     # Check termination condition
#     if X == Y:
#         break

#     # Determine order and print
#     if X < Y:
#         print("Crescente")
#     else: # X > Y, because X == Y was handled by the break
#         print("Decrescente")

# beecrowd | 1114
# # Password
# # my attempt
# while True:
#     password = int(input("write password"))
#     if password == 2002:
#         print("Acesso Permitido")
#         break
#     else:
#         print("Senha Invalida")


# while True:
#     try:
#         attempted_password = int(input("write password: "))
#     except EOFError:
#         break
#     if attempted_password == 2002:
#         print("Acesso Permitido")
#         break
#     else:
#         print("Senha Invalida")


# beecrowd | 1115
# # Quadrant
# my Attempt
# while True:
#     x,y = map(float, input("enter x and y: ").split())
#     if x == 0.0 and y == 0.0:
#         break
#     elif x > 0.0 and y >0.0:
#         print("Q1")
#     elif x < 0.0 and y >0.0:
#         print("Q2")
#     elif x < 0.0 and y < 0.0:
#         print("Q3")
#     elif x > 0.0 and y < 0.0:
#         print("Q4")

# while True:
#     try:
#         # Read X and Y from a single line, space-separated
#         line_values = input().split()
#         X = int(line_values[0])
#         Y = int(line_values[1])
#     except EOFError:
#         # Handle potential end of input if not terminated by X/Y==0
#         break
#     except (ValueError, IndexError):
#         # Handle malformed lines, if necessary (e.g., empty line at end)
#         # For this problem, X=0 or Y=0 is the defined terminator.
#         break 

#     # Check termination condition
#     if X == 0 or Y == 0:
#         break

#     # Determine and print the quadrant
#     if X > 0 and Y > 0:
#         print("primeiro")
#     elif X < 0 and Y > 0:
#         print("segundo")
#     elif X < 0 and Y < 0:
#         print("terceiro")
#     elif X > 0 and Y < 0: # Could also be just 'else:' here
#         print("quarto")

# beecrowd | 1116
# # Divided x by y

# while True:
#     x,y = map(int, input().split())
#     if y == 0:
#         print("divisao impossivel")
#         break
#     else:
#         result = x / y
#         print(f"{result:.1f}")
# #     # Check termination condition

# N = int(input()) # Read the number of test cases

# for _ in range(N):
#     # Read X and Y for the current test case
#     # Assume X and Y are space-separated on a single line
#     line_values = input().split()
#     X = int(line_values[0])
#     Y = int(line_values[1])
    
#     # Alternative using map:
#     # X, Y = map(int, input().split())

#     # Check if the divisor Y is zero
#     if Y == 0:
#         print("divisao impossivel")
#     else:
#         # Perform float division
#         result = X / Y # In Python 3, this is float division
#         # result = float(X) / Y # Also works, more explicit
        
#         # Print the result formatted to one decimal place
#         print(f"{result:.1f}")

# beecrowd | 1117
# # Valid Score
# my attempt
# while True:
#     a,b = map(float, input("enter a and b: ").split())
#     if a < 0 or a > 10:
#         print("nota invalida")
#         continue
#     if b < 0 or b > 10:
#         print("nota invalida")
#         continue
#     average = (a+b) / 2
#     print(f"media = {average:.2f}")
#     break

# valid_scores_count = 0
# sum_of_valid_scores = 0.0

# while valid_scores_count < 2:
#     try:
#         score = float(input())
#     except EOFError:
#         # Should not happen if problem guarantees enough input to get 2 valid scores
#         break
#     except ValueError:
#         # Handle non-float input if necessary, though problem implies float inputs
#         print("nota invalida") # Treat malformed input as invalid
#         continue

#     if 0 <= score <= 10:
#         sum_of_valid_scores += score
#         valid_scores_count += 1
#     else:
#         print("nota invalida")

# # After the loop, we are guaranteed to have 2 valid scores
# average = sum_of_valid_scores / 2.0
# print(f"media = {average:.2f}")

# beecrowd | 1118
# # Valid Score II

# valid_score = 0
# sum = 0.0
# while valid_score < 2:
#     a = int(input("enter a number: "))
#     if a < 0 or a > 10:
#         print("nota invalida")
#     else:
#         valid_score += sum
#         valid_score+=1

# result = sum / 2.0
# if valid_score == 2:
#     print("media = {:.2f}".format(result))
# print(f"media = {result:.2f}")


# while True: # Main loop for new calculations
#     valid_scores_collected = 0
#     sum_of_valid_scores = 0.0

#     # Loop to get two valid scores
#     while valid_scores_collected < 2:
#         try:
#             score = float(input())
#         except EOFError: # Should not happen with specified termination
#             exit() # Or break all loops
#         except ValueError: # Handle non-float input
#             print("nota invalida")
#             continue
            
#         if 0 <= score <= 10:
#             sum_of_valid_scores += score
#             valid_scores_collected += 1
#         else:
#             print("nota invalida")
            
#     # Calculate and print the average for the two valid scores
#     average = sum_of_valid_scores / 2.0
#     print(f"media = {average:.2f}")

#     # Loop to get a valid option for "novo calculo"
#     while True:
#         print("novo calculo (1-sim 2-nao)")
#         try:
#             option_x = int(input())
#         except EOFError:
#             exit()
#         except ValueError:
#             # If input is not an integer, it's an invalid option, loop continues by default
#             # No specific error message for malformed option, just re-prompt.
#             continue 
            
#         if option_x == 1 or option_x == 2:
#             break # Valid option received, exit option loop
#         # If option is not 1 or 2, this option loop continues, re-printing the prompt
            
#     # Check if the main program should terminate
#     if option_x == 2:
#         break # Exit the main 'while True' loop for calculations
#     # If option_x == 1, the main loop continues for a new set of scores

# beecrowd | 1131
# # Grenais

# my attempt
# grenais_count = 0
# win_inter = 0
# win_gremio = 0
# draws = 0

# while True:
#     try:
#         inter, gremio = map(int,input("enter the scores: ").split())
#     except EOFError:
#         break
#     except (ValueError, IndexError):
#         print("Invalid input, please enter two integers.")
#         continue
#     grenais_count += 1
#     if inter > gremio:
#         win_inter += 1
#     elif gremio > inter:
#         win_gremio += 1
#     else:
#         draws += 1

#     print("Novo grenal (1-sim 2-nao)")
    

#     print(f"{grenais_count} grenais")
#     print(f"Inter: {win_inter}")
#     print(f"Gremio: {win_gremio}")
#     print(f"Empates: {draws}")
#     print(f"Inter venceu {win_inter} grenais.")
#     print(f"Gremio venceu {win_gremio} grenais.")
#     print(f"Empates: {draws}")
    
# Initialize statistics counters
# grenais_count = 0
# inter_wins = 0
# gremio_wins = 0
# draws = 0

# while True:
#     # Read goals for Inter and Gremio
#     # Assume they are space-separated on one line
#     try:
#         goals_input = input().split()
#         gols_inter = int(goals_input[0])
#         gols_gremio = int(goals_input[1])
#     except EOFError: # Should not happen based on problem structure
#         break
#     except (ValueError, IndexError): # For malformed goal input
#         # This case is unlikely for Beecrowd if format is fixed.
#         # If it happened, we might want to break or re-prompt, but problem implies clean input for goals.
#         continue 

#     # Update total Grenais
#     grenais_count += 1

#     # Determine winner and update stats
#     if gols_inter > gols_gremio:
#         inter_wins += 1
#     elif gols_gremio > gols_inter:
#         gremio_wins += 1
#     else: # It's a draw
#         draws += 1

#     # Ask if user wants another Grenal
#     print("Novo grenal (1-sim 2-nao)")
#     try:
#         option = int(input())
#     except EOFError: # If input ends unexpectedly
#         break
#     except ValueError: # If option is not an int
#         # Problem usually assumes valid 1 or 2. If not, could loop for valid option.
#         # For simplicity here, if option is malformed, we might just break.
#         # Or more robustly, loop until option is 1 or 2.
#         # For this problem, likely assume option input is clean.
#         break 


#     if option == 2:
#         break # Exit the main while loop
#     # If option == 1, the loop continues

# # After the loop, print the final statistics
# print(f"{grenais_count} grenais")
# print(f"Inter:{inter_wins}")
# print(f"Gremio:{gremio_wins}")
# print(f"Empates:{draws}")

# if inter_wins > gremio_wins:
#     print("Inter venceu mais")
# elif gremio_wins > inter_wins:
#     print("Gremio venceu mais")
# else:
#     print("Nao houve vencedor")


# while True:
#     summation = 0
#     try:
#         x, y = map(int, input("enter x and y: ").split())   
#     except EOFError:
#         break
#     except ValueError:
#         print("Invalid input, please enter two integers.")
#         continue
# you used while and and which is wrong becouse it would stop and terminate the loop
# you should use for to have a range between x and y

# #     while x % 13 != 0 and y % 13 != 0:
#         if x % 13 == 0:
#             print(f"{x} is a multiple of 13")
#         if y % 13 == 0:
#             print(f"{y} is a multiple of 13")
#         summation += x + y
#         print(f"Summation: {summation}")
#         x += 1
#         y -= 1
        

# while True:
#     try:
#         x, y = map(int, input("Enter x and y: ").split())
#     except EOFError:
#         break
#     except ValueError:
#         print("Invalid input, please enter two integers.")
#         continue

#     # Ensure x is less than y
#     if x > y:
#         x, y = y, x

#     summation = 0
#     for num in range(x, y + 1):
#         if num % 13 != 0:
#             print(f"{num} is not a multiple of 13")
#             summation += num
#             print("Summation: ", summation)

#     print(f"Summation: {summation}")


# beecrowd | 1132
# # Multiples of 5 to equal 3 and 2

# x,y = map(int, input("enter x and y: ").split())
# # Ensure x is less than y
# x = min(x, y)
# y = max(x, y)
# for i in range(x,y+1):
#     if i % 5 == 2 or i % 5 == 3:
#         print(i)

# Read the two integer values
# X = int(input())
# Y = int(input())

# # Determine the smaller and larger values to define the range
# lower_bound = min(X, Y)
# upper_bound = max(X, Y)

# # Iterate through numbers strictly between lower_bound and upper_bound,
# # in ascending order.
# # range(start, stop) goes from start up to stop-1.
# # We need to iterate from lower_bound + 1 up to (but not including) upper_bound.
# for number in range(lower_bound + 1, upper_bound):
#     remainder = number % 5
#     if remainder == 2 or remainder == 3:
#         print(number)


# beecrowd | 1134
# # Type of Fuel
# N = int(input()) # Read the number of lines

# current_start_number = 1

# for _ in range(N): # Loop N times for N lines of output
#     # The three numbers for the current line
#     num1 = current_start_number
#     num2 = current_start_number + 1
#     num3 = current_start_number + 2
    
#     # Print the line in the required format
#     print(f"{num1} {num2} {num3} PUM")
    
#     # Update current_start_number for the next line
#     # We printed 3 numbers, and PUM takes the place of the 4th.
#     # So, the next sequence starts 4 numbers after the current_start_number.
#     current_start_number += 4 



# beecrowd | 1135
# # PUM
# Initialize counters for each fuel type
# count_alcohol = 0
# count_gasoline = 0
# count_diesel = 0

# while True:
#     try:
#         code = int(input())
#     except EOFError:
#         # In case input stream ends before code 4, though problem implies code 4 will terminate
#         break
#     except ValueError:
#         # If input is not an integer, problem says "integer and positive values"
#         # but an invalid code (like a letter) might cause ValueError.
#         # The problem implies we just re-request if outside 1-4.
#         # So, if it's not an int, it's effectively an invalid code.
#         continue # Skips to the next iteration to read a new code

#     if code == 1:
#         count_alcohol += 1
#     elif code == 2:
#         count_gasoline += 1
#     elif code == 3:
#         count_diesel += 1
#     elif code == 4:
#         break # Exit the loop when code 4 is entered
#     # No 'else' needed here: if code is not 1, 2, 3, or 4,
#     # we just loop again to get the next input, as per "a new code must be requested".

# # After the loop terminates (due to code 4)
# print("MUITO OBRIGADO")
# print(f"Alcool: {count_alcohol}")
# print(f"Gasolina: {count_gasoline}")
# print(f"Diesel: {count_diesel}")

# N = int(input()) # Read the number of lines

# current_start_number = 1

# for _ in range(N): # Loop N times for N lines of output
#     # The three numbers for the current line
#     num1 = current_start_number
#     num2 = current_start_number + 1
#     num3 = current_start_number + 2
    
#     # Print the line in the required format
#     print(f"{num1} {num2} {num3} PUM")
    
#     # Update current_start_number for the next line
#     # We printed 3 numbers, and PUM takes the place of the 4th.
#     # So, the next sequence starts 4 numbers after the current_start_number.
#     current_start_number += 4 

# beecrowd | 1143
# Squared and Cubic
# n = int(input("enter a number: "))
# for i in range(1, n +1):
#     square = i ** 2
#     cube = i **3
#     print(f"{i} {square} {cube}")

# N = int(input()) # Read the number of lines

# # Loop from 1 to N (inclusive)
# # range(1, N + 1) will generate numbers 1, 2, ..., N
# for i in range(1, N + 1):
#     square = i * i   # or i**2
#     cube = i * i * i # or i**3 or square * i
    
#     # Print the number, its square, and its cube, separated by spaces
#     print(f"{i} {square} {cube}")

# beecrowd | 1144
# Logical Sequence

# N = int(input()) # Read the integer N

# # Loop from 1 to N (inclusive)
# # range(1, N + 1) will generate numbers 1, 2, ..., N
# for i in range(1, N + 1):
#     # Calculate square and cube for the current i
#     i_square = i * i   # or i**2
#     i_cube = i * i * i # or i**3
    
#     # Print the first line for the current i
#     print(f"{i} {i_square} {i_cube}")
    
#     # Print the second line for the current i
#     # It uses i, i_square + 1, and i_cube + 1
#     print(f"{i} {i_square + 1} {i_cube + 1}")

# beecrowd | 1145
# Logical Sequence II

# Read X and Y from a single line, space-separated
# line_input = input().split()
# X = int(line_input[0])
# Y = int(line_input[1])

# # Alternative using map:
# # X, Y = map(int, input().split())

# current_line_elements = []

# for i in range(1, Y + 1): # Loop from 1 to Y inclusive
#     current_line_elements.append(str(i)) # Add number as string

#     # Check if the line is full (X elements) OR if it's the very last number (i == Y)
#     if len(current_line_elements) == X or i == Y:
#         print(" ".join(current_line_elements)) # Print elements joined by space
#         current_line_elements = [] # Reset for the next line


# X, Y = map(int, input().split())

# for i in range(1, Y + 1):
#     if i % X == 0:
       
#         print(i)
#     else:
#         print(i, end=' ')





# beecrowd | 1145
# Logical Sequence II
# while True:
#     try:
#         X = int(input())
#     except EOFError: # Should not happen given X=0 is terminator
#         break
#     except ValueError: # If input is not an int
#         # Problem implies integer inputs. If X=0 is terminator, invalid format before that is unlikely.
#         break 

#     if X == 0:
#         break # Terminate if X is 0

#     # Build the sequence for the current X
#     sequence_parts = []
#     for i in range(1, X + 1): # Loop from 1 to X inclusive
#         sequence_parts.append(str(i))
#         print(sequence_parts)
#     # Join the parts with a space and print
#     # This inherently handles the no trailing space issue.
#     print(" ".join(sequence_parts))
    



# Read all integer values from the single input line
# input().split() creates a list of strings.
# map(int, ...) converts each string to an integer.
# list(...) converts the map object to a list.
all_input_numbers = list(map(int, input().split()))

A = all_input_numbers[0]
N = 0 # Initialize N

# Find the first positive N from the second element onwards
# We iterate starting from index 1 of all_input_numbers
for i in range(1, len(all_input_numbers)):
    potential_N = all_input_numbers[i]
    print("potential_N", potential_N)
    if potential_N > 0:
        N = potential_N
        break # Found the valid N, exit this loop

# Calculate the sum of N consecutive integers starting from A
total_sum = 0
for i in range(N): # This will loop N times, with i from 0 to N-1
    print("i",i)
    term = A + i
    print("term",term)
    total_sum += term
    print("total_sum",total_sum)

# Print the sum
print(total_sum)