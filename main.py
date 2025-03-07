import time
import numpy as np
import matplotlib.pyplot as plt

class TemperatureController:
    def __init__(self, set_temp=25, initial_temp=18, min_temp=20):
        self.set_temp = set_temp  # target temperature
        self.current_temp = initial_temp  # current temperature
        self.min_temp = min_temp  # minimum threshold for heating activation
        self.state = "OFF"  # initial state
        self.time_in_state = 0
    
    def update(self, dt=1):
        """Updates the system state every dt seconds."""
        if self.state == "OFF":
            self.time_in_state += dt
            self.current_temp -= 0.1  # cooling (-0.1 degree per second)
            if self.current_temp < 18:
                self.current_temp = 18  # prevent temperature from dropping too low
            if self.time_in_state >= 40 and self.current_temp < self.min_temp:
                self.state = "ON"
                self.time_in_state = 0
        
        elif self.state == "ON":
            self.time_in_state += dt
            self.current_temp += 1  # heating (+1 degree per second)
            if self.time_in_state >= 20 or self.current_temp >= self.set_temp:
                self.state = "OFF"
                self.time_in_state = 0
                
    def run(self, total_time, dt=1):
        """Runs the simulation for total_time seconds and returns time and temperature data."""
        time_data = np.arange(0, total_time, dt)  # Create a numpy array for time
        temp_data = np.zeros_like(time_data)  # Initialize an array to store temperature data
        
        for i, t in enumerate(time_data):
            self.update(dt)
            temp_data[i] = self.current_temp  # Store temperature in numpy array
            # Printing the state and temperature in the console
            print(f"Time: {t}s | Temperature: {self.current_temp:.1f}°C | State: {self.state}")
            time.sleep(0.1)  # for better visualization
        
        return time_data, temp_data

if __name__ == "__main__":
    while True:
        try:
            user_time = int(input("Enter simulation time (in seconds): "))
            controller = TemperatureController()
            time_data, temp_data = controller.run(user_time)
            
            # Plotting the results
            plt.plot(time_data, temp_data, label="Temperature")
            plt.xlabel("Time (s)")
            plt.ylabel("Temperature (°C)")
            plt.title("Temperature Controller Simulation")
            plt.grid(True)
            plt.legend()
            plt.show()
            
            repeat = input("Do you want to run again? (yes/no): ").strip().lower()
            if repeat != "yes":
                print("Exiting program.")
                break
        except ValueError:
            print("Error: Please enter an integer.")
