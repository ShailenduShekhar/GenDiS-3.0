import json
from bson import ObjectId
from flask import Flask, render_template, jsonify
from gendis_mongodb import coll
import plotly
import plotly.express as px
import pandas as pd


app = Flask(__name__)

final_csv_file_location = '/home/ibab/sem4/project/codes/sunburst_implementation/readyingTheData/superfamilyDataForSunburst/SMS/'
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/tools1")
def tools1():
    return render_template("tools1.html")

@app.route("/tools2")
def tools2():
    return render_template("tools2.html")

@app.route("/tools3")
def tools3():
    return render_template("tools3.html")

@app.route("/superfamily")
def superfamily():
    return render_template("browseby_basic_layout_bs.html")

# get data from MongoDB by using the coll object that has been imported.
# this 'coll' object actually has all the data at once. I would bring the data in parts so as to not slow the server down.
@app.route("/superfamily_data", methods=['POST'])
def getSuperfamilyData():
    tbody_data = list(coll.find({})) # this returns the data in BSON format
    def handleObjectId(obj): # this function takes care of ObjectId object which cannot be serialized into JSON normally, like using jsonify
        if isinstance(obj, ObjectId): return str(obj)
        raise TypeError(f'Object of type {type(obj)} is not JSON serializable')
    return json.dumps(tbody_data, default=handleObjectId)

@app.route("/superfamily_display/<sf_code>")
def superfamily_display(sf_code): # try 144206 as the sf_code, gives a good visualization
    df = pd.read_csv(f'{final_csv_file_location}{sf_code}.csv')
    df.insert(0,'ROOT','Root')
    fig = px.sunburst(
                df, path=list(df.columns)[:8], 
                color='Order',
                maxdepth=4,
                #width=800,
                height=600
            )
    fig.update_layout(title_font_size=42, title_font_family="Arial")
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('superfamily_display.html',sf_code=sf_code, graphJSON=graphJSON)

@app.route("/class")
def _class():
    return render_template("browseby_basic_layout_bs.html",coll=list(coll.find({})))

if __name__ == "__main__": app.run(debug=True)


"""

Some important points to remember:
    1. The url_for function does not direct to routes but functions that are defined here.
    2. 

"""
