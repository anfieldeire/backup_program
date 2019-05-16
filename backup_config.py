

# General variables
dir_to_backup = '/home/admin/python'
backup_dir = '/tmp/backupdir/'
backup_log = '/tmp/backuplog.log'
max_backups = 3
backup_string = 'backup_dir + *backup*.zip'
#gh


# File extensions to exclude from backupzip
ext_list = ('.txt','.jpg', '.py','.pyc', '.rpm')

# Dates
todays_date = date.today()
current_time = datetime.time(datetime.now())

# zip file info
zip_name = 'backup.zip'
zip_file_name_full  = ("{}_{}_{}".format(todays_date, current_time, zip_name))
zip_file_name_abs_path = os.path.join(backup_dir, zip_file_name_full)

# Delete previous backup zips from backup dir
clear_backups = 'yes'

# Email variables
email_user = 'email_user'
email_send = 'email_send'
email_pass = 'emal_pass'
subject = 'Backup Completed'
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject
body = 'See attached log file for details'
msg.attach(MIMEText(body, 'plain'))
email_log_file = 'yes' 
# End email variables
