from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
robotArm.speed = 4
for s in range(1, 5):
  for q in range(s):
    robotArm.grab()
    for x in range(5):
      robotArm.moveRight()
    robotArm.drop()
    for x in range(5 - int(q == s - 1)):
        robotArm.moveLeft()
robotArm.wait()