#! /bin/sh

#DOC#@RUN@$deprecated$ "Used to move volca samples to sampler"

folder="$(ls /home/matias/audio/SAMPLES/volca/ | grep -v wav | dmenu -l 30)"
echo "$folder" >> /home/matias/audio/SAMPLES/volca/log.txt
python3 /home/matias/scripts/volca.py
cd "/home/matias/audio/SAMPLES/volca/""$folder""/output"
cp "/home/matias/audio/SAMPLES/volca/EasyVolcaSample.exe" .
wine EasyVolcaSample.exe
mv out.wav "../../""$folder"".wav"
