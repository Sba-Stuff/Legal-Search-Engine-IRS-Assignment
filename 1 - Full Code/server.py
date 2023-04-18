# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import *
from loader import loadfolders,loadfiles
from CosineSimilarity import  tfidf_cosine_similarity,bm25_cosine_similarity
from filewriter import writefile
import sys
from removeblanklines import removeemptylines,abstract
from pdfreader3 import readpdf
from template import mainpage,tfidfx,bm25x
import os
from qnormalizer import querynormalizer

#TEMPLATE_DIR = os.path.abspath('../templates')
#STATIC_DIR = os.path.abspath('../static')
# app = Flask(__name__) # to make the app run without any
#app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

app = Flask(__name__,template_folder="template/",static_folder="static/")

@app.route('/')
def hello_world():
    #return mainpage()
    return render_template("index.html")
@app.route('/tfidf/',methods=["POST", "GET"])
def tfidf():
    lig = ""
    page = ""
    if request.method == "POST":
        lig = request.form["textfield"]
        page = request.form['search']
    print(querynormalizer(lig))
    return render_template("tfidf.html",output=str(tfidfx(querynormalizer(lig),page)))


@app.route('/bm25/',methods=["POST", "GET"])
def bm25():
    lig = ""
    page = ""
    if request.method == "POST":
        lig = request.form["textfield"]
        page = request.form['search']
    #return bm25x(lig,page)
    print(querynormalizer(lig))
    return render_template("bm25.html",output=str(bm25x(querynormalizer(lig),page)))

    return xieon
# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run()