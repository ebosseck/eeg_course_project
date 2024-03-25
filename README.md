# README - EEG Course Project - Group: Hyacithara

This Git repository contains the finally chosen version of the Hyazinthara's group.
To run the projects source code, these requirements need to be met:

- sufficient system memory (16 GB should be okay)
- Python 3.11.8
- Python modules listed in `./ e s   l i s.txt` (tested version number is also given)
- this Git repository including
    - `./src/` for custom Python modules,
    - `./mne-bids/config/` with the MNE BIDS pipeline configuration, and
    - Jupyter notebooks `./*.ipynb` for preparing the system and running the pipeline
 
1. Install Python 3.11.8, e. g. using the OS package manager (`apt`/`pacman`/`apk`/…) or the binary installer from [python.org](https://www.python.org/downloads/).
2. optinal: Create a virtual environment. You then may start the `venv` by running the activate file, or replace `python` by `/path/to/venv/bin/python`.
3. Get the Git repository, e. g. as `*.zip` file or via `git clone git@github.com:ebosseck/eeg_course_project.git`. Then navigate to the project root directory.
4. Install additional python modules. O d u l e , do this within your new `venv` Python environment.
    - Run `python -m pip install -r requirements.txt` at the project root directory, or
    - install Jupyter lab running `python -m pip install jupyterlab`, and then run the other steps within the Jupyter notebooks.
5. Start Jupyter Lab from the project root directory running `python -m jupyterlab .`
6. Run the Jupyter notebooks.
    - Set up the system including module dependencies.
    - Download and prepare the dataset. The download can take about one hour.
    - Run the pipeline and print checkups. The pipeline seems to run for about one hour.

The notebooks are structured to be self explaining. You can run them using either `[Shift]+[Enter` for one at a time, or by pressing the double-play-button on top of the window to run all cells of the notebook.
