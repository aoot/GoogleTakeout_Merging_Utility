### Script to merge the multiple files created by Google Takeout ###

import os
import shutil
from pathlib import Path, PurePath
from datetime import datetime

## Path to the Google Takeout directory
## The directory needs to be a relative path, relative to home, without the first forward slash.
## Else, the first forward slash will be considered filesystem root.
# path_rel_to_home = Path(input("Relative path of Google Takeout directories (without first forward slash): "))
gTakeout_path_rel_to_home = Path("Downloads/Zotero Takeout")  # Debug use, override the input prompt

## gTakeout Directory name (for naming the output folder)
gTakeout_dir_name = gTakeout_path_rel_to_home.parts[-1]

## Create a full path
gTakeout_src_path = Path.home().joinpath(gTakeout_path_rel_to_home)  # Can also use the resolve() method
## List of Google Takeout split directories
gTakeout_dirs = [directory for directory in gTakeout_src_path.iterdir()]  # Relative to gTakeout_src_path

## Set variables for naming
year, month, day = datetime.now().year, datetime.now().month, datetime.now().day
hour, minute, second = datetime.now().hour, datetime.now().minute, datetime.now().second
## Output directory path
dest_path = gTakeout_src_path.parent.joinpath(f"OUTPUT_{gTakeout_dir_name}_{year}{month}{day}_{hour}{minute}{second}")

## Merging Logic
for directory in gTakeout_dirs:
    split_dir_abs_path_len = len(directory.parts)  # Number of absolute path parts
    
    ## Directory walk
    for root, dirs, filenames in os.walk(directory):
        # print(f"pre-change root: {root}")  # Debug use
        ## pre-change root is absolute path
        ## post-change root is relative to each Google Takeout split directory 
        root = "/".join(Path(root).parts[split_dir_abs_path_len: ])
        # print(f"post-change root {root}")  # Debug use
    
        temp_dest_path = dest_path.joinpath(root)  # New structure into the destination folder
        temp_src_path = Path(directory).joinpath(root)  # Need the source path for copying
    
        ## Iterate and copy each file
        for filename in filenames: 
            # print(temp_dest_path.joinpath(filename))  # Debug use
            # print(temp_src_path.joinpath(filename))  # Debug use
            os.makedirs(temp_dest_path, exist_ok=True)  # Create the dir hierarchy if doesn't exist
            shutil.copy(temp_src_path.joinpath(filename), temp_dest_path.joinpath(filename))  # Copy to output folder
        



'''
## Feature expansion: Async it


source_dir  # Houses all the split up directories
dest_dir =  # New directory a level up '..'

for each directory in source_dir: 
    
    ## FeatureExpansion: check if want to copy over

    copy each directory over to the source  # This would automatically merge the folders because they have the same folder structure.

'''