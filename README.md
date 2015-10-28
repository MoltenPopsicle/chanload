# chanload
Simple 8chan download script written in Python 2.

Pass a thread to the script with:
python2 chanload.py [thread url]

The script will create a folder named after the thread number and download all images in it, saving them as their UNIX timestamp filenames.

If you receive an error about requests, you made need to install the library with pip install requests, or if your main python binary is still python 2, run the package with python rather than python2.
