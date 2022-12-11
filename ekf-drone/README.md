# Python-EKF-Drone

This is Extended Kalman Filter for Quadcoper Inertial Navigation System. The code is derived from [Udacity Flying Car Course](https://www.udacity.com/course/flying-car-nanodegree--nd787).

## Matematical Model

This library implements Extended Kalman Filter in C++ and python wrappers with pyblind11.

## Installation

### Windows

1. Install [Visual Studio](https://www.visualstudio.com/downloads/)
2. Install Cmake
3. Compile the project
   ```bash
   mkdir build
   cd build
   cmake ..
   cmake --build . --target estimator --config Release
   ```
4. Copy pyd file to your python project.

## Config

Refer to config-sample.txt for filter parameters.

## Usage

Create filter configuration file `quad_estimator_ekf.txt` and place in directory with estimator.pyd

```python
import estimator

ekf = estimator.QuadEstimatorEKF("quad_estimator_ekf.txt", "drone1")

dt = 0.002

# Read IMU data
lin_acc = estimator.V3F(0, 0, 0))
ang_acc = estimator.V3F(1.0, 1.0, 1.0)

# Feed IMU data to filter
ekf.UpdateFromIMU(lin_acc, ang_acc)
ekf.Predict(dt, lin_acc, ang_acc)

# Read state data from filter
state = ekf.ekfState # 6x1 np.array
cov = ekf.ekfCov # 6x6 np.array
```

## Acknowledgements

This filter was implemented by Udacity as part of Flying Car Course. The code was modified to be used as a library. Original code can be found [here](https://github.com/udacity/FCND-Estimation-CPP).
