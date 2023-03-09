from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(4):
    robotArm.moveRight()
    robotArm.drop()   
    robotArm.moveLeft()
    robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()