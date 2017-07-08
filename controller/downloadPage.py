# -*- coding: utf-8 -*-
__author__ = "Vinícius Silva Madureira Pereira <contato@viniciusmadureira.com>"
__date__ = "$Jul 7, 2017 8:37:50 PM$"

import sys
sys.path.insert(0, 'model')
from download import Download

class DownloadPage:
    
    @staticmethod
    def get_html_content(url, data, headers, method):                
        return Download.post(url, data, headers) if str(method).lower() == 'post' else Download.get(url)
