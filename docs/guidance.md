# Guidance

## Overview

Guidance is the process of generating a desired path or trajectory for an autonomous vehicle to follow. In a Guidance, Navigation, and Control (GNC) system, the guidance module determines **where the vehicle should go**, while the controller determines **how the vehicle should move** to reach that objective.

In this project, the guidance system continuously generates a sequence of desired positions that form a reference trajectory. These reference positions are provided to the PID controllers, which compute the control forces required to minimize the tracking error.

---

## Guidance in the GNC Framework

A typical GNC system consists of three primary components:

* **Guidance** – Generates the desired trajectory or target position.
* **Navigation** – Estimates the current state of the vehicle using sensor measurements.
* **Control** – Produces actuator commands that minimize the difference between the desired and actual state.

The simulation implemented in this repository focuses primarily on the **Guidance** and **Control** components. Navigation is simplified by assuming perfect state measurements.

---

## Reference Trajectory

The simulator uses a **figure-eight (lemniscate)** trajectory as the reference path.

The desired position is defined using parametric equations:

```text
x(t) = A · sin(ωt)

y(t) = (A / 2) · sin(2ωt)
```

where:

* **A** is the trajectory amplitude (radius).
* **ω** is the angular speed.
* **t** is the simulation time.

The trajectory continuously changes over time, requiring the controller to update the drone's motion at every simulation step.

---

## Trajectory Tracking

During each simulation step, the following sequence is executed:

1. Generate the desired position from the trajectory.
2. Measure the current drone position.
3. Compute the tracking error.
4. Calculate control forces using the PID controllers.
5. Update the drone dynamics.
6. Repeat until the simulation ends.

This continuous feedback loop allows the drone to remain close to the desired path even when disturbances are introduced.

---

## Disturbance Rejection

External disturbances, such as wind, cause deviations from the desired trajectory.

The controller attempts to reduce these deviations by continuously correcting the drone's motion. The effectiveness of this correction depends on the selected PID gains.

Good guidance combined with a properly tuned controller results in:

* Accurate trajectory tracking
* Smooth vehicle motion
* Minimal oscillation
* Fast disturbance recovery
* Stable closed-loop behavior

---

## Simplifications

This simulator intentionally uses a simplified guidance model for educational purposes.

Assumptions include:

* Perfect knowledge of the vehicle position.
* Ideal trajectory generation.
* No obstacle avoidance.
* No path replanning.
* Two-dimensional motion only.

These assumptions allow the focus to remain on understanding the interaction between guidance and feedback control.

---

## Future Improvements

Potential enhancements include:

* Waypoint-based navigation
* Circular trajectories
* Spiral trajectories
* Obstacle avoidance
* Path planning algorithms
* Multi-vehicle coordination
* Three-dimensional guidance
* ROS 2 and PX4 integration

These additions would extend the simulator beyond classical trajectory tracking toward more realistic autonomous navigation systems.
