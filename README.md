# Temperature Controller Program

This program simulates a temperature control system that manages the heating process based on the current temperature and a target setpoint. The system alternates between heating and cooling phases to maintain the temperature around the desired setpoint.

## Features:
- **Set Temperature**: The user can define a target temperature (default: 25°C).
- **Initial Temperature**: The system starts with an initial temperature (default: 18°C).
- **Minimum Temperature**: If the temperature falls below a certain threshold (default: 20°C), the heating is activated.
- **State**: The system can either be in a heating state ("ON") or cooling state ("OFF").
- **Time-Driven Updates**: The system updates every second, either cooling or heating depending on the current state.

## Process:
- **Cooling Phase ("OFF")**: When the system is in the "OFF" state, the temperature decreases by 0.1°C per second.
- **Heating Phase ("ON")**: When the system is in the "ON" state, the temperature increases by 1°C per second.

## State Transition:
- The system transitions to the "ON" state if the current temperature is below the minimum threshold and has been in the "OFF" state for more than 40 seconds.
- The system transitions back to the "OFF" state if the temperature reaches the setpoint or the system has been heating for 20 seconds.

## Simulation for 300 seconds:
The program runs for a total of 300 seconds, during which the temperature fluctuates between heating and cooling phases.  
The temperature and time are tracked, and at the end of the simulation, a plot of the temperature over time is displayed.

## Example Run:
- **Set Temperature**: 25°C
- **Initial Temperature**: 18°C
- **Minimum Temperature**: 20°C
- **Total Simulation Time**: 300 seconds

The plot visualizes the temperature changes over the simulation time, showing periods of heating and cooling. The system attempts to maintain the temperature near 25°C, cooling when necessary and heating when the temperature drops below the threshold.

<div id="header" align="center">
  <img src="https://github.com/AveRake/Heating-Control/blob/main/diagram.png?raw=true" width="100%"/>
</div>
