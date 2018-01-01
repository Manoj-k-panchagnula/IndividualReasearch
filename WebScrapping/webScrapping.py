'''
Created on May 10, 2017

@author: Manoj Kumar
'''
import urllib
from BeautifulSoup import *
import time
import urlparse

'''Reading the main page and finding the different nodes in them'''
url = 'https://csn.cancer.org/forum'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
count = 0
anchorTags = []
nodeTags = []
BreastCancerNodes =[]


# Retrieve all of the anchor tags
tags = soup('a')
print 'Searching for Breast Cancer files'
for tag in tags:
    num = tag.get('href')
    anchorTags.append(num)
for item in anchorTags:
    if item == '/forum/127':
        print 'Breast Cancer file found'
        url = urlparse.urljoin(url, item)


#Retrieving all the nodes
print "Parsing the Breast cancer folder "
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
nodes = soup('a')

for tag in nodes:
    num = tag.get('href')
    nums = urlparse.urljoin(url, num)
    nodeTags.append(nums)
print "Completed Parsing"

'''Parsing the nodes and extracting the user_id and his/her comments from the node'''
print "Parsing the nodes"
for item in nodeTags:
    if item.startswith("https://csn.cancer.org/node"):
        BreastCancerNodes.append(item)
for each_node in BreastCancerNodes:
    authornames = []
    content_text = []
    nodeNum = each_node[-6:]
    html = urllib.urlopen(each_node)
    soup = BeautifulSoup(html)
    anchorData = soup.findAll("div",{"class":"clearfix"})
    
    '''Finding the author, user_id and their comments'''
    for tag_data in anchorData:
        author_name = tag_data.findAll("div",{"class":"author"})
        author_text = tag_data.findAll("div",{"class":"field-item even"})
        
    #Extracting the author or the user_id    
    for author in author_name:
        authors = author.findAll("span",{"class":"username"})
        authornames.append(authors[0].text)
    
    #extracting the comments 
    for content in author_text:
        content = content.text
        content_text.append(content)
     
    
    '''Writing the extracted data to a text file with user_id on the top and their comments below
    Note: Since it is written into a text file all the odd numbered lines are user_ids and their comments are in even numbered line
    if you open the file in a text editor we can find the line numbers easily(Notepad++ recommended)
    The two lists authornames and content_text always have the user_ids and their comments respectively 
     '''   
    i = 1
    j = 0
    m = 0
    f = open('node'+nodeNum+".txt",'w')
    while (i<44):
        f.write(authornames[j].encode('utf-8')+"\n"+content_text[m].encode('utf-8')+"\n")
        i+=1
        j+=1
        m+=1
    f.close()
    
    #Timer function
    print 'PLEASE WAIT FOR A COUPLE OF MINUTES'
    time.sleep(600)
    print 'Extracting again'
    
