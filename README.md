# Testing `bambi`

This repo takes [`bambi`](https://bambinos.github.io/bambi/) notebooks from [Examples](https://bambinos.github.io/bambi/notebooks/) and runs them to check reproducibility.

## Setup

Using `uv` version 0.5.7

    uv sync

External dependency to run some of the notebooks:

* `model.graph()` like statements require [`graphviz`](https://graphviz.org) to be installed
