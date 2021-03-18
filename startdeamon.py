
import os
import daemon
import time
from daemon import pidfile

def main():
    while True:
        print("Loop unlimited")
        time.sleep(1)

def start_daemon(pid_file: str):

    print('pid file {}'.format(pid_file))
    print('start run daemon')
    
    out = open('stdout_file.log', 'w+')
    # pidfile is a context
    with daemon.DaemonContext(
            stdout=out,
            working_directory=os.getcwd(),
            umask=0o002,
            pidfile=pidfile.TimeoutPIDLockFile(pid_file),
    ) as context:
        main()

start_daemon("/tmp/mypid.pid")
