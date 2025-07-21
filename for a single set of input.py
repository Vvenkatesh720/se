# Stage 4: Weather modeling using a single set of input coefficients
a = -0.1 
b = 2.4  
c = 10   
print("Hour\tTemperature (°C)")
for hour in range(25):  
    temp = a * hour**2 + b * hour + c
    print(f"{hour:02d}\t{temp:.2f}")
