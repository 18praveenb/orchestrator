DATE=`date +%d_%m_%Y`
CODE=src
OUTPUT=results/${DATE}/$1
checkpoint_path=$1
shift

echo "Sampling"
python ${CODE}/data_samples.py --data musicnet/preprocessed/Bach_Solo_Piano/ --output ${OUTPUT} -n 4 --seq 80000 # Cello

echo "Generating"
python ${CODE}/run_on_files.py --files ${OUTPUT} --batch-size 4 --checkpoint $checkpoint_path --output-next-to-orig --decoders $@ --py


