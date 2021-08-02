# TruCol Market Analysis [![Build Status](https://travis-ci.com/a-t-0/Code-LatexReportTemplate.svg?branch=main)](https://travis-ci.com/a-t-0/Code-LatexReportTemplate)

Hi, this is a our roadmap and cost-estimates for the development of a healthy TruCol company. The roadmap consists of a Gantt chart and accompanying elaboration, which are both contained in a single pdf along with the cost estimate. By sharing the code used to generate Gantt chart and cost estimate, we hope to be able to provide more insight in our approach and to improve its accuracy based on the provided feedback. This repository enables you to automatically updates your pdf report every time you run your code. It also syncs with Overleaf so you can do your typing there if you wish.

Our latest roadmap is visible [here](https://github.com/TruCol/Roadmap/blob/master/latex/project1/main.pdf) (refresh page once).

## Usage: do once
Download/clone this repository.
0. If you don't have pip: open Anaconda prompt and browse to the directory of this readme:
```
cd /home/<your path to the repository folder>/
```

1. To use this package, first make a new conda environment and activate (it this automatically installs everything you need)
```
conda env create --file environment.yml
```

## Usage: do every time you start Anaconda:

3. Activate the conda environment you created:
```
conda activate roadmap
```

## Usage: do every run:

3. Performe a run for assignment 1 (named project1) of main code (in `main.py`, called from `__main__.py`)
```
python -m code.project1.src
```

## Testing

4. Testing is as simple as running the following command in the root directory of this repository in Anaconda prompt:
```
python -m pytest
```
from the root directory of this project.

<!-- Un-wrapped URL's below (Mostly for Badges) -->
[black_badge]: https://img.shields.io/badge/code%20style-black-000000.svg
[python_badge]: https://img.shields.io/badge/python-3.8-blue.svg
[apache_badge]: https://img.shields.io/badge/license-Apache%202.0-brightgreen.svg
