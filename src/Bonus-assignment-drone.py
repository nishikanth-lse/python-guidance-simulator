# ============================================================
# Advanced Drone Technology
# Bonus Project: Figure-Eight Drone Guidance using PID Control
# Part 1 - Core Classes & Simulation Setup
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
from IPython.display import HTML

import ipywidgets as widgets
from ipywidgets import interact

from dataclasses import dataclass
from typing import Tuple

# ============================================================
# Simulation Configuration
# ============================================================

DT = 0.02
SIMULATION_TIME = 40

TIME = np.arange(0, SIMULATION_TIME, DT)

# ============================================================
# Drone Parameters
# ============================================================

DRONE_MASS = 1.0

MAX_FORCE = 20.0

MAX_INTEGRAL = 10.0

# ============================================================
# Figure Eight Parameters
# ============================================================

TRAJECTORY_RADIUS = 5.0

TRAJECTORY_SPEED = 0.6

# ============================================================
# Wind Configuration
# ============================================================

ENABLE_WIND = True

WIND_AFTER = 6.0

MAX_WIND = 0.35

# ============================================================
# PID Controller
# ============================================================

@dataclass
class PIDController:

    kp: float
    ki: float
    kd: float

    dt: float

    output_limits: Tuple[float, float] = (-20.0,20.0)

    integral_limits: Tuple[float,float] = (-10.0,10.0)

    derivative_filter: float = 0.20

    def __post_init__(self):

        self.reset()

    def reset(self):

        self.integral = 0.0

        self.previous_error = 0.0

        self.filtered_derivative = 0.0

    def update(self,setpoint,measurement):

        error = setpoint-measurement

        # Integral

        self.integral += error*self.dt

        self.integral = np.clip(
            self.integral,
            self.integral_limits[0],
            self.integral_limits[1]
        )

        # Derivative

        raw_derivative = (
            error-self.previous_error
        )/self.dt

        self.filtered_derivative = (
            self.derivative_filter*raw_derivative
            +
            (1-self.derivative_filter)
            *self.filtered_derivative
        )

        output = (

            self.kp*error

            +

            self.ki*self.integral

            +

            self.kd*self.filtered_derivative

        )

        output=np.clip(
            output,
            self.output_limits[0],
            self.output_limits[1]
        )

        self.previous_error=error

        return output

# ============================================================
# Drone Model
# ============================================================

class Drone2D:

    def __init__(

        self,

        mass=1.0

    ):

        self.mass=mass

        self.reset()

    def reset(self):

        self.x=0.0
        self.y=0.0

        self.vx=0.0
        self.vy=0.0

        self.ax=0.0
        self.ay=0.0

    def update(

        self,

        force_x,

        force_y,

        wind_x,

        wind_y,

        dt

    ):

        self.ax=(force_x+wind_x)/self.mass

        self.ay=(force_y+wind_y)/self.mass

        self.vx+=self.ax*dt
        self.vy+=self.ay*dt

        self.x+=self.vx*dt
        self.y+=self.vy*dt

        return self.x,self.y

# ============================================================
# Wind Model
# ============================================================

class WindModel:

    def __init__(

        self,

        max_wind=0.35,

        start_time=6.0

    ):

        self.max_wind=max_wind

        self.start_time=start_time

    def get(self,t):

        if t<self.start_time:

            return 0.0,0.0

        wind_x=0.6*self.max_wind*np.sin(0.7*t)

        wind_y=0.4*self.max_wind*np.cos(0.5*t)

        gust=np.random.normal(0,self.max_wind*0.05,2)

        wind_x+=gust[0]

        wind_y+=gust[1]

        return wind_x,wind_y

# ============================================================
# Performance Metrics
# ============================================================

class Metrics:

    def __init__(self):

        self.errors=[]

    def update(

        self,

        x,

        y,

        target_x,

        target_y

    ):

        error=np.sqrt(

            (target_x-x)**2

            +

            (target_y-y)**2

        )

        self.errors.append(error)

    def summary(self):

        errors=np.array(self.errors)

        return {

            "RMSE":np.sqrt(np.mean(errors**2)),

            "Average Error":np.mean(errors),

            "Maximum Error":np.max(errors)

        }

print("="*60)
print("Advanced Drone Guidance System Initialized")
print("Part 1 Loaded Successfully")
print("="*60)

# ============================================================
# Part 2 - Guidance, Figure-Eight Trajectory & Simulation Engine
# ============================================================

# ============================================================
# Figure-Eight Trajectory Generator
# ============================================================

