import numpy as np

NOTE_NAMES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

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

def f0_to_notes(f0, times):
    notes = []

    for freq, t in zip(f0, times):
        if np.isnan(freq) or freq <= 0:
            notes.append((t, None))
        else:
            note = hz_to_note_name(freq)
            notes.append((t, note))

    return notes

def group_notes(notes):
    segments = []
    current_note = None
    start_time = None

    for i, (t, note) in enumerate(notes):
        if note != current_note:
            # close previous note
            if current_note is not None:
                segments.append((start_time, notes[i-1][0], current_note))

            # start new note
            current_note = note
            start_time = t

    # close last note
    if current_note is not None:
        segments.append((start_time, notes[-1][0], current_note))

    return segments