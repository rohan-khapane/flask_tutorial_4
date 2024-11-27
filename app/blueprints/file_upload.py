import pandas as pd
from flask import Flask, Blueprint,redirect,request,render_template

bp=Blueprint("file_upload",__name__)

@bp.route('/')
def index():
    return render_template("file_upload.html")

@bp.route('/file',methods=["POST","GET"])
def file():
    file= request.files['file']
    if file.content_type=='text/plain':
        return file.read().decode()
    elif file.content_type=='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'or file.content_type=='application/vnd.ms-excel':
        df=pd.read_excel(file)
        return df.to_html()
    else:
        return "Error in uploading"
    
    

