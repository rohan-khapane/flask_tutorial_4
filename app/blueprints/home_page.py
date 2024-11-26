from flask import Flask,Blueprint,request,render_template

bp=Blueprint("home_page",__name__) #home_page is the blueprint name we initilized the blueprint name

@bp.route('/')
def user():
    return "home page"

@bp.route('/about')
def about():
    return "about page"

@bp.route('/career')
def career():
    return "career page"
