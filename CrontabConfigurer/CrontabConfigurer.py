#!/usr/bin/python3
import subprocess
import logging

class CrontabConfigurer:
	"""
	Class which contains methods to configure a crontab job in a linux-based machine
	"""
	
	def __init__(self):
		self._logger = logging.getLogger(__name__)
		
	def add_crontab_job(self, cron_job):
		"""
		This method will add the given contrab job into the existing crontab configuration
		Args:
			-cron_job (str): crontab task to be executed in the following format: * * * * * [cmd], where '*' are minutes, hour, day of the
			                 week, month, day of the month.
		"""
		steps = ['crontab -l > tmp_crontab', 'echo "' + cron_job + '" >> tmp_crontab', 'crontab tmp_crontab', 'rm tmp_crontab']
		self._logger.debug("Cheking target crontab command...")
		if isinstance(cron_job, str):
			self._logger.info("Updating crontab configuration...")
			for cmd_step in steps:
				if subprocess.call(cmd_step, shell = True) != 0:
					raise Exception("Something went wrong when trying to configure new crontab task! Last erroneous command executed: %s", cmd_step)
			self._logger.info("Crontab task successfully updated!")
		else:
			raise TypeError("'cron_job' variable should be an string with format: * * * * * [cmd]," + 
			                " where '*' are minutes, hour, day of the week, month, day of the month. ")
				
