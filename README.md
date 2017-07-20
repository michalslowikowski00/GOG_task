Gog_task

# DEPENDENCIES:  
- PyCharm Community Editon  
https://www.jetbrains.com/pycharm/download/#section=mac    

- Python 2.7.12  
This Python version is installed on Mac by default  

- Selenium 3.0.1   
pip install -U selenium  
(if you don't have pip on your machine -- please look at this documentation and follow installation steps)  
https://pip.pypa.io/en/stable/installing/  

- Robot Framework 3.0.2  
python -m pip install robotframework  

- Keywords library written in Python 2.7.12  
Library written by me in Python  

- Builtin Robot Framework library  
This library is default library in Robot Framework  

# SETUP Robot Framework in Pycharm  
- go to PyCharm preferences -> plugins -> browse repositories and type in 'intellibot'. Install it  

# RUN test via Robot Framework  
- make sure that Python keywords library is imported to robot file. Copy Python keywords path and paste in robot file like in this exapmle:  
*** Settings ***  
Library  path/to/the/python/file.py  
  
- follow this instruction to be able to run Robot test in Pycharm:  
http://blog.bigbinary.com/2015/10/11/configuring-pycharm-to-run-tests.html  

# RUN Robot Framework via terminal:  
- go to directory where Robot file is and run command (in this case -- robot gog.robot):  
robot file_name.robot 
