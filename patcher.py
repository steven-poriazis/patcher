import json
import psutil
import os
import time
import urllib2

# read json file
with open("git_config.json", "r") as json_file:
    git_config = json.load(json_file)

if(git_config["install"] == 0):
    current_dir = os.getcwd()
    current_dir = os.path.dirname(os.path.realpath(__file__))
    url = 'https://github.com/git-for-windows/git/releases/download/v2.19.0.windows.1/Git-2.19.0-32-bit.exe' 
    file = urllib2.urlopen(url)
    with open('Git-2.19.0-32-bit.exe', 'wb') as f:
        f.write(file.read())

	# AUTO INSTALL GIT
    os.system('Git-2.19.0-32-bit.exe')
	# AUTO INSTALL GIT

    os.remove('Git-2.19.0-32-bit.exe')
    print("Downloaded and installed git.")
    time.sleep(2)

    # update json file
    git_config["install"] = 1
    with open("git_config.json", "w") as json_file:
        json.dump(git_config, json_file)

    if(git_config["repo_init"] == 0):
        # git configuration
        os.chdir("./")          # change directory to client folder
        os.system('git init')   # create empty repo in client folder
        os.system('git config --global user.name "steven-poriazis"')                    # config git username
        os.system('git config --global user.email steve.poriazis.contact@gmail.com')	# config git email
        os.system('git remote add origin https://github.com/steven-poriazis/dawn-of-heroes_client.git')	   # config git remote
        print("Created empty repo and connected to remote.")	# inform user that repo is ready for update
        time.sleep(2)			# wait
        
        # update json file
        git_config["repo_init"] = 1
        with open("git_config.json", "w") as json_file:
            json.dump(git_config, json_file)

# update client
print("Executing pull request...")
os.chdir('./')
os.system('git pull origin master')
print("Update completed successfully! Press enter to exit...")
raw_input('')

# exit patcher and kill all related processes
PROCNAME_1 = "git.exe"
PROCNAME_2 = "git-remote-https.exe"
for proc in psutil.process_iter():
    if proc.name() == PROCNAME_1 or proc.name() == PROCNAME_2: # check if the process names match
		proc.kill()    # kill patcher-related processes
exit(0)