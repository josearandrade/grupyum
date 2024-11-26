![GitHub License](https://img.shields.io/github/license/josearandrade/grupyum)
[![Version](https://img.shields.io/badge/version-1.0-blue.svg)](VERSION)

## Description

This application was developed by Biomedical Informatics students at the University of São Paulo, Ribeirão Preto campus, as part of the "Fundamentals of Medical Imaging" course. The goal of the app is to automate a repetitive process used in a master's project related to medical imaging.

## Table of Contents

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## About

Development Environment: VSCodium (vscode fork project) with virtualenv for dependencies control.

#### Dependencies

##### Geral

- Python 3.11.9
- Virtualenv

##### Processing

- Pandas
- CV2
- Numpy
- Matplotlib

##### Interface

- PyQT6

#### Methods

- cv2.imread
- cv2.cvtcolor (BGR2RGB)
- color thresholding (lower and upper RGB)
- cv2.inRange
- cv2.bitwise_and
- plt.figure
- cv2.cvtColor (BGR2GRAY)
- cv2.GaussianBlur
- cv2.Canny
- cv2.dilate
- cv2.findContours
- cv2.contourArea
- cv2.arcLength
  - circularity and perimeter limits
- cv2.drawContours


## Installation

### Prerequisites

- Python 3.x
- pip

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/josearandrade/grupyum.git
   ```
2. Navigate to the project directory:
   ```bash
   cd grupyum
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run widget.py:
   ```bash
   python gui/widget.py
   ```

## Features

## License

This project is licensed under the MIT License.

## Acknowledgements

Thank any collaborators, mentors, or resources that helped in the development.
