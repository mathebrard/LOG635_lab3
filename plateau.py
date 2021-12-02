import cozmo
from cozmo import robot 
from cozmo.util import degrees, Pose 
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes
import time
WALL_HEIGHT = 60 
WALL_WIDTH = 10 


def create_walls(robot: cozmo.robot.Robot):     
    # --- Grands MURS ---     
    wallA = Pose(445, -55, 30,  angle_z=degrees(0))     
    wallA = robot.world.create_custom_fixed_object(wallA, 1000, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False) 

    wallB = Pose(-55, 555, 30,  angle_z=degrees(0))     
    wallB = robot.world.create_custom_fixed_object(wallB, WALL_WIDTH, 1200, WALL_HEIGHT , relative_to_robot=False) 
    
    wallC = Pose(445, 1155, 30,  angle_z=degrees(0))     
    wallC = robot.world.create_custom_fixed_object(wallC, 1000, WALL_WIDTH, WALL_HEIGHT , relative_to_robot=False) 
    
    wallD = Pose(955, 555, 30,  angle_z=degrees(0))     
    wallD = robot.world.create_custom_fixed_object(wallD, WALL_WIDTH , 1200, WALL_HEIGHT , relative_to_robot=False) 
    
    # --- MUR INTERIEUR ---
    # --- DU BAS ---
    wallE = Pose(100, 300, 30,  angle_z=degrees(0))     
    wallE = robot.world.create_custom_fixed_object(wallE, 300 , WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    
    wallF = Pose(100, 600, 30,  angle_z=degrees(0))     
    wallF = robot.world.create_custom_fixed_object(wallF, 300 , WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    
    wallG = Pose(100, 900, 30,  angle_z=degrees(0))     
    wallG = robot.world.create_custom_fixed_object(wallG, 300 ,WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    
    # --- DU MILIEU ---
    wallH = Pose(450, 1000, 30,  angle_z=degrees(0))     
    wallH = robot.world.create_custom_fixed_object(wallH,  WALL_WIDTH, 240 , WALL_HEIGHT , relative_to_robot=False)
    
    # wallL = Pose(450, 70, 30,  angle_z=degrees(0))     
    # wallL = robot.world.create_custom_fixed_object(wallL,  WALL_WIDTH, 240 , WALL_HEIGHT , relative_to_robot=False)
    
    # --- DU HAUT ---
    wallI = Pose(800, 300, 30,  angle_z=degrees(0))     
    wallI = robot.world.create_custom_fixed_object(wallI, 300 , WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    
    wallJ = Pose(800, 600, 30,  angle_z=degrees(0))     
    wallJ = robot.world.create_custom_fixed_object(wallJ, 300 , WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    
    wallK = Pose(800, 900, 30,  angle_z=degrees(0))     
    wallK = robot.world.create_custom_fixed_object(wallK, 300 ,WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    



def define_markers(self):
    # Définition de tous les markeurs pour que le robot puisse les reconnaitre
    for marker_type in self.markers:
        custom_type = self.markers[marker_type]
        self.custom_objects.append(
            self.world.define_custom_cube(
                getattr(CustomObjectTypes, custom_type), 
                getattr(CustomObjectMarkers, marker_type), 
                60, 24.19, 24.19, True
            )
        )

## Definit toutes les actions a faire en fonction du marker vu ##
def action_manager(self, object_type):
    print(object_type.name)
    if (object_type.name == 'CustomType06'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Couteau", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType01'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Revolver", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType02'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Corde", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType03'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Tuyau", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType04'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Matraque", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType05'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Chandelier", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType11'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Mustard", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType12'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Peacock", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType13'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Scarlet", in_parallel=True).wait_for_completed()
        time.sleep(2)
    if (object_type.name == 'CustomType14'):
        self.markersFound.append(object_type.name)
        print(self.markersFound)
        self.say_text("Plum", in_parallel=True).wait_for_completed()
        time.sleep(2)
    
    
def checkMarkers(robot: cozmo.robot.Robot):
    time.sleep(0.1)
    robot.look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    
    markers = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
    if markers[0] in robot.markersFound:
        print("Continue")
        # continue
    else:
        robot.markersFound.append(markers[0])
        action_manager(robot, markers[0].object_type)
        
    robot.look_around.stop()
    
    
def action_manager_cube(self, cube):
    if cube.cube_id == 1:
        self.say_text("cube 1", in_parallel=True).wait_for_completed()
    if cube.cube_id == 2:
        self.say_text("cube 2", in_parallel=True).wait_for_completed()
 
 
def checkCubes(robot: cozmo.robot.Robot):
    lookaround = robot.start_behavior(
        cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
    action_manager_cube(robot, cubes[0])
    lookaround.stop()    


def cozmo_program(robot: cozmo.robot.Robot):
    robot.world.delete_all_custom_objects()  
    
    robot.markersFound = []
    robot.custom_objects = []
    robot.look_around = None
    robot.initial_pose = None
    robot.markers = {
            'Triangles2': 'CustomType06', #Triangles2 Couteau
            'Triangles3': 'CustomType01', #Triangles3 Revolver
            'Triangles4': 'CustomType02', #Triangles4 Corde
            'Triangles5': 'CustomType03', #Triangles5 Tuyau
            'Circles2': 'CustomType04', #Circles2 Matraque
            'Circles3': 'CustomType05', #Circles3 Chandelier
            'Hexagons2': 'CustomType11', #Hexagons2 Mustard
            'Diamonds2': 'CustomType12', #Hexagons3 Peacock
            'Diamonds3': 'CustomType13', #Hexagons4 Scarlet
            'Diamonds5': 'CustomType14' #Hexagons5 Plum
        }
    robot.initial_pose = Pose(0, 0, 0, angle_z=degrees(45))
    create_walls(robot)
    define_markers(robot)
    
    salon = Pose(700, 450, 30, angle_z=degrees(0))   
    robot.go_to_pose(salon).wait_for_completed() 
    checkCubes(robot)
     
    cuisine = Pose(700, 750, 30, angle_z=degrees(0))   
    robot.go_to_pose(cuisine).wait_for_completed()
    checkMarkers(robot)
    
    bureau = Pose(700, 1000, 30, angle_z=degrees(0))   
    robot.go_to_pose(bureau).wait_for_completed()
    checkMarkers(robot)
    
    studio = Pose(200, 1000, 30, angle_z=degrees(180))   
    robot.go_to_pose(studio).wait_for_completed()  
    checkMarkers(robot)
    
    bibliotheque = Pose(200, 750, 30, angle_z=degrees(180))   
    robot.go_to_pose(bibliotheque).wait_for_completed()  
    checkMarkers(robot)
    
    cave = Pose(200, 420, 30, angle_z=degrees(180))   
    robot.go_to_pose(cave).wait_for_completed()    
    checkMarkers(robot)
    
    robot.say_text("fini").wait_for_completed()
    # for x in robot.markersFound:
    #   print(x.object_type.name)
    # time.sleep(10)
    
    
    
        
        
cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)