Backup program written in python for linux
Tested in centos version 7
Run as a user who will have write permissions to the target directory to zip, and the destination diectory where the zip will go


This program does the following -
	 - Create a backup directory that will contain the backup zip
	 - Clear out the existing backups in the backup folder up to the max_backups specified parameter
	 - Zip up all files in the specified directory to be backed up, excluding files with extension configured in ext_list
	 - Create a log file to capture the programs progress
	 - When the zip is complete email the email user specified to alert that the backup is complete, and attached the log file 
