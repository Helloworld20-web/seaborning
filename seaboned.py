import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

seaboneds = pd.read_csv("Salary.csv")

#Matplot
seaboneds.plot(x="YearsExperience", y="Salary", marker='o', color="black")
plt.title("Correlation between Health Problems and Absences")
plt.xlabel("Years of Experience")
plt.ylabel("Employees' Salary")
plt.show()

#Main Plots
sns.set_style("darkgrid")
sns.color_palette("viridis")

sns.scatterplot(x="YearsExperience", y="Salary", data=seaboneds)

sns.pairplot(seaboneds)

sns.relplot(x="YearsExperience", y="Salary", data=seaboneds, kind="scatter")

sns.lineplot(x="YearsExperience", y="Salary", data=seaboneds)

sns.displot(seaboneds, kind="ecdf")

sns.catplot(x="YearsExperience", y="Salary", data=seaboneds, kind="strip")

sns.catplot(x="YearsExperience", y="Salary", data=seaboneds, kind="violin")

sns.catplot(x="YearsExperience", y="Salary", data=seaboneds, kind="bar")

sns.catplot(x="YearsExperience", y="Salary", data=seaboneds, kind="point")

sns.lmplot(x="YearsExperience", y="Salary", data=seaboneds, hue="YearsExperience")

plt.show()

#Bar Plot
sns.barplot(x="YearsExperience", y="Salary", data=seaboneds)

plt.show()

#Heatmaps
sns.heatmap(seaboneds.corr(), annot=True)
sns.clustermap(seaboneds)

plt.show()

#Useless Stuff
sns.histplot(seaboneds, bins=10, kde=True)

sns.displot(seaboneds, kind="kde")

sns.displot(seaboneds, kind="hist")

sns.catplot(x="YearsExperience", y="Salary", data=seaboneds, kind="box")

sns.catplot(x="YearsExperience", y="Salary", data=seaboneds, kind="swarm")

sns.catplot(data=seaboneds, kind="count")

sns.regplot(x="YearsExperience", y="Salary", data=seaboneds)

plt.show()
