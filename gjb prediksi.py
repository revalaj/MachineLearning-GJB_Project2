import numpy as np
import pandas as pd
from sklearn import svm
import matplotlib.pyplot as plt

# Function to generate data for free fall motion
def generate_free_fall_data():
    t_values = np.linspace(0, 2.4, 100)
    x_values = 0.5 * 9.8 * t_values**2  # Position for free fall: x(t) = (1/2) * g * t^2
    v_values = 9.8 * t_values  # Velocity for free fall: v(t) = g * t

    data = {'t': t_values, 'Position': x_values, 'Velocity': v_values}
    return pd.DataFrame(data)

# Generate free fall data
free_fall_data = generate_free_fall_data()

# Creating SVR model for Position
clf_position = svm.SVR()
clf_position.fit(free_fall_data[['t']], free_fall_data['Position'])

# Creating SVR model for Velocity
clf_velocity = svm.SVR()
clf_velocity.fit(free_fall_data[['t']], free_fall_data['Velocity'])

# Making predictions for some specific time values
time_values = np.linspace(0, 2.4, 10).reshape(-1, 1)
predictions_position = clf_position.predict(time_values)
predictions_velocity = clf_velocity.predict(time_values)

# Creating subplot with 2 rows and 2 columns
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plotting Position vs Time
axs[0, 0].plot(free_fall_data['t'], free_fall_data['Position'], color='black', label='Actual Position')
axs[0, 0].plot(time_values, predictions_position, color='red', label='Predicted Position')
axs[0, 0].set_ylabel('Position')
axs[0, 0].legend()

# Plotting Velocity vs Time
axs[0, 1].plot(free_fall_data['t'], free_fall_data['Velocity'], color='blue', label='Actual Velocity')
axs[0, 1].plot(time_values, predictions_velocity, color='green', label='Predicted Velocity')
axs[0, 1].set_ylabel('Velocity')
axs[0, 1].legend()

# Plotting Position vs Velocity
axs[1, 0].scatter(free_fall_data['Position'], free_fall_data['Velocity'], color='purple', label='Actual Position vs Velocity')
axs[1, 0].set_xlabel('Position')
axs[1, 0].set_ylabel('Velocity')
axs[1, 0].legend()

# Plotting Predicted Position vs Predicted Velocity
axs[1, 1].scatter(predictions_position, predictions_velocity, color='orange', label='Predicted Position vs Velocity')
axs[1, 1].set_xlabel('Predicted Position')
axs[1, 1].set_ylabel('Predicted Velocity')
axs[1, 1].legend()

# Displaying the predictions
for time, position, velocity in zip(time_values, predictions_position, predictions_velocity):
    print(f"Time = {time[0]:.2f} s, Predicted (Position, Velocity) = ({position:.2f} m, {velocity:.2f} m/s) ")

plt.show()
