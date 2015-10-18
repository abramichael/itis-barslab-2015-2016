# -*- coding: utf-8 -*-

import os
import shutil

print os.path.abspath(os.curdir)
print os.path.abspath(os.pardir)

#os.chdir("F:\\")
#print os.path.abspath(os.curdir)

for f in os.listdir(os.curdir):
    if f.startswith("cw"):
        #renaming
        os.rename(f, "h" + f[1:])


start_path = os.curdir
end_path = "my_function"
result_path = os.path.abspath(os.path.join(start_path, end_path))
print result_path

# try:
#     shutil.copy("abstr.py", "abstract.py")
# except:
#     pass
#
# os.remove("abstr.py")

for d, dirs, files in os.walk("F:\\praxis\\barslab"):
    print "========"
    print d
    print dirs
    print files