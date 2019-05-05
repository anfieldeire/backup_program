Backup program written in python for linux

Tested in centos version 7

Prerequisites: 
	- Run as user with permissions to both the folder to zip and the destination directory
	- The variables are contained in backup_config
	- Configure the email account, and the user to send to, in backup_config

This program does the following -

	 - Create a backup directory that will contain the backup zip
	 - Clear out the existing backups in the backup folder up to the max_backups specified parameter (keeps the newest files)
	 - Zip up all files in the specified directory to be backed up, excluding files with extension configured in ext_list 
	 - Create a log file to capture the programs progress
	 - When the zip is complete email the email user specified to alert that the backup is complete, and attach the log file 
