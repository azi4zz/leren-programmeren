
from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for s in range(5):
    for x in range(s): robotArm.moveRight()
    robotArm.grab()
    for q in range(9 -s -s): robotArm.moveRight()
    robotArm.drop()
    for p in range(9 + s): robotArm.moveLeft()
robotArm.wait()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()