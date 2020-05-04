#!/usr/bin/env python3
import os
import sys
from pathlib import Path

import click
import IPython as ipy
import torch
import torchaudio
from torchaudio import functional as taf
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils import data
import librosa
import numpy as np
import matplotlib.pyplot as plt

def normalized(tensor):
    # https://pytorch.org/tutorials/beginner/audio_preprocessing_tutorial.html
    centered = tensor - tensor.mean()
    normalized = tensor / tensor.abs().max()
    return normalized

_mu_encoder = torchaudio.transforms.MuLawEncoding()
_mu_decoder = torchaudio.transforms.MuLawDecoding()

def mu_law_encode(waveform):
    return _mu_encoder(normalized(waveform))

def mu_law_decode(waveform):
    return _mu_decoder(normalized(waveform))

def load_audio(path):
    """ Load .wav file to Mu law encoding tensor """
    waveform, sample_rate = torchaudio.load(path)
    return mu_law_encode(waveform), sample_rate

def save_audio(path, data, sample_rate):
    """ Save Mu law encoding tensor to .wav file """
    waveform = mu_law_decode(data)
    torchaudio.save(path, data, sample_rate)

@click.group()
def main():
    pass

@main.command()
@click.argument('path')
def load_wav(path):
    waveform, sample_rate = torchaudio.load(path)
    mu = mu_law_encode(waveform)
    ipy.embed()

@main.command()
def test_lstm():
    pass

if __name__ == '__main__':
    main()
