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
# # map(int, ...) converts each string to an integer.
# # list(...) converts the map object to a list.
# all_input_numbers = list(map(int, input().split()))

# A = all_input_numbers[0]
# N = 0 # Initialize N

# # Find the first positive N from the second element onwards
# # We iterate starting from index 1 of all_input_numbers
# for i in range(1, len(all_input_numbers)):
#     potential_N = all_input_numbers[i]
#     print("potential_N", potential_N)
#     if potential_N > 0:
#         N = potential_N
#         break # Found the valid N, exit this loop

# # Calculate the sum of N consecutive integers starting from A
# total_sum = 0
# for i in range(N): # This will loop N times, with i from 0 to N-1
#     print("i",i)
#     term = A + i
#     print("term",term)
#     total_sum += term
#     print("total_sum",total_sum)

# # Print the sum
# print(total_sum)

# Read the entire line of space-separated numbers
# and convert them into a list of integers.
# all_input_numbers = list(map(int, input().split()))
# print(all_input_numbers)
# # The first number in the list is always A.
# A = all_input_numbers[0]

# # Initialize N. We will find its value in the loop.
# N = 0

# # Loop through the rest of the list to find the first positive N.
# # We start iterating from the second element (index 1).
# for i in range(1, len(all_input_numbers)):
#     potential_N = all_input_numbers[i]
#     print("potential_N", potential_N)
#     if potential_N > 0:
#         N = potential_N
#         break # Exit the loop as soon as we find a valid N

# # Now that we have A and a valid N, calculate the sum.
# total_sum = 0
# for i in range(N): # This loop runs N times, with 'i' from 0 to N-1
#     # The term to add in each step is A + i
#     term = A + i
#     print("term", term)
#     total_sum += term
#     print("total_sum", total_sum)

# # Print the final calculated sum.
# print(total_sum)

# beecrowd | 1150
# Exceeding Z

# x = int(input("x :"))
# while True:
#     z = int(input("z :"))
#     if z > x:
#         break
    
# # print(f"Z is greater than X: {z} > {x}")

# total = 0
# count = 0
# current = x
# while total <= z:
#     total += current
#     print("total ", total)
#     current += 1
#     print("current ", current)
#     count += 1
#     print("count ", count)

# print(count)
# S = 0.0 # Initialize S as a float

# # Initialize the numerator and denominator for the first term
# numerator = 1.0
# denominator = 1.0

# # The numerator sequence is 1, 3, 5, ..., 39
# # We can loop using the numerator as the control variable
# while numerator <= 39:
#     term = numerator / denominator
#     S += term
    
#     # Update for the next term in the sequence
#     numerator += 2
#     denominator *= 2

# # Print the final sum formatted to 2 decimal places
# print(f"{S:.2f}")
# division = int(input("write "))
# for i in range(1, division + 1):
#     if 6 % i == 0:
#         print(i)
# beecrowd | 1158
# Sum of Consecutive Odd Numbers III
# my version which was wrong
# X = int(input())
# Y = int(input())
# arr_consecutive = []
# suma = 0
# for i in range(X, Y + 1):
#     if i % 2 != 0:
#         suma += i
#         arr_consecutive.append(i)
#         if sum(arr_consecutive) == Y:
#             break
# print(suma," ", arr_consecutive )

# T = int(input())

# for _ in range(T):
#     X, Y = map(int, input().split())
#     if X % 2 == 0:
#         print("x if is even ",X)
#         X += 1  # make X odd if it's even

#     total = 0
#     for i in range(Y):
#         print("i", i)
#         total += X + 2 * i  # add next Y odd numbers
#         print("total", total)
#     print(total)

# N = int(input())

# for _ in range(N):
#     X, Y = map(int, input().split())

#     start_number = 0
#     if X % 2 == 0:
#         start_number = X + 1
#     else:
#         start_number = X
        
#     current_sum = 0
#     current_odd = start_number
#     for _ in range(Y):
#         current_sum += current_odd
#         current_odd += 2
        
#     print(current_sum)



# Sum of Consecutive Even Numbers	 1159		
# x = int(input("Enter a number: "))
# if x % 2 == 0:
#     print("x is even")
# else:
#     x +=1

# attempt = x
# summation = 0
# for _ in range(attempt):
#     summation += x
#     x += 2

# print(summation)

# while True:
#     X = int(input())
#     if X == 0:
#         break

#     start_even = 0
#     if X % 2 == 0:
#         start_even = X
#     else:
#         start_even = X + 1
        
#     current_sum = 0
#     current_even = start_even
#     for _ in range(5):
#         current_sum += current_even
#         current_even += 2
        
#     print(current_sum)

# beecrowd | 1151
# Easy Fibonacci

# a = 0
# b = 1
# n = int(input("Enter a number: "))

# for i in range(n):
#     print("aaaa",a)
#     result = a + b
#     print("result, ", result)
#     a = b
#     print("a, ", a)
#     b = result
#     print("b",b)

# print("**** ,",result)

# Fibonacci sum: F0 + F1 + F2 + F3 + F4
# a = 0
# b = 1
# fib_sum = 0
# for i in range(5):
#     fib_sum += a
#     a, b = b, a + b
# print("Sum of first 5 Fibonacci numbers:", fib_sum)
# N = int(input())

# # Handle edge cases first
# if N == 1:
#     print("0")
# elif N == 2:
#     print("0 1")
# else: # N > 2
#     # Start with the first two numbers
#     fib_list = [0, 1]
    
#     # We already have 2 numbers, so we need to generate N-2 more.
#     for _ in range(N - 2):
#         # The next number is the sum of the last two in the list
#         next_fib = fib_list[-1] + fib_list[-2]
#         fib_list.append(next_fib)
        
#     # Convert all numbers to strings and join them for printing
#     print(" ".join(map(str, fib_list)))
# Read the integer N, which is the number of Fibonacci numbers to generate.
# N = int(input())

# # Initialize the first two Fibonacci numbers.
# # We'll use 'a' and 'b' to keep track of the two previous numbers.
# a, b = 0, 1

# # Create a list to store the sequence of numbers we generate.
# # This makes it easy to print with correct spacing at the end.
# fib_sequence = []

# # Loop N times to generate N numbers.
# for _ in range(N):
#     # Add the current number ('a') to our sequence list.
#     fib_sequence.append(a)
    
#     # Update the numbers for the next iteration.
#     # The new 'a' becomes the old 'b', and the new 'b' becomes the sum (a+b).
#     # This is a classic, elegant way to advance the Fibonacci sequence.
#     a, b = b, a + b

# # Convert all the integer numbers in our list to strings.
# # The .join() method requires a list of strings.
# fib_sequence_as_strings = [str(num) for num in fib_sequence]

# # Join the list of strings with a space separator and print the result.
# # This automatically handles the "no trailing space" requirement.
# print(" ".join(fib_sequence_as_strings))

# beecrowd | 1153
# Simple Factorial
# s = 1
# n = int(input("Enter a number: "))
# for i in range(1,n):
#     s*=i
# print("result , ",s)
# Read the integer N
# N = int(input())

# # Initialize the result for multiplication to 1.
# # This is crucial, as starting with 0 would always result in 0.
# factorial_result = 1

# # Loop from 1 to N (inclusive) to multiply all numbers in the range.
# # range(1, N + 1) generates the sequence of numbers 1, 2, 3, ..., N.
# for i in range(1, N + 1):
#     # In each step, multiply the current result by the loop number.
#     factorial_result = factorial_result * i
    
#     # A more concise way to write this is:
#     # factorial_result *= i

# # After the loop has finished, print the final calculated factorial.
# print(factorial_result)

# beecrowd | 1160
# Population Increase

# X, Y, Z = map(int, input().split())
# # X is the initial population of the first city

# beecrowd | 1173
# Array fill I
# N = int(input())
# array = [0] * 10
# print("array ", array)
# array[0] = N

# for i in range(1, 10):
#     array[i] = array[i - 1] * 2
#     print(f"array[{i}] = {array[i]}")
# for i in range(10):
#     print(f"X[{i}] = {array[i]}")


# # Read the initial integer value from the input.
# V = int(input())

# # This variable will hold the value for the current position in the array.
# # It's initialized with the input value V, which is the value for N[0].
# current_value = V

# # We need to generate and print 10 values for the array N[0] to N[9].
# # A for loop iterating 10 times is perfect for this.
# # The variable 'i' will represent the array index, from 0 to 9.
# for i in range(10):
#     # Print the value for the current position 'i' in the required format.
#     print(f"N[{i}] = {current_value}")
    
#     # Calculate the value for the next position by doubling the current one.
#     # This prepares the variable for the next iteration of the loop.
#     current_value = current_value * 2
#     # A more concise way to write this is:
#     # current_value *= 2


# beecrowd | 1174
# Array Selection I
# new_arr = []
# for i in range(10):
#     X = int(input())
#     new_arr.append(X)
#     print(f"X[{i}] = {X}")

# # Initialize an empty list to store the array elements
# A = []

# # Step 1: Read all 20 numbers into the list
# for _ in range(20):
#     try:
#         # Read a number, convert to float, and append to the list
#         number = float(input())
#         A.append(number)
#     except (ValueError, EOFError):
#         # Handle potential errors, e.g., break if input ends unexpectedly
#         break

# # Step 2: Iterate through the list and print elements that meet the condition
# for i in range(len(A)): # Use len(A) in case input ended early
#     # Check if the number at position i is less than or equal to 10
#     if A[i] <= 10:
#         # Print the index and the value formatted to one decimal place
#         print(f"A[{i}] = {A[i]:.1f}")



# beecrowd | 1175
# Array change I

# A=[]
# for i in range(5):
#     A.append(int(input("new num: ")))
# for j in range(-1,-6,-1):
#     print(f"A[{j}] = {A[j]}")
# Initialize an empty list
# N = []

# # Step 1: Read all 20 numbers into the list
# for _ in range(20):
#     num = int(input())
#     N.append(num)

# # Step 2: Reverse the list in-place
# # Loop from the start to the middle of the list.
# # For a list of 20, we loop for i = 0 to 9.
# for i in range(10): # range(10) gives 0, 1, ..., 9
#     # Python has a very elegant way to swap two variables
#     # N[i] becomes N[19-i] and N[19-i] becomes N[i] simultaneously
#     N[i], N[19 - i] = N[19 - i], N[i]

# # Step 3: Print the modified list
# for i in range(20):
#     print(f"N[{i}] = {N[i]}")


# beecrowd | 1176
# Fibonacci Array
# Read number of test cases
# T = int(input("Enter the number of test cases: "))

# # Precompute Fibonacci sequence up to Fib(60)
# fib = [0, 1]  # first two numbers
# for i in range(2, 10):
#     fib.append(fib[i-1] + fib[i-2])
#     print(f"Fib({i}) = {fib[i]}")

# # Process each test case
# for _ in range(T):
#     N = int(input("enter a number: "))
#     print(f"******* Fib({N}) = {fib[N]}")


# beecrowd | 1177
# Array Fill II


# # Read the integer T, which determines the length of the repeating cycle.
# T = int(input())

# # We need to generate and print 1000 lines for the array N[0] to N[999].
# # A for loop iterating from 0 to 999 is the perfect tool for this.
# # The variable 'i' will represent the array index.
# for i in range(10):
#     # The value at position 'i' is determined by the remainder of i divided by T.
#     # This creates the repeating cycle of 0, 1, 2, ..., T-1.
#     value = i % T
    
#     # Print the output for the current position in the required format.
#     print(f"N[{i}] = {value}")
    
# # beecrowd | 1178
# # Array Fill III
# # new_array = []
# # result = 1000

# # for i in range(10):
# #     result = result // 2
# #     new_array.append(result)
# #     print(f"A[{i}] = {result:.4f}")


# X = float(input("Enter a number: "))

# N = [0.0] * 100
# N[0] = X

# for i in range(1, 20):
#     N[i] = N[i - 1] / 2

# for i in range(100):
#     print(f"N[{i}] = {N[i]:.4f}")

# beecrowd | 1179
# Array IV

# par = []
# impar = []

# def print_array(arr, name):
#     for i, val in enumerate(arr):
#         print(f"{name}[{i}] = {val}")

# for _ in range(15):
#     num = int(input())
    
#     if num % 2 == 0:
#         par.append(num)
#         if len(par) == 5:
#             print_array(par, "par")
#             par.clear()
#     else:
#         impar.append(num)
#         if len(impar) == 5:
#             print_array(impar, "impar")
#             impar.clear()

# # Print remaining odd numbers first
# if len(impar) > 0:
#     print_array(impar, "impar")

# # Then print remaining even numbers
# if len(par) > 0:
#     print_array(par, "par")
# Helper function to print the contents of a list in the required format.
# It takes the name of the list (as a string) and the list itself.
# def print_list_contents(name, lst):
#     for i in range(len(lst)):
#         print(f"{name}[{i}] = {lst[i]}")

# # Initialize the two lists that will act as 5-element buffers.
# par = []
# impar = []

# # Loop 15 times to read all the integer inputs.
# for _ in range(15):
#     try:
#         num = int(input("Enter an integer: "))
#     except (ValueError, EOFError):
#         # This handles potential errors, though not expected by the problem spec.
#         continue

#     # Check if the number is even or odd and append to the correct list.
#     if num % 2 == 0:
#         par.append(num)
#     else:
#         impar.append(num)
        
