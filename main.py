import env
import sensors
import pygame

# build the virtual environment
environment = env.BuildEnvironment((600, 1200))
# make a copy of the original map
environment.originalMap = environment.map.copy()
# Create a laser sensor instance
laser = sensors.LaserSensor(200, environment.originalMap, uncertainty=(0.5, 0.01))
# Fill the main map as all black (representing no initial data and save this map as the info map)
environment.map.fill((0, 0, 0))
environment.infomap = environment.map.copy()  # infomap is where we draw the point cloud

running = True  # useful to close the pygame

while running:
    sensorON = False  # This flag is set to true only if the mouse cursor is inside the window.
    # (For this testing instance, we are using the move movements as our autonomous robot)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if red stop button is pressed, loop is terminated
            running = False
        if pygame.mouse.get_focused():
            sensorON = True
        elif not pygame.mouse.get_focused():
            sensorON = False
    if sensorON:
        position = pygame.mouse.get_pos()  # Getting the mouse position
        laser.position = position  # Assign this position to the sensor position
        sensor_data = laser.sense_obstacles()  # Run the LIDAR for one turn
        environment.dataStorage(sensor_data)  # store the sensor data
        environment.show_sensorData()  # show the data

    environment.map.blit(environment.infomap, (0, 0))  # drawing the data on the infomap onto the main map

    # call the pygame display to update any changes to the map
    pygame.display.update()
