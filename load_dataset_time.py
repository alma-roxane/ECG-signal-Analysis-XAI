import wfdb
import matplotlib.pyplot as plt
import numpy as np

record_path = "data/mitdb/102"

record = wfdb.rdrecord(record_path)
annotation = wfdb.rdann(record_path, 'atr')

ecg_signal = record.p_signal[:,0]

r_peaks = annotation.sample
labels = annotation.symbol
fs = record.fs
num_beats = len(r_peaks)

# -------- Convert Samples to Time --------
time = np.arange(len(ecg_signal)) / fs
# -----------------------------------------

sample_number = 1000
time_sample = sample_number / fs

print("Time of sample:", time_sample, "seconds")
print("Total number of beats:", num_beats)
print("Sampling Frequency:", fs)
print("Signal Length:", len(ecg_signal))
print("Number of annotations:", len(annotation.sample))

print("First 10 beat labels:")
print(labels[:10])

# Plot ECG with beat markers using TIME
plt.figure(figsize=(12,4))
plt.plot(time[:2000], ecg_signal[:2000])

for peak in r_peaks:
    if peak < 2000:
        plt.axvline(x=peak/fs, color='red', alpha=0.4)

plt.title("ECG Signal with Beat Annotations")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()