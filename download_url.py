"""
Download multiple files from www.
"""
import os, urllib

# Links- list all files' URL
download_links = ["http://your-url.com/filename1.tar.gz",
                  "http://your-url.com/filename2.tar.gz"]

# Save to- distination dir
dist_dir = "/path/to/save"

for i in range(len(download_links)):
    print "*****************************************"
    save_to = os.path.join(dist_dir,  os.path.basename(download_links[i]))
    print "Downloading " + download_links[i] + " => " + save_to
    #urllib.urlretrieve(download_links[i], save_to)
    scmd = "wget " + download_links[i] + " -P " + dist_dir
    os.system(scmd)
