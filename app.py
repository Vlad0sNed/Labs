from flask import Flask, jsonify, render_template, request
from flask_cors import CORS  # Импортируем Flask-CORS
import json
import websocket
import threading
import time

app = Flask(__name__)
CORS(app)  # Включаем CORS для всего приложения

EXPIRATION_TIME = 4  # Время жизни данных, например, 5 секунд
data = []  # Массив для хранения данных

# Главная страница с графиком
@app.route('/')
def index():
    return render_template('index.html')  # HTML страница с графиком

# Маршрут для API обновления параметров
@app.route('/config', methods=['POST'])
def update_parameters():
    try:
        # Получаем данные из запроса
        params = request.json
        emulation_zone_size = params.get('emulationZoneSize')
        message_frequency = params.get('messageFrequency')
        satellite_speed = params.get('satelliteSpeed')
        object_speed = params.get('objectSpeed')

        # Здесь можно добавить логику обработки этих параметров
        return jsonify({"status": "success", "message": "Parameters updated successfully!"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Маршрут для получения данных графика
@app.route('/data')
def get_data():
    if len(data) < 3:
        return jsonify({"status": "error", "message": "Not enough data points"}), 400

    calculated_x, calculated_y = location(
        data[0]['x'], data[0]['y'], data[0]['radius'],
        data[1]['x'], data[1]['y'], data[1]['radius'],
        data[2]['x'], data[2]['y'], data[2]['radius']
    )

    # Возвращаем данные
    return jsonify({
        "data": data,
        "calculated": {"x": calculated_x, "y": calculated_y}
    })

# WebSocket логика
def on_message(ws, message):
    global data
    try:
        message_data = json.loads(message)
        id = message_data.get('id')
        x = message_data.get('x')
        y = message_data.get('y')
        sentAt = message_data.get('sentAt')
        receivedAt = message_data.get('receivedAt')

        # Вычисляем радиус
        radius = distance(sentAt, receivedAt)

        # Проверяем, существует ли уже элемент с таким id
        thePointExists = next((item for item in data if item['id'] == id), None)

        if thePointExists:
            # Обновляем существующую запись
            thePointExists.update({
                'x': x,
                'y': y,
                'sentAt': sentAt,
                'receivedAt': receivedAt,
                'radius': radius,
                'last_updated': time.time()  # Обновляем время последнего обновления
            })
        else:
            # Добавляем новую запись
            data.append({
                'id': id,
                'x': x,
                'y': y,
                'sentAt': sentAt,
                'receivedAt': receivedAt,
                'radius': radius,
                'last_updated': time.time()  # Устанавливаем время последнего обновления
            })

        # Удаляем устаревшие точки
        current_time = time.time()
        data = [point for point in data if current_time - point['last_updated'] < EXPIRATION_TIME]

    except json.JSONDecodeError:
        print("Ошибка разбора JSON:", message)

def on_open(ws):
    print("Подключено к WebSocket серверу")

def on_close(ws):
    print("Соединение закрыто")

def on_error(ws, error):
    print("Ошибка WebSocket:", error)

def distance(sentAt, receivedAt):
    return (((sentAt - receivedAt) / 1000) * 300000) / 1000

def location(x1, y1, r1, x2, y2, r2, x3, y3, r3):
    a = 2 * (x2 - x1)
    b = 2 * (y2 - y1)
    c = r1 ** 2 - r2 ** 2 - x1 ** 2 + x2 ** 2 - y1 ** 2 + y2 ** 2

    d = 2 * (x3 - x2)
    e = 2 * (y3 - y2)
    f = r2 ** 2 - r3 ** 2 - x2 ** 2 + x3 ** 2 - y2 ** 2 + y3 ** 2

    x = (c * e - f * b) / (e * a - b * d)
    y = (c * d - a * f) / (b * d - a * e)
    return x, y  # Возвращаем координаты

def run_websocket():
    ws = websocket.WebSocketApp("ws://localhost:4001",
                                on_open=on_open,
                                on_message=on_message,
                                on_close=on_close,
                                on_error=on_error)
    ws.run_forever()

if __name__ == "__main__":
    threading.Thread(target=run_websocket).start()  # Запускаем WebSocket в отдельном потоке
    app.run(debug=True, host='0.0.0.0')  # Запускаем Flask сервер
