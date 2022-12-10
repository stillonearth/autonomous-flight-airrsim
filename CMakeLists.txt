cmake_minimum_required(VERSION 3.4...3.18)
project (estimator LANGUAGES CXX)

find_package(Eigen3 REQUIRED)

link_directories(${Eigen_INCLUDE_DIRS})

add_subdirectory(pybind11)
pybind11_add_module(estimator src/QuadEstimatorEKF.cpp src/BaseQuadEstimator.cpp src/Utility/SimpleConfig.cpp)

target_link_libraries(estimator
    ${Eigen_LIBRARIES}
)

target_compile_definitions(estimator
                           PRIVATE VERSION_INFO=${EXAMPLE_VERSION_INFO})