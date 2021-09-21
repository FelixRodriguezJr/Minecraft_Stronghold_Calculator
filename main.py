import math
import sys

inputY = "Y"

while str(inputY) == "Y":
    try:
        print("")
        inputX = int(input("Enter the X coordinate: "))
        inputZ = int(input("Enter the Z coordinate: "))
    except ValueError:
        print("Input a number!")
        sys.exit()


    print("")

    distance = math.sqrt(math.pow(inputX, 2) + math.pow(inputZ, 2))

    try:
        theta0 = math.atan(inputX / inputZ)
    except ZeroDivisionError:
        theta0 = math.atan(inputX / 0.000001)

    theta1 = math.radians(360 / 3)
    theta2 = math.radians(360 / 6)
    theta3 = math.radians(360 / 10)
    theta4 = math.radians(360 / 15)
    theta5 = math.radians(360 / 21)
    theta6 = math.radians(360 / 28)
    theta7 = math.radians(360 / 36)
    theta8 = math.radians(360 / 9)

    count = 1

    def calc(n, theta, i):
        value_x = int(math.floor(1 + ((i - 1) * 1.5)) * 2048 * math.cos(theta0 + (theta * n)))
        value_z = int(math.floor(1 + ((i - 1) * 1.5)) * 2048 * math.sin(theta0 + (theta * n)))
        print("Coordinate #" + str(n) + " (" + str(value_x) + ", " + str(value_z) + ")")

    if 1280 <= distance <= 2816:
        while count < 3:
            calc(count, theta1, 1)
            count += 1

    elif 4352 <= distance <= 5888:
        while count < 6:
            calc(count, theta2, 2)
            count += 1

    elif 7424 <= distance <= 8960:
        while count < 10:
            calc(count, theta3, 3)
            count += 1

    elif 10496 <= distance <= 12032:
        while count < 15:
            calc(count, theta4, 4)
            count += 1

    elif 13568 <= distance <= 15104:
        while count < 21:
            calc(count, theta5, 5)
            count += 1

    elif 16640 <= distance <= 18176:
        while count < 28:
            calc(count, theta6, 6)
            count += 1

    elif 19712 <= distance <= 21248:
        while count < 36:
            calc(count, theta7, 7)
            count += 1

    elif 22784 <= distance <= 23552:
        while count < 9:
            calc(count, theta8, 8)
            count += 1

    else:
        print("No strongholds detected.")

    print("")
    inputY = input("Try again <Y/N>: ").upper()