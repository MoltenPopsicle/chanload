import re
import urllib, urllib2
import os
import sys
import requests, shutil

class imgdownload(object):
  def __init__(self):
    return
  def imginsert(self):
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    agent = urllib2.Request(thread_url, None, headers)
    tfile = urllib2.urlopen(agent)
    tparse = re.findall(r'href="(/[a-z]+/src/+\d+\.(jpg|jpeg|png|webm|mp4|gif|pdf))"', str(tfile.read()))

    global imglist
    imglist = []
    for i in tparse:
      imglist.append(i[0])
    
    imglist =  self.unique(imglist)
    
    print("Found "+str(len(imglist))+" in the thread")
  def unique(self, values):
    output = []
    seen = set()

    for value in values:
      if value not in seen:
        output.append(value)
        seen.add(value)
    return output 
 
  def listdl(self):
    folder = ''.join(re.findall(r'[0-9]', thread_url))

    if not os.path.exists(folder):
      os.makedirs(folder)
      os.chdir(folder)
    else:
      os.chdir(folder)
    print("Making folder")
 
    fileno = 0
    while fileno < len(imglist):
      img_file = 'https://8ch.net' + imglist[fileno]
      imagelist = str(tuple(imglist))
      filename = ''.join(re.findall(r'\d+', str(imglist[fileno])))

      response = requests.get(img_file, stream=True)
      
      with open(filename, 'wb') as f:  
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)
      print("Downloading image "+str(fileno + 1)+" of the thread")
      fileno += 1
      
if __name__ ==  '__main__':
  thread_url = sys.argv[1]
  threadlist = imgdownload().imginsert()
  

  imgdownload().listdl() 
