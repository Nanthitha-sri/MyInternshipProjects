def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles * 1.60934

def km_to_meters(km):
    return km * 1000

def meters_to_km(meters):
    return meters / 1000

def meters_to_yards(meters):
    return meters * 1.09361

def yards_to_meters(yards):
    return yards / 1.09361

def meters_to_feet(meters):
    return meters * 3.28084

def feet_to_meters(feet):
    return feet / 3.28084

def meters_to_inches(meters):
    return meters * 39.3701

def inches_to_meters(inches):
    return inches / 39.3701

def main():
    print("Select conversion:")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Kilometers to Meters")
    print("4. Meters to Kilometers")
    print("5. Meters to Yards")
    print("6. Yards to Meters")
    print("7. Meters to Feet")
    print("8. Feet to Meters")
    print("9. Meters to Inches")
    print("10. Inches to Meters")
    
    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} kilometers = {km_to_miles(km)} miles")
    elif choice == 2:
        miles = float(input("Enter distance in miles: "))
        print(f"{miles} miles = {miles_to_km(miles)} kilometers")
    elif choice == 3:
        km = float(input("Enter distance in kilometers: "))
        print(f"{km} kilometers = {km_to_meters(km)} meters")
    elif choice == 4:
        meters = float(input("Enter distance in meters: "))
        print(f"{meters} meters = {meters_to_km(meters)} kilometers")
    elif choice == 5:
        meters = float(input("Enter distance in meters: "))
        print(f"{meters} meters = {meters_to_yards(meters)} yards")
    elif choice == 6:
        yards = float(input("Enter distance in yards: "))
        print(f"{yards} yards = {yards_to_meters(yards)} meters")
    elif choice == 7:
        meters = float(input("Enter distance in meters: "))
        print(f"{meters} meters = {meters_to_feet(meters)} feet")
    elif choice == 8:
        feet = float(input("Enter distance in feet: "))
        print(f"{feet} feet = {feet_to_meters(feet)} meters")
    elif choice == 9:
        meters = float(input("Enter distance in meters: "))
        print(f"{meters} meters = {meters_to_inches(meters)} inches")
    elif choice == 10:
        inches = float(input("Enter distance in inches: "))
        print(f"{inches} inches = {inches_to_meters(inches)} meters")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
