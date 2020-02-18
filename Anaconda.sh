#!/bin/bash
# sudo chmod +x Anaconda.sh
##################################
# source .bashrc
# anaconda-navigator
# source deactivate
# __________________________________
# !/bin/bash
# source /home/$USERNAME/anaconda3/bin/activate
# anaconda-navigator
# ___________________________________
# conda config --set auto_activate_base False
#####################################
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
echo -e "|" $white"INSTALL"$blue" Anaconda"$transparent" |"
echo "--------------------"
echo -e $yellow"["$red"0"$yellow"]"$red" Exit"
echo -e $red"["$yellow"1"$red"]"$transparent" Update"
echo -e $red"["$blue"2"$red"]"$transparent" INSTALL Anaconda"
echo -e $red"["$yellow"3"$red"]"$transparent" run Anaconda"
echo -e $red"["$blue"4"$red"]"$transparent" No more (base)"
echo -e $red"["$yellow"5"$red"]"$transparent" source deactivate"
# get-e input from the user
echo -e $blue "Enter your choice $yellow[$red 0 $white-$yellow 4 ] $transparent" $green ; read -p  "Number: " choice
# make decision using case..in..esac
 case $choice in
1)
sudo apt-get update&&apt-get upgrade -y
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
2)
sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6 curl -y
cd /tmp && curl -O https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh;
bash ~/tmp/Anaconda3-2019.10-Linux-x86_64.sh;
source ~/.bashrc;
conda info;
conda update conda;
conda update anaconda;
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
3)
source /home/$USERNAME/anaconda3/bin/activate
anaconda-navigator
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
4)
conda config --set auto_activate_base False
echo -e $yellow"Done"$transparent
read -p "Press [Enter] key to continue..."
readEnterKey
;;
5)
source deactivate
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
