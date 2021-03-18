import os
pid = int(open('/tmp/mypid.pid').read())
try:
    os.kill(pid, 9)
    print('Stopped!')
    os.remove('/tmp/mypid.pid')
except:
    print('No process with PID {} found'.format(str(pid)))





