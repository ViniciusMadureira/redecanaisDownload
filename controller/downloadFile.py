# -*- coding: utf-8 -*-
__author__ = "Vinícius Silva Madureira Pereira <viniciusmadureira@outlook.com>"
__date__ = "$Jul 7, 2017 10:12:11 PM$"

import sys
sys.path.insert(0, '../model')
from download import Download

class DownloadFile:

    def __init__(self, url, file_name):
        self.url = url
        self.file_name = file_name

    def file(self):
        Download.file(self.url, self.file_name)