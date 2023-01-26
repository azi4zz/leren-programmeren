from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for j in range(1):
    robotArm.moveRight()
robotArm.drop()
for s in range(1):
   robotArm.moveLeft()
robotArm.grab()
for i in range(1):
    robotArm.moveRight()
robotArm.drop()        
for w in range(1):
   robotArm.moveLeft()
robotArm.grab()
for f in range(1):
    robotArm.moveRight()
robotArm.drop()     
for n in range(1):
   robotArm.moveLeft()
robotArm.grab()
for o in range(1):
    robotArm.moveRight()
robotArm.drop()         


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()