# Color Picker

This repository helps to generate large sets of attractive and accessible color schemes based on Mathew Strom's work in [*How to pick the least wrong colors*](https://matthewstrom.com/writing/how-to-pick-the-least-wrong-colors).

## Table of Contents

* [**Description**](#description)
* [**Dependencies**](#dependencies)
* [**Usage**](#usage)
* [**Project structure**](#project-structure)
* [**Background and Motivation**](#background-and-motivation)
* [**License**](#license)

## Description

This code is, in many cases, a direct NodeJS-to-Python port of Mathew Strom's work in [*How to pick the least wrong colors*](https://matthewstrom.com/writing/how-to-pick-the-least-wrong-colors). I have made minor improvements in certain areas.

`target_colors` is an array of colors in hexadecimal format. If set, the script will attempt to find colors that are similar to these.

`energy_weight`, `range_weight`, `target_weight`, `protanopia_weight`, `deuteranopia_weight`, and `tritanopia_weight` can be any floating point number. They adjust the relative impact of each factor in the algorithm's decisionmaking:

- A higher energy weight (`energy_weight`) will result in colors that are more differentiable from each other.
- A higher range weight (`range_weight`) will result in colors that are more uniformly spread through color space.
- A higher target weight (`target_weight`) will result in colors that are closer to the target colors specified with `target_colors`.
- A higher protanopia weight (`protanopia_weight`) will result in colors that are more differentiable to people with protanopia.
- A higher deuteranopia weight (`deuteranopia_weight`) will result in colors that are more differentiable to people with deuteranopia.
- A higher tritanopia weight (`tritanopia_weight`) will result in colors that are more differentiable to people with tritanopia.

`temperature` can be any floating point number. It is the starting point temperature of the algorithm - a higher temperature means that early iterations are more likely to be randomly-chosen than optimized.

`cooling_rate` can be any floating point number. It is the decrease in temperature at each iteration. A lower cooling rate will result in more iterations.

`cutoff` is the temperature at which the algorithm will stop optimizing and return results. A lower cutoff means more late-stage iterations where improvements are minimal.

## Dependencies

This project requires Python 3. This project has no other dependencies, including any non-standard Python libraries.

## Usage

To use this notebook, download it, open it in a Jupyter environment, and run all cells.

## Project structure

```
./colors
|_ README.md # This file.
|
|_ colors.ipynb # Color pallette generator.
|
|_ makefile # Project makefile
|_ LICENSE.md # Project license.
```

## Background and Motivation

Mathew Strom made a good case for this project in [*How to pick the least wrong colors*](https://matthewstrom.com/writing/how-to-pick-the-least-wrong-colors), so I won't belabor the point here.

## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/). You can view the full text of the license in [LICENSE.md](./LICENSE.md). Read more about the license [at the original author’s website](https://zacs.site/disclaimers.html). Generally speaking, this license allows individuals to remix this work provided they release their adaptation under the same license and cite this project as the original, and prevents anyone from turning this work or its derivatives into a commercial product.
