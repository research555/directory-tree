# Directory Tree
This script will print your directory tree in a tree format. I have made it into an executible on my PC using pyinstaller. I use this when I want to put the directory structure into README's or when asking chatgpt to optimize my project structure. You can find the instructions below:
## Instructions

To turn the Python script into an executable, you can use a tool like `PyInstaller`. Here are the steps to do this:

### 1. Clone the repo and install pyinstaller

```bash
git clone https://github.com/research555/directory-tree.git
pip install pyinstaller
```

### 3. Create the Executable

Navigate to the directory where your script is saved using the command prompt or terminal. Then run the following command:

```bash
pyinstaller --onefile dir-tree.py
```

Magic will happen and youll get a bunch of output. If everything goes well, you'll see a `dist` folder in your directory.
### 4. Locate the Executable

After the process completes, you'll find the executable in the `dist` directory located in the same directory as your script. 

### 5. Add .exe to PATH

If you want to be able to run the executable from anywhere on your system, you'll need to add it to your PATH. You do this by adding the directory where the executable is located to your system variables PATH

On Windows just search for env and click on Edit the system environment variables. Then click on Environment Variables. Under System variables, find the variable named Path and click Edit. Click New and add the path to the directory where your executable is located. Click OK to save the changes and voila.

I like to save my executables in a folder called bin in my user directory. So I add the following to my PATH:

```bash
C:\Users\immi\local-scripts\execs
```
Makes things easier to add to path, find and manage.
### 6. Run the Executable
Navigate to the directory you want to print the tree of and run the following command:
```bash
dir-tree
```
it should produce something like this:

```bash
Directory structure of: C:\Users\immi\PyCharmProjects\Templates\api
├─app/
│   ├─api/
│   │   ├─v1/
│   │   │   ├─routers_1.py
│   │   │   ├─routers_2.py
│   │   │   └─__init__.py
│   │   ├─deps.py
│   │   └─__init__.py
│   ├─core/
│   │   ├─config.py
│   │   ├─params.yml
│   │   └─__init__.py
│   ├─crud/
│   │   └─__init__.py
│   ├─database/
│   │   ├─base_class.py
│   │   ├─initialize.py
│   │   ├─session.py
│   │   └─__init__.py
│   ├─exceptions/
│   │   └─__init__.py
│   ├─models/
│   │   └─__init__.py
│   ├─schemas/
│   │   └─__init__.py
│   ├─services/
│   │   ├─external_services/
│   │   │   └─__init__.py
│   │   └─__init__.py
│   ├─utils/
│   │   └─__init__.py
│   ├─main.py
│   └─__init__.py
├─credentials/
├─migrations/
│   └─versions/
├─tests/
│   ├─integration/
│   ├─unit/
│   └─configure_test.py
├─.env
├─.gitignore
├─.gitlab-ci.yml
├─alembic.ini
├─docker-compose.yml
├─Dockerfile
├─LICENSE
├─README.md
└─requirements.txt
```
