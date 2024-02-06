# convert bids format events from version 1 to version 2

# How To

# alternative 1
# 
# run this script from project root, e.g.
# bash ./src/data_handling_convert_brainvision2bids_version1to2updater.sh
sed -i 's/sticks/s3042/g' ./data/ds003702/sub-??/eeg/*_events.tsv
sed -i 's/avatar/s3022/g' ./data/ds003702/sub-??/eeg/*_events.tsv

# alternative 2:
# 
# 1.) rm ./data/ds003702/sub-*/eeg/*_events.tsv
# 2.) python3 ./src/data_handling_convert_brainvision2bids.py