#     # Check if the 'par' list is full. If so, print and clear it.
#     if len(par) == 5:
#         print_list_contents("par", par)
#         par = [] # Reset the list (buffer is now empty)
        
#     # Check if the 'impar' list is full. If so, print and clear it.
#     if len(impar) == 5:
#         print_list_contents("impar", impar)
#         impar = [] # Reset the list (buffer is now empty)

# # After the loop finishes, there might be leftover numbers in the lists.
# # Print the remaining items as specified by the problem: odd first, then even.
# print_list_contents("impar", impar)
# print_list_contents("par", par)


# lowest number and position

# N = int(input("Enter the number of elements: "))
# new_array = []
# for i in range(N):
#     num = int(input())
#     new_array.append(num)

# # Find the lowest number and its position
# lowest = min(new_array)
# position = new_array.index(lowest)

# print(f"Lowest number: {lowest}")
# print(f"Position: {position}")
# def maskEmail(email):
#     # Split the email into local and domain parts
#     local, domain = email.split("@")
#     # Mask the local part
#     masked_local = local[0] + "*****" + local[-1]
#     # Return the masked email
#     return masked_local + "@" + domain
# print(maskEmail("aramkhasro75@gmail.com "))


# Line in Array
# 1181
# L = int(input("Enter the line index: "))              # Line index
# T = input("Enter the operation type (S for sum, M for mean): ").strip()           # Operation type
# M = []                        # Matrix

# # Reading the 12x12 matrix
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(float(input("Enter value for M[{}][{}]: ".format(i, j))))
#     M.append(row)
# print("M ", M)

# # Select the row L
# line_values = M[L]

# # Compute result
# if T == 'S':
#     result = sum(line_values)
# elif T == 'M':
#     result = sum(line_values) / 12

# # Output with 1 decimal place
# print(f"{result:.1f}")
# beecrowd | 1182
# Column in Array
# column = int(input("Enter the column index: "))
# T = input("Enter the operation type (S for sum, M for mean): ").strip()           # Operation type
# M= []
# for i in range(4):
#     row = []
#     for j in range(4):
#         row.append(float(input("Enter value for M[{}][{}]: ".format(i, j))))
#     M.append(row)
# print("M ", M)
# column_values = []
# for i in range(len(M)):
#     column_values.append(M[i][column])

# if T == "S":
#     sum_column = sum(column_values)
#     print(f"Sum of column {column}: {sum_column}")
# elif T == "M":
#     mean_column = sum(column_values) / len(column_values) if column_values else 0
#     print(f"Mean of column {column}: {mean_column:.1f}")
# beecrowd | 1182
# Column in Array

# C = int(input())                 # Column index (0-11)
# T = input().strip()               # 'S' or 'M'

# M = []
# for i in range(12):
#     row = []
#     for j in range(12):
#         row.append(float(input()))
#     M.append(row)

# # Get all elements from column C (long form)
# column_values = []
# for i in range(len(M)):
#     value = M[i][C]
#     column_values.append(value)

# # Calculate result
# if T == 'S':
#     result = sum(column_values)
# elif T == 'M':
#     result = sum(column_values) / len(column_values)

# print(f"{result:.1f}")



# # above digonal
#             # Line index (0-11)
# T = input().strip()               # 'S' or 'M'
# M = []
# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(float(input("Enter value for M[{}][{}]: ".format(i, j))))
#     M.append(row)
# print("M ",M)
# # Get all elements from column C (long form)
        # total = 0.0
        # count = 0

        # for i in range(len(M)):
        #     for j in range(len(M)):
        #         if j>i:
        #             print("M[i][j] ",M[i][j])
        #             total += M[i][j]
        #             count += 1

        # # Calculate result
        # # Output
        # if T == 'S':
        #     result = total
        # elif T == 'M':
        #     result = total / count

        # print(f"{result:.1f}")


# above secondary diagonal
# beecrowd | 1185
# Above the Secondary Diagonal

# O = input().strip()  # Operation: 'S' or 'M'

# M = []
# for i in range(12):
#     row = []
#     for j in range(12):
#         row.append(float(input()))
#     M.append(row)

# total = 0.0
# count = 0

# for i in range(12):
#     for j in range(12):
#         if i + j < 11:  # Above secondary diagonal
#             total += M[i][j]
#             count += 1

# if O == 'S':
#     result = total
# else:  # O == 'M'
#     result = total / count

# print(f"{result:.1f}")


# beecrowd | 1186
# Below the Secondary Diagonal

# O = input().strip()  # 'S' or 'M'

# M = []
# for i in range(12):
#     row = []
#     for j in range(12):
#         row.append(float(input()))
#     M.append(row)

# total = 0.0
# count = 0

# for i in range(12):
#     for j in range(12):
#         if i + j > 11:  # Below secondary diagonal
#             total += M[i][j]
#             count += 1

# if O == 'S':
#     result = total
# else:  # O == 'M'
#     result = total / count

# print(f"{result:.1f}")










# beecrowd | 1187
# Top Area
# my attempt
# O = input().strip()  # 'S' or 'M'

# M = []
# for i in range(4):
#     row = []
#     for j in range(4):
#         row.append(float(input()))
#     M.append(row)
# print("M ",M)
# total = 0.0
# count = 0

# for i in range(2):
#     for j in range(i,4-i):
#         total += M[i][j]
#         print(f"M[{i}][{j}] = {M[i][j]}")
#         print(f"total = {total}")
#         count += 1

# if O == 'S':
#     result = total
# else:  # O == 'M'
#     result = total / count

# print(f"{result:.1f}")
# beecrowd | 1187
# Top Area

# O = input().strip()  # 'S' or 'M'
# M = []
# for i in range(4):
#     row = []
#     for j in range(4):
#         row.append(float(input()))
#     M.append(row)
# print("M ",M)
# total = 0.0
# count = 0

# for i in range(4):
#     for j in range(4):
#         if j > i and i + j < 3:  # Top area condition
#             total += M[i][j]
#             print(f"M[{i}][{j}] = {M[i][j]}")
#             print(f"total = {total}")
#             count += 1

# if O == 'S':
#     result = total
# else:  # O == 'M'
#     result = total / count

# print(f"{result:.1f}")


# |         | **j=0** | **j=1** | **j=2** | **j=3** | **j=4** |
# | ------- | ------- | ------- | ------- | ------- | ------- |
# | **i=0** | (0,0)   | (0,1)   | (0,2)   | (0,3)   | (0,4)   |
# | **i=1** | (1,0)   | (1,1)   | (1,2)   | (1,3)   | (1,4)   |
# | **i=2** | (2,0)   | (2,1)   | (2,2)   | (2,3)   | (2,4)   |
# | **i=3** | (3,0)   | (3,1)   | (3,2)   | (3,3)   | (3,4)   |
# | **i=4** | (4,0)   | (4,1)   | (4,2)   | (4,3)   | (4,4)   |

# Inferior Area
# beecrowd | 1187
# Top Area

# O = input().strip()  # 'S' or 'M'
# M = []
# for i in range(4):
#     row = []
#     for j in range(4):
#         row.append(float(input()))
#     M.append(row)
# print("M ",M)
# total = 0.0
# count = 0

# for i in range(4):
#     for j in range(4):
#         if i > j and i + j > 3:  # Top area condition
#             total += M[i][j]
#             print(f"M[{i}][{j}] = {M[i][j]}")
#             print(f"total = {total}")
#             count += 1

# if O == 'S':
#     result = total
# else:  # O == 'M'
#     result = total / count

# print(f"{result:.1f}")



# # left area
# O = input().strip()  # 'S' or 'M'
# M = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(float(input("enter a number: ")))
#     M.append(row)
# print("M ",M)

# total = 0.0
# count = 0

# for i in range(5):
#     for j in range(5):
#         if i > j and  j < 4 -i:  # Top area condition
#             total += M[i][j]
#             print(f"M[{i}][{j}] = {M[i][j]}")
#             print(f"total = {total}")
#             count += 1

# if O == 'S':
#     result = total
# else:  # O == 'M'
#     result = total / count

# print(f"{result:.1f}")

# right area 

# O = input().strip()  # 'S' or 'M'
# M = []
# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(float(input("enter a number: ")))
#     M.append(row)
# print("M ",M)

# total = 0.0
# count = 0

# for i in range(5):
#     for j in range(5):
#         if i < j and  i < 4 -j:  # Top area condition
#             total += M[i][j]
#             print(f"M[{i}][{j}] = {M[i][j]}")
#             print(f"total = {total}")
#             count += 1

# if O == 'S':
#     result = total
# else:  # O == 'M'
#     result = total / count

# print(f"{result:.1f}")

# O = input().strip()
# M = [[float(input()) for _ in range(12)] for _ in range(12)]

# total = 0.0
# count = 0

# for i in range(12):
#     for j in range(12):
#         if j > i and j > 11 - i:
#             total += M[i][j]
#             count += 1

# if O == 'S':
#     print(f"{total:.1f}")
# else:  # 'M'
#     print(f"{total / count:.1f}")



# beecrowd | 1435
# Square Matrix I

# while True:
#     N = int(input("Enter N: "))
#     if N == 0:
#         break
    
#     M = [[0] * N for _ in range(N)]
#     print("<Matrix> ", M)
#     for i in range(N):
#         for j in range(N):
#             # distance from top, bottom, left, right edges
#             top = i
#             print("Top: ", top)
#             left = j
#             print("Left: ", left)
#             bottom = N - 1 - i
#             print("Bottom: ", bottom)
#             right = N - 1 - j
#             print("Right: ", right)
            
#             # layer number is min distance + 1
#             M[i][j] = min(top, left, bottom, right) + 1
#             print(f"M[{i}][{j}] ",min(top, left, bottom, right) + 1)
#     # printing in required format
#     for row in M:
#         print(" ".join(f"{num:3d}" for num in row))
#     print()



# while True:
#     M = []
#     N = int(input("Enter N: "))
#     for i in range(N):
#         row = []
#         for j in range(N):
#             row.append(abs(i-j) + 1)
#         M.append(row)
#     for row in M:
#         print(" ".join(f"{num:3d}" for num in row))
#     print()



# while True:
#     try:
#         # Read N. The loop will break when input() raises an EOFError.
#         N = int(input())
#     except EOFError:
#         break # Exit the loop at the end of the file

#     # Outer loop for rows (i)
#     for i in range(N):
#         current_row = [] # A list to build the parts of the row
#         # Inner loop for columns (j)
#         for j in range(N):
#             # Apply the rules to determine the value
#             if i == j:
#                 # Main diagonal
#                 current_row.append('1')
#             elif (i + j) == (N - 1):
#                 # Secondary diagonal
#                 current_row.append('2')
#             else:
#                 # Everything else
#                 current_row.append('3')
        
#         # Join the parts of the row into a single string and print
#         print("".join(current_row))


# import math
# while True:
#     values = input().split()
#     A = int(values[0])
#     if A == 0:  # stop condition
#         break
#     B = int(values[1])
#     C = int(values[2])
#     print("A, B, C: ", A, B, C)
#     house_area = A * B
#     print("House Area: ", house_area)
#     land_area = (house_area * 100) / C
#     print("Land Area: ", land_area)
#     side = int(math.sqrt(land_area))  # truncate
#     print(side)
# while True:
#     values = int(input())
#     if values == 0:
#         print("there would be no a world cup")
#     else:
#         print("there would be a world cup")



# import sys

# for line in sys.stdin:  # read until EOF
#     n = int(line.strip())
#     if n == 0:
#         print("vai ter copa!")
#     else:
#         print("vai ter duas!")


# beecrowd | 1589
# Bob Conduit
# N = int(input())
# for i in range(N):
#     a, b = map(int, input().split())
#     area = a + b


#
# t = int(input())  # number of test cases
# for _ in range(t):
#     r1, r2 = map(int, input().split())
#     print(r1 + r2)



# beecrowd | 1759
# Ho Ho Ho
# t = int(input())
# st = ""
# for i in range(t):
#     st+="HO "
#     print(st, "!")

# words = ["apple", "banana", "cherry"]
# result = ", ".join(words)  # join with comma and space
# print(result)






# # beecrowd the race of slugs 1789
# t = int(input(" test cases: "))
# result = 0
# for i in range(t):
#     level = int(input("level: "))
#     result += level
# print("result: ", result)
# result = result / t
# print("average: ", result)
# if result < 10:
#     print("you are in level 1")
# elif result < 20 and result >= 10:
#     print("you are in level 2")
# else:
#     print("you are in level 3")


# import sys

# for line in sys.stdin:  # read until EOF
#     L = int(line.strip("write L "))
#     print("L ", L)
#     speed = list(map(int, sys.stdin.readline().split()))
#     print("Speed: ", speed)
#     fastest = max(speed)
#     if fastest < 10:
#         print(1)
#     elif fastest < 20:
#         print(2)
#     else:
#         print(3)







# beecrowd | 1827
# Square Array IV

# Input Sample	Output Sample
# 5
# 11

# 20003
# 01110
# 01410
# 01110
# 30002

# 20000000003
# 02000000030
# 00200000300
# 00011111000
# 00011111000
# 00011411000
# 00011111000
# 00011111000
# 00300000200
# 03000000020
# 30000000002

# import sys

# for line in sys.stdin:
#     n = int(line.strip())

#     # step 1: make matrix of 0's
#     matrix = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append(0)
#         matrix.append(row)

