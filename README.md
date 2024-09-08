# Disease Spread Simulation with Vaccination and Isolation Scenarios

## Description

This project is a Pygame-based simulation of the spread of a disease in a population. It takes into account multiple variables such as infection rate, mortality rate, probability of reinfection, vaccination efficacy, and the impact of isolation. The simulation visualizes how these factors influence the evolution of the population's health status over time, allowing for the exploration of different disease scenarios with and without vaccination and isolation.

The simulation displays key metrics such as the number of healthy, infected, vaccinated, recovered, and deceased individuals, and it plots these statistics over time using Matplotlib.

## Features

- **Disease Simulation**: Models disease spread in a population based on configurable infection, mortality, and reinfection rates.
- **Vaccination and Isolation**: Simulates the effects of vaccination and population isolation on disease control.
- **Real-time Statistics**: Displays the number of healthy, infected, vaccinated, recovered, and deceased individuals in real time.
- **Plotting**: Saves a graph of the simulation results at the end of each run.
- **Customizable Parameters**: The simulation parameters such as infection rate, mortality rate, vaccine efficacy, and more can be adjusted to test different scenarios.

## Requirements

- **Python 3.x**
- **Pygame**: For running the simulation.
- **Matplotlib**: For generating the statistical plots.
- **Pillow**: Optional, if using custom fonts for the interface.

### Install dependencies

```bash
pip install pygame matplotlib pillow
```

## Usage

1. **Configure the simulation**:
   - Before running the simulation, you can configure parameters such as infection rate, mortality rate, vaccine efficacy, and more. These settings are loaded from the `settings.json` file, which is generated based on user input at the start of the script.

2. **Run the simulation**:

   ```bash
   python main.py
   ```

3. **Input simulation parameters**:
   - After launching the script, you will be prompted to input parameters such as infection rate, mortality rate, reinfection rate, and the day vaccination starts. The program will save these settings to `settings.json` and begin the simulation.

4. **Monitor the simulation**:
   - The simulation will display dots representing healthy, infected, vaccinated, recovered, and deceased individuals moving within a defined space.
   - Real-time statistics are shown at the bottom of the window.
   - The simulation continues until it is manually stopped, and the statistics will be saved and plotted.

### Simulation Parameters

- **Infection Rate**: Probability of healthy individuals becoming infected upon contact with an infected person.
- **Mortality Rate**: Percentage of infected individuals who die after the incubation period.
- **Reinfection Rate**: Probability of recovered individuals being reinfected upon contact with an infected person.
- **Vaccination Efficacy**: Percentage of vaccinated individuals who are protected from infection.
- **Incubation Period**: Duration (in days) before an infected individual either recovers or dies.
- **Population Size**: Initial size of the population.
- **Isolation Rate**: Percentage of the population that remains isolated and does not move.

### Example

```bash
# After running the script, you will be prompted for these inputs:
Вероятность заражения при контакте (20%): 25
Смертность (15%): 10
Вероятность повторного заражения (10%): 5
День старта вакцинации (10001) / (>10_000 - никогда): 50
Эффективность вакцины (95%): 85
Инкубационный период (14 дней): 10
Население (1000 человек): 1000
Доля населения на самоизоляции (0%): 10
```

After inputting these values, the simulation will begin and the dots representing individuals will start moving on the screen.

### Output

At the end of the simulation, the following data is saved:
- A JSON file (`stat.json`) with the collected data throughout the simulation.
- A PNG file with a plot of key metrics (healthy, infected, vaccinated, recovered, deceased individuals) over time, saved in the `figures` folder.

## File Structure

- `main.py`: The main simulation script.
- `dot.py`: Defines the `Dot` class, representing each individual in the population.
- `config.py`: Handles the configuration of simulation settings.
- `settings.json`: A configuration file that stores the simulation parameters entered by the user.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](./LICENSE) file for more details.
