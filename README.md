# eduonix-devops-p1
First project for Eduonix Devops E-Degree

This project is meant to configure a linux-based machine crontab daemon in order to perform a periodic backup of a given set of files into a selectable location. All you need to make it work is to execute the "main.py" script with the following arguments:

`main.py --indir [dir with the data to backup] --outdir [dir where the backup will be stored] --period [period in crontab format]`

You can type `main.py --help` in order to get a detailed description of the arguments.
