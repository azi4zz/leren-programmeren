from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
robotArm.grab()
for x in range (1,8):
    for i in range(8):
        robotArm.moveRight()
    for x in range(1):
        robotArm.drop()
    for n in range(8):
        robotArm.moveLeft()
    for r in range(1):
        robotArm.grab()    
robotArm.wait()