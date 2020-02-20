Configuring Pipenv in Visual Studio Code

Pipenv is a more modern way to manage project dependencies in Python. However, if you want to use Visual Studio Code's Python plugin for your project, you need to tell it where it can find your virtualenv.

First, navigate to your Pipenv directory (where your Pipfile is located). Then run pipenv --venv, to get the full path to the Pipenv's virtualenv. This is probably something like /home/myuser/.local/share/virtualenvs/projectname, depending on which operating system you are on.

Next, press CTRL+Shift+P (Cmd in MacOS) and search for "Select Workspace Interpreter". Press enter, and select any of the suggested interpreters. Upon doing this, a .vscode directory will be created inside your project root, containing a settings.json. Open this file, and set python.pythonPath to the virtualenv path you found earlier, and add /bin/python at the end.

In other words, settings.json should look something like this:

{
    "python.pythonPath": "/home/myuser/.local/share/virtualenvs/projectname/bin/python"
}

Save the settings file, and restart Visual Studio Code, for the changes to take effect.
