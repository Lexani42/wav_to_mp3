from os import listdir
from subprocess import call
from time import sleep
temp = listdir('wavfolder')



def check_unique(x, y):
    """ return unique elements from y list
    """
    temp = []
    for i in y:
        if i not in x and i not in temp:
            temp.append(i)
    return temp



def get_wavs(temp_list):
    """ returns a list only with wav file's names
    """
    temp = []
    for i in temp_list:
        splitted = i.split('.')
        if splitted[-1] == 'wav':
            temp.append(splitted[0])
    return temp



def check_folder(temp):
    """ check if there are new flies in the folder
    """
    now = listdir('wavfolder') # present data state
    if now != temp:
        new_wav_files = get_wavs(check_unique(temp, now))
        temp = now
        for i in new_wav_files:
            convert_to_mp3(i.split('.')[0])
    return temp



def convert_to_mp3(file):
    """ convert wav file to mp3 file and put it into selected folder
        ATTENTION! names such as qwe.rty.wav will be rewritten as qwe.mp3
    """
    call(f'lame --preset studio wavfolder/"{file}.wav" mp3folder/"{file}.mp3"', shell=True)



while True:
    try:
        temp = check_folder(temp)
    except:
        print('smth went wrong')
    sleep(1)