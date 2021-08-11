#! /usr/bin/bash

chmod +x ./dist/def
sudo cp ./dist/def /bin/


#creating directory and file

if [ -d ~/ter_dict ] 
then 
	echo "directory is present no need to creat";
else
	mkdir ~/ter_dict;
	cd ~/ter_dict;
	touch history.csv ;
fi