#     # step 2: inner square with 1's
#     start = n // 3
#     end = n - start
#     i = start
#     while i < end:
#         j = start
#         while j < end:
#             matrix[i][j] = 1
#             j += 1
#         i += 1

#     # step 3: main diagonal with 2's
#     i = 0
#     while i < n:
#         matrix[i][i] = 2
#         i += 1

#     # step 4: secondary diagonal with 3's
#     i = 0
#     while i < n:
#         j = n - 1 - i
#         matrix[i][j] = 3
#         i += 1

#     # step 5: center = 4
#     center = n // 2
#     matrix[center][center] = 4

#     # step 6: print
#     i = 0
#     while i < n:
#         row_as_string = ""
#         j = 0
#         while j < n:
#             row_as_string += str(matrix[i][j])
#             j += 1
#         print(row_as_string)
#         i += 1
#     print()



# beecrowd | 1828
# Bazinga!

# beecrowd 1873 - Pedra, Papel, Tesoura, Lagarto, Spock
# import sys

# # Winning relationships (Sheldon beats Raj if (Sheldon, Raj) is in this set)
# win_cases = {
#     ("tesoura", "papel"),
#     ("papel", "pedra"),
#     ("pedra", "lagarto"),
#     ("lagarto", "Spock"),
#     ("Spock", "tesoura"),
#     ("tesoura", "lagarto"),
#     ("lagarto", "papel"),
#     ("papel", "Spock"),
#     ("Spock", "pedra"),
#     ("pedra", "tesoura"),
# }

# T = int(sys.stdin.readline().strip())

# for case in range(1, T + 1):
#     sheldon, raj = sys.stdin.readline().split()
#     print(f"{sheldon} , {raj}")

#     if sheldon == raj:
#         result = "De novo!"
#     elif (sheldon, raj) in win_cases:
#         result = "Bazinga!"
#     else:
#         result = "Raj trapaceou!"

#     print(f"Caso #{case}: {result}")
# import sys 
# win_cases  = {
#     ("bard","maqas"),
#     ("bard","asn"),
#     ("bard","hawa")
# }
# T = int(input())
# for case in range(1, T + 1):
#     sheldon, raj = sys.stdin.readline().split()
#     if sheldon == raj:
#         result = "de novo"
#     elif (sheldon, raj) in win_cases:
#         result = "bazinga"
#     else:
#         result = "raj trapaceou"
#     print(f"caso #{case}: {result}")

    # # Winning relationships (Sheldon beats Raj if (Sheldon, Raj) is in this set)
    # win_cases = {
    #     ("tesoura", "papel"),
    #     ("papel", "pedra"),
    #     ("pedra", "lagarto"),
    #     ("lagarto", "Spock"),
    #     ("Spock", "tesoura"),
    #     ("tesoura", "lagarto"),
    #     ("lagarto", "papel"),
    #     ("papel", "Spock"),
    #     ("Spock", "pedra"),
    #     ("pedra", "tesoura"),
    # }

    # T = int(input())
    # for case in range(1, T + 1):
    # sheldon, raj = input().split()
    # print(f"{sheldon} , {raj}")
    # if sheldon == raj:
    #     result = "De novo!"
    # elif (sheldon, raj) in win_cases:
    #     result = "Bazinga!"
    # else:
    #     result = "Raj trapaceou!"
    # print(f"Caso #{case}: {result}")


# beecrowd | 1837
# Preface

# a = b × q + r
# Input Samples	|   Output Samples
# 7 3	            2 1
# this is not accepted if we have negative number
# T = int(input("Enter number of test cases: "))
# for i in range(T):
#     a, b = map(int, input("Enter values for a and b: ").split())
#     q = a // b
#     r = a % b
#     print(f"{q} {r}")


# try:
#     a, b = map(int, input().split())
# except (ValueError, EOFError):
#     # Handle end of file or bad input
#     exit()

# # Python's default operators behave differently for negative divisors.
# # For a positive divisor `b`, Python's `//` and `%` already follow Euclidean rules.
# # For a negative divisor `b`, they do not, `r` will be negative.
# # So we only need to correct for the case where b is negative.

# q = 0
# r = 0

# if b < 0:
    # We need to find q, r such that a = b*q + r and 0 <= r < abs(b)
    # Let's use a formula that works for both positive and negative `a`
    # We search for the correct q. The standard quotient is a/b.
    # The Euclidean quotient `q` is either floor(a/b) or ceil(a/b).
    # Let's test them. A simpler way is to find a correct `r` first.
    
    # abs_b = abs(b)
    # r = a % abs_b
    # This formula above is not quite right for negative `a`.
    # Let's stick to the correction method. It's the most reliable.
    
#     q_initial = a // b
#     print("**** q_initial ", q_initial)
#     r_initial = a % b
#     print("**** r_initial ", r_initial)
    
#     if r_initial < 0:
#         r = r_initial + abs(b)
#         print("r r_initial < 0", r)
#         q = q_initial + 1 # Because b is negative
#         print("q ", q)
#     else: # This happens if a is a perfect multiple of b
#         r = r_initial
#         print("r r_initial > 0", r)
#         q = q_initial
#         print("q initial", q)
# else: # b > 0 (b cannot be 0 as per Euclidean Division Theorem)
#     # Python's operators work correctly for positive divisors
#     q = a // b
#     r = a % b
    
# print(f"{q} {r}")

# A, B, C = map(int, input().split())
# print(A, B, C)
# if A > B and B <= C:
#     print(":)")
# elif A < B and B >= C:
#     print(":(")
# elif A < B and B < C:
#     # strictly increasing twice
#     if (C - B) >= (B - A):
#         print(":)")
#     else:
#         print(":(")
# elif A > B and B > C:
#     # strictly decreasing twice
#     if (B - C) < (A - B):
#         print(":)")
#     else:
#         print(":(")
# else:
#     # A == B
#     if C > B:
#         print(":)")
#     else:
#         print(":(")
# import sys 
# dash = 0
# arstrick = 0
# for i in sys.stdin.readline():
#     if i == "-":
#         dash += 1
#     elif i == "*":
#         arstrick += 1
#         print("arstrick:", arstrick)
#     else:
#         print("write again")

# import sys
# total = 0
# scream = 0
# for line in sys.stdin:
#     s = line.strip()
#     print("s:", s)
#     if not s:
#         continue
#     if s == "cow cow":
#         scream+=1
#         total = 0
#         if scream == 3:
#             break
#     else:
#         bits = s.replace("*", "1").replace("-", "0")
#         print("bits:", bits)
#         total += int(bits, 2)
#         print("total:", total)


# bits = "10100101"
# total = 0
# total += int(bits, 2)
# print(total)  # Output: 169


# solution A
# N = int(input().strip())
# print("N ", N)
# T = list(map(int, input().split()))
# print("T ", T)
# best_index = 1
# best_value = T[0]
# for i in range(2, N + 1):  # i goes 2..N (1-based)
#     if T[i-1] < best_value:
#         best_value = T[i-1]
#         best_index = i
#         print("best_index: ", best_index)
#         print("best_value: ", best_value)
# best_index = 1
# best_value = T[0]

# for i in range(2, N+1):            # i goes 2..N (1-based)
#     if T[i-1] < best_value:        # T[i-1] is the i-th person's hits
#         best_value = T[i-1]
#         print("best_value: ", best_value)
#         best_index = i
#         print("best_index: ", best_index)

# print(best_index)


# beecrowd | 1864
# Our Days Are Never Coming Back
# T = int(input("how many letters do you want to add"))
# message = "So, have you liked the Winter School this year? In order to make this School happen, many have worked, whether in writing the problems, in configuring the Portal, in making the arrengements for the event or in raising the funds. Our special acknowledgement this year goes to Professor Ricardo Oliveira, who has not only accepted our invitation to come and teach the workshops but has also been participating on the organisation of this School. We are sure that his experience and his career at ICPC as contestant and as coach have motived and inspired us all."
# letter = ""
# for i in range(T):
#     letter += message[i] 
# print(letter)

# beecrowd | 1865
# Mjölnir
# N = int(input("Enter the value of N: "))
# for i in range(N):
#     # print(" " * (N - i - 1) + "*" * (2 * i + 1))
#     name, power = input().split()
#     print(f"{name} {power}")
#     if name == "Thor":
#         print("Mjölnir")
#     else:
#         print("No")
# C = int(input().strip())

# for _ in range(C):
#     name, force = input().split()
#     force = int(force)  # not actually used, but read anyway
#     if name == "Thor":
#         print("Y")
#     else:
#         print("N")




# beecrowd | 1866
# Bill
# n = int(input())
# sum = 0
# for i in range(n):
#     test = int(input())
#     if test % 2 == 0:
#         test = 0
#     else:
#         test = 1
#     sum += test
# print(sum)

# C = int(input().strip())

# for _ in range(C):
#     N = int(input().strip())
#     if N % 2 == 0:
#         print(0)
#     else:
#         print(1)






# # beecrowd 1914
# # Read the number of test cases
# try:
#     QT = int(input("Enter the number of test cases: "))
# except (ValueError, EOFError):
#     QT = 0

# for _ in range(QT):
#     try:
#         # Read the first line for the current test case
#         player_info = input("Enter the player information: ").split()
#         player1_name = player_info[0]
#         player1_choice = player_info[1]
#         player2_name = player_info[2]
#         player2_choice = player_info[3]
        
#         # Read the second line for the current test case
#         numbers_chosen = input("number chosen").split()
#         N = int(numbers_chosen[0])
#         M = int(numbers_chosen[1])
#     except (ValueError, EOFError, IndexError):
#         # Skip malformed test cases
#         continue

#     # Calculate the sum
#     total_sum = N + M
#     print("total sum:", total_sum)
#     # Determine the outcome (even or odd)
#     if total_sum % 2 == 0:
#         # Sum is EVEN, the player who chose "PAR" wins
#         if player1_choice == "PAR":
#             print(player1_name)
#         else: # Player 2 must have chosen "PAR"
#             print(player2_name)
#     else: # total_sum % 2 != 0
#         # Sum is ODD, the player who chose "IMPAR" wins
#         if player1_choice == "IMPAR":
#             print(player1_name)
#         else: # Player 2 must have chosen "IMPAR"
#             print(player2_name)


# Read the four integers from a single line
# input().split() creates a list of strings
# map(int, ...) converts each string to an integer
# try:
#     T1, T2, T3, T4 = map(int, input().split())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     exit()

# # The total number of outlets provided by all strips
# total_outlets = T1 + T2 + T3 + T4

# # To connect the 4 strips in a chain, we use up 3 outlets.
# # (Strip 1 uses the wall socket. Strip 2 uses an outlet on Strip 1.
# # Strip 3 uses an outlet on Strip 2. Strip 4 uses an outlet on Strip 3).
# # The net result is the sum of all outlets minus 3.
# sockets_for_devices = total_outlets - 3

# # Print the final result
# print(sockets_for_devices)

# beecrowd | 1957
# Converting to Hexadecimal
# hexa = {
#     0: "0",
#     1: "1",
#     2: "2",
#     3: "3",
#     4: "4",
#     5: "5",
#     6: "6",
#     7: "7",
#     8: "8",
#     9: "9",
#     10: "A",
#     11: "B",
#     12: "C",
#     13: "D",
#     14: "E",
#     15: "F"
# }
# def decimal_to_hexa(n):
#     new_n = n.split(".")
#     for i in range(len(new_n)):
#         new_n[i] = hexa[int(new_n[i])]
#     return "".join(new_n)
# print(decimal_to_hexa("14.12.13.11"))

# digits = "0123456789ABCDEF"
# V = int(input().strip())
# print("V: ", V)
# if V == 0:
#     print("0")
# else:
#     out = []
#     while V > 0:
#         r = V % 16
#         print("r: ", r)
#         out.append(digits[r])
#         print("out: ", out)
#         V //= 16
#         print("V after //= 16: ", V)
#     print("".join(reversed(out)))

# finding polygon
# Read input
# N, L = map(int, input().split())

# # Calculate perimeter
# P = N * L

# # Print result
# print(P)
# beecrowd | 1960
# Roman Numerals for Page Numbers
# roman_numbers = {
#     1: "I",
#     5: "V",
#     10: "X",
#     50: "L",
#     100: "C",
#     500: "D",
#     1000: "M",
# }
# num = int(input("Enter a number: "))
# print(num)
# roman = ""
# for value in [1000,500,100,50,10,5,1]:
#     while num >= value:
#         num -= value
#         roman += roman_numbers[value]
# print(roman)



# P, N = map(int, input().split())
# print("P ",P, " N ", N)
# pipes = list(map(int, input().split()))
# print("pipes: ", pipes)
# win = True
# for i in range(1, N):
#     if abs(pipes[i] - pipes[i-1]) > P:
#         print("abs: ", abs(pipes[i] - pipes[i-1]))
#         win = False
#         break

# if win:
#     print("YOU WIN")
# else:
#     print("GAME OVER")



# 1963		The Motion Picture
# Read N, the number of test cases
# try:
#     N = int(input())
# except (ValueError, EOFError):
#     N = 0

# REFERENCE_YEAR = 2015

# for _ in range(N):
#     try:
#         T = int(input()) # Years that have passed
#     except (ValueError, EOFError):
#         continue # Skip this test case if input is bad

#     # Calculate the difference from the reference year
#     year_diff = REFERENCE_YEAR - T
    
