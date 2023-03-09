from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.speed = 2
# Jouw python instructies zet je vanaf hier:
for i in range(1,6):
    for x in range(6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    for r in range (2):
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()