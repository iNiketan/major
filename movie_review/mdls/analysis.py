import pandas as pd
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

pickle_file = "dataout.pkl"
data = pd.read_pickle(os.path.join(BASE_DIR, pickle_file))
data.groupby('expressions').count()
n_row = data.shape[0]
tm = pd.DataFrame(data=[x for x in range(n_row)])
data.insert(2, "tm", tm, True)

scatter_plot = sns.catplot(x='tm', y='expressions',kind="strip",data=data)
scatter_plot.savefig(os.path.join(os.path.dirname(BASE_DIR), "static/images/scatter_plot.png"))

sns.catplot(x="expressions", y="tm", kind="swarm", data=data)
box_plot = sns.catplot(x="expressions", y="tm", kind="box", data=data);
box_plot.savefig(os.path.join(os.path.dirname(BASE_DIR), "static/images/box_plot.png"))

g = sns.catplot(x="expressions", y="tm", kind="violin", inner=None, data=data)
#sns.swarmplot(x="expressions", y="tm", color="k", size=3, data=data, ax=g.ax);
g.savefig(os.path.join(os.path.dirname(BASE_DIR), "static/images/violin_plot.png"))
