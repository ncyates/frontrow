import sys
import time
import os
from multiprocessing import Pool
import motionCalc2
import thread

#start_time = time.time()
#def playVid(video):
#    os.system('python player.py ' + str(video))

def runVid(video):
    return motionCalc2.main(video)


if __name__ == '__main__':
    argList = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]]
    clipList = []
    for c in argList:
        temp = c.strip('\'[],')
        clipList.append(temp)

    pool = Pool()
    start_time = time.time()
    tup = pool.map(runVid,clipList)
    print("took %s seconds" % (time.time() - start_time))
    setDict = {}
    setDict[tup[0][0]] = tup[0][1]
    setDict[tup[1][0]] = tup[1][1]
    setDict[tup[2][0]] = tup[2][1]
    setDict[tup[3][0]] = tup[3][1]
    choice = min(setDict.keys())
    clip = setDict.get(choice)
    playlist = open('playlist.txt', 'a')
    playlist.write(clip +'\n')
    #if clip is not None:
    #   thread.start_new_thread(playVid, (clip,))
    #print("took %s seconds" % (time.time() - start_time))
