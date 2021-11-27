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
    
    wallL = Pose(450, 70, 30,  angle_z=degrees(0))     
    wallL = robot.world.create_custom_fixed_object(wallL,  WALL_WIDTH, 240 , WALL_HEIGHT , relative_to_robot=False)
    
    # --- DU HAUT ---
    wallI = Pose(800, 300, 30,  angle_z=degrees(0))     
    wallI = robot.world.create_custom_fixed_object(wallI, 300 , WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    
    wallJ = Pose(800, 600, 30,  angle_z=degrees(0))     
    wallJ = robot.world.create_custom_fixed_object(wallJ, 300 , WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    
    wallK = Pose(800, 900, 30,  angle_z=degrees(0))     
    wallK = robot.world.create_custom_fixed_object(wallK, 300 ,WALL_WIDTH , WALL_HEIGHT , relative_to_robot=False)
    

    

stop_a = Pose(1100, 110, 0, angle_z=degrees(0)) 



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



def cozmo_program(robot: cozmo.robot.Robot):
    robot.world.delete_all_custom_objects()  
    
    robot.markersFound = []
    robot.custom_objects = []
    robot.look_around = None
    robot.initial_pose = None
    robot.markers = {
            'Triangles2': 'CustomType06', #Triangles2
            'Triangles3': 'CustomType01', #Triangles3
            'Triangles4': 'CustomType02', #Triangles4
            'Triangles5': 'CustomType03', #Triangles5
            'Circles2': 'CustomType04', #Circles2
            'Circles3': 'CustomType05', #Circles3
            'Hexagons2': 'CustomType11', #Hexagons2
            'Hexagons3': 'CustomType12', #Hexagons3
            'Hexagons4': 'CustomType13', #Hexagons4
            'Hexagons5': 'CustomType14' #Hexagons5
        }
    robot.initial_pose = Pose(0, 0, 0, angle_z=degrees(45))
    define_markers(robot)
     
    while len(robot.markersFound) < 2:
        time.sleep(0.1)
        
        robot.look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        
        markers = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=60)
        
        print(robot.custom_objects)
        print("###################")
        print(markers[0].object_type)
        if markers[0] in robot.markersFound:
                print("ace")
                continue
        else:
            robot.markersFound.append(markers[0])
            # print(robot.markersFound)
        print("RESULTAT ::::::::::::::::::")
        print(robot.markersFound)
        robot.look_around.stop()
        
        actionManager()
        
    
    
    




cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)