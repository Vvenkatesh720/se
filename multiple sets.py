#Weather modeling with multiple sets of input
def simulate_weather(a, b, c, day_num):
    print(f"\nDay {day_num} Temperature Simulation:")
    print("Hour\tTemperature (°C)")
    for hour in range(25):
        # Using the quadratic formula: y = ax² + bx + c
        temp = a * hour**2 + b * hour + c
        print(f"{hour:02d}\t{temp:.2f}")
def get_coefficients_from_user(day_num):
    print(f"\nEnter the coefficients for Day {day_num}:")
    while True:
        try:
            a = float(input("Enter coefficient a (quadratic term): "))
            b = float(input("Enter coefficient b (linear term): "))
            c = float(input("Enter coefficient c (constant term): "))
            return a, b, c
        except ValueError:
            print("Invalid input. Please enter numeric values for a, b, and c.")
def weather_modeling():
    try:
        num_days = int(input("Enter the number of days to simulate: "))
        if num_days <= 0:
            print("Number of days must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a positive integer for the number of days.")
        return
    for day_num in range(1, num_days + 1):
        a, b, c = get_coefficients_from_user(day_num)
        simulate_weather(a, b, c, day_num)
weather_modeling()
