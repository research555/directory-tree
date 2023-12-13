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

### 6. Run the Executable
navigate to the directory you want to print the tree of and run the following command:
```bash
dir-tree
```
it should produce something like this:

