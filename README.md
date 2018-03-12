# Using virtualenv environments with CodeRunner

I use this tiny script to make CodeRunner use python virtual 
environments.  

1. put this script anywhere (let's assume it is at ~/run_python.py).

2. When you create a virtual environment for your project, make sure 
   a directory called ".venv"

3. In CodeRunner preferences, select "Languages/Python3" and change
   the run command to: `python3 ~/run_python.py  $filename`
   
   
# Cheers !
   

