# Generating datasets

Requirements:

Most requirements will install through `setup.zsh` which also creates
a python virtual env.

However you will need to install fluidsynth: [http://www.fluidsynth.org]

I could not figure out how to get fluidsynth working on latte.
Recommended workflow is to run the dataset generator on your computer
and `scp` or `rsync` the generated files over to latte.

`midi_gen.py` generates datasets.
