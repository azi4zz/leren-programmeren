from RobotArm import RobotArm

robotArm = RobotArm('exercise 5')

# Jouw python instructies zet je vanaf hier:
robotArm.speed = 2
for i in range(7):
    robotArm.moveRight()
robotArm.grab()

for g in range (17): 
    robotArm.moveRight()
    robotArm.drop()     
    robotArm.moveLeft()
    robotArm.grab() 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()