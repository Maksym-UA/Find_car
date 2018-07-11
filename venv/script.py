from flask import Flask
from flask import url_for
from flask import request
from flask import render_template
from flask import make_response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Compare Cars!'
	
@app.route('/debug')
def hello():
    return 'debug is working'
	
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/about')
def about():
    return 'The about page'

	
# @app.route('/login')
# def login():
#     return 'login'
	
@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
  
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'	
	
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
		
		
# @app.route('/comparecars')
# def comparecars():
    # return render_template('index.html')
	


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('index.html', error=error)

	
@app.route('/comparecars')
def index():
    # read coolies
    price_range_end = request.cookies.get('range_end')
    # store
    resp1 = make_response(render_template('index.html'))
    resp1.set_cookie('range_end', 'price range end', max_age=3600)

    return resp1
	
# redirect	
@app.route('/')
def index2():
    return redirect(url_for('login'))

	
# responses of server
# customize the error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404