cmake_minimum_required(VERSION 2.8.9)

project (estimator)

set(CMAKE_CXX_STANDARD 11)

message(STATUS ${PRIMEUTIL_LIB})

add_library(estimator SHARED  src/QuadEstimatorEKF.cpp src/BaseQuadEstimator.cpp src/Utility/SimpleConfig.cpp)

