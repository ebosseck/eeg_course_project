# define a function which gets used in application of the ICA results to the raw data
def get_input_fnames_apply_ica(
    *,
    cfg,
    subject: str,
    session: Optional[str],
) -> dict:
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
