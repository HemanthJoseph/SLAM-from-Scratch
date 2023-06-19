# Simultaneous Localization and Mapping from Scratch
In this project I am working on creating a SLAM project for Autonomous Robot only
using Python and simulating it in Pygame. <br>

Disclaimer: I am in the progress of completing this project and have yet to code up
more functionality for the project. I will keep pushing more, as and when I'm done.

## Methodology
First we design a LIDAR sensor using only Python which we will use to go through the
map and give us a 2-D point cloud of the obstacles in the map environment. <br>
To test our implementation of the LIDAR scanner, we use Pygame so as use our mouse
movements to represent the robot exploration of the environment. Once we have our
functionality in place we will integrate it to a mobile robot in our environment.

### Map
For the map, we look up floor plans online and download them. I use MS Paint to clean
up the map and save it.
![Map of Environment](/Map1.png)

### Environment
Creating the Environment class and creating necessary attributes. <br>
We also create the following class methods
1. Angle and Data to Coordinates - which will help us convert the raw data from the sensor
into Cartesian Coordinates
2. Data Storage - to save data to our point cloud
3. Data Show - show this sensor data on the environment.

### Sensors

We create a Laser Sensor class and create necessary attributes to it. <br>
We create the following methods.
1. Distance - get the distance between two points
2. Uncertainty - takes the measurement data and a user defined uncertainty to add 
uncertainty to the data. This is usually a Gaussian noise.

#### LIDAR Measurement technique
We do this by sampling. From the robot position that we know, we send out a straight
line segment of length equal to the range of the laser sensor we designed. Along
this line segment, we take number of samples of the environment. If the colour of
the sample is black, it means we reached an obstacle, and we don't need to sample
any further in that direction. If none found, it means this range of distances are
obstacle free. We do this is all 360 degree directions from a particular point by
rotating the line segment. Each point in the map can be represented by a tuple.
The distance from the robot itself and the angle in which it was found.

3. Sensing Obstacles - Using the above-mentioned technique

### Testing our implementation
So far, we have designed the environment and also written a code to write out the
functionality of a LIDAR sensor. We have also written functionality to get this data
from the sensor and update out point cloud map.

We know that in real life applications, we have LIDAR mounted on a Mobile robot.
For this test instance, we write some Pygame code to use the tip of the mouse pointer
as a robot and as we move the mouse in the environment, the LIDAR scanning and
sampling takes place, and we get a 2-D point cloud of the environment. 

You can see the implementation of the sensor here. As we move the mouse, the map
keeps being built through the 2-D point cloud.

![Designing a LIDAR Sensor](/Mouse_SLAM.gif)