#     if year_diff > 0:
#         # If the result is positive, it's an A.D. year
#         print(f"{year_diff} D.C.")
#     else: # year_diff is 0 or negative, so it's a B.C. year
#         # The year before 1 A.D. is 1 B.C.
#         # year_diff = 0 corresponds to 1 B.C.
#         # year_diff = -1 corresponds to 2 B.C.
#         # So the formula is abs(year_diff) + 1
#         bc_year = abs(year_diff) + 1
#         print(f"{bc_year} A.C.")
# reference = 2025
# n = int(input())
# for i in range(n):
#     test = input()
#     year_diff = reference - int(test)
#     if year_diff > 0:
#         print(f"{year_diff} D.C.")
#     else:
#         bc_year = abs(year_diff) + 1
#         print(f"{bc_year} A.C.")


# try:
#     # Read A (old price) and B (new price) from a single line
#     # map(float, ...) converts the split strings to floats
#     A, B = map(float, input().split())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     exit()

# # Formula for percentage increase: ((New - Old) / Old) * 100
# increase_amount = B - A
# percentage_increase = (increase_amount / A) * 100

# # Print the result formatted to two decimal places, followed by the '%' symbol
# print(f"{percentage_increase:.2f}%")


# beecrowd | 1983
# The Chosen
# Read the number of students
# n = int(input())

# # Initialize variables to track the best student and their grade
# max_note = -1.0
# best_student_reg = -1

# # Loop through each student to find the one with the highest grade
# for _ in range(n):
#     # Read the registration number and grade as a single line
#     reg, note = input().split()
    
#     # Convert reg to an integer and note to a float
#     reg = int(reg)
#     note = float(note)
    
#     # Check if the current student's grade is the highest found so far
#     if note > max_note:
#         max_note = note
#         best_student_reg = reg

# # Check if the highest grade meets the minimum requirement
# if max_note >= 8.0:
#     print(best_student_reg)
# else:
#     print("Minimum note not reached")



# beecrowd | 1984
# The Pronalância Puzzle

# n = input()
# for _ in range(len(n)):
#     new_n = n[::-1]
# print(new_n)
# n = input().strip()  # read as string
# print(n[::-1])       # reverse using slicing


# MacPRONALTS ={
#     1001 :1.50,
#     1002 : 2.50,
#     1003 : 3.50,
#     1004 : 4.50,
#     1005 : 5.50
# }
# n = int(input())
# for i in range(n):
#     details,num = input().split()
#     num = int(num)
#     details = int(details)
#     price = MacPRONALTS[num]
#     new_price = price * details
#     print(f"Total: R$ {new_price:.2f}")

# Create a dictionary to store the menu prices
# menu = {
#     1001: 1.50,
#     1002: 2.50,
#     1003: 3.50,
#     1004: 4.50,
#     1005: 5.50
# }

# # Read the number of purchased products
# num_products = int(input())

# # Initialize the total cost
# total_cost = 0.0

# # Loop through each purchased product
# for _ in range(num_products):
#     # Read the product code and quantity from a single line
#     product_code, quantity = map(int, input().split())
    
#     # Get the price from the menu and calculate the item's cost
#     price = menu[product_code]
#     item_cost = price * quantity
    
#     # Add the item's cost to the total
#     total_cost += item_cost

# # Print the final total cost, formatted to two decimal places
# print(f"{total_cost:.2f}")

# time delay if there was late on time

# import sys

# for line in sys.stdin:
#     time_str = line.strip()
#     if not time_str:
#         continue
    
#     hour, minute = map(int, time_str.split(':'))

#     if hour < 7 or (hour == 7 and minute == 0):
#         delay = 0
#     else:
#         delay = (hour - 7) * 60 + minute
    
#     print(f"Atraso maximo: {delay}")

# counting number beecrowed problem
# import sys

# case = 1
# for line in sys.stdin:
#     N = int(line.strip())
#     print("N ", N)

#     # total numbers
#     total = 1 + (N * (N + 1)) // 2
#     print("total ", total)

#     # singular/plural
#     if total == 1:
#         print(f"Caso {case}: {total} numero")
#     else:
#         print(f"Caso {case}: {total} numeros")

#     # print sequence
#     for i in range(N + 1):      # from 0 to N
#         for j in range(i if i > 0 else 1):   # repeat i times, but 0 once
#             print(i, end=" ")
#     print("\n")   # new line + blank line

#     case += 1

# beecrowed proble build the sequence like this 0122333444455555666666
# import sys

# case_num = 1

# # Loop through each line of input until EOF
# for line in sys.stdin:
#     try:
#         n = int(line.strip())
#     except (ValueError, IndexError):
#         # Skip empty lines or malformed input
#         continue

#     # Build the sequence
#     sequence = [0]
#     for i in range(1, n + 1):
#         for _ in range(i):
#             sequence.append(i)
#     print('sequence ',sequence)
#     # Determine the count of numbers in the sequence
#     count = len(sequence)

#     # Format the header based on the number of elements
#     if count == 1:
#         header = f"Caso {case_num}: 1 numero"
#     else:
#         header = f"Caso {case_num}: {count} numeros"
    
#     print(header)

#     # Print the sequence elements separated by spaces
#     print(*sequence)

#     # Print a blank line after each case
#     print()

#     # Increment the case number
#     case_num += 1


# Read correct tea type
# T = int(input().strip())
# print("T ", T)
# # Read contestants' answers
# answers = list(map(int, input().split()))
# print("answers ", answers)
# # Counter for correct guesses
# correct = 0

# # Loop through each contestant's answer
# for ans in answers:
#     if ans == T:   # If the guess matches the correct tea
#         correct += 1

# print(correct)



# beecrowd | 2029
# Honey Reservoir

# import sys

# PI = 3.14

# for line in sys.stdin:
#     if not line.strip():
#         continue
#     V, D = map(float, line.split())

#     r = D / 2
#     area = PI * r * r
#     altura = V / area

#     print(f"ALTURA = {altura:.2f}")
#     print(f"AREA = {area:.2f}")

# beecrowd | 2057 Time Zone
# a, b, c = map(int,input().split())
# take = (a+b+c) % 24
# print(take)

# S, T, F = map(int, input().split())
# arrival = (S + T + F) % 24
# print(arrival)


# beecrowd 2059 - Odd, Even or Cheating

# Read inputs
# beecrowd 2059 - Odd, Even or Cheating

# Read inputs
# p, j1, j2, r, a = map(int, input().split())

# # Step 1: If player 1 cheated
# if r == 1:
#     if a == 1:  # cheated and accused correctly
#         print("Jogador 2 ganha!")
#     else:       # cheated and not accused
#         print("Jogador 1 ganha!")

# # Step 2: If player 1 did not cheat
# else:
#     if a == 1:  # accused wrongly
#         print("Jogador 1 ganha!")
#     else:       # normal odd/even game
#         total = j1 + j2
#         if total % 2 == 0:   # even sum
#             if p == 1:  # Player 1 chose even
#                 print("Jogador 1 ganha!")
#             else:
#                 print("Jogador 2 ganha!")
#         else:               # odd sum
#             if p == 0:  # Player 1 chose odd
#                 print("Jogador 1 ganha!")
#             else:
#                 print("Jogador 2 ganha!")



# beecrowd 2060 - Bino's Challenge

# numbers = list(map(int, input().split()))
# print("numbers ", numbers)
# # Initialize counters
# count2 = count3 = count4 = count5 = count6 = 0

# # Check multiples
# for num in numbers:
#     if num % 2 == 0:
#         count2 += 1
#     if num % 3 == 0:
#         count3 += 1
#     if num % 4 == 0:
#         count4 += 1
#     if num % 5 == 0:
#         count5 += 1
#     if num % 6 == 0:
#         count6 +=1

# # Print results
# print(f"{count2} Multiplo(s) de 2")
# print(f"{count3} Multiplo(s) de 3")
# print(f"{count4} Multiplo(s) de 4")
# print(f"{count5} Multiplo(s) de 5")
# print(f"{count6} Multiplo(s) de 6")




# beecrowd 2061 - Closing Tabs

# N, M = map(int, input().split())
# tabs = N

# for _ in range(M):
#     action = input().strip()
#     if action == "fechou":
#         tabs += 1
#     else:  # "clicou"
#         tabs -= 1

# print(tabs)





# beecrowd | 2126
# Searching Subsequences

# s1, s2 = input().split()
# print(s1,s2)
# while True:
#     account = s2.count(s1)
#     print(account)
#     if account > 0:


# beecrowd 2126 - Searching Subsequences

# case = 1
# while True:
#     try:
#         N1 = input("N1 ").strip()
#         N2 = input("N2 ").strip()
#     except EOFError:
#         break

#     count = 0
#     last_pos = -1

#     # search for all occurrences
#     for i in range(len(N2) - len(N1) + 1):
#         if N2[i:i+len(N1)] == N1:
#             print("N2[] ",N2[i:i+len(N1)])
#             count += 1
#             print("i , count ",i , count)
#             last_pos = i + 1  # 1-based index
            
#     print(f"Caso #{case}:")
#     if count == 0:
#         print("Nao existe subsequencia\n")
#     else:
#         print(f"Qtd.Subsequencias: {count}")
#         print(f"Pos: {last_pos}\n")

#     case += 1




# Salary cycle length
# CYCLE = 30

# # Ask how many days passed
# days = int(input("Enter how many days have passed since last salary: "))

# # Use modulo to normalize within the cycle
# days_passed = days % CYCLE  

# # Remaining days
# remaining = CYCLE - days_passed

# if days_passed == 0:
#     print("It's payday today! 🎉")
# elif days_passed < CYCLE:
#     print(f"Warning: {remaining} days left until payday.")


# days_in_month = [31, 29, 31, 30, 31, 30, 
#                  31, 31, 30, 31, 30, 31]
# while True:
#     try:
#         m,d= map(int,input().split())
#     except EOFError:
#         break
#     target_month,target_day = 12,31
#     days_of_year =sum(days_in_month[:m-1]) + d
#     print("days_of_year ", days_of_year)
#     days_of_christmas = sum(days_in_month[:target_month-1]) + target_day
#     print("days of christmas ", days_of_christmas)
#     remaining = days_of_year - days_of_christmas
#     print(remaining)

# beecrowd 2139 - Pedrinho's Christmas

# Days in each month for leap year 2016
# days_in_month = [31, 29, 31, 30, 31, 30, 
#                  31, 31, 30, 31, 30, 31]

# while True:
#     try:
#         m, d = map(int, input().split())
#     except EOFError:
#         break

#     # Target date: December 25
#     target_month, target_day = 12, 25

#     # Convert current date to "day of year"
#     day_of_year = sum(days_in_month[:m-1]) + d
#     christmas_day = sum(days_in_month[:target_month-1]) + target_day

#     remaining = christmas_day - day_of_year

#     if remaining == 0:
#         print("E natal!")
#     elif remaining == 1:
#         print("E vespera de natal!")
#     elif remaining < 0:
#         print("Ja passou!")
#     else:
#         print(f"Faltam {remaining} dias para o natal!")


# bills = [2, 5, 10, 20, 50, 100]

# while True:
#     N, M = map(int, input().split())
#     print("N ",N,"M ",M)
#     if N == 0 and M == 0:
#         break

#     change = M - N
#     print("change")
#     possible = False
#     new_change = []
#     # Check all pairs of bills
#     for i in range(len(bills)):
#         for j in range(i + 1, len(bills)):  # ensures different bills
#             if bills[i] + bills[j] == change:
#                 new_change.append(bills[i])
#                 new_change.append(bills[j])
#                 print(f"bills[i]: {bills[i]}, bills[j]: {bills[j]}")
#                 possible = True
#                 break
#         if possible:
#             break
#     print(new_change)
#     if possible:
#         print("possible")
#     else:
#         print("impossible")


# beecrowd | 2143
# The Return of Radar

# while True:
#     T = int(input())
#     if T == 0:
#         break

#     for _ in range(T):
#         N = int(input())
#         if N % 2 == 0:  # even → both ends
#             print(2 * N - 2)
#         else:           # odd → one end
#             print(2 * N - 1)



# # beecrowd | 2146
# # Password
# while True:
#     n = int(input("enter a password "))
#     new_pasword = n - 1
#     print(new_pasword)



# beecrowd | 2147
# Galopeira
# import time 

# sec = 0
# T = int(input())

# for i in range(T):
#     start_time = time.time()
#     taken_glop = input()
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f"Elapsed time: {elapsed_time:.2f} seconds")

# C = int(input())

# for _ in range(C):
#     word = input().strip()
#     time = len(word) * 0.01
#     print(f"{time:.2f}")
# beecrowd | 2152
# Pepe, I Already Took the Candle!
# N = int(input())

# for _ in range(N):
#     H, M, O = map(int, input().split())
    
#     # Format time with leading zeros
#     time_str = f"{H:02d}:{M:02d}"
    
#     if O == 1:
#         print(f"{time_str} - A porta abriu!")
#     else:
#         print(f"{time_str} - A porta fechou!")




# beecrowd | 2159
# Approximate Number of Primes
# import math # Import the math module for math.log()

# try:
#     # Read the integer n
#     n = int(input())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     exit()

# # The natural logarithm of n
# ln_n = math.log(n)

# # Calculate the minimum approximate value (P)
# # P = n / ln(n)
# P = n / ln_n

# # Calculate the maximum approximate value (M)
# # M = 1.25506 * (n / ln(n))
# M = 1.25506 * P

