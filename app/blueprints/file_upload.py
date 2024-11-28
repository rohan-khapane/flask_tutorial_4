import pandas as pd
import os
import uuid
from flask import Flask, Blueprint,redirect,request,render_template,send_from_directory

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

@bp.route('/csv/',methods=['GET','POST'])
def csv():
    file2=request.files['file2']
    dataframe=pd.read_excel(file2)
    if not os.path.exists('Downloads'):
        print('creating downloading folder')
        os.makedirs('Downloads')
    filename=f'{uuid.uuid4()}.csv'
    dataframe.to_csv(os.path.join('Downloads',filename))
    return render_template('download.html',filename=filename)

    
@bp.route('/download/<path:filename>',methods=['GET'])
def download(filename):
    print(filename)
    #return f"{filename}"
    df=pd.read_csv(f'Downloads/{filename}')
    return df.to_html()
    #return send_from_directory('Downloads',filename)
    # return send_from_directory('Downloads',filename)
    # return send_from_directory('Downloads',filename,download_name='results.csv')
    #sreturn send_from_directory('Downloads',filename,download_name=f'{uuid.uuid4()}.csv')