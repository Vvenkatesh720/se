# Stage 3: Reading coefficients from a file

# Function to read coefficients from a file
def read_coefficients(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Extracting coefficients from the file lines
            a = float(lines[0].split(':')[1].strip())
            b = float(lines[1].split(':')[1].strip())
            c = float(lines[2].split(':')[1].strip())
            return a, b, c
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None, None, None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None, None

# Read coefficients from the file
filename = 'coefficients.txt'  # Make sure this file exists in the same directory
a, b, c = read_coefficients(filename)

if a is not None and b is not None and c is not None:
    # Simulate hourly temperature over 24 hours
    print("\nHour\tTemperature (°C)")
    for hour in range(25):  # 0 to 24 hours
        temp = a * hour**2 + b * hour + c
        print(f"{hour:02d}\t{temp:.2f}")
