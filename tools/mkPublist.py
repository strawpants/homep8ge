#!/usr/bin/python3
#python script to parse publications from zotero in html for my academic homepage
# the produced html (written to stdout) is intended to be used as a partial layout for the hugo generated webpage
# aug 2016, Roelof Rietbroek
# This script is called in the following way:
# mkPubList.py STORAGESUBDIROFZOTERO ZOTEROUSERID AUTHORNAMETOHIGHLIGHT 'SECTIONTITLE;ZOTEROTAG' 'SECTIONTITLE2;ZOTEROTAG2' ..


from pyzotero import zotero
import keyring
import os.path
import shutil
import re
import codecs
import datetime
import sys

#global counter for tooltip references
tt=0

#def print_bibitem(item,zotinstance,fid,style,authorre,divre,doire):
        

def main(args):
    #get some variables from command line arguments (first argumetn is root directory of the zotero storage
    zoterodatdir=args[1]
    library_id=args[2]
    authorhighlight=args[3]
    
    #get the to be parsed sections with their tags (format of the  argument is: sectiontitle;zoterotag)
    sections=args[4:]
    library_type='user'
    

    #to put your APIkey in your keyring adapt the following:
    #keyring.set_password('Zotero','PyzoteroKey','YOURAPIkey')
    api_key=keyring.get_password('Zotero','PyzoteroKey')
   
   
    #get an instance of the zotero communicator
    zot = zotero.Zotero(library_id, library_type, api_key)
    #print to stdout
    fid=sys.stdout.buffer

#loop over the requested sections
    for sec in sections:
        tmp=str(sec).split(';')
        print_bibitems(fid,zot,zoterodatdir,authorhighlight,tmp[1],tmp[0])

            
    #add modification tag with date 
    now=datetime.datetime.now()
    fid.write(b'<div class="mdl-card__supporting-text"><small> Bibliography generated from zotero by <a href="https://github.com/strawpants/homep8ge/blob/master/tools/mkPublist.py"> mkPublist.py </a> on '+now.strftime("%b %d, %Y").encode('utf-8')+b'</small>\n</div>\n')
    


 
    
    
def print_bibitems(fid,zot,datadir,author,tag,name):
    citestyle='geophysical-research-letters'
    zot.add_parameters(tag=tag,sort='date')
    fid.write(b'<div class="mdl-card__supporting-text" >\n\t<h4>'+str(name).encode('utf-8')+b'</h4>\n</div>\n')
    fid.write(b'<div class="mdl-list">\n')
    items = zot.everything(zot.top())
    global tt;
    for item in items:
    #get a parsed entry for each hit 
            htmlentry=zot.item(item['key'],content='bib',style=citestyle)[0].encode('utf-8')
            #highlight author
            htmlentry=re.sub(author.encode('utf-8'),b'<b>'+author.encode('utf-8')+b'</b>',htmlentry)
           
            #replace doi by a highlighted link:
            #htmlentry=re.sub(b'doi:(.+)\.<\/div>',b'<a href="http://dx.doi.org/\\1">doi:\\1.</a></div>',htmlentry)
            htmlentry=re.sub(b'https:\/\/doi.org\/(.+)<\/div>',b'<a href="https://doi.org/\\1">doi:\\1.</a></div>',htmlentry)
           
            #also turn "Retrieved from entries in highlighted links"
            htmlentry=re.sub(b'Retrieved from (.+)<\/div>',b'<a href="\\1">Repository link.</a></div>',htmlentry)


            htmlentry=re.sub(b'div',b'p',htmlentry)
            #fid.write(b'\t<div class="hugo-ref-item">\n')
            fid.write(b'\t<div class="mdl-list__item mdl-color-text--grey-700">\n')
            
            fid.write(b'\t\t<div class="mdl-list-primary-content">\n')
            
            fid.write(b'\t\t\t'+htmlentry+b'\n')
            
            fid.write(b'\t\t</div>\n')
            #find out if there is a free pdf attached which we can provide a link to
            freepdfentry=zot.children(item['key'],tag='freepdf')
            if freepdfentry:
                    src=datadir+'/'+freepdfentry[0]['data']['key']+'/'+freepdfentry[0]['data']['filename']
                    destpdf='/data/'+freepdfentry[0]['data']['filename']
                    #copy the pdf to the static folder if there does not exist one yet
                    if not os.path.isfile('static'+destpdf):
                            shutil.copy2(src,'static'+destpdf)

                    #modify the html entry to include the link
                    tt+=1
                    ttid=('tt'+str(tt)).encode('utf-8')
                    fid.write(b'\t\t<div class=mdl-list-secondary-content>\n')
                    
                    fid.write(b'\t\t\t<a  id='+ttid+b' class="mdl-list__item-secondary-action mdl-button mdl-button--colored mdl-js-button mdl-js-ripple-effect icon-button" href="'+destpdf.encode('utf-8')+b'" aria-label="Download pdf" data-upgraded="MaterialButton,MaterialRipple"><i class="material-icons_2x icon ion-archive"></i><span class="mdl-button__ripple-container"><span class="mdl-ripple"></span></span>\n')
                    fid.write(b'\t\t\t</a>\n')
                    
                    fid.write(b'\t\t\t<div class="mdl-tooltip" for="'+ttid+b'">Download pdf\n')
                    fid.write(b'\t\t\t</div>\n')
                    
                    fid.write(b'\t\t</div>\n')
            
            fid.write(b'\t</div>\n')
    fid.write(b'</div>\n')    


if __name__ == "__main__":
    main(sys.argv)
