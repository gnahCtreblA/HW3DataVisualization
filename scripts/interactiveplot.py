import os
import pandas as pd
import panel as pn
import matplotlib.pyplot as plt
from bokeh.plotting import figure
from bokeh.io import output_notebook
from bokeh.models import ColumnDataSource, TapTool, CustomJS
from collections import Counter

# Initialize Panel extension
pn.extension()

# Define the path to your dataset
dataset_path = "../dataset/images"

# Dictionary to store counts for each category
category_counts = Counter()

# Loop through each folder in the dataset directory
for category in os.listdir(dataset_path):
    category_path = os.path.join(dataset_path, category)
    if os.path.isdir(category_path):
        num_images = len([f for f in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, f))])
        category_counts[category] = num_images

# Convert to DataFrame
data = pd.DataFrame.from_dict(category_counts, orient='index', columns=['Count']).reset_index()
data.columns = ['Category', 'Count']


# Create a Bokeh plot
def create_interactive_plot():
    source = ColumnDataSource(data)

    p = figure(x_range=data['Category'], title="Number of Images in Each Category",
               tools="tap", height=400, width=700)
    p.vbar(x='Category', top='Count', source=source, width=0.9, color='skyblue')

    # Customize the hover tool to display counts
    p.add_tools(TapTool())
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.yaxis.axis_label = "Number of Images"
    p.xaxis.axis_label = "Categories"

    # JavaScript callback to show the count when a bar is clicked
    callback = CustomJS(args=dict(source=source), code="""
        var indices = source.selected.indices;
        if (indices.length > 0) {
            var index = indices[0];
            var count = source.data['Count'][index];
            alert('Count: ' + count);
        }
    """)

    p.js_on_event('tap', callback)

    return pn.pane.Bokeh(p)


# Create the Panel layout
layout = pn.Column("# Image Count by Category", create_interactive_plot())

# Display the Panel
layout.show()