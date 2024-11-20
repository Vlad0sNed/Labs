import math

# Перевод из сферической в декартову систему координат
def spherical_to_cartesian(r, theta, phi):
    x = r * math.sin(phi) * math.cos(theta)
    y = r * math.sin(phi) * math.sin(theta)
    z = r * math.cos(phi)
    return x, y, z

# Перевод из декартовой в сферическую систему координат
def cartesian_to_spherical(x, y, z):
    r = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    theta = math.atan2(y, x)   # Азимут в радианах
    phi = math.acos(z / r)     # Угол возвышения в радианах
    return round(r, 2), theta, phi  # Округляем r до 2 знаков

def main():
    print("Введите значения сферических координат (углы в радианах):")

    # Ввод радиуса r
    r = float(input("Введите радиус (r): "))

    # Ввод азимута theta в радианах
    theta = float(input("Введите угол азимута (θ в радианах): "))

    # Ввод угла возвышения phi в радианах
    phi = float(input("Введите угол возвышения (φ в радианах): "))

    # Перевод в декартову систему координат
    cartesian = spherical_to_cartesian(r, theta, phi)
    print(f"Декартовы координаты: x = {cartesian[0]}, y = {cartesian[1]}, z = {cartesian[2]}")

    # Перевод обратно в сферическую систему координат
    spherical = cartesian_to_spherical(cartesian[0], cartesian[1], cartesian[2])
    print(f"Проверка обратного преобразования: r = {spherical[0]}, θ = {spherical[1]} радиан, φ = {spherical[2]} радиан")

if __name__ == "__main__":
    main()