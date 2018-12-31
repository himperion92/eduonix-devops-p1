import argparse

from BackupScheme import BackupScheme

parser = argparse.ArgumentParser(description="Configures the backup of a set of files periodically.")
parser.add_argument("--indir", help="Directory which contains the files whose backup will be performed periodically.")
parser.add_argument("--outdir", help="Directory where the backup of the input files will be stored.")
parser.add_argument("--period", help="Period when the backup of the given files has to be performed. In crontab format ***** (min, hour, day of the month, month, day of the week)")
arguments = parser.parse_args()
backup = BackupScheme()
backup.perform_backup(arguments.indir, arguments.outdir)
