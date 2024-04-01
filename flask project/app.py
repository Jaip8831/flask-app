# from flask import Flask,render_template,request
from flask import *

from insertData import inser
from getData import check





                 

    


app=Flask(__name__)



@app.route('/')
def home():
    return render_template('/index.html')



@app.route('/register',methods=['GET','POST'])
def register():
    
    if request.method=='POST':
        fName=request.form.get('fName')
        lName=request.form.get('lName')
        uName=request.form.get('uName')
        uMail=request.form.get('uMail')
        uPass=request.form.get('uPass')
        
        inser(fName,lName,uName,uMail,uPass,)


        return redirect('/login')
    return render_template('/register.html')

@app.route('/login',methods=['POST','GET'])
def login():
    good=None
    
    
    if request.method=='POST':
        un=request.form.get('username')
        ps=request.form.get('password')
        good=check(un,ps)
        
        
        # return redirect('/login')
        
        

        
    return render_template('/login.html',good=good)                                                               

@app.route('/about')
def about():
    return render_template('/about.html')

                                                                                                                                   







if __name__=='__main__':
    app.run(debug=True,port=9000)