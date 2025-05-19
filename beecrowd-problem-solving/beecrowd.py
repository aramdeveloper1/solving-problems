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