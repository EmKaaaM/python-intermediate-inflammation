# Inflam

<img src="Python-Symbol.png" width="200" height="200">

Inflam is a data management system written in Python that manages trial data used in clinical inflammation studies.

![Continuous Integration build in GitHub Actions](https://github.com/EmKaaaM/python-intermediate-inflammation/workflows/CI/badge.svg?branch=main)

## Main features

Here are some key features of Inflam:

- Provide basic statistical analyses over clinical trial data
- Ability to work on trial data in Comma-Separated Value (CSV) format
- Generate plots of trial data
- Analytical functions and views can be easily extended based on its Model-View-Controller architecture

## Prerequisites

Inflam requires the following Python packages:

- [NumPy](https://www.numpy.org/) - makes use of NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) - uses Matplotlib to generate statistical plots

The following optional packages are required to run Inflam's unit tests:

- [pytest](https://docs.pytest.org/en/stable/) - Inflam's unit tests are written using pytest
- [pytest-cov](https://pypi.org/project/pytest-cov/) - Adds test coverage stats to unit testing

## Installation

- Clone the repo ``git clone https://github.com/EmKaaaM/python-intermediate-inflammation.git``
- Create a new virtual environment using ``python3 -m venv venv``
- Activate your new environment using ``source venv/bin/activate``
- Install via ``pip install -r requirements.txt.``
- Run the setup file via python ``python3 setup.py build`` and ``python3 setup.py install``
- Check everything runs by running ``pytest`` in the root directory


## Usage

- After following the installation instructions run ``python3 inflammation-analysis.py data/inflammation-01.csv``
- A GUI should pop up displaying different data.
- If using WSL2 you might need to run X11-forward and XLaunch server to see GUI

## Contributing

- Create an issue [here](https://github.com/EmKaaaM/python-intermediate-inflammation/issues)
- Please open an issue if you spot any problems

## Credits

- Thanks to me for working on this!

## License

- This source code is protected under international copyright law.  All rights reserved and protected by the copyright holders.
- This file is confidential and only available to authorized individuals with the permission of the copyright holders.  If you encounter this file and do not have permission, please contact the copyright holders and delete this file.
