#Makefile to build the website using hugo
all:build

build:
	hugo -t HugoMDL
	
publish:
	@echo 'Publishing website to http://strawpants.github.io'
	#git subtree push --prefix=public publish master
show:
	@echo 'running test server, visit http://localhost:1313 to preview the page'
	hugo server --baseURL public/
#make an automated publication list
pubs:
	tools/mkPublist.py /home/roelof/wolk7/zoteroData/storage 3253202 Rietbroek 'Theses;RRthesis' 'Peer Reviewed Articles;RRpeer'  > layouts/partials/pubsbody.html

clean:
	cd public; rm -rf 404.html  about  categories  css  favicon.png  fonts  images  index.html  index.xml  js  post  project  sitemap.xml  tags publications
