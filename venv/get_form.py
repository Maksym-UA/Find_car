from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from werkzeug.exceptions import abort

# creates a Blueprint named 'get_form'. the blueprint needs to know where it is
# defined so __name__ is passed as the second argument. The url_prefix will be
# prepended to all the URLs associated with the blueprint.
bp = Blueprint('get_form', __name__)

fuel = ['gasoline', 'diesel', 'electro']
transmissions = ['automatic', 'manual']
brands = ['Alfa Romeo', 'BMW', 'Citroen', 'Ford']


@bp.route('/index', methods=['POST', 'GET'])
def set_parameteres():
    if request.method == 'POST':
        range_start = request.form['range_start']
        range_end = request.form['range_end']
        fuel_type = request.form['fuel_type']
        transmission = request.form['transmission']
        brand = request.form['brand']
        error = None

        if not range_start or not range_end:
            error = 'Please add start or end price range.'

        if error is not None:
            flash(error)
        else:
            print(range_start)
            print(transmission)
            return redirect(
                url_for(
                    'get_form.search',
                    range_start=range_start, range_end=range_end,
                    transmission=transmission, brand=brand
                    )
                    )

    return render_template('index.html', transmissions=transmissions, fuel=fuel, brands=brands)


@bp.route('/results', methods=['POST', 'GET'])
def search():

    error = None
    if error is None:
        print('results page')

    return render_template('results.html', error=error, transmissions=transmissions, fuel=fuel, brands=brands)
