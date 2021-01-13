import sys, os

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/source/python/")

import io
import random
from flask import Flask, Response, render_template, request
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


import machine_learning as ML

# import sql_methods as SQLM

# print(SQLM.gets_sample_df(10, 5))
# SQLM.save_df_as_sqlite(SQLM.gets_sample_df(10, 5))
# print(ML.isWorking())
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def welcome():
    ML.run()
    return render_template("index.html")
    # if request.method == "POST":
    #    print("button pressed")
    #    ML.run()
    #    return render_template("index.html")


app.run(debug=True)
