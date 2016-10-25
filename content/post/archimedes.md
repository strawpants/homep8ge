---
draft: true
author:
  description: Researches geodesy at the University of Bonn
  email: roelof@wobbly.earth
  github: https://github.com/
  image: /images/WBlogo_64x64.png
  name: Roelof Rietbroek
  twitter: https://twitter.com/
  website: http://wobbly.earth/about
cardheaderimage: /images/iceberg.jpg
cardimageattr: "Image from imaggeo.egu.eu by Steffen Seitz"
cardthumbimage: /images/iceberg.jpg
cardtitlecolor: '#fafafa'
categories:
- post
date: 2016-10-24T09:00:00+02:00
description: "Does sea level change when floating ice melts? Here's what would happen to regional sea level if you would melt the loose hanging chunk of the Larsen C ice shelf." 
images:
- /images/iceberg_og.jpg
layout: single
levels:
- somewhat technical
sitemap:
  changefreq: monthly
  priority: 0.6
tags:
- Archimedes
- "floating ice"
- Antarctica
- "Larsen C"
- "Sea level"
- Salinity
- Temperature
- Density
- "code example"
title: "Guess what: Sea level does rise when you melt floating ice"
tweetshare: "Guess what: Sea level does rise when you melt floating ice"
---

You would suspect that melting a chunk of floating ice would not cause a sea level change, but dissolving a chunk of the Larsen C ice shelf actually changes *regional* sea level by up to a meter. <!--more-->

#### "Remember Arquimedes before being silly"
This was the subject of an email I received last week: 

>Dear Roelof, 

>The melting of the Artic ice sheets contributes ZERO to the sea level rise, simply because they are afloat, its basic hydrostatic!!!

>A basic mistake and a shame to see these words coming from the mouth of a TUDelft graduate.
>
>XXXXX, 

>Naval Architect

>XXX

Initially, I decided to ignore the email because of its tone, and obvious [strawman argument](https://en.wikipedia.org/wiki/Straw_man). But I then reconsidered turning it into a post, since [the Archimedes argument has an interesting twist to it](http://www.skepticalscience.com/Sea-level-rise-due-to-floating-ice.html) when applied to melting ice in sea water. Furthermore, there are obviously still people today, who happily ignore the melting of grounded ice masses, while desperately clinging on the Archimedes bandwagon. So, why not reopen this case and try to quantify what would happen if the loose hanging chunk of the Larsen C ice shelf would go adrift and disintegrate (i.e. melt).

To get an idea of the factors at play here, I repeat my email-reply below.

>Dear XXXXXXX,

>seeing that you took the effort to write me an email, and noticing that the topic obviously got you emotionally involved, I took the liberty to write you a quick response.

>Just to set the record straight, you can not have heard me claiming that floating sea ice is driving  sea level change, so I don't understand where you got that idea.

>Secondly, grounded (not floating) glaciers and ice sheets do contribute to sea level change. Besides the obvious Greenland ice sheet, the Arctic houses several islands which are home to grounded glaciers (e.g. Nova Zembla, Svalbard. etc), you only need to have a look at google earth to spot a few of those.

>Thirdly, and here's some food for thought, melting sea-ice may actually cause (small) changes in sea level.  The salt concentration in ice bergs and sea -ice is less  than that of the sea water which holds it buoyant. So if sea-ice melts in the water , the local salt concentration, and hence the sea water density, decreases. To maintain a constant pressure at the bottom of the ocean, which is a fine assumption when considering the surrounding waters to be unchanged,  one would (regionally) need a higher column of less dense water. The Archimedes argument breaks down there because the density of the water obviously does not remain constant throughout the melting process.  Density changes also occur when the temperature of the sea water changes due to the latent heat needed to convert ice to water, essentially counteracting (some of) the above effect. So regionally, melting of icebergs and sea-ice could in fact cause some sea level change. However, this effect is expected to be smaller than the direct contributions of the grounded ice sources.

>You being a naval architect and former university employee, I trust you to be skeptical enough to reconsider your thoughts.

>Kind regards,

>Roelof Rietbroek

>PS. In the future, please refrain from using patronizing language such as "Remember Arquimedes before being silly", it does not impress me and it degrades an open discussion.


I apologize for the final sneer, a little patronizing by itself, but considering how the correspondence started of, it could have been worse.

#### Grounded versus Floating Ice
{{< figure src="/images/Grounding-line.png" title="A large part of the world's ice sheets are resting on the bedrock, compared to floating ice which either comes from the calving of glaciers or is formed at the surface during cold winter times." attr="Source: antarcticglaciers.org" attrlink="http://www.antarcticglaciers.org/glaciers-and-climate/ice-ocean-interactions/grounding-lines/">}}


There are some things to note here. The first is that sea level rise is for a large part driven by the melting of grounded ice sources (Ice sitting on top of the bedrock, see the left part of the figure above). This post won't go into detail on these grounded ice sheets. Secondly, there is floating ice which either has been calved of a glacier (i.e. ice bergs),  or sea ice may form at the ocean's surface under cold conditions. The folks from the BBC have even filmed this process from underneath the ice, including commentary by David Attenborough's, where the growing sea ice expells a very cold and salty brine, forming a 'Brinicle'.
{{< youtube id="lAupJzH31tc">}}


#### Archimedes Principle with a Twist 
Reversely, when floating ice melts, the opposite effect, a freshening of the water below, takes place. As a first guess, it makes sense to apply the Archimedes principle. The weight of the water displayed by the ice equals the weight of the ice itself. Turning ice in water would therefore only be able to fill up the space left by the submerged part of the ice right? Well yes in terms of weight, this makes perfect sense, but due to the effects above we find that *the density, and thus volume* of the sea water has changed.


#### What happens to sea level if a chunk comes off the Larsen C ice shelf?
To get an impression of how much this could be let's do a back-on-the-envelope computation. For some time now, scientist have looking at a [a crack which has been growing in the Larsen C ice shelf](http://www.jpl.nasa.gov/spaceimages/details.php?id=PIA20894). The part which could potentially break off covers about 6000 km^2, which is about 1/7th of the Netherlands (e.g. [the area of North and South Holland together](http://www.volkskrant.nl/wetenschap/gigantische-ijsvlakte-antarctica-staat-op-breken~a3851188/)). 

{{< figure src="/images/larsenCchunk.png" title="A crack growing in the Larsen C ice sheet may lead to a significant piece breaking off" attr="Source: Project MIDAS" attrlink="http://www.projectmidas.org/blog/a-growing-rift-in-larsen-c">}}

{{< figure src="/images/LarsenCSealevel.png" title="Local Sea level change when a 6000 sqkm floating chunk of the Larsen C ice shelf would be melted in a pool of sea water which is about 33 times the mass of the ice shelf itself" >}}

Geometry and parameters (educated guess) | Larsen C chunk 
---------------:|----
Surface area | 6000 sq. km
Ice Thickness | 200 m 
Total depth of affected water column | 500 m
ice density | 917 kg per cubic m
sea water density | 1027 kg per cubic m
initial temperature of sea water | -2 deg Celcius
initial salt concentration | 34.5 psu (practical salinity units)
salt concentration of ice shelf | 0 psu (assume all originates from calved glaciers)

