from ast import Str
from email.policy import default
from typing import Optional
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField, RadioField, widgets, HiddenField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, Email, InputRequired, Length
from blog.models import User
from wtforms_validators import AlphaNumeric

class RegistrationForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired(), Length(max=20), \
    AlphaNumeric(message='Your username contains invalid characters. Please try alphanumeric characters only.')])
  password = PasswordField('New Password',validators=[InputRequired(), Length(max=20), \
    EqualTo('confirm_password', message='Passwords do not match. Please try again.'), \
      AlphaNumeric(message='Your password contains invalid characters. Please try alphanumeric characters only.')])
  confirm_password = PasswordField('Repeat Password',validators=[InputRequired()])
  email = StringField('Email',validators=[Email(message='Invalid email. Please check.'), DataRequired()])
  submit = SubmitField('Register')
  
  def validate_username(self, username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
      raise ValidationError('Sorry, there is a problem with your registration.')
      #raise ValidationError('Username already exist. Please choose a different one.')

class LoginForm(FlaskForm):
  username = StringField('Username',validators=[DataRequired(),Length(max=20)])
  password = PasswordField('Password',validators=[DataRequired(),Length(max=20)])
  submit = SubmitField('Login')

class PostForm(FlaskForm):
  post_order = SelectField('Post Order', default='date_desc', choices=[('date_desc', 'Newest'), ('date_asc', 'Oldest')], coerce=str, validators=[DataRequired()], render_kw={"onchange":"myFunction()"})
  #post_order = SelectField('Post Order', default=0, choices=[(0, 'Newest'), (1, 'Oldest')], coerce=int, validators=[DataRequired()])


class CommentForm(FlaskForm):
  title = StringField('Title (required)',validators=[DataRequired()])
  content = TextAreaField('Your Comment (required)',validators=[DataRequired()])
  #rating = RadioField('Rating', default = 5, choices=[(1, 'Bad'), (2, 'Good'), (3, 'Very good'), (4, 'Great'), (5, 'Awesome')], widget=widgets.TableWidget(with_table_tag=True))
  rating = HiddenField('Rating', validators=[InputRequired(message='Please select your rating.')])
  submit = SubmitField('Submit')