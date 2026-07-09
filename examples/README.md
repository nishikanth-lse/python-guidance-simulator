# Examples

This directory contains a collection of self-contained examples that demonstrate the individual components of the Drone Guidance and Control Simulator.

Each example focuses on a specific Guidance, Navigation, or Control (GNC) concept and is intended to help users understand the underlying algorithms without navigating the complete simulation framework.

The examples are designed for learning, experimentation, and rapid prototyping.

---

## Available Examples

| Example                | Description                                                                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `basic_pid.py`         | Demonstrates the fundamentals of a PID controller by regulating a simple one-dimensional system. Introduces proportional, integral, and derivative control actions.            |
| `altitude_hold.py`     | Simulates one-dimensional drone altitude control using a PID controller. Useful for understanding rise time, overshoot, settling time, and steady-state error.                 |
| `figure8_tracking.py`  | Demonstrates two-dimensional trajectory tracking using a figure-eight reference path. Shows how independent PID controllers regulate motion along both axes.                   |
| `wind_disturbance.py`  | Evaluates controller performance under external disturbances. Demonstrates disturbance rejection and recovery using configurable wind forces.                                  |
| `custom_trajectory.py` | Provides a template for implementing new trajectory generators. Users only need to modify the trajectory function while reusing the existing control and simulation framework. |

---

## Purpose

The examples are intentionally smaller than the primary simulator.

Instead of presenting every component simultaneously, each example isolates a single concept, making it easier to understand, modify, and extend.

They are suitable for:

* Learning the fundamentals of PID control.
* Understanding trajectory generation.
* Experimenting with controller gains.
* Studying disturbance rejection.
* Developing new guidance algorithms.

---

## Running an Example

From the project root directory, execute any example using Python.

```bash
python examples/figure8_tracking.py
```

Alternatively, examples can be copied into a Jupyter Notebook or Google Colab environment for interactive experimentation.

---

## Recommended Learning Order

For users who are new to Guidance and Control, the following progression is recommended:

1. `basic_pid.py`
2. `altitude_hold.py`
3. `figure8_tracking.py`
4. `wind_disturbance.py`
5. `custom_trajectory.py`

This sequence introduces the concepts incrementally, beginning with basic feedback control and progressing toward two-dimensional trajectory tracking under environmental disturbances.

---

## Extending the Examples

Contributions that demonstrate additional Guidance and Control techniques are encouraged.

Potential additions include:

* Circular trajectory tracking
* Square and waypoint navigation
* Spiral trajectories
* Three-dimensional flight dynamics
* Pure Pursuit guidance
* Stanley controller
* Linear Quadratic Regulator (LQR)
* Model Predictive Control (MPC)
* Obstacle avoidance
* Multi-agent coordination

Please refer to the project's `CONTRIBUTING.md` before submitting new examples.
