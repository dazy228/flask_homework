from flask import Flask, request
from faker import Faker
import csv
import requests

app = Flask(__name__)
fake = Faker('ru_RU')


@app.route("/")
def welcome():
    return "<h1>Welcome to my site!</h1>"


@app.route("/requirements/")
def read_requirements():
    # Открываем requirements.txt в режиме чтения
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        requirements = f.read()

    # Возвращаем в формате, удобном для чтения (используем <pre> для сохранения форматирования)
    return f"<pre>{requirements}</pre>"


@app.route('/generate-users/')
def generate_users():
    # Получаем параметр 'count' из запроса, по умолчанию 100
    count = request.args.get('count', default=100, type=int)

    # Генерируем нужное количество фейковых пользователей
    users = []
    for _ in range(count):
        name = fake.name()
        email = fake.email()
        users.append(f"{name} - {email}")

    # Возвращаем список (например, через <br> для переноса строк)
    return "<br>".join(users)


@app.route('/mean/')
def mean_height_weight():

    total_height_in = 0.0  # Сумма роста в дюймах
    total_weight_lb = 0.0  # Сумма веса в фунтах
    count = 0  # Число записей

    # Читаем CSV с помощью встроенного модуля csv
    with open('hw.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f,
                                delimiter=',',
                                skipinitialspace=True,
                                quotechar='"')
        for row in reader:
            # Считываем значения из колонок "Height(Inches)" и "Weight(Pounds)"
            height_in = float(row["Height(Inches)"])
            weight_lb = float(row["Weight(Pounds)"])

            total_height_in += height_in
            total_weight_lb += weight_lb
            count += 1

    if count == 0:
        return "Нет данных для вычисления среднего"

    # Считаем средние значения
    mean_height_in = total_height_in / count  # средний рост в дюймах
    mean_weight_lb = total_weight_lb / count  # средний вес в фунтах

    # Переводим:
    #  1 дюйм ≈ 2.54 см
    #  1 фунт ≈ 0.45359237 кг
    mean_height_cm = mean_height_in * 2.54
    mean_weight_kg = mean_weight_lb * 0.45359237

    # Формируем ответ
    # Округлим результаты до 2 знаков после запятой
    return f"<h2>Средний рост: {mean_height_cm:.2f} см<br>Cредний вес: {mean_weight_kg:.2f} кг</h2>"


@app.route('/space/')
def people_in_space():
    response = requests.get('http://api.open-notify.org/astros.json')
    people = response.json()['number']

    return f'<h2>{people} people in space NOW!</h2>'


if __name__ == '__main__':
    app.run(debug=True)
