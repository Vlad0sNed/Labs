import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:
    def __init__(self, F, H, Q, R, P, x):
        self.F = F  # State transition matrix
        self.H = H  # Measurement matrix
        self.Q = Q  # Process noise covariance
        self.R = R  # Measurement noise covariance
        self.P = P  # Initial estimation error covariance
        self.x = x  # Initial state

    def predict(self):
        # Predict the state and error covariance
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(self.F, np.dot(self.P, self.F.T)) + self.Q
        return self.x

    def update(self, z):
        # Calculate Kalman Gain
        K = np.dot(self.P, self.H.T) / (np.dot(self.H, np.dot(self.P, self.H.T)) + self.R)

        # Update the estimate via measurement z
        self.x = self.x + K * (z - np.dot(self.H, self.x))

        # Update the error covariance
        self.P = (np.eye(len(self.P)) - K * self.H) @ self.P

        return self.x

# === Signal Parameters ===
frequency = 1  # Frequency of the sine wave in Hz
amplitude = 10  # Amplitude of the sine wave
offset = 10  # Offset of the sine wave
sampling_interval = 0.001  # Sampling interval in seconds (1 ms)
total_time = 4  # Total duration in seconds (1 second)

# === Noise Parameters ===
noise_variance = 16  # Variance of the Gaussian noise
noise_std_dev = np.sqrt(noise_variance)  # Calculate the standard deviation from the variance

# === Filter Parameters ===
F = np.array([[1]])  # State transition matrix
H = np.array([[1]])  # Measurement matrix

Q = np.array([[20]])  # Process noise covariance
R = np.array([[10000]])  # Measurement noise covariance

P = np.array([[1]])  # Initial estimation error covariance
x = np.array([[10]])  # Initial state estimate

# Create Kalman filter instance
kf = KalmanFilter(F, H, Q, R, P, x)

# === Signal Generation ===
time_steps = np.arange(0, total_time, sampling_interval)  # Generate time steps from 0 to total_time with step size of sampling_interval
true_signal = offset + amplitude * np.sin(2 * np.pi * frequency * time_steps)  # Generate sine wave based on parameters
noisy_signal = [val + np.random.normal(0, noise_std_dev) for val in true_signal]  # Add Gaussian noise with calculated standard deviation

# === Apply Kalman Filter ===
kalman_estimates = []

for measurement in noisy_signal:
    kf.predict()  # Predict next state
    estimate = kf.update(measurement)  # Update with noisy measurement
    kalman_estimates.append(estimate[0][0])  # Store the filtered result

# === Calculate Variance Before and After Filtering ===
noise_variance_before = np.var(noisy_signal - true_signal)  # Variance of noise in the original signal
noise_variance_after = np.var(kalman_estimates - true_signal)  # Variance of noise after Kalman filtering

# Display variances
print(f"Noise Variance Before Filtering: {noise_variance_before:.2f}")
print(f"Noise Variance After Filtering: {noise_variance_after:.2f}")

# === Plot the Results ===
plt.figure(figsize=(12, 6))
plt.plot(time_steps, noisy_signal, label='Noisy Signal', color='orange', linestyle='-', alpha=0.6)
plt.plot(time_steps, true_signal, label='True Signal (Sine Wave)', linestyle='--', color='blue')
plt.plot(time_steps, kalman_estimates, label='Kalman Filter Estimate', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Kalman Filter Applied to a Noisy Sinusoidal Wave')
plt.legend()
plt.grid()
plt.show()
