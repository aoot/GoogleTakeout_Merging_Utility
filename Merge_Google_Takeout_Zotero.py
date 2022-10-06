### Script to merge the multiple files created by Google Takeout ###

import os
import shutil
from pathlib import Path, PurePath
from weakref import getweakrefcount
from datetime import datetime

### Notes: ###
## NOTE: If a component is an absolute path, all previous components are discarded.

path_rel_to_home = Path("Downloads/Zotero Takeout")
gTakeout_dir_name = path_rel_to_home.parts[-1]

gTakeout_src_path = Path.home().joinpath(path_rel_to_home)
gTakeout_dirs = [directory for directory in gTakeout_src_path.iterdir()]
year, month, day = datetime.now().year, datetime.now().month, datetime.now().day
hour, minute, second = datetime.now().hour, datetime.now().minute, datetime.now().second
dest_path = gTakeout_src_path.parent.joinpath(f"OUTPUT_{gTakeout_dir_name}_{year}{month}{day}_{hour}{minute}{second}")


for directory in gTakeout_dirs:
    print("\n\n\n #################################")
    print(directory)
    temp_len = len(directory.parts)
    print(len(directory.parts))
    for root, dirs, filenames in os.walk(directory):
        root = "/".join(Path(root).parts[temp_len: ])
        temp_dest_path = dest_path.joinpath(root)
        temp_src_path = Path(directory).joinpath(root)
        # print(temp_dest_path)
        
        
        print("\n\n\n #################################")
        print(root)
        for filename in filenames: 
            # print(temp_dest_path.joinpath(filename))
            # print(temp_src_path.joinpath(filename))
            os.makedirs(temp_dest_path, exist_ok=True)
            shutil.copy(temp_src_path.joinpath(filename), temp_dest_path.joinpath(filename))
        






# for root, dirs, files in os.walk(gTakeout_src_path, topdown=True):
#     print("### " + root)
#     for file in files: 
#         print(file)


'''
## Feature expansion: Async it


source_dir  # Houses all the split up directories
dest_dir =  # New directory a level up '..'

for each directory in source_dir: 
    
    ## FeatureExpansion: check if want to copy over

    copy each directory over to the source  # This would automatically merge the folders because they have the same folder structure.

'''