# # Print the results, each formatted to one decimal place, separated by a space
# print(f"{P:.1f} {M:.1f}")



# beecrowd | 2160
# Name at Form
# Read the entire line of text from the input
# try:
#     L = input()
# except EOFError:
#     # Handle case where input is empty
#     exit()

# # Get the length of the string using the built-in len() function
# length_of_L = len(L)

# # Check if the length is within the 80-character limit
# if length_of_L <= 80:
#     print("YES")
# else:
#     print("NO")



# try:
#     # Read N, the number of repetitions
#     N = int(input())
# except (ValueError, EOFError):
#     # Handle bad input
#     exit()

# # This will store the result of the nested fractional part (1 / (6 + ...))
# # We start from the innermost part and build outwards.
# # For N=0, this loop doesn't run, and fraction_part remains 0.
# fraction_part = 0.0

# for i in range(N):
#     # Each iteration adds one more layer of (6 + ...) to the denominator
#     fraction_part = 1.0 / (6.0 + fraction_part)
#     print(f"Iteration {i}: fraction_part = {fraction_part}")
# # The final result is 3 + the entire fractional part
# final_result = 3.0 + fraction_part

# # Print the result formatted to 10 decimal places
# print(f"{final_result:.10f}")




# high and peak
# N = int(input().strip())
# H = list(map(int, input().split()))

# valid = True
# directions = []

# for i in range(1, N):
#     if H[i] > H[i-1]:
#         directions.append(1)   # peak
#     elif H[i] < H[i-1]:
#         directions.append(-1)  # valley
#     else:
#         valid = False          # equal → invalid
#         break
# print("direction ", directions)
# if valid:
#     for i in range(1, len(directions)):
#         if directions[i] == directions[i-1]:  # not alternating
#             print(f"in teration of {i} happend {directions[i], directions[i-1]}")
#             valid = False
#             break

# print("last ",1 if valid else 0)



# find number in matrix
# matrix = []

# for i in range(5):
#     row = []
#     for j in range(5):
#         row.append(j)   # add values to row
#     matrix.append(row)  # add row to matrix

# print(matrix)
# try:
#     N, M = map(int, input("Enter N and M: ").split())
# except (ValueError, EOFError):
#     exit()

# # Read the entire terrain into a 2D list (list of lists)
# terrain = []
# for _ in range(N):
#     try:
#         row = list(map(int, input("Enter row values: ").split()))
#         terrain.append(row)
#     except (ValueError, EOFError):
#         # Handle case where input might not be complete
#         break

# # Initialize found coordinates to (0, 0)
# found_x = 0
# found_y = 0

# # Loop through the inner cells of the terrain, which are potential centers of the pattern
# # range(1, N-1) goes from 1 to N-2
# for row in range(1, N - 1):
#     for col in range(1, M - 1):
#         # Check if the current cell is the center of the lightsaber pattern (42)
#         if terrain[row][col] == 42:
#             # If it's 42, check all 8 surrounding cells for 7
#             if (terrain[row-1][col-1] == 1 and
#                 terrain[row-1][col]   == 1 and
#                 terrain[row-1][col+1] == 1 and
#                 terrain[row][col-1]   == 1 and
#                 terrain[row][col+1]   == 1 and
#                 terrain[row+1][col-1] == 1 and
#                 terrain[row+1][col]   == 1 and
#                 terrain[row+1][col+1] == 1):
                
#                 # Pattern found! Store the 1-indexed coordinates.
#                 found_x = row + 1
#                 found_y = col + 1
#                 # Since there's at most one pattern, we can stop searching.
#                 break # Exit the inner (column) loop
    
#     # If we found the pattern in the inner loop, also exit the outer (row) loop
#     if found_x != 0:
#         break

# # Print the final coordinates
# print(f"{found_x} {found_y}")


# import math # Import the math module for sqrt and pow

# try:
#     # Read the integer n
#     n = int(input())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     exit()

# # Pre-calculate the constant values from the formula
# sqrt_5 = math.sqrt(5)
# phi = (1 + sqrt_5) / 2
# psi = (1 - sqrt_5) / 2

# # Apply Binet's formula
# # math.pow(base, exp) is used for exponentiation
# fib_n = (math.pow(phi, n) - math.pow(psi, n)) / sqrt_5

# # Print the result formatted to one decimal place
# print(f"{fib_n:.1f}")

# # An alternative for exponentiation is the ** operator
# # fib_n = ( (phi**n) - (psi**n) ) / sqrt_5
# # print(f"{fib_n:.1f}")


# # This will store the result of the nested fractional part (1 / (2 + ...))
# # We start from the innermost part and build outwards.
# # For N=0, this loop doesn't run, and fraction_part remains 0.
# fraction_part = 0.0

# for _ in range(N):
#     # Each iteration adds one more layer of (2 + ...) to the denominator
#     fraction_part = 1.0 / (2.0 + fraction_part)

# # The final result is 1 + the entire fractional part
# final_result = 1.0 + fraction_part

# # Print the result formatted to 10 decimal places
# print(f"{final_result:.10f}")
# try:
#     # Read N, the number of measurements
#     N = int(input())
    
#     # Read the N RPM values into a list of integers
#     rpms = list(map(int, input().split()))
# except (ValueError, EOFError, IndexError):
#     # Handle bad input
#     exit()

# # Initialize the result to 0. This will be the output if no fall is found.
# fall_position = 0

# # Loop from the second measurement (index 1) to the end of the list
# # range(1, N) will give indices 1, 2, ..., N-1
# for i in range(1, N):
#     # Check if the current measurement is less than the previous one
#     if rpms[i] < rpms[i-1]:
#         # If a fall is detected, store its 1-indexed position
#         fall_position = i + 1
#         # Since we only need the *first* fall, we can stop searching.
#         break

# # Print the final result
# print(fall_position)


# try:
#     N = int(input("Enter N: "))
# except (ValueError, EOFError):
#     # Handle bad input
#     exit()

# # Read the (N+1) x (N+1) camera grid
# camera_grid = []
# for _ in range(N + 1):
#     try:
#         row = list(map(int, input("Enter row: ").split()))
#         camera_grid.append(row)
#     except (ValueError, EOFError, IndexError):
#         # Handle bad input during grid reading
#         break
# print("camera_grid ", camera_grid)
# # Iterate through each of the N x N blocks
# for i in range(N): # i is the block row
#     output_row = ""
#     for j in range(N): # j is the block column
#         print("i, j ", i, j)
#         print("camera_grid[i][j] ", camera_grid[i][j])
#         print("camera_grid[i][j+1] ", camera_grid[i][j+1])
#         print("camera_grid[i+1][j] ", camera_grid[i+1][j])
#         print("camera_grid[i+1][j+1] ", camera_grid[i+1][j+1])
#         print("----")
#         # Sum the cameras at the four corners of the block (i, j)
#         num_cameras = (camera_grid[i][j] + camera_grid[i][j+1] +
#                        camera_grid[i+1][j] + camera_grid[i+1][j+1])
        
#         # Determine if the block is safe or unsafe
#         if num_cameras >= 2:
#             output_row += "S"
#         else:
#             output_row += "U"
            
#     # Print the resulting string for the current row of blocks
#     print(" output_row ",output_row)




# beecrowd | 2172
# Event

# n = int(input())
# exp = int(input())
# for i in range(n):
#     if exp == 0 and i == 0:
#         break
#     else:
#         new_exp = i * exp
#     print(new_exp)



# The program needs to read inputs until a specific terminator (0 0) is found.
# A while True loop with a try-except and an if-break is a robust way to handle this.
# while True:
#     try:
#         # Read X and M from a single line, space-separated
#         X, M = map(int, input().split())
#     except EOFError:
#         # Stop if the input stream ends before the terminator
#         break
#     except ValueError:
#         # Stop if the input line is not two valid integers
#         break

#     # Check for the termination condition
#     if X == 0 and M == 0:
#         break

#     # Calculate the new experience value by multiplication
#     new_xp = X * M
    
#     # Print the result
#     print(new_xp)



# while True:
#     x, m = map(int, input().split())
#     if x == 0 and m == 0:
#         break
#     new_xp = x * m
#     print(new_xp)


# beecrowd | 2176
# Parity
# while True:
#     m = map(str, input().split())
#     if m == "0 0":
#         break
#     else:
# m = input("Enter m: ").split()
# for i in m:
#     print("int(i)  ",int(i))
#     if int(i) % 2 == 0:
#         print("0", end=" ")
#     else:
#         print("1", end=" ")
# print()

# try:
#     # Read the binary message S as a string
#     S = input("Enter binary message S: ")
# except EOFError:
#     # Handle case where input is empty
#     exit()

# # Use the built-in string.count() method to find the number of '1's
# ones_count = S.count('1')
# print("ones_count ", ones_count)
# # Check if the count of '1's is even or odd
# if ones_count % 2 == 0:
#     # If the count is even, append a '0'
#     new_S = S + '0'
#     print("new_S ", new_S)
# else: # The count is odd
#     # If the count is odd, append a '1'
#     new_S = S + '1'

# # Print the resulting message
# print(new_S)



# s = input().strip()
# ones_count = s.count('1')
# if ones_count % 2 == 0:
#     print(s + '0')
# else:
#     print(s + '1')


# beecrowd | 2203
# Crowstorm

# try:
#     Xf, Xi, Yf, Yi, R1, V1 = map(int, input().split())
#     Xs, Ys, R2, V2 = map(int, input().split())
# except EOFError:
#     exit()
# # Calculate the distance between the centers of the two circles
# dx = Xf - Xi
# dy = Yf - Yi
# distance = (dx**2 + dy**2)**0.5

# # Check if the distance is less than the sum of the radii
# if distance < (R1 + R2):
#     print("RICO")
# else:
#     print("MORTO")
# import math

# while True:
#     try:
#         # Read the line of input. map() is good for mixed types if we
#         # specify the type for each, but split() and manual conversion is clearer.
#         line = input().split()
#         if not line: # Handle empty lines at the end of file
#             break
            
#         Xf = int(line[0])
#         Yf = int(line[1])
#         Xi = int(line[2])
#         Yi = int(line[3])
#         Vi = int(line[4])
#         R1 = int(line[5])
#         R2 = int(line[6])
        
#     except EOFError:
#         break
#     except (ValueError, IndexError):
#         # Handle malformed lines
#         break

#     # Step 1: Calculate the initial distance between Fiddlesticks and the invader
#     # This is the distance Fiddlesticks's teleport must cover.
#     initial_distance = math.sqrt( ((Xi - Xf)**2) + ((Yi - Yf)**2) )
    
#     # Step 2: Calculate the total distance the invader flees during the 1.5s channel time
#     distance_fled = Vi * 1.5
    
#     # Step 3: The total distance the ultimate must effectively cover is the initial
#     # distance plus the distance the invader flees.
#     total_distance_needed = initial_distance + distance_fled
    
#     # Step 4: The total reach of the ultimate is the teleport radius plus the damage radius.
#     total_reach = R1 + R2
    
#     # Step 5: Check if the reach is sufficient.
#     if total_reach >= total_distance_needed:
#         print("Y")
#     else:
#         print("N")



# beecrowd | 2221
# Pomekons Battle


# def calculate_pomekon_value(attack, defense, level, bonus):
#     """Calculates the final battle value for a Pomekon."""
#     value = (attack + defense) / 2.0
    
#     # Add bonus only if the level is even
#     if level % 2 == 0:
#         value += bonus
        
#     return value

# # Read the number of test cases
# try:
#     T = int(input())
# except (ValueError, EOFError):
#     T = 0

# for _ in range(T):
#     try:
#         # Read the bonus value for this test case
#         bonus = int(input())
        
#         # Read Dabriel's stats
#         d_attack, d_defense, d_level = map(int, input().split())
        
#         # Read Guarte's stats
#         g_attack, g_defense, g_level = map(int, input().split())

#     except (ValueError, EOFError, IndexError):
#         # Skip this test case if input is malformed
#         continue

#     # Calculate the final value for each player
#     dabriel_value = calculate_pomekon_value(d_attack, d_defense, d_level, bonus)
#     guarte_value = calculate_pomekon_value(g_attack, g_defense, g_level, bonus)

#     # Compare the values and print the winner
#     if dabriel_value > guarte_value:
#         print("Dabriel")
#     elif guarte_value > dabriel_value:
#         print("Guarte")
#     else: # The values are equal
#         print("Empate")

# becrowd | 2234
# try:
#     # Read H (total hot dogs) and P (total participants) from a single line
#     # map(int, ...) will convert the split strings to integers
#     H, P = map(int, input().split())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     exit()

# # Calculate the average. In Python 3, dividing two integers with /
# # automatically results in a float.
# average = H / P

# # Print the result formatted to exactly two decimal places
# # The f-string format specifier '{value:.2f}' does this.
# print(f"{average:.2f}")




#  let's solve "Walking in Time" (Beecrowrowd 2235)


# try:
#     # Read the three credits from a single line
#     A, B, C = map(int, input().split())
# except (ValueError, EOFError):
#     # Handle bad input
#     exit()

# # Set a flag to track if a solution is found
# possible = False

# # --- Check all conditions for a possible return to the present ---

# # Condition 1: Two credits are equal.
# # This means you can make two trips that cancel each other out.
# # e.g., if A==B, travel +A and -B. Total = A - B = 0.
# if A == B or A == C or B == C:
#     possible = True

