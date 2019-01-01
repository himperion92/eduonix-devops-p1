#!/usr/bin/python3
import sys

from BackupScheme import BackupScheme

backup = BackupScheme()
backup.perform_backup(sys.argv[1], sys.argv[2])
