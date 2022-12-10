import airsim
import os
import numpy as np
import estimator


class Drone:

    def __init__(self):
        self.client = airsim.MultirotorClient()
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

    def visual_observations(self):
        responses = self.client.simGetImages([
        airsim.ImageRequest("0", airsim.ImageType.DepthVis),
        airsim.ImageRequest("1", airsim.ImageType.DepthPlanar, True)])
        for response in responses:
            if response.pixels_as_float:
                print("Type %d, size %d" % (response.image_type, len(response.image_data_float)))
                airsim.write_pfm(os.path.normpath('./temp/py1.pfm'), airsim.get_pfm_array(response))
            else:
                print("Type %d, size %d" % (response.image_type, len(response.image_data_uint8)))
                airsim.write_file(os.path.normpath('./temp/py1.png'), response.image_data_uint8)

    def rotate(self, angle, duration):
        self.client.rotateByYawRateAsync(angle, 1).join()

    def move(self, vx, vy, vz, duration):
        self.client.moveByVelocityBodyFrameAsync(vx, vy, vz, duration).join()

    def takeoff(self):
        self.client.takeoffAsync().join()

    def state(self):
        return self.client.getMultirotorState()

class DroneFlight:

    def __init__(self):
        self.drone = Drone()
        self.ekf = estimator.QuadEstimatorEKF("quad_estimator_ekf.txt", "drone1")
        self.ekf.Init()
        self.estimated_position = np.array([0, 0, 0])
        self.estimated_velocity = np.array([0, 0, 0])
        self.control_freq = (1. / 500.) * 1e9 
        self.flight_plan = [
            np.array([-10, 0, -10]),
            np.array([0, 10, 0]),
            np.array([-10, 0, 0]),
            np.array([0, -10, 0]),
            np.array([0, 0, 10]),
        ]
        self.eps = 0.05

    def update_state(self):
        esti_pos = self.ekf.EstimatedPosition()
        self.estimated_position  = np.array([
            esti_pos.x, 
            esti_pos.y, 
            esti_pos.z
        ])
        esti_vel = self.ekf.EstimatedVelocity()
        self.estimated_velocity  = np.array([
            esti_vel.x, 
            esti_vel.y, 
            esti_vel.z
        ])

    def execute_plan(self):
        # self.drone.takeoff()
        self.update_state()
        for path in self.flight_plan:
            print("executing path: ", path)
            self.execute_flight_program(path)

    def execute_flight_program(self, path):
        timestamp = self.drone.state().timestamp
        end_point = self.estimated_position + path
        
        delta_x = end_point - self.estimated_position
        while np.linalg.norm(delta_x) > self.eps:
            delta_x = end_point - self.estimated_position
            state = self.drone.state()
            delta_t = state.timestamp - timestamp
            if delta_t < self.control_freq:
                continue

            timestamp = state.timestamp

            height = state.kinematics_estimated.position.z_val
            lin_acc = estimator.V3F(
                state.kinematics_estimated.linear_acceleration.x_val, 
                state.kinematics_estimated.linear_acceleration.y_val, 
                state.kinematics_estimated.linear_acceleration.z_val
            )
            ang_acc = estimator.V3F(
                state.kinematics_estimated.angular_velocity.x_val, 
                state.kinematics_estimated.angular_velocity.y_val, 
                state.kinematics_estimated.angular_velocity.z_val
            )
                     
            self.update_state()
            
            
            self.ekf.UpdateFromIMU(lin_acc, ang_acc)
            self.ekf.UpdateFromBaro(-height)
            self.ekf.Predict(0.002, lin_acc, ang_acc)
               
            norm_delta = 2 * delta_x / np.linalg.norm(delta_x)
            self.drone.move(norm_delta[0], norm_delta[1], norm_delta[2], 0.002)
            
            print(self.estimated_position, end_point)
            

flight = DroneFlight()
flight.ekf.ekfState = np.zeros(6)
# flight.execute_plan()


# print("start plan")

flight.execute_flight_program(np.array([0, 0.1, 0.0]))

# print("end!")