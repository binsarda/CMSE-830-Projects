import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
my_iris_df = sns.load_dataset("iris")
my_mpg_df=sns.load_dataset("mpg")
my_fig1 = px.scatter_3d(my_iris_df , x='sepal_length', y='sepal_width', z='petal_length',
              color='species')
my_fig1.show()

plt.scatter(my_mpg_df["mpg"],my_mpg_df["horsepower"], c="pink",
            linewidths=2,
            marker="s",
            edgecolor="green",
            s=50)

plt.scatter(my_mpg_df["mpg"],my_mpg_df["acceleration"], c="yellow",
            linewidths=2,
            marker="^",
            edgecolor="red",
            s=200)

plt.xlabel("MPG")
plt.ylabel("HP and Acc.")
plt.show()