from eeg_positions import get_elec_coords
import mne

def create1010():
    # Get the electrode coordinates
    coords = get_elec_coords(system="1010", as_mne_montage=True)

    mne.channels.get_builtin_montages()
    # Create the montage
    #montage = mne.channels.make_standard_montage('custom_1010')

    # Save the montage to a file
    #montage.save('custom_1010.fif')

if __name__ == "__main__":
    create1010()