# Function to perform float division and floor division
def division_operations(a, b):
    # Float division
    float_result = a / b
    
    # Floor division
    floor_result = a // b
    
    return float_result, floor_result

# Example values
numerator = 10
denominator = 3

# Perform division operations
float_result, floor_result = division_operations(numerator, denominator)

# Display results
print(f"Float Division Result: {float_result}")
print(f"Floor Division Result: {floor_result}")
