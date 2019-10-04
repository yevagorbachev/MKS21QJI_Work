#Real Actual Ukranians_Yevgeniy Gorbachev, Ivan Galakhov
#SoftDev1 pd1
#K16 -- Oh yes, perhaps I do...
#2019-10-07

from flask import Flask
import os

app = Flask(__name__)

parent = lambda str: str.rfind('/') if str.rfind('/') != -1 else str.rfind('\\') # finds parent directory from string
__ppath__ = __file__[: parent(__file__)] # python file's parent directory

