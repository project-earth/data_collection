import os
import io
import re
import requests



############################### EXCEPTION OBJECT #############################
class ExceptionObj:
    def __init__(self, errCode): self.errCode = errCode



############################### STATUS OBJECT #############################
class DownloadStatus:
    def __init__(self, total=1):
        self.prog = 0
        self.tot = total
        self.complete = False

    def updateProg(self, change):
        self.prog += change
        return(0)

    def updateTotal(self, total):
        self.tot = total
        return(0)

    def completed(self):
        self.complete = True
        return(0)



class ExtractionStatus:
    def __init__(self):
        self.prog = 0
        self.tot = 1
    
    def updateTot(self, total):
        self.tot = total
        return(0)

    def updateProg(self, change=1):
        self.prog += change
        return(0)



############################### MISC #############################
# check whether a folder exists, if not the folder is created.
def check_create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path


def remove_slash(value):
    assert(isinstance(value, str))
    return re.sub('(^\/|\/$)', '', value)


def url_builder(segments):
    assert((isinstance(segments, list) or isinstance(segments, tuple)))
    return "/".join([remove_slash(s) for s in segments])


def threeDigitPad(number):
    number = str(number)
    if len(number) == 1:
        return u'00%s' % number
    elif len(number) == 2:
        return u'0%s' % number
    else:
        return number


def remote_file_exists(url):
    status = requests.head(url).status_code
    if status != 200:
        return(ExceptionObj('File at {0} does not exist on remote server'.format(url)))
    return(0)


def get_remote_file_size(url):
    headers = requests.head(url).headers
    return int(headers['content-length'])


def scene_interpreter(scene):
    return {
        'path': scene[3:6],
        'row': scene[6:9],
        'sat': 'L' + scene[2:3],
        'scene': scene
    }
