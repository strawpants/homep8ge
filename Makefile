#Makefile to build the website using hugo
all:build

build:
	git checkout master
	hugo -t HugoMDL
	
publish: build
	@echo 'Publishing website to http://strawpants.github.io'
#	git add public
#	git commit -m "Publish website"
	git subtree push --prefix=public publish master
show:
	@echo 'running test server, visit http://localhost:1313 to preview the page'
	hugo server -F -D --baseURL public/

savedraft:
	@echo saving current branch to git remote 'draft'
	git push draft HEAD
#make an automated publication list
pubs:
	tools/mkPublist.py /home/roelof/hugedata/zoteroData/storage 3253202 Rietbroek 'Theses;RRthesis' 'Peer Reviewed Articles;RRpeer'  > layouts/partials/pubsbody.html

clean:
	cd public; rm -rf 404.html  about  categories  css data favicon.png  fonts  images  index.html  index.xml  js  post  project  sitemap.xml  tags publications
