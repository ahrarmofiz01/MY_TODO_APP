from flask import Blueprint,render_template,request,redirect,url_for,flash
auth_bp=Blueprint('auth',__name__)
USER_CREDENTIALS={
    'username':'admin',
    'password':'1234'
}
@auth_bp.route('/login',methods=["GET","POST"])
def login():
     if request.method == "POST":
          username=request.form.get('username')
          passward = request.form.get('password')