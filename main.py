"""
Unit Conversion Tool
Name: Prashant Subedi
From: Kathmandu, Nepal
"""

from tabulate import tabulate
import cowsay


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 2)


def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621
    return round(miles, 2)


def miles_to_kilometers(miles):
    kilometers = miles * 1.609
    return round(kilometers, 2)


def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return round(centimeters, 2)


def centimeters_to_inches(centimeters):
    inches = centimeters / 2.54
    return round(inches, 2)


def meters_to_feet(meters):
    feet = meters * 3.280
    return round(feet, 2)


def feet_to_meters(feet):
    meters = feet / 3.280
    return round(meters, 2)


def pounds_to_kilograms(pounds):
    kilograms = pounds * 0.453
    return round(kilograms, 2)


def kilograms_to_pounds(kilograms):
    pounds = kilograms / 0.453
    return round(pounds, 2)


def ounces_to_grams(ounces):
    grams = ounces * 28.349
    return round(grams, 2)


def grams_to_ounces(grams):
    ounces = grams / 28.349
    return round(ounces, 2)


def gallons_to_liters(gallons):
    liters = gallons * 3.785
    return round(liters, 2)


def liters_to_gallons(liters):
    gallons = liters / 3.785
    return round(gallons, 2)


def square_meters_to_square_feet(square_meters):
    square_feet = square_meters * 10.763
    return round(square_feet, 2)


def square_feet_to_square_meters(square_feet):
    square_meters = square_feet / 10.763
    return round(square_meters, 2)


def conv():
    conv = None
    table = [
        ["1.", "Temperature conversion"],
        ["2.", "Length conversion"],
        ["3.", "Weight conversion"],
        ["4.", "Volume conversion"],
        ["5.", "Area conversion"],
        ["6.", "Quit ✕"],
    ]
    headers = [
        "#",
        "Unit Conversion Tool",
    ]
    print()
    print(tabulate(table, headers, tablefmt="rounded_grid"))
    try:
        conv = int(input("Enter which conversion do you want: "))
    except:
        pass
    return conv


