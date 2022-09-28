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


# equation of second degree parabola 

# y = a + bx + c(x^2)



# Σy = na + bΣx + c∑(x^2) 			------------------- (i)

# Σ(xy) = aΣx + bΣ(x^2) + c∑(x^3) 			------------------- (ii)

# Σ((x^2)y) = aΣ(x^2) + bΣ(x^3) + c∑(x^4)  			------------------- (ii)



# solving above equation (i), (ii) and (iii) to value of a,b and c

x = np.array([0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4])
y = np.array([1, 1.5, 1.8, 1.4, 1.3, 2.5, 2.78, 5, 6.3])
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
Σx2y = np.sum(x*x*y) # Σ((x^2)*y)
Σx3 = np.sum(x*x*x) # Σ(x^3)
Σx4 = np.sum(x*x*x*x) # Σ(x^4)



# Getting equations (i),(ii) and (iii) in matrix form

# 			n.a    +      ∑x.b   + ∑(x^2).c  =  Σy
#	   		Σx.a   +  Σ(x^2).b   + ∑(x^3).c  =  Σ(xy)
#		Σ(x^2).a   +  Σ(x^3).b   + ∑(x^4).c=  Σ(xy)



# In matrix form


#				  A 		*  C     =    B

#		    [n         Σx 	      ∑(x^2)]    [a]        [Σy]
#		    [Σx        Σ(x^2)	  ∑(x^3)]  * [b]	=   [Σxy]
#		    [Σ(x^2)    Σ(x^3)	  ∑(x^4)]    [c]	    [Σ(x^2)y]


A = np.array([[n, Σx, Σx2], [Σx, Σx2, Σx3], [Σx2, Σx3, Σx4]])
B = np.array([Σy, Σxy, Σx2y])

# Linear algebra
a, b, c = np.linalg.solve(A, B) # C = [a, b, c]


###### Equation of straight line ######
y = a + b*x + c*(x**2)


##### Line plot of equation #####
plt.plot(x, y, c="r")
plt.title("Parabola fitting", fontdict=font1)
plt.xlabel("x", fontdict=font2)
plt.ylabel("y", fontdict=font2)
###################################
plt.show()