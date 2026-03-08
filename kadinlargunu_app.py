import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import streamlit as st

# Gül parametreleri
theta = np.linspace(0, 2*np.pi, 1000)
k = 5          # yaprak sayısı
a = 0
b_max = 1.5    # maksimum yaprak boyutu

fig, ax = plt.subplots(figsize=(6,6), subplot_kw={'polar': True})
ax.set_facecolor('black')
ax.axis('off')
line, = ax.plot([], [], color='red', lw=2)

# Başlangıç
def init():
    line.set_data([], [])
    return line,

# Frame güncelleme
def update(frame):
    b = b_max * (frame / 100)  # yaprak boyutu yavaşça artıyor
    r = a + b * np.sin(k * theta)
    line.set_data(theta, r)
    return line,

# Animasyonu oluştur
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

# GIF olarak kaydet
ani.save('gul_aciliyor.gif', writer=PillowWriter(fps=20))

plt.close(fig)

# Streamlit gösterim
st.title("Anneme Özel🌹")
st.image("gul_aciliyor.gif")
st.write("Oğlun Emre'den Hediyen 💖")
