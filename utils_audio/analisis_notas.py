import numpy as np
import config

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

note_to_freq = {"C3": 130.81, "E3": 164.81, "G3": 196.00,
    "B3": 246.94, "D4": 293.66, "F4": 349.23, "A4": 440.00,
    "C5": 523.25, "E5": 659.25, "G5": 783.99, "B5": 987.77,
    "D6": 1174.66, "F6": 1396.91, "A6": 1760.00, "C7": 2093.00,
    "E7": 2637.02, "G7": 3135.96, "B7": 3951.07, "D8": 4698.63,
    "F8": 5587.65, "A8": 7040.00, "C9": 8372.02, "E9": 10548.08,
    "G9": 12543.85, "B9": 15803.87, "D10": 18743.70, "F10": 22375.30,
    "A10": 28160.00, "C11": 33488.04, "E11": 42196.16
}


def hz_to_midi(freq):
    """Convert frequency to MIDI note number."""
    return 69 + 12 * np.log2(freq / 440.0)

def midi_to_name(midi_number: int):
    """Convert MIDI number to musical note name."""
    midi_number = int(round(midi_number))
    name = NOTE_NAMES[midi_number % 12]
    octave = midi_number // 12 - 1
    return f"{name}{octave}"

def hz_to_note_name(freq):
    """Convert Hz → Note name. freq must be > 0."""
    midi = hz_to_midi(freq)
    return midi_to_name(midi)

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