# # Condition 2: One credit is the sum of the other two.
# # This means you can make three trips that cancel out.
# # e.g., if A+B == C, travel +A, +B, and -C. Total = A + B - C = 0.
# if A + B == C or A + C == B or B + C == A:
#     possible = True
    
# # Print the final result based on the flag
# if possible:
#     print('S')
# else:
#     print('N')


# n = int(input())    
# for i in range(n):
#     try:
#         # Read the three credits from a single line
#          name = input("Enter name: ")
#          A, B, C = map(int, input().split())
#     except (ValueError, EOFError):
#         # Handle bad input
#         exit()
#     total = A + B + C
#     print(name, total)
# try:
#     N = int(input()) # Read the number of players
# except (ValueError, EOFError):
#     N = 0
# # initialize team-wide totals
# total_s, total_b, total_a = 0, 0, 0
# total_s1, total_b1, total_a1 = 0, 0, 0
# # loop for each player
# # for _ in range(N):
# #     name = input() # read and discard the name
# #     S, B, A = map(int, input().split())
# #     total_s += S
# #     total_b += B
# #     total_a += A
# #     S1, B1, A1 = map(int, input().split())
# #     total_s1 += S1
# #     total_b1 += B1
# #     total_a1 += A1
# #     result_s = (total_s1 / total_s) * 100 if total_s > 0 else 0.0
# #     result_b = (total_b1 / total_b) * 100 if total_b > 0 else 0.0
# #     result_a = (total_a1 / total_a) * 100 if total_a > 0 else 0.0
# # # print the final results
# # print(f"Pontos de Saque: {result_s:.2f} %.")
# # print(f"Pontos de Bloqueio: {result_b:.2f} %.")
# # print(f"Pontos de Ataque: {result_a:.2f} %.")



# # beecrowd | 2240
# try:
#     N = int(input()) # Read the number of players
# except (ValueError, EOFError):
#     N = 0

# # Initialize team-wide totals
# total_S, total_B, total_A = 0, 0, 0
# total_S1, total_B1, total_A1 = 0, 0, 0

# # Loop for each player
# for _ in range(N):
#     try:
#         name = input() # Read and discard the name
        
#         # Read attempts and add to totals
#         S, B, A = map(int, input().split())
#         total_S += S
#         total_B += B
#         total_A += A
        
#         # Read successes and add to totals
#         S1, B1, A1 = map(int, input().split())
#         total_S1 += S1
#         total_B1 += B1
#         total_A1 += A1

#     except (ValueError, EOFError, IndexError):
#         # Skip this player if input is bad
#         continue

# # Calculate percentages, checking for division by zero
# percent_saque = (total_S1 / total_S) * 100 if total_S > 0 else 0.0
# percent_bloqueio = (total_B1 / total_B) * 100 if total_B > 0 else 0.0
# percent_ataque = (total_A1 / total_A) * 100 if total_A > 0 else 0.0

# # Print the final results
# print(f"Pontos de Saque: {percent_saque:.2f} %.")
# print(f"Pontos de Bloqueio: {percent_bloqueio:.2f} %.")
# print(f"Pontos de Ataque: {percent_ataque:.2f} %.")





# beecrowd | 2483
# Merry Christmaaas!

# n = int(input())
# name = "aram"
# counts = name[1]
# counts = counts * n
# print(name[0] + str(counts) + name[2:])
# try:
#     # Read the happiness index I
#     I = int(input())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     exit()

# # In Python, the '*' operator can be used to repeat a string
# # 'a' * 5 will result in the string 'aaaaa'
# repeated_a = 'a' * I

# # Construct the final greeting using an f-string
# final_greeting = f"Feliz nat{repeated_a}l!"

# # Print the result
# print(final_greeting)


# # Create a dictionary to map food names to their Vitamin C content
# vitamin_c_map = {
#     "suco de laranja": 120,
#     "morango fresco": 85,
#     "mamao": 85,
#     "goiaba vermelha": 70,
#     "manga": 56,
#     "laranja": 50,
#     "brocolis": 34
# }

# while True:
#     try:
#         T = int(input())
#     except (ValueError, EOFError):
#         # Handle bad input or end of file
#         break

#     # Termination condition
#     if T == 0:
#         break

#     total_vitamin_c = 0
#     # Loop T times to read T food items
#     for _ in range(T):
#         try:
#             # Read the line, e.g., "2 suco de laranja"
#             line = input().split()
#             print("line ", line)
#             # The first part is the quantity
#             quantity = int(line[0])
#             print("quantity ", quantity)
#             # The rest of the parts make up the food name
#             # " ".join(line[1:]) re-joins them with spaces
#             food_name = " ".join(line[1:])
#             print("food_name ", food_name)
#             # Get the vitamin C per serving from our map
#             mg_per_serving = vitamin_c_map[food_name]
#             print("mg_per_serving ", mg_per_serving)
#             # Add to the total
#             total_vitamin_c += quantity * mg_per_serving
#             print("total_vitamin_c ", total_vitamin_c)
#         except (ValueError, EOFError, IndexError, KeyError):
#             # Skip this line if input is malformed
#             continue
            
#     # After processing all foods for this test case, check the total
#     if total_vitamin_c < 110:
#         needed = 110 - total_vitamin_c
#         print(f"Mais {needed} mg")
#     elif total_vitamin_c > 130:
#         excess = total_vitamin_c - 130
#         print(f"Menos {excess} mg")
#     else: # 110 <= total_vitamin_c <= 130
#         print(f"{total_vitamin_c} mg")

# Problem:
# 2510 - Batmain

# try:
#     # Read T, the number of test cases
#     T = int(input())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     T = 0

# # Loop T times
# for _ in range(T):
#     try:
#         # Read the villain's name from the input line.
#         # We don't need to do anything with this name, but we must read the line
#         # to advance the input stream for the next test case.
#         villain_name = input()
#     except EOFError:
#         # Stop if input ends unexpectedly
#         break
    
#     # According to the problem statement, all villains have been captured.
#     # Therefore, the answer is always 'Y'.
#     print('Y')
# while True:
#     t = int(input())
#     for i in range(t):
#         name = input()
#     print('Y')



# beecrowd | 2523
# Will's Message

# while True:
#     leters = "abcdefghijklmnopqrstuvwxyz"
#     text = ""
#     try:
#         # Print the corresponding letter
#         number_of_letters = int(input("Enter number of letters: "))
#     except EOFError:
#         # Stop if input ends
#         break
#     except ValueError:
#         # Handle bad input
#         continue
#     for i in range(number_of_letters):
#         line = int(input("Enter line: "))
#         text += letters[line - 1] + ""
#     print("the text is:", text)

# while True:
#     letters = "abcdefghijklmnopqrstuvwxyz"
#     text = ""
#     try:
#         # Ask for number of letters
#         number_of_letters = int(input("Enter number of letters: "))
#     except EOFError:
#         # Stop if input ends
#         break
#     except ValueError:
#         # Handle bad input
#         continue

#     for i in range(number_of_letters):
#         try:
#             line = int(input("Enter line: "))
#             if 1 <= line <= len(letters):
#                 text += letters[line - 1]
#             else:
#                 print("Invalid number, must be between 1 and 26")
#         except ValueError:
#             print("Please enter a valid number")

#     print("The text is:", text)


# The program needs to read inputs until there are no more (End-of-File).
# A while True loop with a try-except block is a standard way to handle this.




# while True:
#     try:
#         # Read M, the number of subjects for this test case.
#         # If the input stream is empty, input() will raise EOFError.
#         M_str = input()
#         if not M_str: break # Handle empty lines at the end of some inputs
#         M = int(M_str)
        
#     except EOFError:
#         break
#     except ValueError:
#         continue # Skip if M is not a valid int

#     # Initialize the sums for the numerator and the C part of the denominator
#     numerator_sum = 0
#     denominator_c_sum = 0
    
#     # Loop M times to read the data for each subject
#     for _ in range(M):
#         try:
#             # Read Ni (grade) and Ci (workload) from a single line
#             Ni, Ci = map(int, input().split())
            
#             # Add to the respective sums
#             numerator_sum += Ni * Ci
#             denominator_c_sum += Ci

#         except (EOFError, ValueError):
#             # In case input ends mid-test-case
#             break
            
#     # Calculate the final denominator
#     final_denominator = denominator_c_sum * 100
    
#     # Calculate the API.
#     # Check for division by zero as good practice, though constraints prevent it.
#     if final_denominator > 0:
#         api = numerator_sum / final_denominator
#     else:
#         api = 0.0
        
#     # Print the result formatted to four decimal places
#     print(f"{api:.4f}")

# "General Exam" (Beecrowd 2534)

# while True:
#     n, m = map(int, input().split())
#     grade = []
#     for  i in range(n):
#         g = int(input())
#         grade.append(g)
#     grade.sort(reverse=True)
#     print("grade ", grade)
    
#     for _ in range(m):
#         q = int(input())
#         index = q - 1
#         print(grade[index])

# The program needs to read inputs until there are no more (End-of-File).
# A while True loop with a try-except block is a standard way to handle this.
# while True:
#     try:
#         # Read N and Q. If the line is empty at EOF, this will raise an error.
#         line1 = input("Enter N and Q: ")
#         if not line1: break
#         N, Q = map(int, line1.split())
        
#         # Read all N grades into a list
#         grades = []
#         for _ in range(N):
#             grades.append(int(input()))
            
#         # Sort the list of grades in descending (reverse) order
#         grades.sort(reverse=True)
#         print("grades ", grades)
#         # Process the Q queries
#         for _ in range(Q):
#             # Read the position query (pi)
#             pi = int(input("Enter query position: "))
            
#             # Convert the 1-based position to a 0-based index
#             index = pi - 1
            
#             # Print the grade at that index
#             print("grade index", index, "is", grades[index])
#         print()
        
#     except EOFError:
#         break
#     except (ValueError, IndexError):
#         # Handle cases where input might be malformed or incomplete
#         break


# while True:
#     try:
#         n = int(input())
#         if n == 0:
#             break

#         M , L = map(int, input("Enter M and L").split())
#         marcos_deck = []
#         for _ in range(M):
#             attributes = list(map(int, input("Enter attributes").split()))
#             marcos_deck.append(attributes)
#         print("marcos_deck ", marcos_deck)
#         lucas_deck = []
#         for _ in range(L):
#             attributes = list(map(int, input("Enter attributes").split()))
#             lucas_deck.append(attributes)
#         print("lucas_deck ", lucas_deck)


#         CM , CL = map(int, input("Enter CM and CL").split())
#         print("CM, CL ", CM, CL)
#         A = int(input("Enter A: "))

#     except EOFError:
#         break
#     except (ValueError, IndexError):
#         # Handle cases where input might be malformed or incomplete
#         break
#     marcos_attr_value = marcos_deck[CM - 1][A - 1]
#     lucas_attr_value = lucas_deck[CL - 1][A - 1]
#     print("marcos_attr_value ", marcos_attr_value)
#     print("lucas_attr_value ", lucas_attr_value)
#     if marcos_attr_value > lucas_attr_value:
#         print("Marcos")
#     elif lucas_attr_value > marcos_attr_value:
#         print("Lucas")
#     else: # The values are equal
#         print("Empate")


# 2630 Greyscale
# try :
#     # Read the integer n
#     T = int(input())
# except (ValueError, EOFError):
#     # Handle bad input if necessary
#     T = 0

# # Read the n lines of input
# for _ in range(T):
#     try:
#         conversation_type = int(input())
#         r, g, b = map(int, input().split())
#     except (ValueError, EOFError):
#         # Handle bad input if necessary
#         continue
#     if conversation_type == "min":
#         p = min(r,g,b)
#     elif conversation_type == "max":
#         p = max(r,g,b)
#     elif conversation_type == "mean":
#         p = (r + g + b) / 3
#     elif conversation_type == "eye":
#         p = 0.3 * r + 0.59 * g + 0.11 * b
#     else: # conversation_type == "lum"
#         p = 0.2126 * r + 0.7152 * g + 0.0722 * b
#     print(int(p))

# 2632 Magic and Sword
# import math

# # --- Setup: Store spell data in a nested dictionary ---
# # Format: spell_data[name][level] = (damage, radius)
# spell_data = {
#     "fire": {
#         1: (200, 20),
#         2: (300, 30),
#         3: (400, 50)
#     },
#     "water": {
#         1: (300, 10),
#         2: (400, 25),
#         3: (500, 40)
#     },
#     "earth": {
#         1: (400, 25),
#         2: (550, 55),
#         3: (700, 70)
#     },
#     "air": {
#         1: (100, 18),
#         2: (250, 38),
#         3: (400, 60)
#     }
# }

# try:
#     T = int(input())
# except (ValueError, EOFError):
#     T = 0

# for _ in range(T):
#     try:
#         w, h, x0, y0 = map(int, input().split())
#         spell_line = input().split()
#         spell_name = spell_line[0]
#         level = int(spell_line[1])
#         cx = int(spell_line[2])
#         cy = int(spell_line[3])
#     except (ValueError, EOFError, IndexError):
#         continue

#     # Get damage and radius from the lookup table
#     damage, radius = spell_data[spell_name][level]
#     print("damage, radius ", damage, radius)
#     # Define the rectangle's boundaries
#     rect_x_min = x0
#     print("rect_x_min ", rect_x_min)
#     rect_x_max = x0 + w
#     print("rect_x_max ", rect_x_max)
#     rect_y_min = y0
#     print("rect_y_min ", rect_y_min)
#     rect_y_max = y0 + h
#     print("rect_y_max ", rect_y_max)

