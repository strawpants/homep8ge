#!/usr/bin/python3
#python script to parse publications from zotero in html for my academic homepage
# aug 2016, Roelof Rietbroek

from pyzotero import zotero
import keyring
import os.path
import shutil
import re
import codecs
import datetime

zoterodatdir='/home/roelof/wolk7/zoteroData/storage'
root='/home/roelof/work2/homep8ge'
library_id='3253202'
library_type='user'
#to put your APIkey in your keyring adapt the following:
#keyring.set_password('Zotero','PyzoteroKey','YOURAPIkey')
api_key=keyring.get_password('Zotero','PyzoteroKey')

htmlout=root+'/layouts/partials/pubsbody.html'
fid=open(htmlout,'wb')
#fid.write(b'<div class="mdl-color-text--grey-700 mdl-card__supporting-text meta">\n<div class="mdl-card__supporting-text" >\n<h4> Peer reviewed </h4>')
fid.write(b'<div class="mdl-card__supporting-text" >\n\t<h4> Peer reviewed </h4>\n')
fid.write(b'</div>\n')

fid.write(b'<div class="mdl-list">\n')
author=b'Rietbroek'
authorsearch=re.compile(author)
div=re.compile(b'div')

zot = zotero.Zotero(library_id, library_type, api_key)
zot.add_parameters(tag='RRpeer',sort='date')
items = zot.everything(zot.top())
tt=0
for item in items:
	#get a parsed entry for each hit 
	htmlentry=zot.item(item['key'],content='bib',style='geophysical-research-letters')[0].encode('utf-8')
	htmlentry=authorsearch.sub(b'<b>'+author+b'</b>',htmlentry)
	htmlentry=div.sub(b'p',htmlentry)
	#fid.write(b'\t<div class="hugo-ref-item">\n')
	fid.write(b'\t<div class="mdl-list__item mdl-color-text--grey-700">\n')
	
	fid.write(b'\t\t<div class="mdl-list-primary-content">\n')
	
	fid.write(b'\t\t\t'+htmlentry+b'\n')
	
	fid.write(b'\t\t</div>\n')
	#find out if there is a free pdf attached which we can provide a link to
	freepdfentry=zot.children(item['key'],tag='freepdf')
	if freepdfentry:
		src=zoterodatdir+'/'+freepdfentry[0]['data']['key']+'/'+freepdfentry[0]['data']['filename']
		destpdf='/data/'+freepdfentry[0]['data']['filename']
		#copy the pdf to the static folder if there does not exist one yet
		if not os.path.isfile(root+'/static'+destpdf):
			shutil.copy2(src,root+'/static'+destpdf)

		#modify the html entry to include the link
		tt+=1
		ttid=('tt'+str(tt)).encode('utf-8')
		fid.write(b'\t\t<div class=mdl-list-secondary-content>\n')
		
		fid.write(b'\t\t\t<a  id='+ttid+b' class="mdl-list__item-secondary-action mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect icon-button" href="'+destpdf.encode('utf-8')+b'" aria-label="Download pdf" data-upgraded="MaterialButton,MaterialRipple"><i class="material-icons_2x icon ion-archive"></i><span class="mdl-button__ripple-container"><span class="mdl-ripple"></span></span>\n')
		fid.write(b'\t\t\t</a>\n')
		
		fid.write(b'\t\t\t<div class="mdl-tooltip mdl-tooltip" for="'+ttid+b'">Download pdf\n')
		fid.write(b'\t\t\t</div>\n')
		
		fid.write(b'\t\t</div>\n')
		#pdflink=b'<div><a id='+ttid+b' class="mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect icon-button" href="'+destpdf.encode('utf-8')+b'" aria-label="Download pdf" data-upgraded=",MaterialButton,MaterialRipple"><i 		class="material-icons_2x icon ion-archive"></i><span class="mdl-button__ripple-container"><span class="mdl-ripple"></span></span></a><div class="mdl-tooltip mdl-tooltip" for="'+ttid+b'">Download pdf</div></div>\n'
		#fid.write(b'\t\t'+pdflink+b'\n</div>\n')	
	
	fid.write(b'\t</div>\n')
#add date tag 
now=datetime.datetime.now()
fid.write(b'<small> Last updated: '+now.strftime("%B %d, %Y").encode('utf-8')+b'</small>\n')
fid.write(b'</div>\n')



fid.close()	

