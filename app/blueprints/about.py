from flask import Flask ,Blueprint,render_template,redirect,url_for

bp=Blueprint("about",__name__)

@bp.route('/about/')
def about():
    return render_template("about.html")

@bp.route('/about/name/')
def about_name():
    return redirect(url_for('about.think'))


@bp.route('/about/help')
def help():
    return redirect(url_for("home_page.career"))


@bp.route('/about/think')
def think():
    return render_template("static_page.html")