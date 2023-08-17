from tabulate import tabulate


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles


def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers


def pounds_to_kilograms(pounds):
    kilograms = pounds * 0.453592
    return kilograms


def inches_to_centimeters(inches):
    centimeters = inches * 2.54
    return centimeters


def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet


def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters


def ounces_to_grams(ounces):
    grams = ounces * 28.3495
    return grams


def square_meters_to_square_feet(square_meters):
    square_feet = square_meters * 10.7639
    return square_feet


def main():
    end = "n"
    while end != "y":
        table = [
            ["1.", "Celsius to Fahrenheit"],
            ["2.", "Fahrenheit to Celsius"],
            ["3.", "Kilometers to Miles"],
            ["4.", "Miles to Kilometers"],
            ["5.", "Pounds to Kilograms"],
            ["6.", "Inches to Centimeters"],
            ["7.", "Meters to Feet"],
            ["8.", "Gallons to Liters"],
            ["9.", "Ounces to Grams"],
            ["10.", "Square Meters to Square Feet"],
        ]
        headers = [
            "#",
            "Unit Conversion Tool",
        ]
        print(tabulate(table, headers, tablefmt="rounded_grid"))

        choice = int(input("Enter your choice: "))

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
            kilometers = float(input("Enter distance in kilometers: "))
            miles = kilometers_to_miles(kilometers)
            print(f"{kilometers} km is {miles:.2f} miles")
            print()
            end = input("Want to quit?(y/n) ")

        elif choice == 4:
            miles = float(input("Enter distance in miles: "))
            kilometers = miles_to_kilometers(miles)
            print(f"{miles} miles is {kilometers:.2f} km")
            print()
            end = input("Want to quit?(y/n) ")

        elif choice == 5:
            pounds = float(input("Enter weight in pounds: "))
            kilograms = pounds_to_kilograms(pounds)
            print(f"{pounds} lbs is {kilograms:.2f} kg")
            print()
            end = input("Want to quit?(y/n) ")

        elif choice == 6:
            inches = float(input("Enter length in inches: "))
            centimeters = inches_to_centimeters(inches)
            print(f"{inches} inches is {centimeters:.2f} cm")
            print()
            end = input("Want to quit?(y/n) ")

        elif choice == 7:
            meters = float(input("Enter length in meters: "))
            feet = meters_to_feet(meters)
            print(f"{meters} meters is {feet:.2f} feet")
            print()
            end = input("Want to quit?(y/n) ")

        elif choice == 8:
            gallons = float(input("Enter volume in gallons: "))
            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is {liters:.2f} liters")
            print()
            end = input("Want to quit?(y/n) ")

        elif choice == 9:
            ounces = float(input("Enter weight in ounces: "))
            grams = ounces_to_grams(ounces)
            print(f"{ounces} ounces is {grams:.2f} grams")
            print()
            end = input("Want to quit?(y/n) ")

        elif choice == 10:
            square_meters = float(input("Enter area in square meters: "))
            square_feet = square_meters_to_square_feet(square_meters)
            print(f"{square_meters} square meters is {square_feet:.2f} square feet")
            print()
            end = input("Want to quit?(y/n) ")

        else:
            print("Invalid choice")
            print()
            end = input("Want to quit?(y/n) ")


if __name__ == "__main__":
    main()
