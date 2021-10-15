import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sns.set_style("whitegrid")
pd.set_option("display.max_rows", None, "display.max_columns", None)

memento = pd.read_csv("../OutputFiles/ScatterplotInfo.csv")
memento.head()


ax = sns.scatterplot(x="Age(days)", y="Mementos", data=memento)
ax.set_xlabel ('Age in Days')
ax.set_ylabel ('Number of Mementos')
ax.set_title('Analysis of Datetimes of Mementos')
ax.set_xlim(left=0)
ax.set_xticks(ax.get_xticks()[::35])
ticks = ax.get_xticks()
labels = ['{:,.0f}'.format(x) for x in ticks]
ax.set_xticklabels(labels)

plt.show()