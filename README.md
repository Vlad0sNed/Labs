Створено новий графік – візуалізація для відстеження змін у моделі стану. https://github.com/Vlad0sNed/Labs/blob/Lab_7_Дослідження-фільтра-Калмана/lab7/1.png

Матриця переходу стану – використана одинична матриця, оскільки модель реалізує лише збереження поточного значення без додаткових змін.

Матриця спостереження (H) – також одинична, адже спостереження повністю відображає стан, не потребуючи додаткових перетворень.

Задано ковариацію шуму вимірювань: встановлено значення 1000 для врахування рівня невизначеності в вимірюваних даних. https://github.com/Vlad0sNed/Labs/blob/Lab_7_Дослідження-фільтра-Калмана/lab7/2.png

Початкове значення оцінки стану встановлено на рівні 10, що дозволяє моделі починати з певного базового значення. https://github.com/Vlad0sNed/Labs/blob/Lab_7_Дослідження-фільтра-Калмана/lab7/3.png

Час дослідження встановлено на 4 секунди – оптимальний інтервал для збору даних та аналізу динаміки моделі. https://github.com/Vlad0sNed/Labs/blob/Lab_7_Дослідження-фільтра-Калмана/lab7/4.png

Нове значення ковариації шуму вимірювань – виставлено на рівні 10000, підвищуючи рівень шуму для тестування стабільності моделі. https://github.com/Vlad0sNed/Labs/blob/Lab_7_Дослідження-фільтра-Калмана/lab7/5.png

Ковариація шуму процесу – встановлено на рівні 20, що дозволяє моделі обробляти процеси з певним рівнем випадкових збурень. https://github.com/Vlad0sNed/Labs/blob/Lab_7_Дослідження-фільтра-Калмана/lab7/6.png

Амплітуда сигналу – встановлено на рівні 10 для забезпечення належного рівня коливань у моделі. https://github.com/Vlad0sNed/Labs/blob/Lab_7_Дослідження-фільтра-Калмана/lab7/7.png
