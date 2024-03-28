# allow for reading in a comma separated list from file
import pandas as pd

# import some eeg specific modules
from mne import io as mio # allow for reading in raw data
import mne_icalabel       # allow for labelling ica components
from mne.preprocessing import read_ica # self explaining
from mne_bids import BIDSPath # allow for BIDSPath objects

# add pipeline specific tools for loading settings from config object
from mne_bids_pipeline._config_utils import (
    get_subjects,
    get_sessions
)

# allow for definition of optional parameters in a function definition
from typing import Optional

def update_ica_labels(cfg=None, do_print_verbose:bool=True):
    """
    Compute ICA labels for each subject in the current configuration.
    Per subject, also update the comma separated file (*.tsv file)
    containing the `good`/`bad` label per component.
    """
    for subject in get_subjects(cfg):
        for session in get_sessions(cfg):
            paths = get_input_fnames_apply_ica(cfg=cfg, subject=subject, session=session)
            try:
                ica = read_ica(paths["ica"])
            except FileNotFoundError:
                curr_path = paths["ica"]
                Warning(f"FileNotFoundError, the file {curr_path} was not found.")
            try:
                raw = mio.read_raw_fif(paths["raw"])
            except FileNotFoundError:
                curr_path = paths["raw"]
                Warning(f"FileNotFoundError, the file {curr_path} was not found.")

            label_results = mne_icalabel.label_components(raw, ica, method="iclabel")

            if do_print_verbose:
                print("\n\nSUBJECT:", subject)
                print(str(ica)) # checkup print of known data about ICA
                print("\nresulting predictions:", label_results["y_pred_proba"]) # checkup print
                print("\nresulting labels:     ", label_results["labels"])       # checkup print

            labels = label_results["labels"]
            exclude_idx = [
                idx for idx, label in enumerate(labels) if label not in ["brain", "other"]
            ]
            try:
                tsv_data = pd.read_csv(paths["components"], sep="\t")
            except FileNotFoundError:
                curr_path = paths["components"]
                Warning(f"FileNotFoundError, the file {curr_path} was not found.")

            if do_print_verbose:
                # checkup: print old content of the file
                print("\nold tsv file content:")
                print(str(tsv_data))

            tsv_data.loc[exclude_idx, "status"] = "bad"

            if do_print_verbose:
                # checkup: print updated content of the file
                print("\nnew tsv file content:")
                print(tsv_data)

            tsv_data.to_csv(paths["components"], sep="\t", index=False)



def get_input_fnames_apply_ica(
        *,
        cfg,
        subject: str,
        session: Optional[str],
) -> dict:
    """
    Return the paths of the files containing ica components, raw signals, and ica component labels.
    This function gets used in application of the ICA results to the raw data.
    """
    bids_basename = BIDSPath(
        subject=subject,
        session=session,
        task=cfg.task,
        acquisition=cfg.acq,
        recording=cfg.rec,
        space=cfg.space,
        datatype='eeg',
        root=cfg.deriv_root,
        check=False,
    )
    paths = dict()
    paths["ica"] = bids_basename.copy().update(suffix="ica", extension=".fif")
    paths["raw"] = bids_basename.copy().update(suffix="proc-filt_raw", extension=".fif")
    paths["components"] = bids_basename.copy().update(
        processing="ica", suffix="components", extension=".tsv"
    )
    return paths