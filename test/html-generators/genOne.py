#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#-----------------------------------------------------------------------#
#colour = ["red", "red", "green", "yellow"]

#with open('mypage.html', 'w') as myFile:
    #myFile.write('<html>')
    #myFile.write('<body>ciao sono pieno di entusiasmo')
    #myFile.write('<table>')

    #s = '1234567890'
    #for i in range(0, len(s), 60):
        #myFile.write('<tr><td>%04d</td>' % (i+1));
    #for j, k in enumerate(s[i:i+60]):
        #myFile.write('<td><font style="background-color:%s;">%s<font></td>' % (colour[j %len(colour)], k));


    #myFile.write('</tr>')
    #myFile.write('</table>')
    #myFile.write('</body>')
    #myFile.write('</html>') 
#------------------------------------------------------------------------#
#html_str = """
#<table border=1>
     #<tr>
       #<th>Number</th>
       #<th>Square</th>
     #</tr>
     #<indent>
     #<% for i in range(10): %>
       #<tr>
         #<td><%= i %></td>
         #<td><%= i**2 %></td>
       #</tr>
     #</indent>
#</table>
#"""

#Html_file= open("filename.html","w")
#Html_file.write(html_str)
#Html_file.close()
#--------------------------------------------------------------------------#
'''A simple program to create an html file froma given string,
and call the default web browser to display the file.'''

contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
  <meta content="text/html; charset=ISO-8859-1"
 http-equiv="content-type">
  <title>Hello</title>
</head>
<body>
Hello, World!
</body>
</html>
'''

def main():
    browseLocal(contents)

def strToFile(text, filename):
    """Write a file with the given name and the given text."""
    output = open(filename,"w")
    output.write(text)
    output.close()

def browseLocal(webpageText, filename='tempBrowseLocal.html'):
    '''Start your webbrowser on a local file containing the text
    with given filename.'''
    import webbrowser, os.path
    strToFile(webpageText, filename)
    webbrowser.open("file:///" + os.path.abspath(filename)) #elaborated for Mac

main()
#-----------------------------------------------------------------------------#
