from flask import Flask, render_template
from flask_socketio import SocketIO
import websocket
import threading
import json
import numpy as np

app = Flask(__name__)
socketio = SocketIO(app)

received_at_dict = {}  # Словарь для хранения временных меток по источникам

def on_message(ws, message):
    global received_at_dict
    message_data = json.loads(message)
    source_id = message_data.get("sourceId")
    received_at = message_data.get("receivedAt")

    received_at_dict[source_id] = received_at

    if len(received_at_dict) == 3:
        if all(source in received_at_dict for source in ["source1", "source2", "source3"]):
            x1, y1 = 0, 0
            x2, y2 = 100000, 0
            x3, y3 = 0, 100000

            delta_t12 = (received_at_dict['source1'] - received_at_dict['source2']) / 1000 * 10e8
            delta_t13 = (received_at_dict['source1'] - received_at_dict['source3']) / 1000 * 10e8
            c = 3e8 / 10e8

            initial_guess = [50000, 50000]
            x_opt, y_opt, iterations = custom_least_squares(
                tdoa_error, initial_guess,
                args=(x1, y1, x2, y2, x3, y3, delta_t12, delta_t13, c)
            )

            # Отправка данных на клиентскую сторону
            socketio.emit('new_data', {'x': x_opt, 'y': y_opt})

        received_at_dict.clear()


def tdoa_error(params, x1, y1, x2, y2, x3, y3, delta_t12, delta_t13, c):
    x, y = params
    d1 = np.sqrt((x - x1) ** 2 + (y - y1) ** 2)
    d2 = np.sqrt((x - x2) ** 2 + (y - y2) ** 2)
    d3 = np.sqrt((x - x3) ** 2 + (y - y3) ** 2)

    delta_t12_calc = (d1 - d2) / c
    delta_t13_calc = (d1 - d3) / c

    error1 = delta_t12_calc - delta_t12
    error2 = delta_t13_calc - delta_t13

    return [error1, error2]


def loss_function(params, tdoa_error_func, args):
    errors = tdoa_error_func(params, *args)
    loss = sum(e ** 2 for e in errors)
    return loss


def custom_least_squares(tdoa_error_func, initial_guess, args, learning_rate=0.01, max_iterations=10000,
                         tolerance=1e-12):
    x, y = initial_guess
    iteration = 0
    prev_loss = float('inf')

    while iteration < max_iterations:
        loss = loss_function([x, y], tdoa_error_func, args)

        if abs(prev_loss - loss) < tolerance:
            break

        prev_loss = loss

        delta = 1e-6
        loss_x = loss_function([x + delta, y], tdoa_error_func, args)
        grad_x = (loss_x - loss) / delta

        loss_y = loss_function([x, y + delta], tdoa_error_func, args)
        grad_y = (loss_y - loss) / delta

        x -= learning_rate * grad_x
        y -= learning_rate * grad_y

        iteration += 1

    return x, y, iteration


def run_websocket():
    ws = websocket.WebSocketApp("ws://localhost:4002",
                                on_message=on_message)
    ws.run_forever()


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    threading.Thread(target=run_websocket).start()
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)