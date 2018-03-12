import os
import os.path
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # sys.argv[1] is expected to be a file name 
        dir = os.path.dirname(sys.argv[1])
        if (os.path.isdir(os.path.join(dir,'.venv'))):
            python = os.path.join(dir,'.venv','bin','python')
            os.execv(python, [python] + sys.argv[1:])
        else:
            os.execvp('python3',['python3'] + sys.argv[1:])
    else:
        os.execlp('python3','python3')