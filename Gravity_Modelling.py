import numpy as np
import matplotlib.pyplot as plt

# Modelling Gravity
G = 6.673 * 10e-11


def fungsi_model_sphere():
    p = float(input("Masukkan Kerapatan Jenis Benda Pada Model Tersebut( kg/m^3 ): "))
    r = float(input("Masukkan jari-jari Pada Model Tersebut( m ): "))
    z = float(input("Masukkan Kedalaman Titik Pusat Massa Pada Model Tersebut( m ): "))
    i = int(input("Masukkan Nilai Batas Minimum dan Maksimum: "))
    v = 4 / 3 * np.pi * r ** 3
    a = np.arange(0, 360, 1)
    b = np.array(a * np.pi / 180)
    x = np.arange(-i, i, 10)
    m = x ** 2 + z ** 2
    n = np.array(m) ** 1.5
    g = np.array(10e3 * G * p * v * z / n)

    plt.subplot(311)
    plt.xlim(-i, i, 0.01)
    plt.plot(x, g, "*")
    plt.grid()
    plt.xlabel("Jarak Titik Lokasi( m )")
    plt.ylabel("Nilai Percerpatan Gravitasi ( mGal )")
    plt.title("Modelling Gravitasi-Model Sphere")

    plt.subplot(313)
    plt.fill(r * np.cos(b), r * np.sin(b) + z, "-")
    plt.axis("equal")
    plt.xlim(-i, i, 0.01)
    plt.ylim(0, 2 * z, 0.01)
    plt.gca().invert_yaxis()
    plt.grid()
    plt.xlabel("Jarak Titik Lokasi( m )")
    plt.ylabel("Kedalaman( m )")
    plt.show()

    return ()


def fungsi_model_horizontal_cylinder():
    p = float(input("Masukkan Kerapatan Jenis Benda Pada Model Tersebut( kg/m^3 ): "))
    r = float(input("Masukkan Jari-Jari Pada Model Tersebut( m ): "))
    z = float(input("Masukkan Kedalaman Titik Pusat Massa Pada Model Tersebut( m ): "))
    i = int(input("Masukkan Nilai Batas Minimum dan Maksimal: "))
    a = np.arange(0, 360, 1)
    b = np.array(a * np.pi / 180)
    x = np.arange(-i, i, 10)
    m = x ** 2 + z ** 2
    n = np.array(m)
    g = np.array(10e3 * 2 * G * np.pi * p * (r ** 2) * z / n)

    plt.subplot(311)
    plt.xlim(-i, i, 0.01)
    plt.plot(x, g, "*")
    plt.grid()
    plt.xlabel("Jarak Titik Lokasi( m )")
    plt.ylabel("Nilai Percerpatan Gravitasi ( mGal )")
    plt.title("Modelling Gravitasi-Model Horizontal Cylinder")

    plt.subplot(313)
    plt.fill(r * np.cos(b), r * np.sin(b) + z, "-")
    plt.axis("equal")
    plt.xlim(-i, i, 0.01)
    plt.ylim(0, 2 * z, 0.01)
    plt.gca().invert_yaxis()
    plt.grid()
    plt.xlabel("Jarak Titik Lokasi( m )")
    plt.ylabel("Kedalaman( m )")
    plt.show()

    return ()


def fungsi_model_horizontal_sheets():
    p = float(input("Masukkan Kerapatan Jenis Benda Pada Model Tersebut( kg/m^3 ): "))
    t = float(input("Ketebalan Benda Pada Model Tersebut( m ): "))
    z = float(input("Masukkan Kedalaman Titik Pusat Massa Pada Model Tersebut( m ): "))
    i = int(input("Masukkan Nilai Batas Minimum dan Maksimal: "))
    x = np.arange(-i, i, 10)
    m = np.arctan(-x / z) * np.pi / 180
    n = np.array(m)
    g = np.array(10e3 * 2 * G * p * t / (np.pi * 0.5 - n))

    plt.subplot(311)
    plt.xlim(-i, i, 0.01)
    plt.plot(x, g, "*")
    plt.grid()
    plt.xlabel("Jarak Titik Lokasi(m)")
    plt.ylabel("Nilai Percerpatan Gravitasi (mGal)")
    plt.title("Modelling Gravitasi-Model Horizontal Sheets")

    plt.subplot(313)
    k1 = [-i, -i, 0, 0]
    l1 = [z-z*(1/5), z-z*(2/5), z-z*(2/5), z-z*(1/5)]
    plt.fill(k1, l1, "-")
    k2 = [0, 0, i, i]
    l2 = [z, z-z*(1/5), z-z*(1/5), z]
    plt.fill(k2, l2, "-")
    plt.xlim(-i, i, 0.01)
    plt.ylim(0, 2 * z, 0.01)
    plt.grid()
    plt.gca().invert_yaxis()
    plt.xlabel("Jarak Titik Lokasi( m )")
    plt.ylabel("Kedalaman( m )")
    plt.show()

    return ()


l = 0
while l <= 1000000:

    print("1. Fungsi Model Sphere")
    print("2. Fungsi Model Horizontal Cylinder")
    print("3. Fungsi Model Horizontal Sheets")

    Variabel = int(input("Masukkan Model Yang Ingin Dituju( 1/2/3 ): "))

    if Variabel == 1:
        print(fungsi_model_sphere())
    elif Variabel == 2:
        print(fungsi_model_horizontal_cylinder())
    elif Variabel == 3:
        print(fungsi_model_horizontal_sheets())
    else:
        print("Kode Yang Anda Inputkan Error")

    Lanjut = str(input("Mau Lanjut / Tidak ( ya/tidak ): "))

    if Lanjut == "ya":
        print(100*"==")
        l = l + 1
    else:
        print("Terima Kasih Telah Mengunjungi Software Kami")
        break
