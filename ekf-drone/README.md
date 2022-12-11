# Python-EKF-Drone

This is Extended Kalman Filter for Quadcoper Inertial Navigation System. The code is derived from [Udacity Flying Car Course](https://www.udacity.com/course/flying-car-nanodegree--nd787).

## Matematical Model

This library implements Extended Kalman Filter in C++ and python wrappers with pyblind11.

## Installation

### Windows

```bash
mkdir build
cd build
cmake ..
cmake --build . --target estimator --config Release
cmake --install .
```

Copy pyd file to your python project.

## Config

Refer to config-sample.txt for filter parameters.
