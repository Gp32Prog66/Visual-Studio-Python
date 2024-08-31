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


#Student Neighborhood Population
neighborhoods = ["Aspinwall", "Blawnox", "Fox Chapel", "Sharpsburg", "Indiana", "O'hara"]
colors = ['r', 'y', 'm', 'b']
studentPopulation = np.array([582,607,877,700,799,591])

'Legend'
plt.legend(title = 'Fox Chapel School District Neighborhoods', bbox_to_anchor=(0,1.04,1,0.3), loc = "lower left", mode = "expand", borderaxespad=0, ncol=3)

plt.bar(neighborhoods, studentPopulation, width = 0.5)


'Display Bar Chart'
plt.show()



