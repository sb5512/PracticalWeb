import time
import sys
import random

c = 0;
DISTANCE = 10; # Distance you move for the sample. i.e. 10 cm 
ERROR_SIGMA_DISTANCE = 0.5 # in cm
ERROR_SIGMA_ANGLE = 2 #degrees
ERROR_SIGMA_ROTATION_ANGLE = 5 #degrees 

def getX(initialX , initialTheta , errorDistance):
    xNew = initialX + (DISTANCE + errorDistance * math.cos(initialTheta)
    return xNew

def getY(initialY , initialTheta , errorDistance):
    yNew = initialY + (DISTANCE + errorDistance * math.cos(initialTheta)
    return yNew

def getTheta(initialTheta , errorAngle ):
    thetaNew = initialTheta + errorAngle 
    return thetaNew

#def getRandomX():
#    return random.randint((c%10)*50, (c%10 + 1)*50)
#
#def getRandomY():
#    return random.randint((c%10)*50, (c%10 + 1)*50)

#def getRandomTheta(): 
 #   return random.randint(0, 360)

def getRandomNumberGaussian(sigma):
    mean = 0 
    return random.gauss(mean , sigma)

numberOfParticles = 100

line1 = (10, 10, 10, 500) # (x0, y0, x1, y1)
line2 = (20, 20, 500, 200)  # (x0, y0, x1, y1)

print "drawLine:" + str(line1)
print "drawLine:" + str(line2)
print getRandomNumberGaussian()

while True:
    # Create a list of particles to draw. This list should be filled by tuples (x, y, theta).
    initialX = 0
    initialY = 0
    initialTheta = 0
    particles = [0]*numberOfParticles
    for i in range(numberOfParticles):
        particles[i] = (initialX, initialY , initialTheta)
        errorDistance = getRandomNumberGaussian(sigma)
        initialX = getX(initialX , initialTheta , errorDistance)
        initialY = getY(initialY , initialTheta , errorDistance)
        
        errorTheta = getRandomNumberGaussian(ERROR_SIGMA_ANGLE)
        initialTheta = getTheta(initialTheta , errorTheta)
        #particles = [(getX(initialX), getY(initialY), getRandomTheta(initialTheta)) for i in range(numberOfParticles)]
    print "drawParticles:" + str(particles)
    
    c += 1;
    time.sleep(0.25)
