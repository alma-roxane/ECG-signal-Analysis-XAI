import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import butter, filtfilt

# Load ECG record
record_path = "data/mitdb/101"

record = wfdb.rdrecord(record_path)
ecg_signal = record.p_signal[:,0]
fs = record.fs

print("Sampling Frequency:", fs)


# -------------------------
# Bandpass Filter Function
# -------------------------
def bandpass_filter(signal, lowcut=0.5, highcut=45, fs=360, order=4):
    
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    
    b, a = butter(order, [low, high], btype='band')
    filtered_signal = filtfilt(b, a, signal)
    
    return filtered_signal


# Apply filter
filtered_ecg = bandpass_filter(ecg_signal)

# -------------------------
# Normalization
# -------------------------
normalized_ecg = (filtered_ecg - np.mean(filtered_ecg)) / np.std(filtered_ecg)


print("Mean after normalization:", np.mean(normalized_ecg))
print("Std after normalization:", np.std(normalized_ecg))


# Plot comparison
plt.figure(figsize=(12,6))

plt.subplot(3,1,1)
plt.plot(ecg_signal[:2000])
plt.title("Raw ECG Signal")

plt.subplot(3,1,2)
plt.plot(filtered_ecg[:2000])
plt.title("Filtered ECG Signal (0.5–45 Hz)")

plt.subplot(3,1,3)
plt.plot(normalized_ecg[:2000])
plt.title("Normalized ECG")

plt.tight_layout()
plt.show()