class FigureEightTrajectory:

    def __init__(self,
                 radius=5.0,
                 speed=0.6):

        self.radius = radius
        self.speed = speed

    def reference(self, t):
        """
        Returns desired x,y position
        using a Lemniscate (Figure Eight)
        """

        theta = self.speed * t

        x = self.radius * np.sin(theta)

        y = (self.radius / 2) * np.sin(2 * theta)

        return x, y


# ============================================================
# Drone Guidance Simulator
# ============================================================

class DroneGuidanceSimulation:

    def __init__(self,
                 kp=3.5,
                 ki=0.08,
                 kd=1.20):

        self.dt = DT

        # Drone

        self.drone = Drone2D(DRONE_MASS)

        # Controllers

        self.pid_x = PIDController(
            kp,
            ki,
            kd,
            DT,
            (-MAX_FORCE, MAX_FORCE),
            (-MAX_INTEGRAL, MAX_INTEGRAL)
        )

        self.pid_y = PIDController(
            kp,
            ki,
            kd,
            DT,
            (-MAX_FORCE, MAX_FORCE),
            (-MAX_INTEGRAL, MAX_INTEGRAL)
        )

        # Guidance

        self.trajectory = FigureEightTrajectory(
            TRAJECTORY_RADIUS,
            TRAJECTORY_SPEED
        )

        # Wind

        self.wind = WindModel(
            MAX_WIND,
            WIND_AFTER
        )

        # Metrics

        self.metrics = Metrics()

        # Data

        self.time = []

        self.x = []
        self.y = []

        self.ref_x = []
        self.ref_y = []

        self.error = []

        self.wind_x = []
        self.wind_y = []

        self.control_x = []
        self.control_y = []

    # ========================================================

    def reset(self):

        self.drone.reset()

        self.pid_x.reset()

        self.pid_y.reset()

        self.metrics = Metrics()

        self.time.clear()

        self.x.clear()
        self.y.clear()

        self.ref_x.clear()
        self.ref_y.clear()

        self.error.clear()

        self.wind_x.clear()
        self.wind_y.clear()

        self.control_x.clear()
        self.control_y.clear()

    # ========================================================

    def step(self, t):

        # Desired Position

        target_x, target_y = self.trajectory.reference(t)

        # PID Controllers

        force_x = self.pid_x.update(
            target_x,
            self.drone.x
        )

        force_y = self.pid_y.update(
            target_y,
            self.drone.y
        )

        # Wind

        wx, wy = self.wind.get(t)

        # Update Drone

        self.drone.update(
            force_x,
            force_y,
            wx,
            wy,
            DT
        )

        # Error

        tracking_error = np.sqrt(

            (target_x - self.drone.x) ** 2 +

            (target_y - self.drone.y) ** 2

        )

        self.metrics.update(
            self.drone.x,
            self.drone.y,
            target_x,
            target_y
        )

        # Store Data

        self.time.append(t)

        self.x.append(self.drone.x)
        self.y.append(self.drone.y)

        self.ref_x.append(target_x)
        self.ref_y.append(target_y)

        self.wind_x.append(wx)
        self.wind_y.append(wy)

        self.control_x.append(force_x)
        self.control_y.append(force_y)

        self.error.append(tracking_error)

    # ========================================================

    def run(self):

        self.reset()

        for t in TIME:

            self.step(t)

        return self.metrics.summary()


# ============================================================
# Create Simulator
# ============================================================

simulation = DroneGuidanceSimulation(
    kp=3.5,
    ki=0.08,
    kd=1.20
)

results = simulation.run()

print("\nSimulation Complete\n")

print("Performance")

for key, value in results.items():

    print(f"{key:15s}: {value:.4f}")

print("\nTotal Simulation Steps :", len(simulation.time))

# ============================================================
# Part 3 - Visualization, Animation & Interactive Dashboard
# ============================================================

# ------------------------------------------------------------
# Static Plots
# ------------------------------------------------------------

