import customtkinter as ctk

FRAME_LENGTH = 0.1
NOTE_TO_FREQ = note_to_freq = {
    # --- OCTAVA 3 ---
    "C3": 130.81,
    "D3": 146.83,
    "E3": 164.81,
    "F3": 174.61,
    "G3": 196.00,
    "A3": 220.00,
    "B3": 246.94,

    # --- OCTAVA 4 ---
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,

    # --- OCTAVA 5 ---
    "C5": 523.25,
    "D5": 587.33,
    "E5": 659.25,
    "F5": 698.46,
    "G5": 783.99,
    "A5": 880.00,
    "B5": 987.77,

    # --- OCTAVA 6 ---
    "C6": 1046.50,
    "D6": 1174.66,
    "E6": 1318.51,
    "F6": 1396.91,
    "G6": 1567.98,
    "A6": 1760.00,
    "B6": 1975.53,

    # --- OCTAVA 7 ---
    "C7": 2093.00,
    "D7": 2349.32,
    "E7": 2637.02,
    "F7": 2793.83,
    "G7": 3135.96,
    "A7": 3520.00,
    "B7": 3951.07,

    # --- OCTAVA 8 ---
    "C8": 4186.01,
    "D8": 4698.63,
    "E8": 5274.04,
    "F8": 5587.65,
    "G8": 6271.93,
    "A8": 7040.00,
    "B8": 7902.13,

    # --- OCTAVA 9 ---
    "C9": 8372.02,
    "D9": 9397.27,
    "E9": 10548.08,
    "F9": 11175.30,
    "G9": 12543.85,
    "A9": 14080.00,
    "B9": 15804.27,
}

BG_COLOR = "#21653D"
BG2_COLOR = "#B7FBD1"
BG_MSG = "#07AD7E"
BUTTON_BG_COLOR = "#0CF2B0"
BUTTON_HOVER_COLOR = "#078F68"
BUTTON_FG_COLOR = "#000000"
TITLE_COLOR = "#FFFFFF"
FONT_COLOR = "#FFFFFF"
VERIFY_CORR_COLOR = "#2CD22C"
VERIFY_INCORR_COLOR = "#EC0011"

BUTTON_RADIUS = 15

TITLE_FONT_PARAMS = dict(family="Aptos", size=60, weight="bold", slant="italic", underline=True)
FONT_PARAMS = dict(family="Aptos", size=20)
BUTTON_FONT_PARAMS = dict(family="Aptos", size=20, weight="bold")
INFO_FONT_PARAMS = dict(family="Aptos", size=12, weight="bold")
