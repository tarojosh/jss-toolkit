# Josh's Security Suite Toolkit
A set of password security tools made using Python and Click.

## Description
Josh's Security Suite is a personal CLI project built as an extension of a university assignment for User Interfaces & Design.

It includes core tools for basic password handling:

* Store passwords and the associated website in encrypted text to a safe file location

* Easily access those those passwords by providing the name of the website

* A password generator for creating strong ASCII-based passwords

The project uses the Click framework to create a multi-command CLI app, packaged using Poetry.

Intended as a learning experience, this suite will be gradually expanded into a personal set of lightweight security utilities.


## Installation

### Requirements

* Python 3.11+

* [Poetry](https://python-poetry.org/) for dependency management

### Instructions

1. Clone the repo into the directory you desire using `git clone https://github.com/tarojosh/jss-toolkit.git`.

2. Open the cmd and install dependencies using `poetry install`.

3. In the same terminal, type the command `poetry shell` to start a virtual environment.

4. Finally, type `jss` to get started with using this toolkit.

5. Once you're done, you can exit the virtual environment using `exit`.

## Folders

*./src* - Contains the main project files

*./src/cli* - Command scripts directory

*./src/utils* - Contanis helpful scripts that can be used by other commands

## Credits
Author - Josh Tarongoy