def plot_results(sim):

    fig, ax = plt.subplots(2,2,figsize=(14,10))

    # --------------------------------------------------------

    ax[0,0].plot(
        sim.ref_x,
        sim.ref_y,
        '--',
        linewidth=2,
        label='Desired Path'
    )

    ax[0,0].plot(
        sim.x,
        sim.y,
        linewidth=2,
        label='Drone Path'
    )

    ax[0,0].scatter(
        sim.x[0],
        sim.y[0],
        color='green',
        s=80,
        label='Start'
    )

    ax[0,0].scatter(
        sim.x[-1],
        sim.y[-1],
        color='red',
        s=80,
        label='End'
    )

    ax[0,0].set_title("Figure Eight Tracking")

    ax[0,0].set_xlabel("X Position (m)")
    ax[0,0].set_ylabel("Y Position (m)")

    ax[0,0].grid(True)

    ax[0,0].axis("equal")

    ax[0,0].legend()

    # --------------------------------------------------------

    ax[0,1].plot(
        sim.time,
        sim.error,
        color='red'
    )

    ax[0,1].set_title("Tracking Error")

    ax[0,1].set_xlabel("Time (s)")
    ax[0,1].set_ylabel("Error (m)")

    ax[0,1].grid(True)

    # --------------------------------------------------------

    ax[1,0].plot(
        sim.time,
        sim.control_x,
        label="Control X"
    )

    ax[1,0].plot(
        sim.time,
        sim.control_y,
        label="Control Y"
    )

    ax[1,0].set_title("PID Outputs")

    ax[1,0].grid(True)

    ax[1,0].legend()

    # --------------------------------------------------------

    ax[1,1].plot(
        sim.time,
        sim.wind_x,
        label="Wind X"
    )

    ax[1,1].plot(
        sim.time,
        sim.wind_y,
        label="Wind Y"
    )

    ax[1,1].set_title("Wind Disturbance")

    ax[1,1].grid(True)

    ax[1,1].legend()

    plt.tight_layout()

    plt.show()

# ------------------------------------------------------------
# Animation
# ------------------------------------------------------------

def animate(sim):

    fig,ax=plt.subplots(figsize=(8,8))

    ax.set_xlim(-7,7)

    ax.set_ylim(-4,4)

    ax.grid(True)

    ax.set_aspect("equal")

    ax.set_title("Drone Figure Eight Guidance")

    ax.plot(
        sim.ref_x,
        sim.ref_y,
        '--',
        alpha=0.5,
        label='Desired Path'
    )

    trail, = ax.plot(
        [],
        [],
        linewidth=2,
        label='Actual Path'
    )

    drone, = ax.plot(
        [],
        [],
        'o',
        markersize=10,
        label='Drone'
    )

    target, = ax.plot(
        [],
        [],
        'rx',
        markersize=10,
        label='Target'
    )

    timer=ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes
    )

    ax.legend()

    def init():

        trail.set_data([],[])

        drone.set_data([],[])

        target.set_data([],[])

        timer.set_text("")

        return trail,drone,target,timer

    def update(frame):

        trail.set_data(
            sim.x[:frame],
            sim.y[:frame]
        )

        drone.set_data(
            [sim.x[frame]],
            [sim.y[frame]]
        )

        target.set_data(
            [sim.ref_x[frame]],
            [sim.ref_y[frame]]
        )

        timer.set_text(
            f"Time : {sim.time[frame]:.2f} s"
        )

        return trail,drone,target,timer

    ani=FuncAnimation(
        fig,
        update,
        frames=len(sim.time),
        init_func=init,
        interval=20,
        blit=True
    )

    plt.close(fig)

    return HTML(ani.to_jshtml())

# ------------------------------------------------------------
# Interactive Dashboard
# ------------------------------------------------------------

def run_simulation(
        kp,
        ki,
        kd,
        wind_strength,
        radius,
        speed):

    global MAX_WIND

    MAX_WIND = wind_strength

    sim = DroneGuidanceSimulation(
        kp,
        ki,
        kd
    )

    sim.trajectory.radius = radius

    sim.trajectory.speed = speed

    results = sim.run()

    plot_results(sim)

    print("\n==============================")

    print("Performance Metrics")

    print("==============================")

    for k,v in results.items():

        print(f"{k:18s}: {v:.4f}")

    display(
        animate(sim)
    )

# ------------------------------------------------------------
# Widgets
# ------------------------------------------------------------

interact(

    run_simulation,

    kp=widgets.FloatSlider(
        value=3.5,
        min=0.1,
        max=10,
        step=0.1,
        description="Kp"
    ),

    ki=widgets.FloatSlider(
        value=0.08,
        min=0,
        max=2,
        step=0.01,
        description="Ki"
    ),

    kd=widgets.FloatSlider(
        value=1.2,
        min=0,
        max=5,
        step=0.1,
        description="Kd"
    ),

    wind_strength=widgets.FloatSlider(
        value=0.35,
        min=0,
        max=2,
        step=0.05,
        description="Wind"
    ),

    radius=widgets.FloatSlider(
        value=5,
        min=2,
        max=8,
        step=0.5,
        description="Radius"
    ),

    speed=widgets.FloatSlider(
        value=0.6,
        min=0.2,
        max=2,
        step=0.05,
        description="Speed"
    )

)

print("\nProject Ready.")
print("Adjust the sliders and explore different controller settings.")