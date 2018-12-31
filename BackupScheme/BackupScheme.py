import subprocess
import logging

class BackupScheme:
	"""
	Class which contains methods for performing the backup of a set of files
	"""
	
	def __init__(self):
		self._logger = logging.getLogger(__name__)

	def perform_backup(self, backup_dir, dest_dir)
		"""
		Args:
			-backup_dir (str): directory where the backup should be performed.
			-dest_dir (str): directory where the backup from the input files will be stored.
		"""
		
		self._logger.debug("Checking given paths...")
		if isinstance(backup_dir, str) and isinstance (dest_dir, str):
			cmd = "rsync -av --delete " + backup_dir " " + dest_dir 
			self._logger.debug("Command to be executed: %s", cmd)
		else:
			raise TypeError("Directories shall be passed as string values!")
		self._logger.info("Performing backup...")
		if subprocess.call(cmd) != 0:
			raise Exception("Something went wrong while trying to perform the backup of the files!")
		else:
		self._logger.info("Backup correctly performed!")
