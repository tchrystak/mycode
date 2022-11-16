#!/usr/bin/env python3

# library imports
import shutil # used to move files
import os # provides access to low level os operations

# move into this directory
os.chdir('/home/student/mycode/')

#moving file raynor.obj into ceph_storage directory
shutil.move('raynor.obj', 'ceph_storage/')

# program will pause to accept input
xname = input('What is the new name for kerrigan.obj? ') # collect input from user

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moving kerrigan.obj into                                                                  # ceph_storage/ with new name

