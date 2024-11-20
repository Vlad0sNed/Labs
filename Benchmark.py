import numpy as np
import time
import math
import matplotlib.pyplot as plt
import pandas as pd

pi = 3.14159265358979323846

def generate_cartesian_points(n):
    x = np.random.randint(0, 1000, n)
    y = np.random.randint(0, 1000, n)
    z = np.random.randint(0, 1000, n)
    return x, y, z

def generate_polar_points(n):
    r = np.random.randint(0, 1000, n)
    theta = np.random.randint(0, 360, n) * pi / 180.0
    return r, theta

def generate_spherical_points(n):
    r = np.random.randint(0, 1000, n)
    theta = np.random.randint(0, 180, n) * pi / 180.0
    phi = np.random.randint(0, 360, n) * pi / 180.0
    return r, theta, phi

def cartesian_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def cartesian_distance_3d(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def polar_distance(r1, theta1, r2, theta2):
    return math.sqrt(r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * math.cos(theta2 - theta1))

def spherical_distance(r1, theta1, phi1, r2, theta2, phi2):
    return math.sqrt(r1 ** 2 + r2 ** 2 - 2 * r1 * r2 * (math.sin(theta1) * math.sin(theta2) * math.cos(phi1 - phi2) + math.cos(theta1) * math.cos(theta2)))

def spherical_surface_distance(r, theta1, phi1, theta2, phi2):
    arg = math.sin(phi1) * math.sin(phi2) + math.cos(phi1) * math.cos(phi2) * math.cos(theta1 - theta2)
    if arg < -1:
        arg = -1
    elif arg > 1:
        arg = 1
    return r * math.acos(arg)

def main():
    n = 100000
    x, y, z = generate_cartesian_points(n)
    r, theta, phi = generate_spherical_points(n)

    times = []
    labels = ["Cartesian (2D)", "Cartesian (3D)", "Polar", "Spherical (Volume)", "Spherical (Surface)"]

    start = time.time()
    for i in range(n - 1):
        cartesian_distance(x[i], y[i], x[i + 1], y[i + 1])
    end = time.time()
    times.append(end - start)

    start = time.time()
    for i in range(n - 1):
        cartesian_distance_3d(x[i], y[i], z[i], x[i + 1], y[i + 1], z[i + 1])
    end = time.time()
    times.append(end - start)

    r, theta = generate_polar_points(n)

    start = time.time()
    for i in range(n - 1):
        polar_distance(r[i], theta[i], r[i + 1], theta[i + 1])
    end = time.time()
    times.append(end - start)

    r, theta, phi = generate_spherical_points(n)

    start = time.time()
    for i in range(n - 1):
        spherical_distance(r[i], theta[i], phi[i], r[i + 1], theta[i + 1], phi[i + 1])
    end = time.time()
    times.append(end - start)

    start = time.time()
    for i in range(n - 1):
        spherical_surface_distance(r[i], theta[i], phi[i], theta[i + 1], phi[i + 1])
    end = time.time()
    times.append(end - start)

    # Creating a DataFrame for the results
    df = pd.DataFrame({'Coordinate System': labels, 'Time (seconds)': times})
    print(df)

    # Plotting the results
    plt.bar(labels, times)
    plt.xlabel('Coordinate System')
    plt.ylabel('Time (seconds)')
    plt.title('Calculation Time for Different Coordinate Systems')
    plt.show()

if __name__ == "__main__":
    main()
