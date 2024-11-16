### Concept: Wisdom of the Crowd

This project demonstrates how a group's collective judgment can be more accurate than individual opinions, especially when extreme outliers are removed.
By trimming the data, the average (mean) and middle value (median) of the group’s estimates tend to align closely with a true or expected value, showcasing the power of the **Wisdom of the Crowd**.
**Outlier Removal:**
   - To demonstrate the accuracy of the collective opinion, the program removes **the lowest 10% and the highest 10%** of the estimates.
**Data Visualization:**
   - The program then generates a plot to show the estimates after outlier removal:
     - A **red dashed line** representing the filtered estimates.
     - Three key statistical markers are highlighted:
       - **Mean (red circle)**: The average estimate of the remaining data after outlier removal.
       - **Median (blue square)**: The middle value in the sorted estimates.
       - **Fixed Estimate (green triangle)**: A predetermined reference value (375) is plotted for comparison.
 **Key Insight:**
   - The plot demonstrates that, even if individual estimates vary significantly, the *mean and median* of the group's estimates converge toward a more accurate value after eliminating extreme outliers.


![Estimate Plot](https://github.com/santoshisalver/CrowdComputing/blob/master/crowd_comp.jpg?raw=true)


