# Stage 2: User input for quadratic model coefficients
a = float(input("Enter coefficient a (controls the curvature): "))
b = float(input("Enter coefficient b (controls the slope): "))
c = float(input("Enter coefficient c (base temperature at hour 0): "))
print("\nHour\tTemperature (°C)")
for hour in range(25):  # 0 to 24 hours
    temp = a * hour**2 + b * hour + c
    print(f"{hour:02d}\t{temp:.2f}")
