from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure

output_file("color_bars.html")

fruits = ['Бананы', 'Груши', 'Нектарины', 'Вишня', 'Виноград', 'Клубника']
counts = [15, 9, 7, 3, 12, 2]

source = ColumnDataSource(data=dict(fruits=fruits, counts=counts, color=Spectral6))

p = figure(x_range=fruits, y_range=(0,9), plot_height=250, title="Количество фруктов",
           toolbar_location=None, tools="")

p.vbar(x='fruits', top='counts', width=0.6, color='color', legend_field="fruits", source=source)

p.xgrid.grid_line_color = None
p.legend.orientation = "vertical"
p.legend.location = "top_left"

show(p)