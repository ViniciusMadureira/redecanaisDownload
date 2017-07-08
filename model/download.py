# -*- coding: utf-8 -*-
__author__ = "Vinícius Silva Madureira Pereira <viniciusmadureira@outlook.com>"
__date__ = "$Jul 7, 2017 7:14:12 PM$"

import urllib.request

class Download:

    header = None

    @staticmethod
    def get(url):
        request = urllib.request.Request(str(url))
        response = urllib.request.urlopen(request)
        return response.read().decode("utf-8")

    @staticmethod
    def post(url, data, headers):
        request = urllib.request.Request(str(url), data, headers)
        response = urllib.request.urlopen(request)
        return response.read().decode("utf-8")

    @staticmethod
    def file(url, file_name):
        urllib.request.urlretrieve(url, file_name)
