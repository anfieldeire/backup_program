import os
import glob
import zipfile
import logging
import sys
import fnmatch
import time
import datetime
from datetime import date
from datetime import time
from datetime import datetime
import os.path
import smtplib
from pathlib import Path
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import backup_config # configuration file
#

def logging_setup():
    """ Configure logging """
    logging.basicConfig(filename=backup_config.backup_log,
                     level=logging.DEBUG,
                     filemode = 'w',
                     format="%(asctime)s:%(levelname)s:%(message)s")

def checkdir():
    """ Check if the backup dir is present, if not create """ 
    if not os.path.exists(backup_config.backup_dir):
        os.makedirs(backup_config.backup_dir)
        logging.debug("Backup dir has been created {}".format(backup_config.backup_dir))
    else:
        logging.debug("Backup dir exists proceed..")
        

def count_backups():
    """ count backups in the backupdir """
    filecount = 0
    existing_backups = []
    for file in os.listdir(backup_config.backup_dir):
        if fnmatch.fnmatch(file, '*backup*'):
            filecount = filecount + 1
            existing_backups.append(file)
    existing_backups.sort(reverse=True)        
    return(existing_backups)


def delete_extra_backups():
    """ Remove additional backup files beyond the number configured in max backups """
    
    existing_backups = countbackups()
    
    if len(existing_backups) >= backup_config.max_backups:
        for file in existing_backups[backup_config.max_backups-1:]:
            logging.debug("Removing file in dir: {}, file: {}".format(backup_config.backup_dir, file))
            os.remove('{}/{}'.format(backup_config.backup_dir, file))
            print("Removing file: {}".format(file))

def create_zip():
    """ Create the zip file, with the date in the front """
    logging.debug("\n\t\t\t\t ###### ZIP FILE CONTENTS  #######\n")
    backup_config.zip_file_name_abs_path = os.path.join(backup_config.backup_dir, backup_config.zip_file_name_full)
    zip_file_name = zipfile.ZipFile(backup_config.zip_file_name_abs_path, 'w')

    for root, dirs, files in os.walk(backup_config.dir_to_backup):
        zip_file_name.write(root)
        logging.debug("Adding directories: {}".format( root))
        logging.debug("\t Adding subdirs: {}".format( dirs))
        for file in files:
            if not file.endswith(backup_config.ext_list):
                logging.debug("\t \tAdding files: {}".format(file))
                zip_file_name.write(os.path.join(root, file), compress_type=zipfile.ZIP_DEFLATED)
    zip_file_name.close()
    logging.debug("\n\t\t\t\t ######  END OF ZIP FILE CONTENTS ######\n")
    logging.debug("Backup file was created: {}".format(backup_config.zip_file_name_abs_path))
    print("Backup file created")
     

def send_email():

    """ Send an email to the address definied in var email_send with the log file attached """
    filename = backup_config.backup_log
    with open(filename, 'rb') as attachment:
        if backup_config.email_log_file == 'yes':
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename= filename)
            backup_config.msg.attach(part)
            text = backup_config.msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(backup_config.email_user, backup_config.email_pass)
            server.sendmail(backup_config.email_user, backup_config.email_send, text)
            logging.debug("Backup sent to user: {}".format(backup_config.email_send))
            server.quit()
            print("Email sent")
        else:
            logging.debug("Email option not selected")
            print("Confirmation email not selected, no email sent")
    attachment.close()        

if __name__ == '__main__':
    logging_setup()
    checkdir()
    delete_extra_backups()
    create_zip()
    send_email()
    

