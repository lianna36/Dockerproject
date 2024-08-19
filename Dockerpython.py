import numpy as np
import pandas as pd

# Generate a random integer using numpy
random_integer = np.random.randint(1, 101)
print(f"Random integer: {random_integer}")

# Generate a random float between 0 and 1 using numpy
random_float = np.random.rand()
print(f"Random float: {random_float}")

# Generate a random float between two values (e.g., 5.5 and 20.5) using numpy
random_float_range = np.random.uniform(5.5, 20.5)
print(f"Random float in range: {random_float_range}")

# Create a Pandas DataFrame with random integers
df_random_integers = pd.DataFrame(np.random.randint(1, 101, size=(5, 3)), columns=['A', 'B', 'C'])
print("\nDataFrame with random integers:\n", df_random_integers)

# Create a Pandas DataFrame with random floats
df_random_floats = pd.DataFrame(np.random.rand(5, 3), columns=['A', 'B', 'C'])
print("\nDataFrame with random floats:\n", df_random_floats)