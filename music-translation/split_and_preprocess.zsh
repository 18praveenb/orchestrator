#!/usr/bin/env zsh
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 dataset-dir"
    exit 1;
fi
for d in ${1}/*/; do
    python src/split_dir.py -i $d -o ${1}/split/$(basename "$d")
done
python src/preprocess.py -i ${1}/split -o ${1}/preprocessed
