import ctypes
import pathlib


class clilre:

    def __init__(self):
        #self.libname = pathlib.Path().absolute() / "liblilre.so"
        self.libname = "/home/pi/Projects/regex/objects/liblilre.so"
        self.c_lib = ctypes.CDLL(self.libname)

    def re_search(self, base, pattern):
        
        wrkbase = ctypes.c_char_p(base.encode('utf-8'))
        wrkpattern = ctypes.c_char_p(pattern.encode('utf-8'))

        check = self.c_lib.re_search(wrkbase,wrkpattern)

        return check

