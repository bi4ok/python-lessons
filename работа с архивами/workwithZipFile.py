from zipfile import ZipFile
import os.path


def fromoutin(arhiv, ras):
    for i in os.listdir(os.getcwd()):
        if i.endswith(str(ras)) is True:
            with ZipFile(str(arhiv), 'w') as tzip:
                tzip.write(i)


fromoutin('1.zip', '.py')