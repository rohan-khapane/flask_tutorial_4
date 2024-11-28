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
    file2=request.files['file2']#got the file form the html page in using the name tag
    dataframe=pd.read_excel(file2) #convert it to dataframe 
    if not os.path.exists('app/Downloads'):  #creation of the new folder using the os module if not exists
        print('creating downloading folder')
        os.makedirs('app/Downloads')
    filename=f'{uuid.uuid4()}.csv' #created the filename 
    dataframe.to_csv(os.path.join('app/Downloads',filename)) #conversion of the data frame to csv file 
    return render_template('download.html',filename=filename) #redirecting to the download.html page and passes filename to the html page

#the download.html page has redirected here but the path has filename in it so use the <> to get the dynamic file name     
@bp.route('/download/<path:filename>',methods=['GET'])
def download(filename):
    print(filename)
    #return f"{filename}"
    df=pd.read_csv(f'app/Downloads/{filename}')#reading the csv file from the downloads
    return df.to_html() #returning the csv file content in html page as table 

#unable to create a download link for the file 
#return send_from_directory('Downloads',filename)
# return send_from_directory('Downloads',filename)
# return send_from_directory('Downloads',filename,download_name='results.csv')
# return send_from_directory('Downloads',filename,download_name=f'{uuid.uuid4()}.csv')