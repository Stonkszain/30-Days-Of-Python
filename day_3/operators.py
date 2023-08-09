import math

age = 20
height = 169.9
comp_num = 2 + 3j

# print("Triangle area calculator")
# # Get user input
# t_base = float(input("Enter base: ")) 
# t_height = float(input("Enter height: ")) 
# # calculate area using formula
# print(f'The area of the triangle is {0.5 * t_base * t_height}')

# print("Triangle perimeter calculator")
# # Get user input
# side_a = float(input("Enter side a: "))
# side_b = float(input("Enter side b: "))
# side_c = float(input("Enter side c: "))
# # calculate using formula
# print(f'The perimeter of the triangle is {side_a + side_b + side_c}')

# print("Rectangle area and perimeter calculator")
# # Get user input
# r_len = float(input("Enter length: "))
# r_wid = float(input("Enter width: "))

# # calculate area and print
# print(f"The area of the rectangle is {r_len * r_wid}")
# print(f"The perimeter of the rectangle is {(r_len + r_wid) * 2}")

# print("Circle area and circumference calculator")
# # Get user input
# radius = float(input("Enter radius: "))
# # Using formulae and printing
# print(f"The area of the circle is {math.pi * radius ** 2}" +
#       f" and the perimeter is {math.pi * radius * 2 }")

# slope = 2
# x_intercept = (0 - 2) / 2
# y_intercept = 2 * 0 - 2
# print(f"Slope: {slope}\nx intercept: {x_intercept}\ny intercept: {y_intercept}")

# m = (2-10)/(2-6)
# euc_dist = ( (2-6) ** 2 + (2-10) ** 2 ) ** 0.5
# print(f"The slope of point (2, 2) and point (6,10) is {m} and the euclidian distance" +
#       f" is {euc_dist}")

# x = -3
# y = x ** 2 + 6 * x + 9
# print(f"When x is {x}, y is {y}")

# print(len("python") != len("dragon"))

# print("on" in "python" and "a" in "dragon")

# print("jargon" in "I hope this course is not full of jargon")

# print("on" not in "python" and "a" not in "dragon")

# print(str(float(len('python'))))

# checking_num = 12
# print(f"Is {checking_num} divisible by 2? {checking_num % 2 == 0}")

# print((7 // 3) == int(2.7))

# print(type('10') == type(10))

# print(int(9.8) == 10)

# hours = int(input("Enter hours: "))
# rate = float(input("Enter rate per hour: "))
# print(f"Your weekly earning is {rate * hours}")

# years = int(input("Enter the number of years you have lived: "))
# print(f"You have lived for {years * 365.25 * 24 * 60 * 60}")

weird_table = [[1,1,1,1,1],[2,1,2,4,8],[3,1,3,9,27],[4,1,4,16,64],[5,1,5,25,125]]

for i in weird_table:
    for j in i:
        print(j, " " , end="")
    print()