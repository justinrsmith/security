import os, time
import subprocess


path_to_watch = os.path.abspath('..')
before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
  time.sleep (10)
  after = dict ([(f, None) for f in os.listdir (path_to_watch)])
  added = [f for f in after if not f in before]
  removed = [f for f in before if not f in after]
  if added: 
    print("Added: ", ", ".join(added))
    filename=added
    fnconvert=str(filename)
    t = open ('filelog.txt', 'w')
    t.write(fnconvert)
    t.close() 
       
    subprocess.call(['./detect.sh'], shell=True)
  if removed: print("Removed: ", ", ".join (removed))
  before = after
