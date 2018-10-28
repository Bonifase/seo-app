from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UrlForm(FlaskForm):
    url = StringField('Url',
                      validators=[DataRequired(), Length(min=2, max=20)])
    keyword = StringField('Keyword',
                          validators=[DataRequired(), Email()])
    submit = SubmitField('Search')
