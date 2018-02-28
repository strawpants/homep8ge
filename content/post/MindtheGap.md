---
draft: true
title: Mind the GRACE Gap, use Swarm
description: Using Swarm gravity data to fill the GRACE data gap
date: 2018-03-01
layout: single
categories:
    - post
tags:
    - GRACE
    - Swarm
    - gravity
    - Ocean Mass
levels:
    - "general public"
images: 
    - "/images/Mind_the_Gap_Swarm_og.jpg" #specify images which are given to FB and co to add while linking
cardthumbimage: "/images/Mind_the_Gap_Swarm.jpg" #optional: default solid color if unset
cardheaderimage: "/images/Mind_the_Gap_Swarm.jpg" #optional: default solid color if unset set with: hcardbackground: "#263238"
cardtitlecolor: "#fafafa" #optional: can be changed to make text visible over card image
tweetshare: "Mind the gap: how Swarm may help filling the GRACE mission gap"
author:
    name: "Roelof Rietbroek"
    description: "Researches geodesy at the University of Bonn"
    website: "http://wobbly.earth/about"
    email: "roelof@wobbly.earth"
    twitter: "https://twitter.com/"
    github: "https://github.com/"
    image: "/images/WBlogo_64x64.png"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

Around Christmas time last year, a falling star, caused by the reentry of the GRACE-2 satellite vehicle, marked the end of an unprecedented gravity mission. The data coming from the Gravity Recovery and Climate Experiment (GRACE) has yielded many insights and it therefore makes sense to look for alternatives, which can be used to bridge the gap with the GRACE Follow-on mission. A [recent paper by Christina Lück et al.](https://www.solid-earth-discuss.net/se-2017-127/) now shows whether the Swarm mission can help out in filling this gap.
<!--more-->
Christina is a researcher within the DFG funded project ["Consistent Ocean Mass Time Series from LEO Potential Field Missions" (CONTIM)](/project/contim), and her recently published study paves the way for using Swarm as a GRACE-alternative to retrieve large scale ocean bottom pressure variations.   

#### To set the record straight: GRACE beats Swarm hands down in terms of accuracy of the gravity field 
To put this all in perspective first. GRACE relied on a microwave ranging instrument to track the distance between the GRACE-1 and GRACE-2 satellite, which came with an extremely sensitive accuracy of about 5 microns/second. To give you an idea of the sensitivity, **that's about the velocity decrease you experience when you hit a cricket whilst driving in your car on the highway**. 

The [Swarm satellites](http://www.esa.int/Our_Activities/Observing_the_Earth/Swarm/Introducing_Swarm) are not equipped with such ranging instruments, but they do track GPS satellites using geodetic grade GPS receivers. This allows so called kinematic orbits (i.e. purely from geometric techniques), to be computed with about cm accuracy. Both the orbits and the satellite velocity changes are affected by the gravitational pull of the Earth, and therefore contain valuable information of the time varying Earth's gravity field. 
And since the Swarm satellites are still in orbit, trying to compute gravity fields from the orbits, albeit with decreased accuracy, is actually a promising spin-off in addition to its primary mission of measuring the Earth's magnetic field.


####  Mass driven sea level from Swarm data
Ocean mass change is an important contributor to sea level rise, and the corresponding signals are expected to fluctuate on very long spatial wavelengths (e.g. basin scales). And it turns out that it is exactly those large spatial scales where Swarm is sensitive. 

My co-worker, Christina Lück, has been working within the DFG funded CONTIM project, and recently finsihed   those very long have very long spatial scales, e.g. on the scale of the basin, 
{{< figure src="/images/SwarmOceanMass.png" title="Swarm is able to pick up the signals from the changing ocean mass. The force models used for correcting non-conservative forces, play a more important role at the beginning of the time Swarm time series, before the GPS receiver received a firmware update. " attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}

{{< figure src="/images/SwarmABC.png" title="The advantage of using Swarm   is able to pick up the signals from the changing ocean mass. The force models used for correcting non-conservative forces, play a particulalry important role at the beginning of the time Swarm time series. " attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}
**GPS receiver update July 2014**


#### Waiting for GRACE-FO

