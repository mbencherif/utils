"""
Rudra Poudel

Download multiple files from www.
"""
import os, urllib

# Links- list all files' URL
download_links = ["http://ipal.cnrs.fr/data/mitosis_evaluation_set_A.tar.gz",
                  "http://ipal.cnrs.fr/data/mitosis_evaluation_set_H.tar.gz",
                  "http://ipal.cnrs.fr/data/A00_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/A01_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/A02_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/A03_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/A04_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/H00_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/H01_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/H02_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/H03_v2.tar.gz",
                  "http://ipal.cnrs.fr/data/H04_v2.tar.gz"
]

# Save to- distination dir
dist_dir = "/home/rp14/rudra/projects/data/mitosis-icpr12"

for i in range(len(download_links)):
    print "*****************************************"
    save_to = os.path.join(dist_dir,  os.path.basename(download_links[i]))
    print "Downloading " + download_links[i] + " => " + save_to
    #urllib.urlretrieve(download_links[i], save_to)
    scmd = "wget " + download_links[i] + " -P " + dist_dir
    os.system(scmd)
