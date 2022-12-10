import os
import ctypes

basedir = os.path.abspath(os.path.dirname(__file__))
libpath = os.path.join(basedir, 'build/Release/estimator.dll')

estimator = ctypes.CDLL(libpath)

print(estimator.QuadEstimatorEKF)