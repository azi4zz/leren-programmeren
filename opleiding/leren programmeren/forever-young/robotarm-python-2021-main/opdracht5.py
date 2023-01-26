from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(7):
    robotArm.moveRight()
robotArm.grab()
for g in range (1): 
    robotArm.moveRight()
robotArm.drop()     
for u in range(2):
    robotArm.moveLeft()
robotArm.grab() 
for a in range (1): 
    robotArm.moveRight()
robotArm.drop()    
for z in range(2):
    robotArm.moveLeft()
robotArm.grab() 
for l in range (1): 
    robotArm.moveRight()
robotArm.drop()    
for j in range(2):
    robotArm.moveLeft()
robotArm.grab() 
for k in range (1): 
    robotArm.moveRight()
robotArm.drop()    
for x in range(2):
    robotArm.moveLeft()
robotArm.grab() 
for v in range (1): 
    robotArm.moveRight()
robotArm.drop()    
for x in range(2):
    robotArm.moveLeft()
robotArm.grab() 
for g in range (1): 
    robotArm.moveRight()
robotArm.drop()    
for x in range(2):
    robotArm.moveLeft()
robotArm.grab() 
for s in range (1): 
    robotArm.moveRight()
robotArm.drop()    
for x in range(2):
    robotArm.moveLeft()
robotArm.grab() 
for q in range (1): 
    robotArm.moveRight()
robotArm.drop()    
for t in range(1):
    robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()