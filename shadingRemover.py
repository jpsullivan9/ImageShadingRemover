import numpy as np
import cv2
from numpy.random import seed
from numpy.random import randint

def shadingRemove(image_path, nPoints):

    seed(1)

    image = cv2.imread(image_path, 0)

    random_x = []
    random_y = []

    knownIntensity = []

    n, m = np.shape(image)

    #Choose number of random points

    random_x = randint(0,120,nPoints)
    random_y = randint(0,120,nPoints)


    for i in range(nPoints):
        knownIntensity.append(image[random_y[i]][random_x[i]])


    #Now will make it in terms of Aq = b problem. Just to make clear.

    b = knownIntensity
    ones = np.ones(100)
    a = []
    a.append(random_x)
    a.append(random_y)
    a.append(ones)

    a = np.transpose(a)
    # Now A is a nPoints x 3 matrix.

    #Perform least squares to get q.

    q = np.linalg.inv(np.transpose(a)@a)@np.transpose(a)@b


    intensityEstimate = np.zeros((n,m))


    for i in range(n):
        for j in range(m):
            intensityEstimate[i][j] = q[0]*j + q[1]*i + q[2]
            intensityEstimate[i][j] = np.round(intensityEstimate[i][j])


    intensityEstimate = np.array(intensityEstimate, np.uint8)

    # cv2.imshow("Intensity Estimate", intensityEstimate)
    # cv2.waitKey(0)

    outputImage = image - intensityEstimate


    # cv2.imshow("Output Image", outputImage)
    # cv2.waitKey(0)

    # for i in range(n):
    #     for j in range(m):
    #         if outputImage[i][j] < 0:
    #             print("less than 0")
    return outputImage