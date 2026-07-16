from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DecimalField,PasswordField
from wtforms.validators import DataRequired,Email,Length
from flask_ckeditor import CKEditorField


class ProductForm(FlaskForm):
    name = StringField('Product Name',validators=[DataRequired()])
    price = DecimalField('Price',validators=[DataRequired()])
    stock = DecimalField('Stock',validators=[DataRequired()])
    desc = CKEditorField('Description')
    submit = SubmitField('SUBMIT')

class EditForm(FlaskForm):
    name = StringField('Edit Product Name', validators=[DataRequired()])
    price = DecimalField('Edit price', validators=[DataRequired()])
    stock = DecimalField('Edit Stock', validators=[DataRequired()])
    desc = CKEditorField('Description')
    submit = SubmitField('SUBMIT')

class RegisterForm(FlaskForm):
    username = StringField('Enter your name',validators=[DataRequired()])
    email = StringField('Enter your email',validators=[Email('Enter a Valid Email Address')])
    password = PasswordField('Enter your password',validators=[DataRequired(),Length(min=8,message="Password length must be equal or greater than 8")])
    submit = SubmitField('SUBMIT')

class LoginForm(FlaskForm):
    email = StringField('Enter your name',validators=[DataRequired()])
    password = PasswordField('Enter your Password',validators=[DataRequired("Incorrect Password")])
    submit = SubmitField('SUBMIT')
