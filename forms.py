from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField
from wtforms.validators import DataRequired

class PortfolioForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    profile_picture = FileField('Profile Picture', validators=[DataRequired()])
    bio = TextAreaField('Short Bio', validators=[DataRequired()])
    skills = TextAreaField('Skills or Expertise', validators=[DataRequired()])
    online_links = TextAreaField('Links to Online Profiles', validators=[DataRequired()])
    submit = SubmitField('Create Portfolio')