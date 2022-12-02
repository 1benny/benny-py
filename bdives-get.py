import threading
import subprocess as sub

p = sub.DETACHED_PROCESS
sub.Popen(executable="winget.exe", creationflags=p, close_fds=True)