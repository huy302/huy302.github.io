import os
os.chdir("C:\\_DSB\\huy302.github.io\\")

from IPython.display import display, Javascript, HTML
import json

display(Javascript("require.config({paths: {d3: 'https://d3js.org/d3.v5.min'}});"))
display(Javascript(filename="circle.js"))
display(HTML(filename="circle.css.html"))

def draw_circles(data, width=600, height=400):
    display(Javascript("""
        (function(element){
            require(['circles'], function(circles) {
                circles(element.get(0), %s, %d, %d);
            });
        })(element);
    """ % (json.dumps(data), width, height)))

draw_circles([10, 60, 40, 5, 30, 10], width=500, height=200)