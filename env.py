import math
import pygame


class BuildEnvironment:  # class for the environment
    def __init__(self,MapDimensions):  # init method to specify map dimensions as arguments
        pygame.init()
        self.pointCloud = []  # list to store our point cloud map as a group of 2-D points in 2-D space
        self.externalMap = pygame.image.load('Map1.png')  # loading the map and saving it in a variable
        self.map_height, self.map_width = MapDimensions  # split the dimensions of the map to width and height
        self.Map_Window_name = 'SLAM'  # name the window of the map as such
        pygame.display.set_caption(self.Map_Window_name)  # to display the name
        self.map = pygame.display.set_mode((self.map_width, self.map_height))  # return our main map
        self.map.blit(self.externalMap, (0, 0))  # overlap our external map on it
        #  Declaring some commonly used colours
        self.black = (0, 0, 0)
        self.grey = (70, 70, 70)
        self.blue = (0, 0, 255)
        self.green = (0, 255, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)

    # building the point cloud map - list of 2D co-ordinates
    # A method to convert the raw angle & distance data into Cartesian co-ordinates
    def AD2pos(self, distance, angle, robotPosition):
        x = distance * math.cos(angle) + robotPosition[0]
        y = - distance * math.sin(angle) + robotPosition[1]  # Since y-axis is inverted in pygame display
        return (int(x), int(y))

    # A method to send raw data to AD2pos method and storing the cartesian coordinates into a point cloud list after
    # checking for duplicates
    def dataStorage(self, data):
        print(len(self.pointCloud))
        if data != False:
            for element in data:
                point = self.AD2pos(element[0], element[1], element[2])
                if point not in self.pointCloud:
                    self.pointCloud.append(point)

    # A method to show sensor data
    def show_sensorData(self):
        self.infomap = self.map.copy()
        for point in self.pointCloud:
            self.infomap.set_at((int(point[0]), int(point[1])), (255, 0, 0))