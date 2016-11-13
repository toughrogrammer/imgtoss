from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired


class ImageUploadForm(FlaskForm):
    file = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'gif'], 'Images only!')
    ])
