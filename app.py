from flask import Flask, request
from faker import Faker

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route('/requirements/')
def get_requirements():
    with open('requirements.txt', 'r') as file:
        requirements = file.read().splitlines()

    return f'<h1>Requirements:</h1> {requirements}'


@app.route('/generate-users/')
def generate_users():
    fake = Faker()
    users = [fake.name() + ' ' + fake.email() for _ in range(100)]

    return f'<h1>Users:</h1> {users}'


@app.route('/generate-users/<int:count>/')
def generate_users_count(count):
    fake_count = Faker()
    users_count = [fake_count.name() + ' ' + fake_count.email() for _ in range(count)]

    return f'<h1>Users:</h1> {users_count}'

