# Drone Guidance and Control Simulator

A Python-based educational simulator for studying the fundamentals of Guidance, Navigation, and Control (GNC). The project demonstrates PID-based trajectory tracking, disturbance rejection, and feedback control using two-dimensional drone simulations.

This repository is intended as a learning resource for students interested in control systems, robotics, autonomous vehicles, and aerospace engineering.

---

## Overview

This project explores the implementation of classical feedback control techniques for autonomous systems.

The simulator models a two-dimensional drone that tracks reference trajectories using independent PID controllers for the X and Y axes. Environmental disturbances such as wind can be introduced to evaluate controller robustness and trajectory tracking performance.

The repository originated from an academic Guidance and Control assignment and has been refactored into a modular and extensible codebase suitable for experimentation and further development.

---

## Features

* Two-dimensional drone dynamics
* PID position controller
* Independent X and Y control loops
* Figure-eight trajectory generation
* Wind disturbance model
* Interactive controller tuning
* Trajectory visualization
* Animation using Matplotlib
* Tracking error analysis
* Performance metrics (RMSE, average error, maximum error)

---

## Repository Structure

```text
drone-guidance-control/

├── README.md
├── LICENSE
├── requirements.txt
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
│
├── notebook/
│   └── drone_guidance.ipynb
│
├── src/
│   ├── simulation.py
│   ├── pid.py
│   ├── dynamics.py
│   ├── trajectory.py
│   └── visualization.py
│
├── examples/
│   ├── circle.py
│   ├── figure8.py
│   ├── waypoint.py
│   ├── spiral.py
│   └── square.py
│
├── docs/
│   ├── pid.md
│   ├── guidance.md
│   ├── dynamics.md
│   └── wind.md
│
└── assets/
    ├── trajectory.png
    ├── animation.gif
    └── architecture.png
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/<username>/drone-guidance-control.git
```

Move into the project directory.

```bash
cd drone-guidance-control
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Running the Simulator

### Google Colab

Open the notebook located in:

```text
notebook/drone_guidance.ipynb
```

Execute the notebook sequentially.

### Local Execution

```bash
python src/simulation.py
```

---

## Project Architecture

The simulator follows a modular architecture consisting of the following components:

```text
Reference Trajectory
        │
        ▼
Trajectory Generator
        │
        ▼
PID Controller
        │
        ▼
Drone Dynamics
        │
        ▼
State Update
        │
        ▼
Performance Evaluation
        │
        ▼
Visualization
```

---

## Simulation Components

### Guidance

Reference trajectory generation using analytical parametric equations.

### Control

Independent PID controllers regulate motion along the X and Y axes.

### Dynamics

The vehicle state is propagated using a simplified Newtonian motion model.

### Disturbance Model

Optional wind disturbances are applied during simulation to evaluate controller performance.

### Visualization

Trajectory plots, control signals, disturbance profiles, and animation are generated using Matplotlib.

---

## Performance Evaluation

Controller performance is evaluated using:

* Root Mean Square Error (RMSE)
* Average Tracking Error
* Maximum Tracking Error

These metrics provide a quantitative comparison between different controller configurations.

---

## Configuration

The simulator exposes the following configurable parameters:

* Proportional gain (Kp)
* Integral gain (Ki)
* Derivative gain (Kd)
* Wind strength
* Trajectory radius
* Trajectory speed

---

## Roadmap

### Version 1

* PID-based trajectory tracking
* Figure-eight trajectory
* Wind disturbance model
* Interactive parameter tuning

### Version 2

* Circular and waypoint trajectories
* Velocity controller
* Improved visualization

### Version 3

* Three-dimensional dynamics
* Aerodynamic drag model
* Sensor noise simulation
* Vehicle attitude control

### Version 4

* Extended Kalman Filter
* Obstacle avoidance
* Path planning
* Multi-vehicle simulation

### Version 5

* ROS 2 integration
* Gazebo support
* PX4 SITL compatibility

---

## Contributing

Contributions are welcome.

Bug fixes, documentation improvements, new trajectory generators, controller implementations, and simulation enhancements are encouraged.

Please refer to `CONTRIBUTING.md` before opening an issue or submitting a pull request.

---

## Educational Scope

This repository is intended for educational and research purposes.

The implemented models are simplified to illustrate Guidance and Control concepts and should not be considered representative of production flight control software or safety-critical UAV systems.

---

## Acknowledgements

This repository builds upon an academic Guidance and Control assignment. The original assignment provided the foundational simulation, while this repository extends it through code refactoring, modularization, additional trajectory generation, disturbance modeling, improved visualization, and enhanced documentation.

---

## License

This project is licensed under the MIT License.

See the `LICENSE` file for additional information.
