#!/usr/bin/python3
""" models/__init__.py"""


import engine.file_storage


storage = FileStorage()
engine.file_storage.reload(storage)
