'''
Cleans directory and keeps only those files which have both specified extensions.
i.e., both .RAW and .JPG. Assumption is that the extension is four characters,
including the period.


date: 2018. 5. 31.
author: dy-choi
'''

import os, sys

def remove_file(my_dir, s, ext):
    '''
    Remove files in set (s) from directory (dir) by adding extensions (ext).
    s : set
    ext : str
    returns number of files removed.
    '''
    counter = 0
    if len(s) > 0 :
        for file in s:
            os.remove(my_dir + file + ext)
            counter += 1
    return counter

def extension_set(ext, my_dir):
    '''
    return set of file names with extension 'ext' from my_dir.
    extensions removed before adding to set.
    '''
    return set([file[:-4] for file in os.listdir(my_dir) if file.endswith(ext)])

def filter_files(ext1, ext2, my_dir):
    '''
    Filters through files in my_dir and returns set of file names that
    only have ext1 and a set of file names that only have ext2.
    ext1 : extension 1 (str)
    ext2 : extension 2 (str)
    '''
    # add to respective sets but remove file extensions
    ext1_set, ext2_set = extension_set(ext1, my_dir), extension_set(ext2, my_dir)
    
    extra_ext1 = ext1_set - ext2_set
    extra_ext2 = ext2_set - ext1_set
    
    return extra_ext1, extra_ext2

def remove_pairless_files(ext1, ext2, my_dir):
    '''
    remove all files that do not have a pair,
    i.e. has ext1 but not ext2 or vice versa.
    returns the number of files deleted from each set of files (filtered by extension).
    '''
    set1, set2 = filter_files(ext1, ext2, my_dir)
    return remove_file(my_dir, set1, ext1), remove_file(my_dir, set2, ext2)

def main():
    # command line run example: python folder_cleaner.py sample-folder-name
    # define extensions
    ext1, ext2 = ".RAF", ".JPG"
    
    # define directory
    path, _ = os.path.split(os.path.realpath(__file__))
    my_dir = path + "/" + argv[1] + "/"

    num_rem_ext1, num_rem_ext2 = remove_pairless_files(ext1, ext2, my_dir)

    # print resulting number of file removals
    print("Number of", ext1, "removed :", num_rem_ext1)
    print("Number of", ext2, "removed :", num_rem_ext2)

if __name__ == "__main__":
    main()
