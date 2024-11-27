from flask import Flask,Blueprint,request,render_template

bp=Blueprint("home_page",__name__) #home_page is the blueprint name we initilized the blueprint name

@bp.route('/')
def homepage():
    if 'username' in request.args.keys() and 'password' in request.args.keys() and 'list' in request.args.keys() :
        username=request.args['username']
        password=request.args['password']
        list=request.args['list']
        #print(type(request.args['list']))#string
        # return f"home page username={username} password={password}"
        return render_template('/home_page.html',username=username,password=password,list=list)
    else:
        return render_template('/static_page.html')

@bp.route('/about',methods=['GET','POST','PUT','DELETE'])
def about():
    if request.method=='GET':
        print("get")
        return "get method"

    elif request.method=='Post':
        print("post")
        return "post method"

    elif request.method=='PUT':
        print("put")
        return "put method"
    elif request.method=='DELETE':
        print("delete")
        return "delete method"
    else:
        print("other")
    return "about page"

@bp.route('/career')
def career():
    return "career page"
