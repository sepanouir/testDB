from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from wtforms.validators import InputRequired, Length, AnyOf,Email,EqualTo
from wtforms import StringField,EmailField,SubmitField
from flask_wtf import FlaskForm 
from flask_bootstrap import Bootstrap
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tigmtikqbzwerf:b301996756834337f82a634cfcd69734c5ba87a0dceebadc8f65a49e7dc30b94@ec2-52-212-228-71.eu-west-1.compute.amazonaws.com:5432/dcvelmj44a06do'
app.config['SECRET_KEY'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
bootstrap=Bootstrap(app=app)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username


class UserForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    submit = SubmitField('submit')

    def add(self):
        newUser=User(
        username = self.username.data,
        email = self.email.data,
        )  
        db.session.add(newUser)
        db.session.commit()
        return True





@app.route('/users',methods=['GET','POST'])
def users():
    form = UserForm()
    if request.method=='POST':
        if form.validate_on_submit():
            form.add()
    users=User.query.all()
    return render_template("users.html",users=users,form=form)

if __name__=='__main__':
    app.run(debug=True)