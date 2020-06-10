
##  resolve host adress 

ping -a my_computer 

will give the IP of my_computer



##  batch get directory 

for /D  %%I in ("%~dp0..\") do set ENV_VAR=%%dpI


explanation:

for /D : loop on directories
%%I : directory variable in loop

~dp0 : current dir path
..\ : parent path

set ENV_HOME to current parent directory path




##  batch remove final char 

set ENV_VAR=%ENV_VAR:~0,-1%

path/to/dir/  --> path/to/dir




##   
##   
##   
##   
##   
##   
##   
##   



