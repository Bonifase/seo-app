from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UrlForm(FlaskForm):
    url = StringField('Url',
                      validators=[DataRequired(), Length(min=2, max=1000)])
    keyword = StringField('Keyword',
                          validators=[DataRequired(), Length(min=2, max=60)])
    submit = SubmitField('Search')
