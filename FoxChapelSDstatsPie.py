import matplotlib.pyplot as plt
import numpy as np

""""
Important Note. The data for the population and total number of students is accurate. However,
the student population in each town is made up as that information isn't readily available.
*********************************************************************************************************************************************
A source I read indicates that Harmar isn't part of Fox Chapel School District, however the sign in Harmar indicates 
that it is part of Fox Chapel. Harmar isn't included in this demonstration Apparently small parts of cheswick is, but not 100 percent sure. 
"""



print("Fox Chapel School District Population and Student Stat Ratio")


#Neighborhood Population
neighborhoods = ["Aspinwall", "Blawnox", "Fox Chapel", "Sharpsburg", "Indiana", "O'hara"]
colors = ['r', 'y', 'm', 'b']
neighborhoodPopulation = np.array([2839,1417,5234,3102,9206,7341])



'Legend'
plt.legend(title = 'Fox Chapel School District Neighborhoods', loc = 4)

plt.pie(neighborhoodPopulation, labels = neighborhoods)


'Display Pie Chart'
plt.show()




