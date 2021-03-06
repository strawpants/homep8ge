---
draft: false
author:
  description: Researches geodesy at the University of Bonn
  email: roelof@wobbly.earth
  github: https://github.com/strawpants
  image: /images/WBlogo_64x64.png
  name: Roelof Rietbroek
  twitter: https://twitter.com/
  website: http://wobbly.earth/about
cardheaderimage: /images/at-the-earths-core.jpg
cardthumbimage: /images/at-the-earths-core.jpg
cardimageattr: "From the movie: At the Earth's core (1976)"
images:
    - :/images/sat-the-earths-core.jpg"
cardtitlecolor: white
date: 2018-10-16
description: "Geocenter motion: A mind-boggling phenomenon"
categories:
    - "post"
tags:
    - "repost"
    - "SPP1257"
    - "Mass transport"
    - "geocenter"
    - "surface loading"
levels:
    - "somewhat technical"
title: "Geocenter motion: A mind-boggling phenomenon"
tweetshare:  "Geocenter motion"
sitemap:
    changefreq: "monthly"
    priority: 0.6
---

Let's face it, understanding the concept of 'geocenter motion' is not for the faint-hearted. On a good day it is only confusing, while on bad days we would rather avoid the subject all together. The story below is meant to clear the fog somewhat for those of you who have more bad days than good days. We additionally provide links to recently calculated geocenter motion time series, for those of you who want to get started with real data. <!--more-->

*Editorial note: This is repost of a  blog entry which originally appeared in 2011 on the website of the DFG priority program "Mass distribution and mass transport in the Earth system". Several colleagues indicated that the website is offline as of October 2018, but that they were still looking for the post. For that reason I'm reposting the original post here. Some minor edits have been made and links to more recent geocenter motion updates are provided. But besides that it reflects the original post.* 


### The 'motion' part
As far as the 'motion' part is considered, we pretty much all agree that motion has a direction, arising from a starting point and an end point. So let's ask ourselves a question: what are the actual starting and endpoints of the 'geocenter motion'? Would you dare to answer this question in a group of highly respected scientific peers? (insert uncomfortable silence here...). Although deceivingly simple, the question is not so easy to answer, but it is the key to understanding the whole concept.

### The 'geocenter' part 
Let's speculate about the endpoint, which we denote by the so-called 'geocenter'. By 'center' we mean the mass center of the 'geo' (Earth) system. This encompasses the solid part of the Earth, the ocean, the atmosphere, ice sheets, water in rivers and lakes, and a whole lot of other stuff we can think of. In literature it is commonly denoted as center of common mass (CM) and it is a natural choice of origin for satellite-based reference systems.

{{< figure src="/images/geo_anim_smll.gif" title="Figure 1. Geocenter motion as induced by a hypothetical (overweight?) cyclist moving over the Earth's surface. The left and right scenarios are exactly the same but seen from a different perspective. In the left plot we observe a movement of the center of common mass (black) as seen from the solid Earth, while the solid part of the Earth moves as seen from a satellite-based reference frame (right).">}}

### What is causing this so-called motion of the geocenter?
Imagine, we move some masses (e.g. water or ice) from point A to B over the Earth's surface. What will happen with the above defined geocenter (CM)? Well pretty much nothing! From the conservation of linear momentum we know that the center of mass must remain stationary (see figure 1 right) in an inertial frame. On the contrary, the solid part of the Earth will move, and actually deforms a little at the same time.
Since we don't usually find ourselves sitting in an inertial frame, the CM will appear to move in our frame of choice (e.g. Figure 1 left). 


### Observer's perspective
As the starting point of the geocenter motion, we have the freedom to choose a convenient origin of our reference frame. Commonly, scientists tend to bolt down their fancy measurement equipment to firm rocks, which are rigidly connected to the Earth's crust. For global comparisons of such measurements a natural choice would be to use a reference system which has its origin in the center of figure (CF) of the Earth. Alternatively, one could use an origin which is the center of mass of the solid Earth (CE). The origins CE and CF slightly differ from each other as the masses in the Earth are not homogeneously distributed.

### Measuring geocenter motion
In order to observe the relative motion of CM-CF we need data which link the solid part of the Earth to  a space-based reference frame. Observed ranges between Earth-fixed permanent GPS stations and GPS satellites, may provide this link. Alternatively (or in combination), we may deduce the geocenter motion by observing the shape changes (deformations) of the solid Earth. Using an elastic model of the Earth we may derive the surface loading which actually caused such deformations. When we additionally apply the conservation of linear momentum, providing us with the link between the solid Earth and space, we can calculate the associated CM-CF shift.

