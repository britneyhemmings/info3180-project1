from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import FileField, FileRequired, FileAllowed


class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    rooms = IntegerField('No. of Bedrooms', validators=[InputRequired(), NumberRange(min=0)])
    bathrooms = IntegerField('No. of Bathrooms', validators=[InputRequired(), NumberRange(min=0)])
    price = StringField('Price',validators=[InputRequired()])
    pType = SelectField('Property Type',choices=[("House","House"),("Apartment","Apartment")])
    location = StringField('Location',validators=[InputRequired()])    

    image = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only! (jpg, png)')
    ])
