 #!/usr/bin/env python3
numbers = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {numbers}")
new_array = [x + 2 for x in numbers if x > 5]
print(f"New_array:{new_array}")