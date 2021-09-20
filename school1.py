import pandas as pd
import statistics 
import random
import plotly.graph_objects as go
import plotly.figure_factory as ff

df=pd.read_csv("School1.csv")
data=df["Math_score"].tolist()

population_mean=statistics.mean(data)
print(f"population_mean :{population_mean}")

population_stdev=statistics.stdev(data)
print(f"population stdev :{population_stdev}")


def random_set_of_mean(counter):
    data_set=[]
    for i in range (0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    
    mean=statistics.mean(data_set)
    return mean

mean_of_sample=[]

for a in range(0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_of_sample.append(set_of_mean)

sampling_mean=statistics.mean(mean_of_sample)
print(f"sampling mean :{sampling_mean}")
sampling_stdev=statistics.stdev(mean_of_sample)
print(f"sampling stdev :{sampling_stdev}")


first_stdev_start,first_stdev_end=population_mean-population_stdev,population_mean+population_stdev
second_stdev_start,second_stdev_end=population_mean-(2*population_stdev),population_mean+(2*population_stdev)
third_stdev_start,third_stdev_end=population_mean-(3*population_stdev),population_mean+(3*population_stdev)


# finding the population_mean for new sample data

df=pd.read_csv("School_1_Sample.csv")
data=df["Math_score"].tolist()

sample1_mean=statistics.mean(data)
print(sample1_mean)

# showing the distibution plot and traces of population_mean , sample_population_mean , first second and third stdev

fig=ff.create_distplot([mean_of_sample],["Math score"],show_hist=False)
fig.add_trace(go.Scatter(x=[population_mean,population_mean],y=[0,0.2],mode="lines",name="population_mean"))
fig.add_trace(go.Scatter(x=[first_stdev_start,first_stdev_start],y=[0,0.2],mode="lines",name="First stdev start"))
fig.add_trace(go.Scatter(x=[first_stdev_end,first_stdev_end],y=[0,0.2],mode="lines",name="First stdev end"))
fig.add_trace(go.Scatter(x=[second_stdev_start,second_stdev_start],y=[0,0.2],mode="lines",name="Second stdev end"))
fig.add_trace(go.Scatter(x=[second_stdev_end,second_stdev_end],y=[0,0.2],mode="lines",name="Second stdev end"))
fig.add_trace(go.Scatter(x=[third_stdev_start,third_stdev_start],y=[0,0.2],mode="lines",name="Third stdev start"))
fig.add_trace(go.Scatter(x=[third_stdev_end,third_stdev_end],y=[0,0.2],mode="lines",name="Third stdev end"))
fig.add_trace(go.Scatter(x=[sample1_mean,sample1_mean],y=[0,0.2],mode="lines",name="Sample1 mean"))
fig.show()

zscore=(sample1_mean-sampling_mean)/sampling_stdev
print(zscore)
