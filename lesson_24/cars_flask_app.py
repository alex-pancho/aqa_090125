from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import logging

# Налаштування логування
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("cars_flask_app.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = Flask(__name__)

# Конфігурація JWT
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

# Проста БД
cars_db = {
    1: {"brand": "BMW", "year": 2018, "engine_volume": 2.0, "price": 50000},
    2: {"brand": "Audi", "year": 2020, "engine_volume": 1.8, "price": 45000},
    3: {"brand": "Mercedes", "year": 2019, "engine_volume": 2.5, "price": 55000},
    4: {"brand": "Toyota", "year": 2017, "engine_volume": 2.4, "price": 35000},
    5: {"brand": "Honda", "year": 2016, "engine_volume": 1.6, "price": 30000},
}

users = {
    "test_user": "test_pass"
}

def authenticate(username, password):
    return username if users.get(username) == password else None

@app.route('/auth', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return jsonify({"message": "Аутентифікація не пройшла!"}), 401

    username = authenticate(auth.username, auth.password)
    if not username:
        return jsonify({"message": "Неправильне ім'я користувача або пароль!"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200

@app.route('/cars', methods=['GET'])
@jwt_required()
def get_cars():
    sort_by = request.args.get('sort_by')
    limit = request.args.get('limit')

    logger.info(f"Отримано запит: sort_by={sort_by}, limit={limit}")

    try:
        sorted_cars = sorted(cars_db.values(), key=lambda x: x.get(sort_by, 0)) if sort_by else list(cars_db.values())
    except Exception as e:
        logger.warning(f"Некоректне поле для сортування: {sort_by}. Помилка: {e}")
        return jsonify({"error": f"Invalid sort_by field: {sort_by}"}), 400

    try:
        limited_cars = sorted_cars[:int(limit)] if limit else sorted_cars
    except ValueError:
        logger.warning(f"Некоректне значення limit: {limit}")
        return jsonify({"error": "Limit must be an integer"}), 400

    return jsonify(limited_cars), 200

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port, debug=True)
