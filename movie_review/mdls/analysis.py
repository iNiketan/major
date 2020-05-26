import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
points = {'angry': 9, 'disgust': 2, 'fear': 7, 'happy': 10, 'sad': 8,
          'surprise': 8, 'neutral': 5}

pickle_file = "dataout.pkl"
data = pd.read_pickle(os.path.join(BASE_DIR, pickle_file))


n_row = data.shape[0]
tm = pd.DataFrame(data=[x for x in range(n_row)])
data.insert(2, "time", tm, True)

scatter_plot = sns.catplot(x='time', y='expressions',kind="strip",data=data)
scatter_plot.savefig(os.path.join(os.path.dirname(BASE_DIR), "static/images/scatter_plot.png"))

sns.catplot(x="expressions", y="time", kind="swarm", data=data)
box_plot = sns.catplot(x="expressions", y="time", kind="box", data=data);
box_plot.savefig(os.path.join(os.path.dirname(BASE_DIR), "static/images/box_plot.png"))

g = sns.catplot(x="expressions", y="time", kind="violin", inner=None, data=data)
#sns.swarmplot(x="expressions", y="tm", color="k", size=3, data=data, ax=g.ax);
g.savefig(os.path.join(os.path.dirname(BASE_DIR), "static/images/violin_plot.png"))

try:
    labels = data['expressions'].unique()
    p = plt.savefig.pie(data.groupby('expressions').sum(), labels=labels)
    p.savefig(os.path.join(os.path.dirname(BASE_DIR), "static/images/pie_plot.png"))
except:
    pass

# calcutating the score for the movie
exp_count = data['expressions'].value_counts() # couting frequency of each expression
u = dict(exp_count)
sum = 0
for key in u:
    if key in points.keys():
        sum += u[key]*points[key]

score = sum/n_row
print("This is score {0:.1f}".format(score), end="")