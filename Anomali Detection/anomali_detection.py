import pandas as pd
import pickle

print("Aplikasi Deteksi Anomali Log Jaringan Komputer\n")
length = int(input("Masukan panjang packet (length) : "))
protocol = int(input("Masukan index protocol (ProtocolIndex) : "))

new_log = pd.DataFrame({
    'Length': [length],  # Contoh panjang paket
    'ProtocolIndex': [protocol],  # Contoh indeks protokol (misalnya, 2 bisa mewakili TCP)
    # Tambahkan fitur lainnya sesuai dengan data asli Anda
})

print(new_log)

#Membuat kembali model untuk digunakan
with open('/Volumes/Data/MyJobs/Perangkat Ajar/20231/Big Data/Code/Anomali Detection/anomali_detection_model.pkl', 'rb') as file:
    anomalidetection = pickle.load(file)

# Memprediksi dengan model isolation forest dari model yang telah disimpan
prediction = anomalidetection.predict(new_log)

# Interpretasi hasil
if prediction == -1:
    print("Log ini adalah anomali.")
else:
    print("Log ini adalah normal.")
