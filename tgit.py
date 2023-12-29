import os,getpass
USER=getpass.getuser()
file="C:\\winTest\\test.py"
def getToStarttup(filePath=file):
    bat_path=r"C:\Users\Nikita\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
    with open(bat_path+'\\'+'test.bat','w+') as bat_file:
        bat_file.write(r'start "" %s' % filePath)
getToStarttup()
print("dsfdfs")
input()