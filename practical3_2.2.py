import Robot_API.robot_api
import brickpi
import time

robot = Robot_API.robot_api.getRobotInstance()

ultra_port = 3



def median_filtering(array):
	array = sorted(array)
	return array[int(len(array)/2)]




robot.sensorEnable(ultra_port, brickpi.SensorType.SENSOR_ULTRASONIC)
kp = 0.75
DesiredDistance = 30
while True:
 arr = []
 for i in range(0,25):
	sensorDistance = Robot_API.robot_api.getSonarValue(robot)
  	arr.append(sensorDistance[0])
 filteredSpeed = median_filtering(arr)
 newSpeed = -kp*(DesiredDistance - filteredSpeed)
 print newSpeed
 obot_API.robot_api.setSpeed(robot,newSpeed,newSpeed)

robot.terminate()


