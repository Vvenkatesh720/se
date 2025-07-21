# Stage 1: Hard-coded quadratic model for temperature over a 24-hour period
a = -0.1     
b = 2.4      
c = 10         
print("Hour\tTemperature (°C)")
for hour in range(25):  # 0 to 24
    temp = a * hour**2 + b * hour + c
    print(f"{hour:02d}\t{temp:.2f}")
