import numpy as np
import config

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

note_to_freq = config.NOTE_TO_FREQ

def hz_to_note_name(freq):
    """Convierte Hz → nombre de nota usando tabla de frecuencias exacta."""
    closest_note = min(note_to_freq.keys(), key=lambda n: abs(note_to_freq[n]-freq))
    return closest_note

def f0_to_notes(f0):
    notes = []

    for freq in f0:
        if np.isnan(freq) or freq <= 0:
            notes.append(None)
        else:
            note = hz_to_note_name(freq)
            notes.append(note)

    return notes

def notes_to_wave(note, duration=config.FRAME_LENGTH, sr=48000):
    freq = note_to_freq[note]
    t = np.linspace(0, duration, int(sr*duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    return wave