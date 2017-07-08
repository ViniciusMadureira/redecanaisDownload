# -*- coding: utf-8 -*-
__author__ = "Vinícius Silva Madureira Pereira  <viniciusmadureira@outlook.com>"
__date__ = "$Jul 7, 2017 7:03:47 PM$"

import re
import sys
sys.path.insert(0, 'controller')
from downloadPage import DownloadPage
from downloadFile import DownloadFile
from extractDownloadUrl import ExtractDownloadUrl

if __name__ == "__main__":
    download_page = DownloadPage()
    link = sys.argv[1]
    file_path = sys.argv[2] if str(sys.argv[2]).endswith('/') else sys.argv[2] + '/'    
    file_name = None
    salt = 0    
    while not re.match(r'.*mp4', link):
        html_content = download_page.get_html_content(link, None, {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}, 'post')
        file_name = re.search(r'(?<=\<title\>).*(?=\<\/title\>)', html_content).group(0) if file_name is None else file_name
        link = ExtractDownloadUrl(html_content).get_generic_link()        
        salt += 1
        print('Hop {0}: {1}'.format(salt, link))
    print('Downloading: \"{0}\" to \"{1}\".'.format(file_name, file_path + file_name))
    DownloadFile(link, str(file_path + file_name)).file()