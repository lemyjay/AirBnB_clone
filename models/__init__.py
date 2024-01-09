#!/usr/bin/python3
"""
models package initializer
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
