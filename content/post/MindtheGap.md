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
    - CONTIM
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
Christina is a researcher within the DFG funded project ["Consistent Ocean Mass Time Series from LEO Potential Field Missions" (CONTIM)](/project/contim). Her recently published study paves the way for using Swarm as a GRACE-alternative to retrieve large scale ocean bottom pressure variations.   

{{< figure src="/images/Christina.jpg" title="Christina Lück is completing her Phd at the Institute of Geodesy and Geoinformation in Bonn on the topic of using gravity fields from Low Earth Orbiters for studying ocean mass signals.">}}

### To set the record straight: GRACE beats Swarm hands down in terms of accuracy of the gravity field 
To put this all in perspective first. GRACE relied on a microwave ranging instrument to track the distance between the GRACE-1 and GRACE-2 satellite, which came with an extremely sensitive accuracy of about 5 microns/second. To give you an idea of the sensitivity, **that's about the velocity decrease you experience when you hit a cricket whilst driving in your car on the highway**. 

{{< figure src="/images/LoLo_andHiLo.svg" title="The GRACE measurement system has, in addition to the Swarm constellation, a sensitive K-band inter-satellite link. Both GRACE and Swarm are sensitive to mass redistribution in the Earth system, in particular its fluid envelope. ">}}

The [Swarm satellites](http://www.esa.int/Our_Activities/Observing_the_Earth/Swarm/Introducing_Swarm) are not equipped with such ranging instruments, but they do track GPS satellites using geodetic grade GPS receivers. This allows so called kinematic orbits (i.e. purely from geometric techniques), to be computed with about cm accuracy. Both the orbits and the satellite velocity changes are affected by the gravitational pull of the Earth, and therefore contain valuable information of the time varying Earth's gravity field. 
And since the Swarm satellites are still in orbit, trying to compute gravity fields from the orbits, albeit with decreased accuracy, is actually a promising spin-off in addition to its primary mission of measuring the Earth's magnetic field.

The performed study exploited the better accuracy of the K-band data, by actually **using GRACE as a testbed to test the Swarm performance against**.


###  Mass driven sea level from Swarm data
Ocean mass change is responsible for about half of the current sea level rise, and the corresponding signals are expected to fluctuate on very long spatial wavelengths (e.g. basin wide). As it turns out,  Swarm is sensitive to exactly those type of signals.
Christina Lück recently finished [a study](https://www.solid-earth-discuss.net/se-2017-127/) which explored the use of Swarm to fill up the current GRACE mission gap.  To this means, Swarm-only solutions are compared with GRACE solutions, in order to assess it's accuracy.

There are several things which should be considered when retrieving gravity fields from kinematic orbits. One particularly important issue is that a correction needs to be applied to the orbits which account for non-gravitational forces such as air-drag (yes, there is still air at those satellite altitudes).

#### Influence of non-conservational forces on gravity estimation
The Swarm satellites are equipped with accelerometers which would be able to provide such orbit corrections. Unfortunately, the data from the Swarm accelerometers contain jumps and strong temperature dependencies, which makes it, at the moment, unsuitable as an orbit correction. Consequently, one has to the option to either don't apply a correction at all, or try to model these non-conservative forces using a models of the thermosphere. The latter approach has turned out to be effective in reducing the errors in the derived gravity field, which are reflected in the ocean mass time series below.  
 
{{< figure src="/images/SwarmOceanMass.png" title="Swarm is able to pick up the signals from the changing ocean mass. The force models used for correcting non-conservative forces, play a more important role at the beginning of the time Swarm time series. iFor comparison, the more accurate GRACE time series can be considered as the 'truth'." attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}

#### The added-value of combining three Swarm satellites
There are three Swarm satellites orbiting the Earth. Swarm-A and B fly at a similar altitude (450km), and Swarm-C has a slightly higher orbit of 550 km, which will cause it to drift relative to the A and B vehicles. Although each satellite can be used individually to retrieve the gravity field, it is much more advantageous to use all three of them in the same batch. The figure below clearly demonstrates that using data from all three Swarm satellites brings the ocean mass curve closer to the GRACE curves.  
{{< figure src="/images/SwarmABC.png" title="The advantage of using Swarm is the ability to pick up the signals from the changing ocean mass. The force models used for correcting non-conservative forces, play a particularly important role at the beginning of the time Swarm time series. " attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}
**GPS receiver update July 2014**

#### Would Swarm be able to see a drop in sea level arising from a La Nina event?
The strong La Nina in 2010 has been shown to be detectable In the 
{{< figure src="/images/SwarmENSO.png" title="Using all three Swarm satellites notably increases the accuracy of the resulting ocean mass time series." attr="Source: Solid Earth" attrlink="https://www.solid-earth-discuss.net/se-2017-127/">}}
#### Ocean mass  trends 
Comparison with GRACE


#### Waiting for GRACE-FO

