import requests

from flask import Flask, request
from faker import Faker
import pandas as pd


app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h2>Hello, World!</h3>"


@app.route('/requirements/')
def get_requirements():
    with open('requirements.txt', 'r') as file:
        requirements = file.read().splitlines()

    return f'<h3>Requirements:</h3> {requirements}'


@app.route('/generate-users/')
def generate_users():
    fake = Faker()
    users = []
    for i in range(100):
        name = fake.name()
        email = fake.email()
        users.append(f'{name} - {email}')
    return f'<h3>Users:</h3> {users}'


@app.route('/generate-users/<int:count>/')
def generate_users_count(count):
    fake = Faker()
    users = []
    for i in range(count):
        name = fake.name()
        email = fake.email()
        users.append(f'{name} - {email}')
    return f'<h3>Users:</h3> {users}'


@app.route('/mean/')
def get_mean():
    data = pd.read_csv('hw.csv')
    df = pd.DataFrame(data)
    df['Height (centimeters)'] = df[' "Height(Inches)"'] * 2.54
    df['Weight (kilograms)'] = df[' "Weight(Pounds)"'] * 0.45359237
    mean_height = df['Height (centimeters)'].mean()
    mean_weight = df['Weight (kilograms)'].mean()
    return f'<h3>Средний рост:</h3> {mean_height} \n <h3>Средний вес:</h3> {mean_weight}'


@app.route('/space/')
def get_count_spaceman():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()

    number_of_astronauts = data["number"]
    return f'<h3>Количество космонавтов в настоящий момент: </h3> {number_of_astronauts}'
