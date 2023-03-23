#定时执行任务命令
import time,os,sched

schedule = sched.scheduler(time.time,time.sleep) # #生成调度器
def command(cmd):
    os.system(cmd)   # 执行命令
    print('任务执行完成！')
def task(cmd,inc=60):
    schedule.enter(inc,0,command,(cmd,))
    schedule.run()  # 运行调试器
task(r"F: && cd F:\program\Python\Python案例集锦\svn\资源包\Code\05\源程序\foo && python main.py",60)
