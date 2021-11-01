import subprocess as sub
import platform 
import psutil
import time

print(platform.system())
proc = input('Run process: ')
if platform.system() == 'Windows':
    procces_run = sub.Popen([proc]) #, stdout=sub.PIPE, encoding="utf-8")
    p = psutil.Process(procces_run.pid)
    while True:
        time.sleep(1)
        p.cpu_percent()
    # print(sub.run(f'Get-Process -Id ${procces_run.pid}'))
    CPU_time = sub.run(f'typeperf "\{procces_run.pid}\% Processor Time" -si 10 -sc 5', shell=True)
    print(sub.run(f'Get-Process {procces_run})'))
# if __name__ == '__name__':
#     proc = 'Mendeley Desktop'
    