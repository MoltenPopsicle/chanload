import re
import urllib2
import os
import sys
import requests, shutil

class imgdownload(object):
    def __init__(self):
        return
    def imginsert(self):
        headers = { 'User-Agent' : 'Mozilla/5.0' } 
        agent = urllib2.Request(thread_url, None, headers) #Sets the script's user agent header to Mozilla/5.0, as 8chan blocks requests from python user agents
        tfile = urllib2.urlopen(agent)
        tparse = re.findall(r'href="(/[a-z]+/src/+\d+\.(jpg|jpeg|png|webm|mp4|gif|pdf))"', str(tfile.read())) #regex to find images

        global imglist
        imglist = []
        for i in tparse:
            imglist.append(i[0])
        imglist =  self.unique(imglist) #Removes duplicate file entries by invoking uniqueness checker below
     
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
            os.chdir(folder) #Checks if folder already exists. If not, creates it.
        else:
            os.chdir(folder)
        print("Making folder")
 
        fileno = 0 
        while fileno < len(imglist): #Uses a number increasing by 1 to count the current index entry in the list
            img_file = 'https://8ch.net' + imglist[fileno]
            filename = ''.join(re.findall(r'\d+', str(imglist[fileno]))) #Uses file counter and sets filename as the original filename's number of current list entry

            response = requests.get(img_file, stream=True)
       
            with open(filename, 'wb') as f:  
                response.raw.decode_content = True 
                shutil.copyfileobj(response.raw, f)  #Copies raw data gotten from requests into a filee
            print("Downloading image "+str(fileno + 1)+" of the thread")
            fileno += 1
       
if __name__ ==   '__main__':
    thread_url = sys.argv[1]
    threadlist = imgdownload().imginsert()
   

    imgdownload().listdl() 
