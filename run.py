import subprocess
import sys

subprocess.call("sudo apt-get update", shell=True)

subprocess.call("sudo apt-get install libcunit1 libcunit1-doc libcunit1-dev", shell=True)

subprocess.call("gcc test.c -o test -lm -lcunit", shell=True)
subprocess.call("gcc main.c -o main -lm", shell=True)

subprocess.call("echo '# Eredmények' > report.md", shell=True)

subprocess.call("./test >> report.md", shell=True)