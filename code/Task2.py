import math

class DistanceCalculator:
    @staticmethod
    def main():
        print("Виберіть систему координат:")
        print("1. Декартова (2D/3D)")
        print("2. Полярна (2D)")
        print("3. Сферична (3D)")
        choice = int(input("Ваш вибір: "))

        if choice == 1:
            DistanceCalculator.choose_cartesian()
        elif choice == 2:
            DistanceCalculator.calculate_distance_polar()
        elif choice == 3:
            DistanceCalculator.choose_spherical()
        else:
            print("Неправильний вибір.")

    @staticmethod
    def choose_cartesian():
        print("Виберіть вимірність простору:")
        print("1. Двовимірний (2D)")
        print("2. Тривимірний (3D)")
        dimension = int(input("Ваш вибір: "))

        if dimension == 1:
            DistanceCalculator.calculate_distance_cartesian_2d()
        elif dimension == 2:
            DistanceCalculator.calculate_distance_cartesian_3d()
        else:
            print("Неправильний вибір.")

    @staticmethod
    def calculate_distance_cartesian_2d():
        print("Введіть координати для 2D декартової системи:")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(f"Відстань у 2D декартовій системі: {distance}")

    @staticmethod
    def calculate_distance_cartesian_3d():
        print("Введіть координати для 3D декартової системи:")
        x1 = float(input("x1: "))
        y1 = float(input("y1: "))
        z1 = float(input("z1: "))
        x2 = float(input("x2: "))
        y2 = float(input("y2: "))
        z2 = float(input("z2: "))
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
        print(f"Відстань у 3D декартовій системі: {distance}")

    @staticmethod
    def calculate_distance_polar():
        print("Введіть полярні координати (радіус та кут у радіанах) для кожної точки:")
        r1 = float(input("r1: "))
        theta1 = float(input("θ1 (у радіанах): "))
        r2 = float(input("r2: "))
        theta2 = float(input("θ2 (у радіанах): "))
        distance = math.sqrt(r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * math.cos(theta2 - theta1))
        print(f"Відстань у полярній системі координат: {distance}")

    @staticmethod
    def choose_spherical():
        print("Виберіть метод обчислення відстані у сферичній системі:")
        print("1. Пряма лінія (у тривимірному просторі)")
        print("2. По поверхні сфери (велика колова відстань)")
        method = int(input("Ваш вибір: "))

        if method == 1:
            DistanceCalculator.calculate_distance_spherical_line()
        elif method == 2:
            DistanceCalculator.calculate_distance_spherical_surface()
        else:
            print("Неправильний вибір.")

    @staticmethod
    def calculate_distance_spherical_line():
        print("Введіть сферичні координати (радіус, кут азимуту θ, кут підйому φ) для кожної точки:")
        r1 = float(input("r1: "))
        theta1 = float(input("θ1 (у радіанах): "))
        phi1 = float(input("φ1 (у радіанах): "))
        r2 = float(input("r2: "))
        theta2 = float(input("θ2 (у радіанах): "))
        phi2 = float(input("φ2 (у радіанах): "))
        distance = math.sqrt(
            (r2 * math.sin(phi2) * math.cos(theta2) - r1 * math.sin(phi1) * math.cos(theta1)) ** 2 +
            (r2 * math.sin(phi2) * math.sin(theta2) - r1 * math.sin(phi1) * math.sin(theta1)) ** 2 +
            (r2 * math.cos(phi2) - r1 * math.cos(phi1)) ** 2
        )
        print(f"Пряма відстань у сферичній системі координат: {distance}")

    @staticmethod
    def calculate_distance_spherical_surface():
        print("Введіть радіус сфери та сферичні координати (азимут θ і підйом φ) для кожної точки:")
        R = float(input("Радіус сфери (R): "))
        theta1 = float(input("θ1 (у радіанах): "))
        phi1 = float(input("φ1 (у радіанах): "))
        theta2 = float(input("θ2 (у радіанах): "))
        phi2 = float(input("φ2 (у радіанах): "))
        distance = R * math.acos(
            math.sin(phi1) * math.sin(phi2) +
            math.cos(phi1) * math.cos(phi2) * math.cos(theta1 - theta2)
        )
        print(f"Велика колова відстань на поверхні сфери: {distance}")

if __name__ == "__main__":
    DistanceCalculator.main()
