from eeg_positions import get_elec_coords
import mne

# Get the electrode coordinates
coords = get_elec_coords(system="1010", as_mne_montage=True)

# Create the montage
montage = mne.channels.make_standard_montage('custom_1010', pos=coords)

# Save the montage to a file
montage.save('custom_1010.fif')
