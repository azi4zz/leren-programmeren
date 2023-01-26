from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')

# Jouw python instructies zet je vanaf hier:
for i in range(1):
    robotArm.moveRight()
robotArm.grab()
for i in range(1) :
    robotArm.moveLeft()
robotArm.drop() 
for i in range(1):
    robotArm.moveRight()
robotArm.grab()   
for i in range(1) :
    robotArm.moveRight()
robotArm.drop() 
for x in range(1):
    robotArm.moveLeft()
robotArm.grab()     
robotArm.moveLeft()
robotArm.drop() 
for i in range(1):
    robotArm.moveRight()
robotArm.grab()   
for i in range(1) :
    robotArm.moveRight()
robotArm.drop() 
for x in range(1):
    robotArm.moveLeft()
robotArm.grab()     
robotArm.moveLeft()
robotArm.drop() 
for i in range(1):
    robotArm.moveRight()
robotArm.grab()   
for i in range(1) :
    robotArm.moveRight()
robotArm.drop() 
for r in range(1):
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()