#     # Find the closest point on the rectangle to the circle's center
#     # This is done by "clamping" the circle's center coordinates to the rectangle's bounds.
#     closest_x = max(rect_x_min, min(cx, rect_x_max))
#     print("closest_x ", closest_x)
#     closest_y = max(rect_y_min, min(cy, rect_y_max))
#     print("closest_y ", closest_y)

#     # Calculate the squared distance from the circle center to this closest point
#     dist_x = cx - closest_x
#     print("dist_x ", dist_x)
#     dist_y = cy - closest_y
#     print("dist_y ", dist_y)
#     distance_squared = dist_x**2 + dist_y**2
#     print("distance_squared ", distance_squared)
#     # Compare the squared distance to the squared radius
#     if distance_squared <= radius**2:
#         print("damage ", damage)
#     else:
#         print(0)

# beecrowd | 2635
# while True:
#     try:
#         N_str = int(input())
#     except (ValueError, EOFError):
#         N_str = 0
#     history_words = []
#     for _ in range(N_str):
#         history_words.append(input().strip().lower())
#     print("history_words ", history_words)
#     Q_str = int(input("Enter the number of queries: "))
#     for _ in range(Q_str):
#         query_prefix = input().strip().lower()
#         for word in history_words:
#             if word.startswith(query_prefix):
#                 print("words that start with the query prefix",word)
                
#     if not match_found:
#         print("No match found")
#     else:
#         count = len("matching words",matching_words)
#         print(f"{count} matches found")
#         max_length = max(len(word) for word in matching_words)
#         print(f"{count} {max_length}")

# The program needs to read inputs until there are no more (End-of-File).
# while True:
#     try:
#         # Read N, the number of history words.
#         # If the input stream is empty, input() will raise an error.
#         N_str = input("Enter N: ")
#         if not N_str: break
#         N = int(N_str)
        
#         # Read the N history words into a list
#         history_words = []
#         for _ in range(N):
#             history_words.append(input("Enter history word: "))
            
#         # Read Q, the number of queries
#         Q = int(input("Enter Q: " ))
        
#         # Loop Q times to process each query
#         for _ in range(Q):
#             query_prefix = input("Enter query prefix: ")
            
#             # Find all words in the history that start with the prefix
#             matching_words = []
#             for word in history_words:
#                 if word.startswith(query_prefix):
#                     matching_words.append(word)
#             print("matching_words ", matching_words)
#             # Check the result and print accordingly
#             if not matching_words: # An empty list is "falsy"
#                 print(-1)
#             else:
#                 count = len(matching_words)
#                 # Find the length of the longest word among the matches
#                 # We can do this by mapping len() to each word and finding the max
#                 max_length = max(len(word) for word in matching_words)
#                 print(f"********* {count} {max_length}")

#     except EOFError:
#         break
#     except (ValueError, IndexError):
#         # Handle cases where input might be malformed
#         break






# beecrowd | 2653
# Dijkstra
# n = int(input())
# new_set = set()
# for i in range(n):
#     name = input()
#     new_set.add(name)
# print(new_set)

# A set is the ideal data structure to store unique items.
# unique_jewels = set()

# # The program needs to read inputs until there are no more (End-of-File).
# # A while True loop with a try-except block is a standard way to handle this.
# while True:
#     try:
#         # Read a line, which represents one jewel.
#         jewel_type = input()
        
#         # Add the jewel type to our set.
#         # If this type is already in the set, the set remains unchanged.
#         unique_jewels.add(jewel_type)
        
#     except EOFError:
#         # This error is raised when input() reaches the end of the file.
#         # We simply break the loop to stop reading.
#         break

# # After reading all lines, the number of different types of jewelry
# # is the number of items in our set.
# # The built-in len() function gives the size of the set.
# print(len(unique_jewels))


# 2663		Phase
# n = int(input())
# minimum = 3
# count = 0
# for i in range(n):
#     num = int(input())
#     if num < minimum:
#         count += 1
# print(minimum)
# try:
#     N = int(input("number of contestants")) # Number of contestants
#     K = int(input("minimum number to qualify")) # Minimum number to qualify

#     scores = []
#     # Read all N scores
#     for _ in range(N):
#         scores.append(int(input("Enter score: ")))

# except (ValueError, EOFError, IndexError):
#     exit()

# # Sort the scores in descending order (highest first)
# scores.sort(reverse=True)
# print("scores reverse", scores)
# # The score of the K-th person is our cutoff score.
# # In a 0-indexed list, this is at index K-1.
# cutoff_score = scores[K-1]
# print("cutoff_score ", cutoff_score)

# # We know at least K people qualified.
# qualified_count = K
# print("qualified_count ", qualified_count)

# # Now, we check for people who tied with the K-th person.
# # We start checking from the (K+1)-th position, which is index K.
# for i in range(K, N):
#     if scores[i] == cutoff_score:
#         qualified_count += 1
#     else:
#         # Since the list is sorted, if we find a score lower than the cutoff,
#         # we can stop checking immediately.
#         break

# print("qualified_count **", qualified_count)


# 2702
# 
# try:
#     # Read the available meal counts
#     Ca, Ba, Pa = map(int, input().split())
    
#     # Read the requested meal counts
#     Cr, Br, Pr = map(int, input().split())
# except (ValueError, EOFError, IndexError):
#     # Handle bad input if necessary
#     exit()

# # Initialize the total number of passengers who won't get their meal
# total_shortage = 0

# # Calculate the shortage for chicken
# # If requested is more than available, add the difference to the shortage.
# if Cr > Ca:
#     total_shortage += (Cr - Ca)

# # Calculate the shortage for beef
# if Br > Ba:
#     total_shortage += (Br - Ba)

# # Calculate the shortage for pasta
# if Pr > Pa:
#     total_shortage += (Pr - Pa)
    
# # Print the final total
# print(total_shortage)
# Initialize counters for jeeps and tourists in the park
# jeeps_in_park = 0
# tourists_in_park = 0

# # Loop to read actions until "ABEND" is encountered
# while True:
#     try:
#         # Read the line and split it into parts
#         line = input().split()
        
#         # The first part is the action
#         action = line[0]
#     except (EOFError, IndexError):
#         # Stop if input ends unexpectedly or line is empty
#         break

#     # Check for the termination command
#     if action == "ABEND":
#         break
        
#     # If not "ABEND", the second part is the number of tourists
#     try:
#         num_tourists = int(line[1])
#     except (ValueError, IndexError):
#         # Skip if the second part is not a valid number
#         continue

#     # Update counts based on the action
#     if action == "SALIDA":
#         jeeps_in_park += 1
#         tourists_in_park += num_tourists
#     elif action == "VUELTA":
#         jeeps_in_park -= 1
#         tourists_in_park -= num_tourists
#     print("tourists_in_park", tourists_in_park)
#     print("jeeps_in_park", jeeps_in_park)
# # After the loop finishes, print the final counts
# print("*****", tourists_in_park)
# print("*****", jeeps_in_park)




# 2709		The Coins of Robbie
# import math

# def is_prime(num):
#     """Checks if a number is prime."""
#     if num <= 1:
#         return False
#     # Check for divisors from 2 up to the square root of the number
#     limit = int(math.sqrt(num))
#     for i in range(2, limit + 1):
#         if num % i == 0:
#             return False # It has a divisor, so not prime
#     return True # No divisors found, it is prime

# while True:
#     M_str = input("Enter M: ")
#     if not M_str:
#         break
#     M = int(M_str)
#     coins = []
#     for _ in range(M):
#         coins.append(int(input("Enter coin value: ")))
#     print("coins ", coins)

#     N = int(input("Enter N: "))

#     total_sum = 0

#     for i in range(M-1, -1, -N):
#         print("coins[i] ", coins[i])
#         total_sum += coins[i]
#         print("total_sum ", total_sum)

#     if is_prime(total_sum):
#         print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
#     else:
#         print("Bad boy! I’ll hit you.")
    
# beecrowd | 2712
# Vehicular Restriction
# while True:

#     try:
#         # Read the line and split it into parts
#         n = int(input())
#         if n == 0:
#             break
#     except (ValueError, IndexError):
#         # Stop if input ends unexpectedly or line is empty
#         break
#     for i in range(n):
#         name, num = input().split()
#         num = list(map(int, num))
#         if num[-1] == 1 or num[-1] == 2:
#             print("monday")
#         elif num[-1] == 3 or num[-1] == 4:
#             print("tuesday")
#         elif num[-1] == 5 or  num[-1] == 6:
#             print("wednesday")
#         elif num[-1] == 7 or num[-1] == 8:
#             print("thursday")
#         elif num[-1] == 9 or num[-1] == 0:
#             print("friday")
#         else:
#             print("saturday")
    
# Read the number of test cases
# try:
#     N = int(input())
# except (ValueError, EOFError):
#     N = 0

# for _ in range(N):
#     try:
#         plate = input()
#     except EOFError:
#         break

#     # --- Validation ---
#     is_valid = True
    
#     # 1. Check length
#     if len(plate) != 8:
#         is_valid = False
    
#     # 2. Check first three characters (letters and uppercase) and hyphen
#     # and last four characters (digits)
#     # This block only runs if length is correct.
#     if is_valid:
#         letters = plate[0:3]
#         hyphen = plate[3]
#         digits = plate[4:8]
        
#         if not (letters.isalpha() and letters.isupper() and 
#                 hyphen == '-' and 
#                 digits.isdigit()):
#             is_valid = False

#     # --- Output ---
#     if not is_valid:
#         print("FAILURE")
#     else:
#         # Plate is valid, check the last digit
#         last_digit = plate[-1] # -1 index gets the last character
        
#         if last_digit in '12':
#             print("MONDAY")
#         elif last_digit in '34':
#             print("TUESDAY")
#         elif last_digit in '56':
#             print("WEDNESDAY")
#         elif last_digit in '78':
#             print("THURSDAY")
#         elif last_digit in '90':
#             print("FRIDAY")


# new_arr = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']
# n = map(int, input().split())
# sumation_n = sum(n)
# index = (sumation_n % 9) - 1
# print(new_arr[index])





# 2724 - Help Patatatitu
# try:
#     n = int(input())
# except (ValueError, EOFError):
#     n = 0
# for case_index in range(n):
#     try:
#         T = int(input())
#         dangerous_compounds = []
#         for _ in range(T):
#             dangerous_compounds.append(input().strip().lower())
#         U = int(input())
#         for _ in range(U):
#             experiment = input().strip().lower()
#             is_dangerous = False
#             for compound in  dangerous_compounds:
#                 if compound in experiment:
#                     is_dangerous = True
#                     break
#             if is_dangerous:
#                 print("Abortar")
#             else:
#                 print("Prossiga")
#     except (ValueError, EOFError):
#         continue
# "Secret Code" for Beecrowd 2727.


# while True:
#     try:
#         # Read the line and split it into parts
#         n = int(input())
#     except (ValueError, IndexError):
#         # Stop if input ends unexpectedly or line is empty
#         break
#     alpha = "abcdefghijklmnopqrstuvwxyz"

#     for _ in range(n):
#         code = input()
#         dot_group = code.split(" ")
#         print("dot_group ", dot_group)
#         num_groups = len(dot_group)
#         dots_per_group = len(dot_group[0])
#         print("num_groups ", num_groups)
#         print("dots_per_group ", dots_per_group)

#         index = (num_groups - 1) * 3 + (dots_per_group - 1)
#         print("index ", index)
#         print(alpha[index])


# n = int(input())
# name = input()
# doshes = "-"*37
# print(doshes)


# for i in range(n):
#     # print("|", " " * 35, "|")
#     print("|")
#     for i in range(35):
#         print(" ",name, end="")
#     print("|")
# print(doshes)    
# The top and bottom borders are 39 dash characters.
# We can create this string by multiplying the dash character by 39.



# # beecrowd | 2747
# # Output 1
# border_line = '-' * 39

# # The middle lines consist of a pipe, 37 spaces, and another pipe.
# middle_line = '|' + (' ' * 37) + '|'

# # Print the top border
# print(border_line)

# # Loop 5 times to print the middle section
# for _ in range(5):
#     print(middle_line)

# # Print the bottom border
# print(border_line)


# beecrowd | 2748
# Output 2

# print('-' * 39)  # Top border

# # Line 1: "Roberto"
# print('|' + ' ' * 8 + 'Roberto' + ' ' * (37 - 8 - len('Roberto')) + '|')

# # Line 2: blank
# print('|' + ' ' * 37 + '|')

# # Line 3: "5786"
# print('|' + ' ' * 8 + '5786' + ' ' * (37 - 8 - len('5786')) + '|')

# # Line 4: blank
# print('|' + ' ' * 37 + '|')

# # Line 5: "UNIFEI"
# print('|' + ' ' * 8 + 'UNIFEI' + ' ' * (37 - 8 - len('UNIFEI')) + '|')

# print('-' * 39)  # Bottom border
# Define the text and the content width for clarity
# text = "x = 35"
# width = 37

# # --- Print the 7 lines ---

# # Line 1
# print('-' * 39)

# # Line 2: Left-aligned text
# # The f-string formats the text to fill 37 characters, padding with spaces on the right.
# print(f"|{text:<{width}}|")

