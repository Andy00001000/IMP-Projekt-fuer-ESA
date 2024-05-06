import math
import matplotlib.pyplot as plt

class Rocket:
    def __init__(self, mass, thrust):
        self.mass = mass
        self.thrust = thrust
        self.velocity = 0
        self.acceleration = 0
        self.height = 0
        self.time = []

    def update(self, dt):
        self.acceleration = self.thrust / self.mass
        self.velocity += self.acceleration * dt
        self.height += self.velocity * dt
        self.time.append(dt)

class Simulation:
    def __init__(self):
        self.rocket = None

    def initialize_rocket(self, mass, thrust):
        self.rocket = Rocket(mass, thrust)

    def run(self, total_time, dt):
        while sum(self.rocket.time) < total_time:
            self.rocket.update(dt)

    def display_results(self):
        plt.plot(self.rocket.time, [self.rocket.height] * len(self.rocket.time))
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.title("Rocket Height Over Time")
        plt.grid(True)
        plt.show()

# User Story I. Newton
def simulate_rocket_launch(mass, thrust):
    simulation = Simulation()
    simulation.initialize_rocket(mass, thrust)
    simulation.run(total_time=10, dt=1)
    simulation.display_results()

# User Story B. Pascal
def calculate_air_resistance(velocity, air_density, frontal_area, drag_coefficient):
    velocity_values = range(0, velocity + 1, 1)
    air_resistance = [0.5 * drag_coefficient * air_density * frontal_area * v**2 for v in velocity_values]
    plt.plot(velocity_values, air_resistance)
    plt.xlabel("Velocity (m/s)")
    plt.ylabel("Air Resistance (N)")
    plt.title("Air Resistance vs. Velocity")
    plt.grid(True)
    plt.show()

# User Story N. Armstrong
def visualize_flight_parameters(velocity, acceleration, distance):
    time = [i for i in range(len(velocity))]
    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Velocity (m/s)', color=color)
    ax1.plot(time, velocity, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  
    color = 'tab:blue'
    ax2.set_ylabel('Acceleration (m/s^2)', color=color)  
    ax2.plot(time, acceleration, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  
    plt.title('Rocket Flight Parameters Over Time')
    plt.show()

# User Story W. Braun
def simulate_two_stage_rocket():
    rocket_stage1 = Rocket(mass=1000, thrust=5000)
    rocket_stage2 = Rocket(mass=500, thrust=2000)
    total_time = 50  # Total simulation time
    dt = 1  # Time step
    time = 0
    height = []
    while time < total_time:
        rocket_stage1.update(dt)
        if time >= 20:
            rocket_stage2.update(dt)
        height.append(rocket_stage1.height + rocket_stage2.height if time >= 20 else rocket_stage1.height)
        time += dt
    plt.plot([i for i in range(len(height))], height)
    plt.xlabel("Time (s)")
    plt.ylabel("Height (m)")
    plt.title("Two-Stage Rocket Height Over Time")
    plt.grid(True)
    plt.show()

# User Story J. Gagarin
def real_time_simulation():
    rocket = Rocket(mass=1000, thrust=5000)
    total_time = 10  # Total simulation time
    dt = 1  # Time step
    time = 0
    height = []
    while time < total_time:
        rocket.update(dt)
        height.append(rocket.height)
        plt.plot(rocket.time, height)
        plt.xlabel("Time (s)")
        plt.ylabel("Height (m)")
        plt.title("Real-Time Rocket Height")
        plt.grid(True)
        plt.pause(0.1)  # Pause to simulate real-time display
        time += dt
    plt.show()

# User Story Galileo Galilei
def calculate_gravitational_force(mass, gravitational_constant, earth_mass, distance):
    force = gravitational_constant * (earth_mass * mass) / distance**2
    return force

# User Story Nikolaus Kopernikus
def adjust_rocket_trajectory(angle):
    # Placeholder for adjusting rocket trajectory logic
    pass

# User Story Katherine Johnson
def enter_custom_parameters():
    # Placeholder for entering custom parameters logic
    pass

# User Story Leika
def bark():
    print("*Bark!*")

# Beispielanwendung
if __name__ == "__main__":
    simulate_rocket_launch(mass=1000, thrust=5000)
    calculate_air_resistance(velocity=50, air_density=1.2, frontal_area=5, drag_coefficient=0.3)
    visualize_flight_parameters(velocity=[0, 10, 20, 30, 40], acceleration=[5, 10, 15, 20, 25], distance=100)
    simulate_two_stage_rocket()
    real_time_simulation()
    bark()
