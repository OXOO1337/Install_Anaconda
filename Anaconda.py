import os
os.system('cls')
# Colors
# Red: \033[1;31m
# Green: \033[1;32m
# Yellow: \033[1;33m
# Blue: \033[1;34m
# Cyan: \033[0;36m
# White: \033[1;37m
# Reset: \u001b[0m
##########################
def Update_Install_Anaconda3():
	while True:
		os.system("clear")
		banner()
		print("""
  \033[1;33m[\033[1;31m0\033[1;33m] \033[1;31mBack\u001b[0m
  \033[1;31m[\033[1;33m1\033[1;31m] \033[1;37mUpdate PC\u001b[0m
  \033[1;31m[\033[1;34m2\033[1;31m] \033[1;37mInstall Anaconda3\u001b[0m
    \033[1;34mEnter your choice  \033[1;33m[ \033[1;31m0 \033[1;37m- \033[1;33m2 ]\u001b[0m
		""")
		menu = input("\033[1;32mNumber:  \u001b[0m")
		if menu == "1":
			os.system("clear")
			os.system("sudo apt-get update")
		elif menu == "2":
			os.system("sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 curl -y")
			os.system("cd /tmp && curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh")
			os.system("cd /tmp && bash Anaconda3-2019.10-Linux-x86_64.sh")
			os.system("source ~/.bashrc")
			os.system("conda info")
			os.system("conda update conda")
			os.system("sudo rm /tmp/Anaconda3-2019.10-Linux-x86_64.sh")
			os.system("conda update anaconda")
		elif menu == "0":
			os.system("clear")
			main()
		else:
			continue
def Run_Anaconda3():
	while True:
		os.system("clear")
		banner()
		print("""
  \033[1;33m[\033[1;31m0\033[1;33m] \033[1;31mBack\u001b[0m
  \033[1;31m[\033[1;33m1\033[1;31m] \033[1;37mRun Anaconda3\u001b[0m
  \033[1;31m[\033[1;34m2\033[1;31m] \033[1;37mExit (base)\u001b[0m
    \033[1;34mEnter your choice  \033[1;33m[ \033[1;31m0 \033[1;37m- \033[1;33m2 ]\u001b[0m
		""")
		menu = input("\033[1;32mNumber:  \u001b[0m")
		if menu == "1":
			os.system("clear")
			os.system("source /home/$USERNAME/anaconda3/bin/activate;anaconda-navigator")
		elif menu == "2":
			os.system("clear")
			os.system("conda config --set auto_activate_base False;")
		elif menu == "0":
                        os.system("clear")
                        main()
		else:
			continue
def Remove_Anaconda3():
			os.system("clear")
			os.system("sudo rm -rf ~/anaconda3")
			os.system("sudo rm -rf ~/.condarc ~/.conda ~/.continuum")
def main():
	while True:
		os.system("clear")
		banner()
		print("""
  \033[1;33m[\033[1;31m0\033[1;33m] \033[1;31mExit\u001b[0m
  \033[1;31m[\033[1;33m1\033[1;31m] \033[1;37mUpdate & Install Anaconda3\u001b[0m
  \033[1;31m[\033[1;34m2\033[1;31m] \033[1;37mRun Anaconda3\u001b[0m
\033[1;31m.:\033[1;33m[\033[1;31m3\033[1;33m]\033[1;31m:. Remove Anaconda3\u001b[0m

    \033[1;34mEnter your choice  \033[1;33m[ \033[1;31m0 \033[1;37m- \033[1;33m3 ]\u001b[0m
		""")
		menu = input("\033[1;32mNumber:  \u001b[0m")
		if menu == "1":
			Update_Install_Anaconda3()
		elif menu == "2":
			Run_Anaconda3()
		elif menu == "3":
			Remove_Anaconda3()
		elif menu == "0":
			os.system("clear")
			print("\033[1;37mThanks for using this tool.\033[1;31m<3 \033[1;34mBye\u001b[0m")
			exit()
		else:
			continue
def banner():
	print("""\033[1;32m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢴⠂⣴⣤⠈⢻⣿⣿⣶⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⢸⣿⠆⣰⠀⠀⠐⠛⠛⠻⣿⣿⣿⣿⣦
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣬⣤⠐⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠻⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣠⣶⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣬⠛⢴⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣼⣿⡆⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣶⡀⣴⣴⣤⣄⣀⢀⢀⣀⣠⣴⣿⣿⣿⣿⠋
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉
⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⣤⣤⠀⠀⠀⠀⣠⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣀⠀⠀⠀⣀⣤⣤⣤⣀⠀⠀⠀⢠⣀⠀⠀⠀⠀⣤⡀⠀⢠⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⢀⣄
⠀⠀⢀⣴⣿⣿⠀⠀⠀⠀⣿⣿⣤⠀⠀⣿⣿⠀⠀⠀⣰⣿⣿⠀⠀⠀⢠⣿⠛⠉⠀⠉⠛⠀⢠⣿⠟⠉⠈⠉⠻⣿⣄⠀⢺⣿⣷⣀⠀⠀⣿⡇⠀⢸⣿⠈⠈⠉⠻⣿⡄⠀⠀⢀⣿⣿⣄
⠀⠀⣴⣿⠀⢻⣿⢀⠀⢀⣿⠀⠛⣿⣤⣿⣿⠀⠀⣰⣿⠁⠹⣿⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⠀⣸⣿⠈⠻⣷⣄⣿⡇⠀⢸⣿⠀⠀⠀⠀⣿⣿⠀⢀⣿⠋⠈⣿⣄
⠀⣴⣿⠛⠻⠻⢻⣿⠀⢀⣿⠀⠀⠀⠛⣿⣿⠀⣰⣿⠻⠻⠛⠻⣿⠀⠈⢿⣷⣤⣀⣤⣶⠀⠈⢿⣷⣤⣀⣤⣶⡿⠁⠀⣸⣿⠀⠀⠈⠻⣿⡇⠀⢸⣿⣄⣀⣤⣾⡿⠁⢀⣿⠛⠻⠛⠛⣿⣄
⠀⠉⠀⠀⠀⠀⠀⠉⠉⠀⠉⠀⠀⠀⠀⠀⠉⠀⠉⠁⠀⠀⠀⠀⠉⠉⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠈⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠉⠉⠀⠀⠀⠀⠈⠉
\u001b[0m""")
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		os.system("clear")
		print("\033[1;37mThanks for using this tool.\033[1;31m<3 \033[1;34mBye\u001b[0m")
