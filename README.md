# Share Projects Dropbox

## Register an App on Dropbox
- Go to the Dropbox App Center page (top right).
- Click on "Build an App".
- Choose "Scoped Access" for the type of access.
- Select "Full Dropbox" as the default access level.
- Give your app a name and click on "Create App".
- In the app settings page, navigate to the "OAuth 2" section.
- Generate an access token by clicking on the "Generate" button under the "OAuth 2" section.
- Save this access token in a secure place (if someone evil has access to it, he'll be able to delete all your files and such). Do not forget it.
- Make sure to enable the "files.metadata.write", "files.content.write", and "sharing.write" permissions to allow your app to write files to Dropbox.
- Save the changes.

## Virtual Environment

Create a Python virtual environment.

### Windows

Install [Python](https://www.python.org/downloads/) (do not install an "old" version, 3.11 or upwards). You can also install it directly from the Microsoft Store.

Install a nice IDE (e.g. [VS Code](https://code.visualstudio.com/Download)).

Open this directory (the same one containing the virtual environment) in VS Code.

In a PowerShell terminal (which can be opened directly inside of VS Code: in the upper menu click Terminal->New Terminal), create a new virtual environment
```shell
python -m venv .venv
```

Run
```
Set-ExecutionPolicy Unrestricted -Scope Process
```

Source the virtual environment (must be repeated on every newly opened PowerShell)
```shell
.\.venv\Scripts\activate
```

Install the required libraries
```shell
pip3 install -r requirements.txt
```

### Linux

Create a virtual environment
```shell
python3 -m venv .venv
```

Source the virtual environment (must be repeated on every new terminal)
```shell
source .venv/bin/activate
```

Install the required libraries
```shell
pip3 install -r requirements.txt
```

## Script

Edit the `students.csv` file to have the student's emails and names. Make sure that there are no duplicate names.

Edit the `share.py` script. Complete the parts marked with `TODO`.

Run your script (in the virtual environment shell).