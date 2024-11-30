from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from calorie import Calories
from temperature import Temperature

app = Flask(__name__)

class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class CaloriesFormPage(MethodView):
    def get(self):
    
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform = calories_form)

    def post(self):

        calories_form = CaloriesForm(request.form)
        temperature = Temperature(country = calories_form.country.data, city = calories_form.city.data).get()
        calories_calculate = Calories(calories_form.weight.data, calories_form.height.data, calories_form.age.data,
                                      temperature)

        calories = calories_calculate.calculate()

        return render_template('calories_form_page.html',
                               caloriesform = calories_form,
                               calories = calories, result = True )



class CaloriesForm(Form):

    weight = StringField('weight:', default = 70)
    height = StringField('height:', default = 155)
    age = StringField('age:', default = 18)
    country = StringField('country:', default = 'india')
    city = StringField('city:', default = 'pune')

    button = SubmitField('Calculate')


app.add_url_rule('/', view_func= HomePage.as_view('home_page')),

app.add_url_rule('/calories_form', view_func = CaloriesFormPage.as_view('calories_form_page'))

app.run(debug = True)