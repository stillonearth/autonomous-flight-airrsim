# ready to run example: PythonClient/multirotor/hello_drone.py
import airsim
import os


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
