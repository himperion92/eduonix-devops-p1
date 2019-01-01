# eduonix-devops-p1
## First project for Eduonix Devops E-Degree

This project is meant to configure a linux-based machine crontab daemon in order to perform a periodic backup of a given set of files into a selectable location. All you need to make it work is to execute the "main.py" script with the following arguments:

`python3 main.py --indir [dir with the data to backup] --outdir [dir where the backup will be stored] --period [period in crontab format]`

You can type `main.py --help` in order to get a detailed description of the arguments.

*Example:* `python3 main.py --indir /home/adam/workspace/project1 --outdir /media/externalDrive1 --period 00 12 * * *

*In the example mentioned above, the script would permanently configure crontab to perform a backup of all the files contained in /home/adam/workspace/project1 directory into the /media/externalDrive1 location. This operation would be performed each day at 12:00 pm*


