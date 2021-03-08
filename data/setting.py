import os


  
# Parent Directory path 
parent_dir = "C:/code_temp/freeprojects/simpsons-analysis/data"

for i in range(1,10):
    # Directory 
    directory = f"Season_{i}"
    
    # Path 
    path = os.path.join(parent_dir, directory)
    os.mkdir(path) 