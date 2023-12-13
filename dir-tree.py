import os
import sys

def list_directory_structure(startpath):
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
            if os.path.isdir(path):
                print(f'{prefix}{pointer}{name}/')
                extension = '│   ' if pointer == '├─' else '    '
                print_tree(path, prefix=prefix+extension)
            else:
                print(f'{prefix}{pointer}{name}')

    print_tree(startpath)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        directory = os.getcwd()

    print(f"Directory structure of: {directory}")
    list_directory_structure(directory)