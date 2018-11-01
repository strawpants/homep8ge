---
title: "Privacy Policy"
layout: single
description: "Describes the privacy policy for the wobbly.earth website"
date: "2018-05-24"
cardthumbimage: "/images/default.jpg" #optional: default solid color if unset
cardheaderimage: "/images/default.jpg" #optional: default solid color if unset
cardbackground: "#263238" #optional: card background color; only shows when no image specified
cardtitlecolor: "#fafafa" #optional: can be changed to make text visible over card image
---
###  Your data and wobbly.earth
Wobbly.earth is a static site which is hosted on github servers in the United States of America. The static aspect of the site means that there is no backend linked to this website where I store your data. Which means that I cannot provide you with a copy of your data since I have none in my possession. 

Nevertheless, when using this websites connections with other websites, not under my control, may be established. When your browser makes a connection to another webserver, potentially personal data, such as cookies and IP addresses, may be shared. Below I'll explain what connections may be established and how this complies with the [General Data Protection Regulation](https://www.eugdpr.org/).

### Google analytics
This website uses google analytics, so (anonymized IP) information is send to the google servers, which provides me with info how well this site is visited. You can opt out for being tracked in general by google analytics by [installing a browser addon](https://support.google.com/analytics/answer/181881?hl=en)

### Embedded content and sharing buttons
You may encounter embedded youtube videos on posts. Your details will not be shared with the youtube servers **unless** you decide to click on the content.

Furthermore, if you see an embedded tweet on wobbly.earth a connection with twitter servers has been made, and cookies may possibly be read. You may consult [twitter's GDPR policy](https://gdpr.twitter.com) to see how twitter complies with your rights.

You may see some share buttons for twitter, facebook on the website. Note that I've implemented these such that they will only establish contact with the sharing services when you decide to **click** on those. 

### Technical implmentations using the gohugo static site generator
Technically, how this static website implements the GDPR compliance can be read [here](https://gohugo.io/about/hugo-and-gdpr/). For this site the following settings are made:
```
privacy:
    googleAnalytics:
        anonymizeIP: true
        disable: false
        respectDoNotTrack: true
        useSessionStorage: true
    twitter:
        disable: false
        enableDNT: true
        simple: false
    youtube:
        disable: false
        privacyEnhanced: true
```

####  A note on the social sharing buttons
The social sharing buttons (e.g. share on twitter, facebook etc.) are implemented in such a way that you only contact the respective service providers when you actually decide to share (i.e. click) the content. A consequence of this is that the buttons do not provide any information on the number of shares/likes, but I think that is a small price to pay for your privacy.

1st November 2018
