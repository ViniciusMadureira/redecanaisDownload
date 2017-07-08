# -*- coding: utf-8 -*-
__author__ = "Vinícius Silva Madureira Pereira <viniciusmadureira@outlook.com>"
__date__ = "$Jul 7, 2017 9:04:12 PM$"

import re

class ExtractDownloadUrl:

    def __init__(self, html_content):
        self.html_content = html_content

    def get_generic_link(self):
        return re.search(r'(?i)"?http.*server.*(vid=|mp4).*?"', self.html_content).group(0)[1:-1]