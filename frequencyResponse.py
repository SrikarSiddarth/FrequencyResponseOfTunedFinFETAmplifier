import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv




def nothing(x):
    pass

img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('gm','image',1,10,nothing)
cv.createTrackbar('Cgs','image',1,50,nothing)
cv.createTrackbar('Ql','image',1,10,nothing)
cv.createTrackbar('u','image',1,10,nothing)

# number of sample points
n = 1000.0

gm = 1					# conductance of the finfet 
Ql = 1					# quality factor of the Inductor
Cgs = 1					# capacitance between gate and souce
u = 1						# u = Cgd/Cgs
f = np.linspace(1, n+1, n)															
while(1):
	cv.imshow('image',img)
	k = cv.waitKey(1) & 0xFF
	if k == 27:
		break
	# get current positions of four trackbars
	gm_ = cv.getTrackbarPos('gm','image')
	Cgs_ = cv.getTrackbarPos('Cgs','image')
	Ql_ = cv.getTrackbarPos('Ql','image')
	u_ = cv.getTrackbarPos('u','image')
    	gm = gm_
    	Cgs = 10**(-12)*Cgs_
    	Ql = 10**(-8)*Ql_
    	u = 0.1*u_													
	
	if gm>0 and Ql>0 and Cgs>0:

		# This is the equation for gain of a tuned amplifier stage
		Av = gm*Ql/(2*np.pi*Cgs*(1 + u)*f)


		fig, plot = plt.subplots()

		plot.plot(f, 20*np.log10(Av))


		fig.savefig('test.jpg')
		img = cv.imread('test.jpg')
cv.destroyAllWindows()