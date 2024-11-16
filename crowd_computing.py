# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:53:39 2024

@author: santo
"""

import statistics
import matplotlib.pyplot as plt
# List of estimates provided by 75 people
Estimates=[1000, 1010, 1786, 2000, 1500, 1500, 100, 120, 150, 150, 150, 170, 175, 180, 197, 200, 200, 200, 200, 200, 200, 220, 220, 220, 220, 234, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 250, 263, 270, 275, 275, 285, 300, 300, 300, 300, 300, 300, 320, 325, 350, 350, 350, 350, 400, 400, 400, 400, 400, 400, 400, 450, 467, 500, 500, 500, 500, 500, 500, 500, 550, 550, 550, 600, 600, 600, 650, 700, 700, 720]
# Empty list for y-values
y=[]
# Sort the estimates list in ascending order
Estimates.sort()
# calculate 10% of the total number of elements
tv=int(0.1 * len(Estimates))
#remove the bottom 10% to eliminate underestimations
Estimates=Estimates[tv:]
#remove the top 10% to eliminate overestimations
Estimates=Estimates[:len(Estimates)-tv]
for i in range(len(Estimates)):
    y.append(5)
plt.plot(Estimates,y,'r--')
plt.plot([statistics.mean(Estimates)],[5],'ro')
plt.plot([statistics.median(Estimates)],[5],'bs')
plt.plot([375],[5],'g^')
plt.xlabel("Estimate Values")
plt.ylabel("Y (constant value)")
plt.title("Estimates Visualization (After Removing 10% Outliers)")

# Display the plot
plt.show()