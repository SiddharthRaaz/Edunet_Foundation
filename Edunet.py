import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate calories burned
def calculate_calories():
    try:
        weight = float(entry_weight.get())
        distance = float(entry_distance.get())
        time = float(entry_time.get())
        
        # Formula: Calories = Distance (km) × Weight (kg) × 1.036 (walking factor)
        calories = distance * weight * 1.036
        result_label.config(text=f"Calories Burned: {calories:.2f} kcal")
        
        # Store data for graph
        daily_data.append(calories)
        plot_graph()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")

# Function to plot daily calorie graph
def plot_graph():
    plt.clf()  # Clear previous plot
    days = np.arange(1, len(daily_data) + 1)
    plt.bar(days, daily_data, color='blue')
    plt.xlabel("Day")
    plt.ylabel("Calories Burned (kcal)")
    plt.title("Daily Fitness Progress")
    plt.show()

# Initialize main window
root = tk.Tk()
root.title("Personal Fitness Tracker")
root.geometry("400x300")

# Global list to store daily calories
daily_data = []

# GUI Elements
label_weight = tk.Label(root, text="Enter Weight (kg):")
label_weight.pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

label_distance = tk.Label(root, text="Enter Distance Walked (km):")
label_distance.pack(pady=5)
entry_distance = tk.Entry(root)
entry_distance.pack()

label_time = tk.Label(root, text="Enter Time Exercised (min):")
label_time.pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_calories)
calculate_button.pack(pady=20)

result_label = tk.Label(root, text="Calories Burned: 0 kcal", font=("Arial", 12))
result_label.pack(pady=10)

# Start the application
root.mainloop()