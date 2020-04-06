#!/bin/bash
# (there was a facebook copyright message above. see train2.sh)
set -e -x

## USAGE ##
# ALWAYS set EXP to something unique!
# Set DATA to the glob for the files that you're training on.
# For instance, "musicnet/single_notes/preprocessed/*" (with quotes!)
# If you're getting Exception empty for randrange() errors try lowering --seq-len
# To train on only 1 GPU, lower --batch-size to 4

CODE=src
DATA=TODO: SET THIS TO "musicnet/datasetname/preprocessed/*"

# This is really important!
# It's the name of the checkpoint
EXP=TODO: SET THIS TO EXPERIMENT NAME
export MASTER_PORT=29500

python ${CODE}/train.py \
    --data ${DATA} \
    --batch-size 4 \ # Change this to 4 * # gpus to be used
    --lr-decay 0.995 \
    --epoch-len 1000 \
    --num-workers 5 \
    --lr 1e-3 \
    --seq-len 4000 \ # It was 12000 by default. Changed to shorted value because it was crashing on single note dataset.
    --d-lambda 1e-2 \
    --expName ${EXP} \
    --latent-d 64 \
    --layers 14 \
    --blocks 4 \
    --data-aug \
    --grad-clip 1
    --per-epoch
    --epochs 1000