{{< figure src="/images/Surfload_geoc.svg" title="Figure 2. Cartesian components of  the estimated geocenter motion as induced by Hydrology, ice sheet and glacier changes." attr="Data from Rietbroek et al. 2016 (updated)" attrlink="https://wobbly.earth/data/Geocenter_dec2017.tgz">}}

The latter approach has been used in a study together with the use of GRACE gravimetry and bottom pressure variations from the Finite Ocean Sea-Ice model (FESOM) ([Rietbroek et al. 2012](/data/Rietbroek2012_finalMS.pdf)).  Alternatively,  a combination of GRACE and radar altimetry also allows for the resolving of geocenter motion time series.  Time series of the observed geocenter motion can be seen in Fig. 2.


At least for me, it is rather difficult to eyeball the X,Y, Z plot from Fig. 2 and determine where the geocenter offset is actually pointing to. Therefore, a more intuitive plot of the seasonal geocenter motion is shown in Fig. 3. There, we can see that the magnitude of the offset between the CM and CF varies between 2 and 5 mm. The regions which are mostly affected by the geocenter motion can be found on an approximate track crossing Central Asia, Europe, South America and Australia. At the same time the antipode will be equally affected but in the opposite direction.

{{< figure src="/images/geoc_seas_anim_smll.gif" title=" Figure 3. Direction and size of the seasonal (and semi-seasonal) geocenter motion. The colored sphere can be seen as an equivalent mass which induces the observed geocenter motion by means of conservation of linear momentum. Over the season the effect varies between 2 and 5 mm. Areas which are mostly affected lie on the groundtrack of the geocenter motion, such as central Asia, the Amazon region and Australia. Data from Rietbroek et al 2012">}}

### Space-based gravimetry
The Gravity Recovery and Climate Experiment (GRACE) constitutes of 2 satellites which map the time-varying gravity field of the Earth from space. In the satellite frame, the changes in gravity due to geocenter motion are zero. One particularly interesting observable to extract from the GRACE data is surface loading. This is the (surface) density of a thin layer containing Ocean/Atmosphere and hydrosphere, which exerts pressure on the crust of the Earth. Surface loading is also commonly expressed in the height of an equivalent layer of water.

Now here is the problem: In order to calculate surface loading from GRACE we need to change the observer's perspective from the space-based frame to the center of figure frame. This boils down to changing the so-called degree 1 Stokes (Potential) coefficients by external ones. Only then we are allowed to further process the potential coefficients to obtain surface loading. 

In other words, ignoring the geocenter motion in GRACE (cf. observing from the space-based frame) will provide us with surface loading estimates which have no real physical meaning.  In terms of loading, the impact of the geocenter motion is much larger than the actual shift of the CM and CF itself. A geocenter motion shift of 4 mm will cause changes in equivalent water height of around 2 cm.

### References and Further information

* Rietbroek, R., Fritsche, M., Brunnabend, S.E., Daras, I., Kusche, J., Schröter, J., Flechtner, F., Dietrich, R., 2012. Global surface mass from a new combination of GRACE, modelled OBP and reprocessed GPS data. Journal of Geodynamics 59–60, 64–71. https://doi.org/10.1016/j.jog.2011.02.003
* Rietbroek, R., Brunnabend, S.-E., Kusche, J., Schröter, J., Dahle, C., 2016. Revisiting the Contemporary Sea Level Budget on Global and Regional Scales. Proceedings of the National Academy of Sciences 201519132. https://doi.org/10.1073/pnas.1519132113
* Sun, Y., Ditmar, P., Riva, R., 2017. Statistically optimal estimation of degree-1 and C20 coefficients based on GRACE data and an ocean bottom pressure model. Geophysical Journal International.
* Swenson, S., Chambers, D., Wahr, J., 2008. Estimating geocenter variations from a combination of GRACE and ocean model output. J. Geophys. Res. 113. https://doi.org/10.1029/2007JB005338
* [Geocenter motion for separate components (update from Rietbroek et al. 2016)](/data/Geocenter_dec2017.tgz)
* [Geocenter motion estimates generated by Yu (Jade) Sun and colleagues](https://www.tudelft.nl/en/ceg/about-faculty/departments/geoscience-remote-sensing/research/research-themes/gravity/models-data/champgracegoce-gravity-models-data/degree-1-and-c20-coefficients/) 
* [Geocenter motion estimates based on the method of Swenson et al. 2008 (Tellus  website)](https://grace.jpl.nasa.gov/data/get-data/geocenter/)
