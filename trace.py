import numpy as np
import matplotlib.pyplot as plt

# Parameters
n_traces = 5          # Number of seismic traces (channels)
n_samples = 100       # Number of time samples per trace
trace_spacing = 2.0   # Horizontal spacing between traces

# Generate synthetic data (Ricker wavelet + random noise)
def ricker_wavelet(points, a):
    t = np.linspace(-1, 1, points)
    return (1 - 2 * (np.pi**2) * (a**2) * (t**2)) * np.exp(-(np.pi**2) * (a**2) * (t**2))

data = np.zeros((n_samples, n_traces))
for i in range(n_traces):
    amp = np.random.uniform(0.8, 1.2)
    shift = np.random.randint(10, 30)
    data[:, i] = amp * np.roll(ricker_wavelet(n_samples, a=4), shift) + np.random.normal(0, 0.05, n_samples)

# Plot
plt.figure(figsize=(10, 6))
time = np.arange(n_samples)

for i in range(n_traces):
    # Offset each trace horizontally for wiggle plot
    offset = i * trace_spacing
    trace = data[:, i] + offset
    plt.plot(trace, time, color='black')
    plt.fill_betweenx(time, offset, trace, where=(trace > offset), color='blue', alpha=0.5)

plt.gca().invert_yaxis()
plt.xlabel('Trace (offset)')
plt.ylabel('Time sample')
plt.title('Multi-Trace Seismic Wiggle Plot')
plt.grid(True)
plt.tight_layout()
plt.show()
