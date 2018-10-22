# python 3.5

from pathlib import Path
Path.cwd()

# how to combined Path.cwd() with a folder path in order to get to your destination
# this will allow anyone to reuse the code without manually changing the home directory

data_folder =  Path(Path.cwd(),"python/output")
'{}\{}'.format(data_folder,'sshot_medium.png')
