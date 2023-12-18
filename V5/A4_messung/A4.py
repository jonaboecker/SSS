import time
import math
import redlab as rl


# Funktion zur Generierung der Sinusspannung
def generate_sine_wave():
    # Samplingrate des DA-Wandlers
    sampling_rate = 100  # Maximal 100 Samples pro Sekunde
    num_amplitudes = 50  # Anzahl der Amplitudenstufen pro Sinusschwingung

    # Berechnung der Schrittgröße für die Sinusspannung
    step = 2 * math.pi / num_amplitudes

    while True:
        for i in range(num_amplitudes):
            # Berechnung des Sinuswerts für jede Amplitude
            voltage = math.sin(i * step) + 2

            # Ausgabe der Spannungswerte auf den DA-Wandler
            print("Voltage Value: " + str(voltage))
            rl.cbVOut(0, 0, 101, voltage)

            # Pausenzeit zur Einhaltung der Samplingrate
            time.sleep(1 / sampling_rate)


# Aufruf der Funktion zur Generierung der Sinusspannung
generate_sine_wave()