def main():
    end = "n"
    while end != "y":
        try:
            choice = None
            match conv():
                case 1:
                    table_sub = [
                        ["1.", "Celsius to Fahrenheit"],
                        ["2.", "Fahrenheit to Celsius"],
                        ["3.", "Return back ↩"],
                        ["4.", "Quit ✕"],
                    ]
                    headers_sub = [
                        "#",
                        "Temperature conversion",
                    ]
                    print()
                    print(tabulate(table_sub, headers_sub, tablefmt="rounded_grid"))

                    try:
                        choice = int(input("Enter your choice: "))
                    except:
                        pass

                    if choice == 1:
                        celsius = float(input("Enter temperature in Celsius: "))
                        fahrenheit = celsius_to_fahrenheit(celsius)
                        print(f"{celsius}°C is {fahrenheit:.2f}°F")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 2:
                        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                        celsius = fahrenheit_to_celsius(fahrenheit)
                        print(f"{fahrenheit}°F is {celsius:.2f}°C")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 3:
                        continue

                    elif choice == 4:
                        end = "y"

                    else:
                        print("Invalid choice")
                        print()
                        end = input("Want to quit?(y/n) ")

                case 2:
                    table_sub = [
                        ["1.", "Kilometers to Miles"],
                        ["2.", "Miles to Kilometers"],
                        ["3.", "Inches to Centimeters"],
                        ["4.", "Centimeters to Inches"],
                        ["5.", "Meters to Feet"],
                        ["6.", "Feet to Meters"],
                        ["7.", "Return back ↩"],
                        ["8.", "Quit ✕"],
                    ]
                    headers_sub = [
                        "#",
                        "Length conversion",
                    ]
                    print()
                    print(tabulate(table_sub, headers_sub, tablefmt="rounded_grid"))

                    try:
                        choice = int(input("Enter your choice: "))
                    except:
                        pass

                    if choice == 1:
                        kilometers = float(input("Enter distance in kilometers: "))
                        miles = kilometers_to_miles(kilometers)
                        print(f"{kilometers} km is {miles:.2f} miles")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 2:
                        miles = float(input("Enter distance in miles: "))
                        kilometers = miles_to_kilometers(miles)
                        print(f"{miles} miles is {kilometers:.2f} km")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 3:
                        inches = float(input("Enter length in inches: "))
                        centimeters = inches_to_centimeters(inches)
                        print(f"{inches} inches is {centimeters:.2f} cm")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 4:
                        centimeters = float(input("Enter length in centimeters: "))
                        inches = centimeters_to_inches(centimeters)
                        print(f"{centimeters} cm is {inches:.2f} inches")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 5:
                        meters = float(input("Enter length in meters: "))
                        feet = meters_to_feet(meters)
                        print(f"{meters} meters is {feet:.2f} feet")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 6:
                        feet = float(input("Enter length in feet: "))
                        meters = feet_to_meters(feet)
                        print(f"{feet} feet is {meters:.2f} meters")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 7:
                        continue

                    elif choice == 8:
                        end = "y"

                    else:
                        print("Invalid choice")
                        print()
                        end = input("Want to quit?(y/n) ")

                case 3:
                    table_sub = [
                        ["1.", "Pounds to Kilograms"],
                        ["2.", "Kilograms to Pounds"],
                        ["3.", "Ounces to Grams"],
                        ["4.", "Grams to Ounces"],
                        ["5.", "Return back ↩"],
                        ["6.", "Quit ✕"],
                    ]
                    headers_sub = [
                        "#",
                        "Weight conversion",
                    ]
                    print()
                    print(tabulate(table_sub, headers_sub, tablefmt="rounded_grid"))

                    try:
                        choice = int(input("Enter your choice: "))
                    except:
                        pass

                    if choice == 1:
                        pounds = float(input("Enter weight in pounds: "))
                        kilograms = pounds_to_kilograms(pounds)
                        print(f"{pounds} lbs is {kilograms:.2f} kg")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 2:
                        kilograms = float(input("Enter weight in kilograms: "))
                        pounds = kilograms_to_pounds(kilograms)
                        print(f"{kilograms} kg is {pounds:.2f} lbs")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 3:
                        ounces = float(input("Enter weight in ounces: "))
                        grams = ounces_to_grams(ounces)
                        print(f"{ounces} ounces is {grams:.2f} grams")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 4:
                        grams = float(input("Enter weight in grams: "))
                        ounces = grams_to_ounces(grams)
                        print(f"{grams} g is {ounces:.2f} oz")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 5:
                        continue

                    elif choice == 6:
                        end = "y"

                    else:
                        print("Invalid choice")
                        print()
                        end = input("Want to quit?(y/n) ")

                case 4:
                    table_sub = [
                        ["1.", "Gallons to Liters"],
                        ["2.", "Liters to Gallons"],
                        ["3.", "Return back ↩"],
                        ["4.", "Quit ✕"],
                    ]
                    headers_sub = [
                        "#",
                        "Volume conversion",
                    ]
                    print()
                    print(tabulate(table_sub, headers_sub, tablefmt="rounded_grid"))

                    try:
                        choice = int(input("Enter your choice: "))
                    except:
                        pass

                    if choice == 1:
                        gallons = float(input("Enter volume in gallons: "))
                        liters = gallons_to_liters(gallons)
                        print(f"{gallons} gallons is {liters:.2f} liters")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 2:
                        liters = float(input("Enter volume in liters: "))
                        gallons = liters_to_gallons(liters)
                        print(f"{liters} liters is {gallons:.2f} gallons")
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 3:
                        continue

                    elif choice == 4:
                        end = "y"

                    else:
                        print("Invalid choice")
                        print()
                        end = input("Want to quit?(y/n) ")

                case 5:
                    table_sub = [
                        ["1.", "Square Meters to Square Feet"],
                        ["2.", "Square Feet to Square Meters"],
                        ["3.", "Return back ↩"],
                        ["4.", "Quit ✕"],
                    ]
                    headers_sub = [
                        "#",
                        "Weight conversion",
                    ]
                    print()
                    print(tabulate(table_sub, headers_sub, tablefmt="rounded_grid"))

                    try:
                        choice = int(input("Enter your choice: "))
                    except:
                        pass

                    if choice == 1:
                        square_meters = float(input("Enter area in square meters: "))
                        square_feet = square_meters_to_square_feet(square_meters)
                        print(
                            f"{square_meters} square meters is {square_feet:.2f} square feet"
                        )
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 2:
                        square_feet = float(input("Enter area in square feet: "))
                        square_meters = square_feet_to_square_meters(square_feet)
                        print(
                            f"{square_feet} square feet is {square_meters:.2f} square meters"
                        )
                        print()
                        end = input("Want to quit?(y/n) ")

                    elif choice == 3:
                        continue

                    elif choice == 4:
                        end = "y"

                    else:
                        print("Invalid choice")
                        print()
                        end = input("Want to quit?(y/n) ")

                case 6:
                    end = "y"

                case _:
                    print("Invalid choice")
                    print()
                    end = input("Want to quit?(y/n) ")

        except:
            print("Only accepts number")
            print()
            end = input("Want to quit?(y/n) ")
    cowsay.cow("Thanks for using the Unit Conversion Tool")


if __name__ == "__main__":
    main()
