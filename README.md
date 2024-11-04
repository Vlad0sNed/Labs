Цей проект розроблений для визначення місцеположення об’єкта, використовуючи технологію LORAN (Long Range Navigation) і алгоритм TDOA (різниця часу прибуття сигналів). Дані з трьох базових станцій обробляються для обчислення координат приймача, які відображаються на веб-інтерфейсі в режимі реального часу за допомогою Flask і SocketIO.

Структура проекту
app.py: Основний серверний файл, що запускає Flask-сервер та обробляє вхідні повідомлення з WebSocket.

templates/index.html: HTML-шаблон для відображення графіка та оновлення даних в реальному часі.

Опис основних компонентів
WebSocket-з’єднання: Отримує дані про час прибуття сигналів від трьох джерел, що використовуються для визначення позиції об’єкта.

Алгоритм TDOA: Виконує обчислення координат об’єкта на основі різниці часу прибуття сигналів.

Функція custom_least_squares: Реалізує метод найменших квадратів для мінімізації помилок у визначенні координат.

SocketIO: Передає обчислені координати на клієнт для відображення на графіку.
