from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import Email 

class ContactForm(FlaskForm):
 name = StringField('Name', validators=[DataRequired()])
 email = StringField('Email', validators=[DataRequired(), Email()])
 subject = StringField('Subject', validators=[DataRequired()])
 message = StringField('Message', validators=[DataRequired(), ])

