#Justpy is created using quaser framework.
import justpy as jp
from pandas.core.dtypes.common import classes
#you can check styles of quaser in google.

def app():
    wp=jp.QuasarPage()
    #text-h1 makes the text large and text-center moves the text to center.
    h1=jp.QDiv(a=wp, text='Analysis of Course Reviews',classes='text-h3 text-center q-pa-md')
    p1=jp.QDiv(a=wp, text='These graphs represent course review analysis')
    return wp

jp.justpy(app)
