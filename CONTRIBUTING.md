# Contributing Guide

Thank you for your interest in contributing to the Drone Guidance and Control Simulator.

This project is intended to serve as an educational platform for learning Guidance, Navigation, and Control (GNC) concepts using Python. Contributions that improve code quality, documentation, educational value, and simulation accuracy are welcome.

Before contributing, please read this document carefully.

---

# Ways to Contribute

There are many ways to contribute to this project, including but not limited to:

* Reporting bugs
* Improving documentation
* Fixing issues
* Refactoring existing code
* Implementing new trajectory generators
* Improving visualization
* Adding unit tests
* Improving numerical stability
* Implementing new control algorithms
* Optimizing performance

Contributions do not need to be large. Documentation improvements and bug fixes are equally valuable.

---

# Before You Start

Before opening a Pull Request:

1. Check existing Issues to avoid duplicate work.
2. Search existing Pull Requests.
3. Discuss large features through an Issue before implementation.
4. Keep changes focused on a single feature or fix.

---

# Development Environment

Clone the repository:

```bash
git clone https://github.com/<username>/drone-guidance-control.git
```

Move into the project directory:

```bash
cd drone-guidance-control
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the simulator to verify that your environment is configured correctly before making changes.

---

# Branch Naming

Please create a new branch for every contribution.

Recommended naming conventions:

```text
feature/add-circle-trajectory
feature/waypoint-navigation
bugfix/pid-reset
bugfix/wind-model
docs/update-readme
refactor/controller-module
```

Avoid committing directly to the main branch.

---

# Coding Guidelines

Please follow these guidelines when contributing.

## General

* Follow PEP 8.
* Use descriptive variable and function names.
* Keep functions focused on a single responsibility.
* Prefer readable code over clever code.
* Avoid unnecessary dependencies.

## Documentation

Every public class and function should include a docstring describing:

* Purpose
* Parameters
* Return values
* Assumptions

Inline comments should explain *why* something is implemented, rather than repeating what the code already says.

## Type Hints

Use Python type hints where appropriate.

Example:

```python
def update(self, setpoint: float, measurement: float) -> float:
```

---

# Commit Messages

Use clear and descriptive commit messages.

Examples:

```text
Add figure-eight trajectory generator

Improve PID anti-windup implementation

Fix animation frame indexing

Refactor wind disturbance model

Update installation documentation
```

Avoid generic commit messages such as:

```text
Update

Changes

Fix

Final

New Version
```

---

# Pull Requests

A good Pull Request should include:

* A clear description of the change.
* The motivation behind the change.
* Screenshots or animations for visualization updates.
* References to related Issues, when applicable.

Small, focused Pull Requests are easier to review than large unrelated changes.

---

# Reporting Bugs

When reporting a bug, please include:

* Operating system
* Python version
* Package versions
* Steps to reproduce
* Expected behavior
* Actual behavior
* Error messages or stack traces

Providing a minimal reproducible example is highly encouraged.

---

# Feature Requests

Feature requests should explain:

* The problem being addressed.
* Why the feature is useful.
* A possible implementation approach.
* Any relevant references or research.

Whenever possible, open an Issue before beginning implementation.

---

# Project Goals

The long-term objective of this repository is to provide a modular educational framework covering topics in Guidance, Navigation, and Control.

Potential future areas include:

* Additional trajectory generators
* Waypoint navigation
* Three-dimensional dynamics
* Sensor simulation
* Aerodynamic drag
* Extended Kalman Filter
* LQR and MPC controllers
* Obstacle avoidance
* ROS 2 integration
* PX4 SITL support

Contributions aligned with these goals are especially encouraged.

---

# Review Process

All contributions are reviewed before being merged.

Review focuses on:

* Correctness
* Readability
* Maintainability
* Documentation quality
* Consistency with the project's architecture

Maintainers may request revisions before approving a Pull Request.

---

# License

By submitting a contribution, you agree that your work will be licensed under the MIT License used by this repository.

---

Thank you for contributing and helping improve this project for students, developers, and robotics enthusiasts.
