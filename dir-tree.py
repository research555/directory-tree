import os
import sys
import pyperclip

def list_directory_structure(startpath):
    output = []

    def print_tree(folder, prefix=''):
        dirs = [d for d in os.listdir(folder) if os.path.isdir(os.path.join(folder, d))]
        files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

        dirs = [d for d in dirs if not d.startswith('.')
                and not d.startswith('__')
                and 'venv' not in d
                and 'node_modules' not in d
                and 'build' not in d
                and 'dist' not in d
                and '.idea' not in d]

        contents = dirs + files
        pointers = ['├─' if i < len(contents)-1 else '└─' for i in range(len(contents))]

        for pointer, name in zip(pointers, contents):
            path = os.path.join(folder, name)
            line = f'{prefix}{pointer}{name}/' if os.path.isdir(path) else f'{prefix}{pointer}{name}'
            print(line)
            output.append(line)
            if os.path.isdir(path):
                extension = '│   ' if pointer == '├─' else '    '
                print_tree(path, prefix=prefix+extension)

    print_tree(startpath)
    return '\n'.join(output)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()

    print(f"Directory structure of: {directory}")
    directory_structure = list_directory_structure(directory)

    pyperclip.copy(directory_structure)
    print("\nDirectory structure copied to clipboard!")
