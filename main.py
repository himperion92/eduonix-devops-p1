#!/usr/bin/python3
import os
import argparse

from CrontabConfigurer.CrontabConfigurer import CrontabConfigurer

parser = argparse.ArgumentParser(description="Configures the backup of a set of files periodically.")
parser.add_argument("--indir", help="Directory which contains the files whose backup will be performed periodically.")
parser.add_argument("--outdir", help="Directory where the backup of the input files will be stored.")
parser.add_argument("--period", help="Period when the backup will be executed. In crontab format * * * * * (minutes, hour, day of the week, month, day of the month)")
arguments = parser.parse_args()
crontab = CrontabConfigurer()
backup_script_path = os.path.dirname(os.path.abspath(__file__)) + "/system_backup.py"
crontab.add_crontab_job(arguments.period + " " + backup_script_path + " " + arguments.indir + " " + arguments.outdir)
