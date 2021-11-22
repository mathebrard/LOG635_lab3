import cozmo
from cozmo import robot 
from cozmo.util import degrees, Pose 
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes
import time
WALL_HEIGHT = 60 
WALL_WIDTH = 10 

class Plateau:
##########DEBUT DE MA PARTIE ###########""    
 
    def __init__(self, robot):
        self.robot = robot
        self.custom_objects = []
        self.look_around = None
        self.initial_pose = None
        self.markers = {
                'Poignard': 'CustomType00', #Triangles2
                'Revolver': 'CustomType01', #Triangles3
                'Chandelier': 'CustomType02', #Triangles4
                'Corde': 'CustomType03', #Triangles5
                'Clé anglaise': 'CustomType04', #Circles2
                'Matraque': 'CustomType05', #Circles3
                # 'Salle de bal': 'CustomType06', #Circles4
                # 'Salle de bain': 'CustomType07', #Diamonds2
                # 'Salon': 'CustomType08', #Diamonds3
                # 'Cuisine': 'CustomType09', #Diamonds4
                # 'Salle à manger': 'CustomType10', #Diamonds5
                'Scarlet': 'CustomType11', #Hexagons2
                'Plum': 'CustomType12', #Hexagons3
                'Peacock': 'CustomType13', #Hexagons4
                'Green': 'CustomType14' #Hexagons5
            }
    
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

# def animWhenCubes(robot: cozmo.robot.Robot):
#     lookaround = robot.start_behavior(
#         cozmo.behavior.BehaviorTypes.LookAroundInPlace)
#     cubes = robot.world.wait_until_observe_num_objects(
#         num=1, object_type=cozmo.objects.LightCube, timeout=60)
#     lookaround.stop()
#     if len(cubes) > 0:
#         robot.say_text("hello")
    
def cozmo_program(robot: cozmo.robot.Robot):
    loop = True  
    robot.world.delete_all_custom_objects()  
    print(robot.pose.position)   
    create_walls(robot)  
    #pour avoir le temps de regarder ce qu'il se passe sur la map
    print(robot.world)   
    # robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    # robot.go_to_pose(stop_a, relative_to_robot=False).wait_for_completed() 
    time.sleep(60)
    # while loop is True :
    #     cubes = robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)  
    #     robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace).stop()
    #     if len(cubes) == 1:
    #             # robot.say_text("Cube trouvé !").wait_for_completed()
    #             # time.sleep(10)
    #             continue
    #     if len(cubes) == 2:
    #             robot.say_text("Cube 2 trouvé !").wait_for_completed()
    #             loop = False   
                
    #     if (object_type == 'CustomType14'):
    #         robot.say_text("I can't dance I'm shy").wait_for_completed()  











#    # cube_taps = [0]*3  
#     def handle_object_tapped(evt, **kw):     
#         global keepGoing 
#         # This will be called whenever an EvtObjectMovingStarted event is dispatched -     
#         # # whenever we detect a cube starts moving (via an accelerometer in the cube)     
#         i = evt.obj.object_id - 1     
#         cube_taps[i] = cube_taps[i] + evt.tap_count if cube_taps[i] < 3 else 0      
#         print(cube_taps)      
#         if all(x == 3 for x in cube_taps):         
#             keepGoing=False  
            
            
#     def cozmo_program(robot: cozmo.robot.Robot):     
#         global keepGoing     
#         # Add event handlers that will be called for the corresponding event     
#         robot.add_event_handler(cozmo.objects.EvtObjectTapped, handle_object_tapped) 
#         robot.say_text("waiting for tapped cube").wait_for_completed()     
#         keepGoing=True     
#         # keep the program running until user closes / quits it     
#         # #print("Press CTRL-C to quit")     
#         while keepGoing: 
#             time.sleep(0.1)     
#         robot.say_text("cube Tapped").wait_for_completed()




cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)