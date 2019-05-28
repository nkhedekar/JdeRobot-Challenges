# JdeRobot-Challenges

This repository contains my solutions to the JDERobot Challenges for the GSoC 2019 Application.

## Installation

The details of the challenge itself can be found in [this](installation/gsoc2019-installation_test.pdf) file.

The terminal dump of the installation is provided in [installation.log](installation/install.log) and a screenshot of the working cameraview and cameraserver are provided in [cam_proof.png](installation/cam_proof.png).

## Python

The details of the challenge itself can be found in [this](python/gsoc2019-python_test.pdf) file.

The game has been implemented as a module in [cgol.py](python/cgol.py) with the game configurable settings in [config.json](python/config.json). The game is instantiated in [sample_app.py](python/sample_app.py)

### Dependancies

This package requires the standard python3 libraries and numpy to be intalled.

### Usage

To run the game, run `python3 sample_app.py` from the python directory and follow the instructions on the terminal.

To run the tests, run `python3 tests.py -v` from the python directory

### Proof of working

Some videos of the working code are available at the following links:

- [Link1](https://youtu.be/dzcdh2ZqXl0)
- [Link2](https://youtu.be/mSpgKjWAkdI)

Testing:

```bash
......
----------------------------------------------------------------------
Ran 6 tests in 0.015s

OK
zeus@Olympus:~/Desktop/workspaces/jderobot-challenges/python$ python3 tests.py -v
test_created_grid (__main__.TestCgolMethods) ... ok
test_oscillators (__main__.TestCgolMethods) ... ok
test_pattern_placement (__main__.TestCgolMethods) ... ok
test_spaceships (__main__.TestCgolMethods) ... ok
test_still_life (__main__.TestCgolMethods) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.009s

OK
```
