from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ActivityForm(FlaskForm):
    name = StringField("Activity name", [DataRequired()])
    
    class Meta:
        csrf = False