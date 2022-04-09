# Add any form classes for Flask-WTF here
from distutils.command.upload import upload
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Must be an Image')])
    description = TextAreaField('Description', validators=[DataRequired()])
