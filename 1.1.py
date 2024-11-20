import math

# Перевод из полярной в декартову
def polar_to_cartesian(r, theta):
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

# Перевод из декартовой в полярную
def cartesian_to_polar(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    theta = math.atan2(y, x)
    return r, theta

def main():
    print("Введите значения полярных координат:")

    # Ввод радиуса r
    r = float(input("Введите радиус (r): "))

    # Ввод угла theta
    theta = float(input("Введите угол (θ в радианах): "))

    # Перевод в декартову систему координат
    cartesian = polar_to_cartesian(r, theta)
    print(f"Декартовы координаты: x = {cartesian[0]}, y = {cartesian[1]}")

    # Перевод обратно в полярную систему координат
    polar = cartesian_to_polar(cartesian[0], cartesian[1])
    print(f"Проверка обратного преобразования: r = {polar[0]}, θ = {polar[1]}")

if __name__ == "__main__":
    main()