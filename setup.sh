# install some dependencies
python3 -m pip install mne mne-bids-pipeline torch mne-icalabel

## ICA label
# pip install mne-icalabel # added above
# pip install torch # added above
#
## GUI functionalities
pip install mne-icalabel[gui]
#
# MNE's ICA dependencies
pip install mne-icalabel[ica]
#
## check, whether icalabel is properly installed
mne_icalabel-sys_info

