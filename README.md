# Disease Spread Simulation

## Overview
This simulation program is designed to visually represent the spreading dynamics of diseases similar to COVID-19. It allows users to explore how different factors, such as vaccination rates, infection rates, and social distancing measures, affect the spread and control of infectious diseases.

## Setup
Before running the simulation, please follow these setup instructions:

### Directories and Fonts
- **Create Directories**: Ensure that two directories, `figures` and `fonts`, are created in the same directory as the `main.py` file.
- **Fonts**: Copy your `.ttf` font files into the `fonts` directory. The simulation uses these fonts to render text on-screen for statistics and information display.

### Configuration
The simulation settings can be customized through the `settings.json` file, which should be located in the same directory as `main.py`. If the file does not exist, the program will prompt you to input initial parameters upon startup, and a new `settings.json` file will be generated accordingly.

### Running the Simulation
Execute the `main.py` script to start the simulation. During runtime, the simulation window will display real-time statistics, including the total number of individuals, the count of healthy, infected, vaccinated, and recovered individuals, alongside the number of days the simulation has been running.

## Key Features
- **Real-Time Statistics**: View how the disease spreads through a population over time with updates on various health statuses displayed live.
- **Interactive Controls**: Use the `Esc` key at any time to exit the simulation.
- **Data Visualization**: Upon exiting, the simulation results are plotted and saved in the `figures` directory, showing the progression of the disease and the impact of interventions over time.

## Enhancements in the Latest Version
- Improved display resolution and visualization for a more detailed view.
- Adjustments to dot size for better visibility of simulation entities.
- Updated the statistics display functionality for enhanced real-time data monitoring.

## Requirements
- Python 3.x
- Pygame
- Matplotlib

Ensure all required libraries are installed using pip:
```
pip install pygame matplotlib
```

## Contribution
Contributions to the simulation are welcome! If you have suggestions for improvements or have found bugs, please feel free to open an issue or submit a pull request.
