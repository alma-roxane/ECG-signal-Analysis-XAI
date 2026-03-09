# import wfdb
# import matplotlib.pyplot as plt

# # Path to record
# record_path = "data/mitdb/100"

# # Load ECG record
# record = wfdb.rdrecord(record_path)

# # Load annotations
# annotation = wfdb.rdann(record_path, 'atr')

# # Extract ECG signal (Lead 1)
# ecg_signal = record.p_signal[:,0]

# # Sampling frequency
# fs = record.fs

# print("Sampling Frequency:", fs)
# print("Signal Length:", len(ecg_signal))
# print("Number of annotations:", len(annotation.sample))

# # Plot first 2000 samples
# plt.figure(figsize=(12,4))
# plt.plot(ecg_signal[:2000])
# plt.title("Raw ECG Signal (Record 100)")
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")
# plt.show()

import wfdb
import matplotlib.pyplot as plt

record_path = "data/mitdb/102"

record = wfdb.rdrecord(record_path)
annotation = wfdb.rdann(record_path, 'atr')

ecg_signal = record.p_signal[:,0]

r_peaks = annotation.sample
labels = annotation.symbol
fs = record.fs
time = np.arange(len(ecg_signal)) / fs

print("Sampling Frequency:", fs)
print("Signal Length:", len(ecg_signal))
print("Number of annotations:", len(annotation.sample))

print("First 10 beat labels:")
print(labels[:10])

# Plot ECG with beat markers
plt.figure(figsize=(12,4))
plt.plot(ecg_signal[:2000])

for peak in r_peaks:
    if peak < 2000:
        plt.axvline(x=peak, color='red', alpha=0.4)

plt.title("ECG Signal with Beat Annotations")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.show()