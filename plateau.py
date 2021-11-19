import cozmo
from cozmo import robot 
from cozmo.util import degrees, Pose 
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes
import time
WALL_HEIGHT = 60 
WALL_WIDTH = 10 

##########DEBUT DE MA PARTIE ###########""    
 
def __init__(self, robot):
    loop = True
    self.robot = robot
    self.found = []
    self.custom_objects = []
    self.look_around = None
    self.initial_pose = None
    
def create_walls(robot: cozmo.robot.Robot):     
    # --- VERTICAL ---     
    wallA = Pose(0, 0, WALL_HEIGHT,  angle_z=degrees(0))     
    wallA = robot.world.create_custom_fixed_object(wallA, 1000, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False) 
    wallCB = Pose(800, 300, WALL_HEIGHT,  angle_z=degrees(0))     
    wallCB = robot.world.create_custom_fixed_object(wallCB, 200, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False) 
    wallDC = Pose(800, 600, WALL_HEIGHT,  angle_z=degrees(0))     
    wallDC = robot.world.create_custom_fixed_object(wallDC, 200, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False)  
    wallE = Pose(500, 1200, WALL_HEIGHT,  angle_z=degrees(0))     
    wallE = robot.world.create_custom_fixed_object(wallE, 500, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False)  
    wallF = Pose(0, 1200, WALL_HEIGHT,  angle_z=degrees(0))     
    wallF = robot.world.create_custom_fixed_object(wallF, 500, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False)
    wallGH = Pose(0, 900, WALL_HEIGHT,  angle_z=degrees(0))     
    wallGH = robot.world.create_custom_fixed_object(wallGH, 250, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False)  
    wallHI = Pose(0, 600, WALL_HEIGHT,  angle_z=degrees(0))     
    wallHI = robot.world.create_custom_fixed_object(wallHI, 250, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False)  
    wallJI = Pose(0, 300, WALL_HEIGHT,  angle_z=degrees(0))     
    wallJI = robot.world.create_custom_fixed_object(wallJI, 250, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False)      
    
    # --- HORIZONTAL ---
    wallB = Pose(1000, 0, WALL_HEIGHT,  angle_z=degrees(0))     
    wallB = robot.world.create_custom_fixed_object(wallB, WALL_WIDTH, 300, WALL_HEIGHT , relative_to_robot=False)
    wallC = Pose(1000, 300, WALL_HEIGHT,  angle_z=degrees(0))     
    wallC = robot.world.create_custom_fixed_object(wallC, WALL_WIDTH, 300, WALL_HEIGHT , relative_to_robot=False)   
    wallD = Pose(1000, 600, WALL_HEIGHT,  angle_z=degrees(0))     
    wallD = robot.world.create_custom_fixed_object(wallD, WALL_WIDTH, 600, WALL_HEIGHT , relative_to_robot=False)  
    
    wallEF = Pose(500, 1200, WALL_HEIGHT,  angle_z=degrees(0))     
    wallEF = robot.world.create_custom_fixed_object(wallEF, 200, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False) 
        
    wallG = Pose(0, 900, WALL_HEIGHT,  angle_z=degrees(0))     
    wallG = robot.world.create_custom_fixed_object(wallG, WALL_WIDTH, 300, WALL_HEIGHT , relative_to_robot=False)  
    wallH = Pose(0, 600, WALL_HEIGHT,  angle_z=degrees(0))     
    wallH = robot.world.create_custom_fixed_object(wallH, WALL_WIDTH, 300, WALL_HEIGHT , relative_to_robot=False)  
    wallI = Pose(0, 300, WALL_HEIGHT,  angle_z=degrees(0))     
    wallI = robot.world.create_custom_fixed_object(wallI, WALL_WIDTH, 300, WALL_HEIGHT , relative_to_robot=False)    
    wallJ = Pose(0, 0, WALL_HEIGHT,  angle_z=degrees(0))     
    wallJ = robot.world.create_custom_fixed_object(wallJ, WALL_WIDTH, 300, WALL_HEIGHT , relative_to_robot=False)  
        
    
stop_a = Pose(650, 500, 0, angle_z=degrees(0)) 

def animWhenCubes(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(
        cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(
        num=1, object_type=cozmo.objects.LightCube, timeout=60)
    lookaround.stop()
    if len(cubes) > 0:
        robot.say_text("hello")
    
def cozmo_program(robot: cozmo.robot.Robot):  
    robot.world.delete_all_custom_objects()  
    print(robot.pose.position)   
    create_walls(robot)  
    #pour avoir le temps de regarder ce qu'il se passe sur la map
    #time.sleep(60)
    print(robot.world)   
    robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    #robot.go_to_pose(stop_a, relative_to_robot=False).wait_for_completed() 
    while loop is True :
        cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)  
        robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).stop()
        if len(cubes) > 0:
                robot.say_text("Found marker !").wait_for_completed()
                time.sleep(10)
                loop = False
                
    


cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)