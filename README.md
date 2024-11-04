В цьому репозиторії я показую як ознайомлювався з докером

Після того як ми встановили докер, нам потрібно переконатися що все встановилося корректно, можна це зробити за допомогою команди docker run -d -p 8080:80 docker/welcome-to-docker та перейдіть до сайту http://localhost:8080
https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/1.jpg
якщо ви все зробили вірно, то на сайті буде показана картинка

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/4.jpg

2.Тепер клонуємо або завантажуємо проєкт, та переходимо в каталог проєкту. Скопіювати проєкт можна за допомогою команди: git clone https://github.com/docker/getting-started-todo-app Перейти до каталогу проєкту: cd getting-started-todo-app Коли ми перейшли до каталогу, треба запустити докер за допомогою команди docker compose watch

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/10.jpg

якщо все зроблено вірно, то на сайті буде показуватися наступне

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/2.jpg

Тепер пропоную змінити деякі файли, та подивитися на результат,я змінив файли getGreeting.js, AddNewItemForm.jsx, index.scss А саме я змінив колір сторінки, зробив різні написи, та в полі для введеня тексту зробив заглушку у виді тексту

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/8.jpg

Ось що змінилося після зміни: https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/9.jpg

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/14.jpg

ось що змінилося після зміни:screenshots/photo_11_2024-09-09_21-49-46.jpg

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/7.jpg

Результат зміни усіх файлів:https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/1.jpg

Наступним кроком буде створення репозиторію для докера, для цього потрібно авторизуватися та створити докер на сайті Docker Hub Я вже авторизувався та створив репозиторій

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/3.jpg

Оскільки ви вже завантажили/скопіювали проєкт, та перейшли до каталогу проєкту, потрібно ввести наступну команду: docker build -t <DOCKER_USERNAME>/getting-started-todo-app . де замість DOCKER_USERNAME ви підставляете свій юзернейм

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/12.jpg

Щоб переконатися що зображення існують, використовуйте команду docker image ls

https://github.com/Vlad0sNed/Labs/blob/Lab_2_Docker/Screenshots/6.jpg

Для того щоб відправити зображення, використовуйте команду docker push <DOCKER_USERNAME>/getting-started-todo-app, де замість DOCKER_USERNAME ви підставляете свій юзернейм Але мені це не потрібно, оскільки під час виконання команди docker build -t <DOCKER_USERNAME>/getting-started-todo-app,він відправляв зображення

На цьому все, дякую за увагу!
