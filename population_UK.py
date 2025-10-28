from pyecharts.charts import Bar,Timeline
from pyecharts.options import TitleOpts, ToolboxOpts, LabelOpts

# get data
f = open("pop.csv", "r", encoding="UTF-8")
after_read = f.readlines()
f.close()

# optimize data
after_read.pop(0)
print(after_read)
data_set = []

for i in after_read:
    data_set.append(i.strip())
print(data_set)

# transform to dictionary
a1 = "Scotland"
a2 = "England"
a3 = "Northern Ireland"
a4 = "Wales"

data_dict = {}
for i in data_set:
    year = int(i.split(",")[0])
    a11 = int(i.split(",")[1])
    a22 = int(i.split(",")[2])
    a33 = int(i.split(",")[3])
    a44 = int(i.split(",")[4])
    try:
        data_dict[year].extend([[a1, a11],[a2, a22], [a3, a33], [a4, a44]])
    except KeyError:
        data_dict[year] = []
        data_dict[year].extend([[a1, a11],[a2, a22], [a3, a33], [a4, a44]])
print(data_dict)

# get x(area) and y(population) data

timeline = Timeline(
    init_opts={
        "width": "1500px",
        "height": "600px",
        "style": {"margin": "0 auto", "display": "block"}  #
    }
)

keys = data_dict.keys() #get years
for i in keys:
    data_dict[i].sort(key=lambda e:e[1],reverse=True) # sort by population
    year_data = data_dict[i] # get value
    x_data = []
    y_data = []
    for j in year_data:
        x_data.append(j[0])
        y_data.append(j[1])

    # construct bar chart
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("Poulation", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"Population of {i}"),
    )

    # construct timeline
    timeline.add(bar,str(i))


# optimize timeline
timeline.add_schema(
    play_interval=1000,
    is_auto_play=True,
    is_timeline_show=False,
    is_loop_play=True
)

# render
timeline.render()
