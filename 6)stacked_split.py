from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import GnBu3, OrRd3
from bokeh.plotting import figure

output_file("stacked_split.html")

fruits = ['Бананы', 'Груши', 'Нектарины', 'Вишня', 'Виноград', 'Клубника']
years = ["2019", "2020", "2021"]

exports = {'fruits' : fruits,
           '2019'   : [2, 1, 4, 3, 2, 4],
           '2020'   : [5, 3, 4, 2, 4, 6],
           '2021'   : [3, 2, 4, 4, 5, 3]}
imports = {'fruits' : fruits,
           '2019'   : [-1, 0, -1, -3, -2, -1],
           '2020'   : [-2, -1, -3, -1, -2, -2],
           '2021'   : [-1, -2, -1, 0, -2, -2]}

p = figure(y_range=fruits, plot_height=250, x_range=(-16, 16), title="Импорт/Экспорт фруктов по годам",
           toolbar_location=None)

p.hbar_stack(years, y='fruits', height=0.9, color=GnBu3, source=ColumnDataSource(exports),
             legend_label=["%s экспорт" % x for x in years])

p.hbar_stack(years, y='fruits', height=0.9, color=OrRd3, source=ColumnDataSource(imports),
             legend_label=["%s импорт" % x for x in years])

p.y_range.range_padding = 0.1
p.ygrid.grid_line_color = None
p.legend.location = "top_left"
p.axis.minor_tick_line_color = None
p.outline_line_color = None

show(p)