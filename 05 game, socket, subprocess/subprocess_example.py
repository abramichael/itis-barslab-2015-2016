import subprocess

p = subprocess.Popen(["notepad", "server.py"],
                     cwd=".")
p.wait()