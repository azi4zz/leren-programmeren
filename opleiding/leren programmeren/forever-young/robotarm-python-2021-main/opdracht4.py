from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(1):
    robotArm.moveRight()
robotArm.drop()   
for i in range(1):
    robotArm.moveLeft()
robotArm.grab()
for q in range(1):
    robotArm.moveRight()
robotArm.drop()   
for e in range(1):
    robotArm.moveLeft()
robotArm.grab()
for t in range(1):
    robotArm.moveRight()
robotArm.drop()   
for h in range(1):
    robotArm.moveLeft()
robotArm.grab()
for k in range(1):
    robotArm.moveRight()
robotArm.drop()   
for x in range(1):
    robotArm.moveLeft()    
robotArm.grab()
for a in range(1):
    robotArm.moveRight()
robotArm.drop()   
for p in range(1):
    robotArm.moveRight()            


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()