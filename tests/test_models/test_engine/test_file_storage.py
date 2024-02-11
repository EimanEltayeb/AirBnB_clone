#!/usr/bin/python3
""" test engine storage"""


import unittest
import models.engine.file_storage


class TestFileStorage(unittest.TestCase):
	"""filestorage test"""

	def test_reload(self):
		"""tests the reload method"""

		with self.assertRaises(FileNotFoundError):
			pass
