#!/usr/bin/env python3
import os
import subprocess

import mido
import click

from instruments import Instrument

temp_mid = './tmp/tmp.mid'

class Dur:
    quarter = 480
    eighth = int(quarter / 2)
    sixteenth = int(quarter / 4)
    thirtysecond = int(quarter / 8)
    half = quarter * 2
    whole = quarter * 4

def single_track_midi(program=None):
    """
    Create a MIDI file.
    Returns (midi_file, track)
    Can optionally add a program change at the beginning
    """
    midi = mido.MidiFile(type=0)
    track = mido.MidiTrack()
    midi.tracks.append(track)
    if program is not None:
        set_program(track, program)
    return midi, track

def set_program(track, program):
    """
    Add a program change at the beginning of a track.
    This sets the instrument. See instruments.py for complete list
    """
    track.insert(0, mido.Message('program_change', program=program, time=0))

def change_program(track, program):
    """
    Change the instrument of the track.
    Only use if the program was already set
    via the `program` flag of `single_track_midi` or the `set_program` function
    """
    old = track.pop(0)
    if old.dict()['type'] != 'program_change':
        raise RuntimeError(f'{old.dict()["type"]} != program_change')
    set_program(track, program)

def fluidsynth_render(input_file_name, output_file_name):
    """
    Convert a .mid file to .wav
    """
    # based on https://pypi.org/project/midi2audio/ sample command
    subprocess.call(['fluidsynth', '-ni', './GeneralUserGS.sf2',
                     input_file_name, '-F', output_file_name, '-r', '44100'])

@click.group(help="Generate datasets")
def main():
    os.makedirs('./tmp', exist_ok=True)

@main.command()
def single_notes(help="Generate a dataset of single notes in ./single_notes"):
    """
    Generate single notes with variety of different instruments
    """
    programs = [Instrument.LEAD_1_SQUARE, Instrument.LEAD_2_SAWTOOTH, Instrument.RECORDER]
    for program in programs:
        os.makedirs(f'./single_notes/{program}')
    for note in range(40, 100):
        midi, track = single_track_midi(program=0)
        track.append(mido.Message('note_on', note=note, velocity=80, time=0))
        track.append(mido.Message('note_off', note=note, velocity=127,
                                  time=Dur.quarter))
        for program in [Instrument.LEAD_1_SQUARE, Instrument.LEAD_2_SAWTOOTH,
                        Instrument.RECORDER]:
            change_program(track, program) 
            midi.save(temp_mid)
            fluidsynth_render(temp_mid, f'./single_notes/{program}/{program}_{note}.wav')

if __name__ == '__main__':
   main() 
