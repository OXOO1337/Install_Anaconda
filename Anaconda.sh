#!/bin/bash
# sudo chmod +x Anaconda.sh
##################################
# Debian - ubuntu - kali linux
##################################
#Colors
white="\033[1;37m"
grey="\033[0;37m"
purple="\033[0;35m"
red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
Purple="\033[0;35m"
Cyan="\033[0;36m"
Cafe="\033[0;33m"
Fiuscha="\033[0;35m"
blue="\033[1;34m"
transparent="\e[0m"
# set an infinite loop
while :
do
clear
# display menu
echo -e $transparent"PC Name - $red$(hostname)$transparent"
echo "--------------------"
echo -e "|   "$blue" Anaconda3"$transparent"     |"
echo "--------------------"
echo -e $yellow"["$red"0"$yellow"]"$red" Exit$transparent"
echo -e $red"["$yellow"1"$red"]"$transparent" PC Update"
echo -e $red"["$blue"2"$red"]"$transparent" INSTALL Anaconda3"
echo -e $red"["$yellow"3"$red"]"$transparent" Run Anaconda"
echo -e $red"["$blue"4"$red"]"$transparent" Exit (base)"
echo -e $red"["$yellow"5"$red"]"$transparent" No more (base)"
echo -e $red"["$blue"6"$red"]"$transparent"$red Remove Anaconda3$transparent"
# get-e input from the user
echo -e $blue "Enter your choice $yellow[$red 0 $white-$yellow 6 ] $transparent" $green ; read -p  "Number: " choice
# make decision using case..in..esac
 case $choice in
   #CP Update
1)
sudo apt-get update&&apt-get upgrade -y
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
   #INSTALL Anaconda3
2)
sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 curl -y
cd /tmp && curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh;
bash Anaconda3-2019.10-Linux-x86_64.sh;
source ~/.bashrc;
conda info;
conda update conda;
conda update anaconda;
sudo rm /tmp/Anaconda3-2019.10-Linux-x86_64.sh;
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
   #Run Anaconda
3)
source /home/$USERNAME/anaconda3/bin/activate
anaconda-navigator
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
   #Exit (base)
4)
source deactivate
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
   #No more (base)
5)
conda config --set auto_activate_base False
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
   #Remove Anaconda
6)
sudo rm -rf ~/anaconda3;
sudo rm -rf ~/.condarc ~/.conda ~/.continuum;
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
0)
echo -e $red "Bye ):" $transparent
exit 0
;;
*)
echo -e $red"Error: Invalid option..."$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
esac


done
