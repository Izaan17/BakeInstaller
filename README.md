## Bake Installer

### What is Bake Installer?

Bake Installer is a Python script that is required for the installation and setup of the [Bake](https://github.com/Izaan17/Bake.git) repository. This script does the following for you:

* Clones the Bake repository from GitHub.
* Installs the required dependencies.
* Runs the main installation script automatically.

With just one command, you can have everything set up and ready to go!

### Requirements

* Python 3.8 or higher
* Git installed on your system
* `pip` for Python package management


### Installation and Usage

1. **Clone the Repository and Install Dependencies:**

Simply run the following command:
```bash
python3 install.py
```
The script will:

1. Clone the Bake repository from GitHub.
2. Save it to the `.bake` directory in your home folder (or another specified location).
3. Overwrite the existing installation if `overwrite=True`.
4. Install the dependencies listed in `requirements.txt`.
5. Run the `main.py` script.