from typing import Literal, Tuple

from mne_bids_pipeline._config_import import _import_config
import mne

FILE_PATH_TEMPLATE = '{data}/derivatives/mne-bids-pipeline/sub-{sub}/eeg/sub-{sub}_task-SocialMemoryCuing_power+{cue}+tfr.h5'

BANDS = {
    'alpha': [8.0, 12.0],
    'theta': [4.0, 7.0]
}

def plot_power(config_path: str, subject: str, cue: Literal['avatar', 'sticks'], band: Literal['alpha', 'theta'],
              time_range: Tuple[float, float], filename: str):
    cfg = _import_config(
        config_path=config_path
    )

    path = FILE_PATH_TEMPLATE.format(data=cfg.bids_root, sub=subject, cue=cue)

    power = mne.time_frequency.read_tfrs(path, condition=0)
    power.apply_baseline(
        baseline=cfg.time_frequency_baseline,
        mode=cfg.time_frequency_baseline_mode,
    )

    time_frequency_crop = {
        'tmin': min(time_range),
        'tmax': max(time_range),
        'fmin': min(BANDS[band]),
        'fmax': max(BANDS[band]),
    }

    if time_frequency_crop:
        power.crop(**time_frequency_crop)

    fig_power = power.plot_topomap(ch_type='eeg', show=True)
    fig_power.axes[0].set_title('{}: {}'.format(cue, band))
    fig_power.set_size_inches(5, 5)

    fig_power.savefig(filename.format(cue=cue, band=band, **time_frequency_crop))
