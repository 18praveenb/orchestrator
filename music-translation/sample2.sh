# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.
#
#!/usr/bin/env bash

DATE=`date +%d_%m_%Y`
CODE=src
OUTPUT=results/${DATE}/$1

echo "Sampling"
python ${CODE}/data_samples.py --data musicnet/preprocessed/Bach_Solo_Piano/ --output ${OUTPUT}  -n 4 --seq 80000 # Cello

echo "Generating"
python ${CODE}/run_on_files.py --files ${OUTPUT} --batch-size 4 --checkpoint $checkpoint_path --output-next-to-orig --decoders $2 --py
