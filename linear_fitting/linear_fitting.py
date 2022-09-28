import numpy as np
import matplotlib.pyplot as plt


# Fonts for labels and title
font1 = {
	'family':'serif',
	'size':20,
	'color':'black'
}
font2 = {
	'family':'serif',
	'size':15,
	'color':'brown'
}


# equation of fitted line 

# y = a + bx

# Σy = na + bΣx 			------------------- (i)
# Σ(xy) = aΣx + bΣ(x^2) 	------------------- (ii)

# solving above equation (i) and (ii) to value of a and b


x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.4, 3, 3.6, 4, 4.6, 5, 5.56, 6])
# length of both arrays
n=len(x)

##### Scatter plot of x and y #####
plt.scatter(x, y)
###################################

# summations
Σx = np.sum(x)
Σy = np.sum(y)
Σxy = np.sum(x*y)
Σx2 = np.sum(x*x) # Σ(x^2)


# Getting equations (i) and (ii) in matrix form

# 			n.a    +      ∑x.b  =  Σy
#	   		Σx.a   +  Σ(x^2).b  =  Σ(xy)



# In matrix form


#				  A 		*  C     =    B

#		    [n         Σx ] * [a]    =   [Σy]
#		    [Σx     Σ(x^2)]   [b]	     [Σxy]


A = np.array([[n, Σx], [Σx, Σx2]])
B = np.array([Σy, Σxy])

# Linear algebra
a, b = np.linalg.solve(A, B) # C = [a, b]


###### Equation of straight line ######
y = a + b*x


##### Line plot of equation #####
plt.plot(x, y, c="r")
plt.title("Line fitting", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y", fontdict=font2)
###################################
plt.show()