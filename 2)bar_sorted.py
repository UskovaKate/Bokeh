from bokeh.io import show, output_file
from bokeh.plotting import figure

output_file("bar_sorted.html")

fruits = ['Бананы', 'Груши', 'Нектарины', 'Вишня', 'Виноград', 'Клубника']
counts = [15, 9, 7, 3, 12, 2]

# sorting the bars means sorting the range factors
sorted_fruits = sorted(fruits, key=lambda x: counts[fruits.index(x)])

p = figure(x_range=sorted_fruits, plot_height=350, title="Количество фруктов",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)