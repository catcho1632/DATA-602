from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/')
def main_page():
    return render_template('main_page.html')

@main.route('/calc', methods = ['post'])
def sign_post():
    number = request.form.get('number')
    calc = int(number) * 5

    return f'Your input times 5 is: {calc}'

