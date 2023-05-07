# sportpy
A collection of tools to read and visualize data from sport watch

**In Construction**


## Objectives

- A collectino of tools to convert and use `.fit` file from sport watch
- Create dashboard for:
    - a given activity: map with track, choice of color/metric to display. and a number of additional plots
    - comparing 2 activities (e.g. to see progress)

## Installation

```sh
conda create -n fit python=3.9 ipython pip
conda activate fit
pip install fitdecode pyproj pandas matplotlib bokeh

# clone where needed
git clone https://github.com/ArcticSnow/sportpy

# to install in development mode
pip install -e sportpy

```

## Resource:
- A nice `fit` file viewer: https://www.fitfileviewer.com/
- A neat collection of health calculator methods: https://www.omnicalculator.com/sports/fat-burning-zone
