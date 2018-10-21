from flask import Blueprint, render_template, url_for, redirect
from myproject import db
from myproject.models import Car
from myproject.cars.forms import AddForm, DelForm

cars_blueprint = Blueprint('cars', __name__, template_folder='templates/cars')


@cars_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        new_car = Car(name)
        db.session.add(new_car)
        db.session.commit()

        return redirect(url_for('cars.list'))

    return render_template('add.html', form=form)


@cars_blueprint.route('/list')
def list():
    cars = Car.query.all()
    return render_template('list.html', cars=cars)


@cars_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        car = Car.query.get(id)
        db.session.delete(car)
        db.session.commit()

        return redirect(url_for('cars.list'))
    return render_template('delete.html', form=form)
