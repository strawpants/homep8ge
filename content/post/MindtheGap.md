---
draft: false
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
    - CONTIM
levels:
    - "undergraduate"
images: 
    - "/images/Mind_the_Gap_Swarm_og.jpg" #specify images which are given to FB and co to add while linking
cardthumbimage: "/images/Mind_the_Gap_Swarm.jpg" #optional: default solid color if unset
cardheaderimage: "/images/Mind_the_Gap_Swarm.jpg" #optional: default solid color if unset set with: hcardbackground: "#263238"
cardtitlecolor: "#fafafa" #optional: can be changed to make text visible over card image
tweetshare: "Mind the gap: how Swarm can help filling the GRACE mission gap"
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

Around Christmas time last year, a falling star, caused by the reentry of the GRACE-2 satellite vehicle, marked the end of an unprecedented gravity mission. It therefore makes sense to find alternatives for the Gravity Recovery and Climate Experiment (GRACE), which can be used to bridge the gap with the GRACE Follow-on mission. A [recent paper by Christina Lück et al.](https://www.solid-earth.net/9/323/2018/se-9-323-2018.html/) now shows whether the Swarm mission can help out in filling this gap.
<!--more-->

Christina is a researcher within the DFG funded project ["Consistent Ocean Mass Time Series from LEO Potential Field Missions" (CONTIM)](/project/contim). Her recently published study paves the way for using Swarm as a GRACE-alternative to retrieve large scale ocean bottom pressure variations.   

{{< figure src="/images/Christina.jpg" title="Christina Lück is completing her Phd at the Institute of Geodesy and Geoinformation in Bonn on the topic of using gravity fields from Low Earth Orbiters for studying ocean mass signals.">}}

### To set the record straight: GRACE beats Swarm hands down in terms of accuracy of the gravity field 
To put this all in perspective first. GRACE relied on a microwave ranging instrument to track the distance between the GRACE-1 and GRACE-2 satellite, which came with an extremely sensitive accuracy of about 5 microns/second. To give you an idea of the sensitivity, **that's about the velocity decrease you experience when you hit a cricket whilst driving your car on the highway**. 

{{< figure src="/images/LoLo_andHiLo.svg" title="The GRACE measurement system has, in addition to the Swarm constellation, a sensitive K-band inter-satellite link. Both GRACE and Swarm orbits are affected by mass redistribution in the Earth system, with its fluid envelope varying strongest over time. ">}}

The [Swarm satellites](http://www.esa.int/Our_Activities/Observing_the_Earth/Swarm/Introducing_Swarm) are not equipped with such ranging instruments, but they do track GPS satellites using geodetic grade GPS receivers. This allows so called kinematic orbits (i.e. purely from geometric techniques), to be computed with a few cm accuracy. Both the orbits and the satellite velocity changes are affected by the gravitational pull of the Earth, and therefore contain valuable information of the time varying Earth's gravity field. 
And since the Swarm satellites are still in orbit, trying to compute gravity fields from the orbits, albeit with decreased accuracy, is actually a promising spin-off in addition to its primary mission of measuring the Earth's magnetic field.

The study by Christina Lück exploited the better accuracy of the K-band data, by **using GRACE as a testbed to test the Swarm performance against**.


###  Mass driven sea level from Swarm data
Ocean mass change is responsible for about half of the current sea level rise (~3 mm/yr), and the corresponding signals are expected to fluctuate on very long spatial wavelengths (e.g. basin wide scales). As it turns out,  Swarm is sensitive to exactly those type of signals.

There are several things which should be considered when retrieving gravity fields from kinematic orbits. One particularly important issue is that a correction needs to be applied to the orbits which account for non-gravitational forces such as air-drag (yes, there is still air at those satellite altitudes).

### Air drag on satellites affect the gravity estimation
The Swarm satellites are equipped with accelerometers which would be able to provide corrections for non-gravitational forces. Unfortunately, the data from the Swarm accelerometers contain jumps and strong temperature dependencies, which makes it, at the moment, unsuitable as an orbit correction. Consequently, one has the option to either don't apply a correction at all, or try to model these non-conservative forces using models of the thermosphere. The latter approach has turned out to be effective in reducing the errors in the derived gravity field, which are reflected in the ocean mass time series below.  
 
{{< figure src="/images/SwarmOceanMass.png" title="Swarm is able to pick up the signals from the changing ocean mass. The force models used for correcting non-conservative forces, play a more important role at the beginning of the time Swarm time series. For comparison, the more accurate GRACE time series can be considered as the 'truth'." attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}

### The added-value of combining three Swarm satellites
There are three Swarm satellites orbiting the Earth. Swarm-A and C fly at a similar altitude (450km), and Swarm-B has a slightly higher orbit of 515 km, which will cause it to drift relative to the A and B vehicles. Although each satellite can be used individually to retrieve the gravity field, it is much more advantageous to use all three of them in the same batch. The figure below clearly demonstrates that using data from all three Swarm satellites brings the ocean mass curve closer to the GRACE curves.  
{{< figure src="/images/SwarmABC.png" title="The three Swarm satellites (A,B and C) not only provide more observations, they also sample the Earth's gravity field more uniformly. The manifests itself in an increased accuracy of the combined solution." attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}

### Would Swarm be able to see a drop in sea level arising from a La Nina event?
The strong 2010-2011 [La Nina caused a temporary drop in sea level which has been detected with GRACE data](http://onlinelibrary.wiley.com/doi/10.1029/2012GL053055/full). So would such an event be detectable when we had Swarm data in that period? A La Nina of that magnitude did not occur during the Swarm mission time, but we may try to see if the accuracy of Swarm would be sufficiently high for detection. By comparing the Swarm derived ocean mass curve with the time series of GRACE an estimate of the ocean mass error can be made. The resulting error is indeed small enough such that the expected sea level drop would be detectable by Swarm.
{{< figure src="/images/SwarmENSO.png" title="Using all three Swarm satellites notably increases the accuracy of the resulting ocean mass time series." attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}

### Ocean mass  trends 
The time span where Swarm data is available is still relatively small such that trends will be affected by interannual variability. The comparison with GRACE nevertheless shows that Swarm solutions have trends similar (3.3 mm/yr) to GRACE (3.5 mm/yr), which puts more confidence in using Swarm as gap filler substitute.

### Waiting for GRACE follow on
For the time being, Swarm may therefore be a potential candidate to use until the GRACE-FO (Follow-on) mission is started (anticipated launch is end of April 2018). And it may serve as useful resource for validating the initial gravity field solutions of the new mission. 

{{< figure src="/images/GRACE-FO.jpg" title="GRACE Follow on satellite vehicles in the Airbus production facility." attr="Source: GFZ Potsdam" attrlink="https://www.gfz-potsdam.de/en/media-and-communication/news/details/article/grace-fo-satellites-on-their-way-to-the-launch-pad/">}}