# # Line 3: Empty line
# print(f"|{' ' * width}|")

# # Line 4: Center-aligned text
# print(f"|{text:^{width}}|")

# # Line 5: Empty line
# print(f"|{' ' * width}|")

# # Line 6: Right-aligned text
# print(f"|{text:>{width}}|")

# # Line 7
# print('-' * 39)


# beecrowd | 2750 - Output 4

# Step 1: print the top line
# print("---------------------------------------")

# # Step 2: print the header
# print("| decimal   |  octal  |  Hexadecimal  |")

# # Step 3: print the separator line
# print("---------------------------------------")

# # Step 4: print the 16 rows (0 to 15)
# for i in range(16):
#     dec = i
#     octal = oct(i)[2:]           # remove '0o' prefix
#     hexa = hex(i)[2:].upper()    # remove '0x' and make uppercase
    
#     # Format each line with correct spacing
#     print(f"|{dec:7d}    |{octal:6s}   |{hexa:8s}      |")

# # Step 5: print the bottom line
# print("---------------------------------------")

# ---------------------------------------
# | decimal   |  octal  |  Hexadecimal  |
# ---------------------------------------
# |      0    |0        |0             |
# |      1    |1        |1             |
# |      2    |2        |2             |
# |      3    |3        |3             |
# |      4    |4        |4             |
# |      5    |5        |5             |
# |      6    |6        |6             |
# |      7    |7        |7             |
# |      8    |10       |8             |
# |      9    |11       |9             |
# |     10    |12       |A             |
# |     11    |13       |B             |
# |     12    |14       |C             |
# |     13    |15       |D             |
# |     14    |16       |E             |
# |     15    |17       |F             |
# ---------------------------------------




# beecrowd | 2774
# Sensor Accuracy



# import math
# import sys

# The program needs to read inputs until there are no more (End-of-File).
# while True:
#     try:
#         # Read the H, M line. We don't use these values.
#         # sys.stdin.readline() is good for EOF handling
#         line1 = sys.stdin.readline()
#         print("line1 ", line1)
#         if not line1:
#             break
        
#         # Read the line of measurements
#         measurements_str = sys.stdin.readline()
#         print("measurements_str ", measurements_str)
#         if not measurements_str:
#             break
        
#         # Convert the space-separated strings to a list of floats
#         measurements = list(map(float, measurements_str.split()))
#         print("measurements ", measurements)

#     except (EOFError, ValueError, IndexError):
#         break

#     # Get the number of measurements
#     QT = len(measurements)
#     print("QT ", QT)
    
#     # Handle the case where there's only one measurement (or none)
#     # to avoid division by zero in (QT - 1)
#     if QT < 2:
#         print("0.00000")
#         continue

#     # --- Calculate Standard Deviation ---
    
#     # 1. Calculate the mean (average)
#     mean = sum(measurements) / QT
#     print("mean ", mean)
#     # 2. Calculate the sum of the squared differences from the mean
#     sum_of_squared_diffs = 0
#     for x_i in measurements:
#         sum_of_squared_diffs += (x_i - mean) ** 2
#         print("sum_of_squared_diffs ", sum_of_squared_diffs)
#     # 3. Calculate the sample variance
#     variance = sum_of_squared_diffs / (QT - 1)
#     print("variance ", variance)
#     # 4. The standard deviation is the square root of the variance
#     std_dev = math.sqrt(variance)
    
#     # Print the result formatted to 5 decimal places
#     print(f"{std_dev:.5f}")

# "Board Size" (Beecrowd 2770)
# import sys
# while True:
#     try:
#         line = sys.stdin.readline()
#         if not line:
#             break
#         X,Y,M = map(int, line.split())
#     except (EOFError, ValueError):
#         break
    
#     board_long = max(X, Y)
#     board_short = min(X, Y)

#     for _ in range(M):
#         Xi, Yi = map(int, sys.stdin.readline().split())
#         piece_long = max(Xi, Yi)
#         piece_short = min(Xi, Yi)
#         if piece_long <= board_long and piece_short <= board_short:
#             print("Sim")
#         else:
#             print("Nao")

# beecrowd 2826 - Lexical

# A = input().strip()
# B = input().strip()

# if A < B:
#     print(A)
#     print(B)
# else:
#     print(B)
#     print(A)


# beecrowd | 2823 — Earliest Deadline First (EDF)
# Step 1: Read number of processes
# N = int(input())

# # Step 2: Initialize total utilization
# utilization = 0

# # Step 3: Read each task
# for _ in range(N):
#     C, P = map(int, input().split())
#     utilization += C / P

# # Step 4: Check EDF condition
# if utilization <= 1:
#     print("OK")
# else:
#     print("FAIL")



# try:
#     N = int(input())
# except (ValueError, EOFError):
#     N = 0

# # Track umbrellas currently at each location
# umbrellas_at_home = 0
# umbrellas_at_office = 0

# # Track total umbrellas purchased when leaving each location
# umbrellas_bought_for_home = 0
# umbrellas_bought_for_office = 0

# # Loop for N days
# for _ in range(N):
#     try:
#         # Read the forecasts for the day
#         to_work_forecast, to_home_forecast = input("working, home: ").split()
#     except (ValueError, EOFError):
#         break

#     # --- Morning Trip: Home to Office ---
#     if to_work_forecast == "chuva":
#         if umbrellas_at_home > 0:
#             # Use an existing umbrella from home
#             umbrellas_at_home -= 1
#             umbrellas_at_office += 1
#         else:
#             # No umbrella at home, must buy one
#             umbrellas_bought_for_home += 1
#             # The new umbrella is used and ends up at the office
#             umbrellas_at_office += 1
#         print("umbrellas_at_office ", umbrellas_at_office)
#         print("umbrellas_at_home ", umbrellas_at_home)
#         print("umbrellas_bought_for_home ", umbrellas_bought_for_home)
#         print("umbrellas_bought_for_office ", umbrellas_bought_for_office)
#     # --- Evening Trip: Office to Home ---
#     if to_home_forecast == "chuva":
#         if umbrellas_at_office > 0:
#             # Use an existing umbrella from the office
#             umbrellas_at_office -= 1
#             umbrellas_at_home += 1
#         else:
#             # No umbrella at the office, must buy one
#             umbrellas_bought_for_office += 1
#             # The new umbrella is used and ends up at home
#             umbrellas_at_home += 1
#         print("** umbrellas_at_office ", umbrellas_at_office)
#         print("** umbrellas_at_home ", umbrellas_at_home)
#         print("** umbrellas_bought_for_home ", umbrellas_bought_for_home)
#         print("** umbrellas_bought_for_office ", umbrellas_bought_for_office)
# # Print the final counts of purchased umbrellas
# print(f"{umbrellas_bought_for_home} {umbrellas_bought_for_office}")

# beecrowd 2813 - Avoiding Rain

# import sys

# def main():
#     data = sys.stdin.read().strip().split()
#     if not data:
#         return
#     it = iter(data)
#     N = int(next(it))
#     home = 0
#     office = 0
#     buy_home = 0
#     buy_office = 0

#     for _ in range(N):
#         sd = next(it)  # morning
#         sn = next(it)  # evening

#         # morning
#         if sd == "chuva":
#             if home > 0:
#                 home -= 1
#             else:
#                 buy_home += 1
#             office += 1  # umbrella arrives at office after trip

#         # evening
#         if sn == "chuva":
#             if office > 0:
#                 office -= 1
#             else:
#                 buy_office += 1
#             home += 1  # umbrella arrives at home after trip

#     print(buy_home, buy_office)

# if __name__ == "__main__":
#     main()
# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(input().strip())
# int_arr = list(map(int, arr))
# print("INT ARR", int_arr)
# arr_odd = []
# for i in int_arr:
#     if i % 2 == 0:
#         print("EVEN")
#     else:
#         print("ODD")
#         arr_odd.append(i)

# print("ODD LIST:", arr_odd)
# sorted_odd = sorted(arr_odd)
# print("ODD LIST: sorted", sorted_odd)

# new_arr_odd = []
# while arr_odd:
#     new_arr_odd.append(arr_odd.pop())
#     print("ODD LIST after pop:", arr_odd)
#     if arr_odd:
#         new_arr_odd.append(arr_odd.pop(0))
#         print("ODD LIST after pop(0):", arr_odd)

# print("FINAL ODD LIST:", new_arr_odd)


# # "Laércio" (Beecrowd 2812)
# # Read the number of test cases
# try:
#     N = int(input())
# except (ValueError, EOFError):
#     N = 0

# for _ in range(N):
#     try:
#         M = int(input())
#         numbers = list(map(int, input().split()))
#     except (ValueError, EOFError, IndexError):
#         continue

#     # Step 1: Filter to get only the odd numbers
#     odd_numbers = []
#     for num in numbers:
#         if num % 2 != 0:
#             odd_numbers.append(num)
            
#     # A more Pythonic way to filter:
#     # odd_numbers = [num for num in numbers if num % 2 != 0]

#     # Step 2: Sort the odd numbers. Sorting ascending is easiest.
#     odd_numbers.sort()
    
#     # Step 3: Arrange into the new pattern
#     result = []
    
#     # Continue as long as there are numbers to process
#     while odd_numbers: # An empty list evaluates to False
#         # Take the largest (last element) and remove it from the list
#         result.append(odd_numbers.pop())
        
#         # If the list is not empty after popping the largest,
#         # take the smallest (first element)
#         if odd_numbers:
#             result.append(odd_numbers.pop(0))
            
#     # Step 4: Print the result
#     # Convert all numbers in the result list to strings before joining
#     result_str_list = [str(num) for num in result]
#     print(" ".join(result_str_list))

# beecrowd 2808 - Knights Again

# def main():
#     start, end = input().split()

#     # Convert letters to numbers
#     print("ord('a')", ord('a') + 1, ord(start[0]), ord(end[0]))
#     x1 = ord(start[0]) - ord('a') + 1
#     print("x1 ", x1)
#     y1 = int(start[1])
#     print("y1 ", y1)
#     x2 = ord(end[0]) - ord('a') + 1
#     print("x2 ", x2)
#     y2 = int(end[1])
#     print("y2 ", y2)

#     # Compute absolute differences
#     dx = abs(x2 - x1)
#     print("dx ", dx)
#     dy = abs(y2 - y1)
#     print("dy ", dy)

#     # Check knight move
#     if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
#         print("VALIDO")
#     else:
#         print("INVALIDO")

# if __name__ == "__main__":
#     main()



# # Step 1: Read N
# N = int(input())

# # Step 2: Start the sequence with [1, 1]
# seq = [1, 1]

# # Step 3: Build sequence backwards (reverse Fibonacci)
# for i in range(2, N):
#     seq.append(seq[i - 1] + seq[i - 2])

# # Step 4: Reverse and print
# seq.reverse()
# print(" ".join(map(str, seq)))



# beecrowd | 2863
# Umil Bolt
# while True:
#     n = int(input())
#     arr = []
#     for i in range(n):
#         num = int(input())
#         arr.append(num)
#     print("ARRAY:", arr)
#     min_num = min(arr)
#     print("MIN:", min_num)



# # The program needs to read inputs until there are no more (End-of-File).
# # A while True loop with a try-except block is a standard way to handle this.
# while True:
#     try:
#         # Read the three ages from a single line.
#         # If the input stream is empty, input() will raise an EOFError.
#         line = input()
#         if not line: break
#         H, Z, L = map(int, line.split())
#         print("READ AGES:", H, Z, L)
#     except EOFError:
#         break
#     except (ValueError, IndexError):
#         # Handle cases where input might be malformed
#         break

#     # Put the ages into a list
#     ages = [H, Z, L]
    
#     # Sort the list to easily find the middle value
#     ages.sort()
#     print("SORTED AGES:", ages)
#     # The middle age is the element at index 1 of the sorted list
#     middle_age = ages[1]
#     print("MIDDLE AGE:", middle_age)
#     # Check which original variable corresponds to the middle age
#     if H == middle_age:
#         print("huguinho")
#     elif Z == middle_age:
#         print("zezinho")
#     else: # L must be the middle age
#         print("luisinho")




# beecrowd 3342 - Keanu

# n = int(input())

# total = n * n

# if n % 2 == 0:
#     white = black = total // 2
# else:
#     white = total // 2 + 1
#     black = total // 2

# print(f"{white} casas brancas e {black} casas pretas")
try:
    # Read N and X
    N, X = map(int, input().split())
    
    # Read the sequence of titan sizes
    titan_sizes = input() # The string of letters, e.g., "MPG"
    
    # Read the sizes of the titans: p, m, g.
    p, m, g = map(int, input().split())
except (ValueError, EOFError, IndexError):
    exit()

# Build a lookup table for converting titan types to sizes
size_map = {
    'P': p,
    'M': m,
    'G': g
}

# Initialize the number of walls
walls_needed = 0
current_wall_height = X

# Iterate through each titan
for titan_type in titan_sizes:
    titan_size = size_map[titan_type]

    # Check if the current wall can stop the titan.
    if titan_size <= current_wall_height:
        # Wall blocks the titan, reduce the wall's height
        current_wall_height -= titan_size
    else:
        # Titan is too big. Build a new wall of maximum size (X).
        walls_needed += 1
        # and reduces the remaining value
        current_wall_height = X - titan_size
        
# Print the total number of walls needed
print(walls_needed)


