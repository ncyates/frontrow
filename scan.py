import os
from os import listdir
from os import path
import time
import sys
#import thread
from multiprocessing import Process
#from multiprocessing import Pool
#import player

start_time = time.time()


#def run_mult(clips):
    #print(clips)
    #os.system('python multiProc.py ' + str(clips))
    #return
"""
Assumptions:
    -- We are accepting a command line parameter that is the path to a directory containing four directories. 
    -- Each of these directories contains video clips for the camera it represents.
Notes:
    -- There is no error checking yet.
    -- In the application comments:
        -- "camera" refers to the directory that holds a camera's video files.
        -- "clip" refers to the video files.
    
Questions:
    -- What is the max number of files per folder? 10,000?

"""

# TODO: Error checking on command line input (use argparse package)
# TODO: Output helpful error message for erroneous input e.g. "usage = ... " etc.
# TODO: Null checking on folders / files
# TODO: Prevent blocking if a file can't be found in a folder (use a timer?)
# TODO: Get and send playlist argument

# mainDir is the path of the parent directory that holds the directory for each camera.
mainDir = sys.argv[1]

dirs = listdir(mainDir)

# camList is the list of cameras.
camList = []
for dir in dirs:
    dir = mainDir + '/' + str(dir)
    if path.isdir(dir):
        camList.append(dir)
#print('\n\nThe cameras are: ' + str(camList))  # test camList

# clipNumber is an index for the nth clip we want to look for in the camera.
clipNumber = 0

# clipName is the numeric string version of clipNumber we use for concatenation in building the file path.
clipName = str(clipNumber)

# clipNamePrefix is the prefix of the name of the clip. Change this if the file names change.
clipNamePrefix = 'out'

# clipNameExt is the file extension of the clip. Change this if the file types change.
clipNameExt = '.mp4'

# MAX_FILES is the maximum expected number of clips per camera.
MAX_CLIPS = 100

# CAMERA_COUNT is the number of cameras.
CAMERA_COUNT = len(camList)

"""
Search each of the directories we were given for the currentClip
If we find it in a directory, add the path to the clipSet

Currently an all-or-nothing approach -- will block if one or more files are not found
"""
#os.system('python player.py')
playlist = open('playlist.xspf', 'w')
playlist.write('<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n <playlist version=\"1\" xmlns=\"http://xspf.org/ns/0/\">\n    <trackList>\n')
playlist.close()

while clipNumber < MAX_CLIPS:

    currentClip = clipNamePrefix + (str(clipNumber)).zfill(4) + clipNameExt  # currentClip is the name of the clip we are looking for.

    cameras = {}
    for cam in camList:
        cameras[cam] = False

    # clipSet is a list containing the file paths of the nth clip from each camera.
    clipSet = []

    print ('processing ' + str(currentClip) + ' files...')
    while False in cameras.itervalues():
        #print('\n')
        #print('Not all ' + currentClip + ' files have been found')
        for camera, hasClip in cameras.iteritems():
            #print(camera, hasClip)
            if hasClip == False:
                #print('\t' + currentClip + ' is not yet found in ' + camera)
                #print('\tChecking for file...')
                if path.isfile(camera + '/' + currentClip):
                    #print('\t\tSuccess! File was found')
                    #clipSet.append(mainDir + '/' + camera + '/' + currentClip)
                    clipSet.append(camera + '/' + currentClip)
                    cameras[camera] = True
    #print('\n\tcalling processor with: \n\t python processor.py ' + str(clipSet))
    #if __name__ == '__main__':
        #p = Process(target = run_mult, args = (clipSet,))
        #p.start()
    os.system('python multiProc.py ' + str(clipSet))
    clipNumber +=1


playlist = open('playlist.xspf', 'a')
playlist.write('    </trackList>\n </playlist>')
playlist.close()
# print the elapsed time of processing the clips
print("%s seconds" % (time.time() - start_time))