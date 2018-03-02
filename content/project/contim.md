---
author:
  description: Geodetic researcher at the university of Bonn
  email: roelof@wobbly.earth
  github: https://github.com/strawpants
  image: /images/WBlogo_64x64.png
  name: Roelof Rietbroek
  twitter: https://twitter.com/r_rietje
  website: http://wobbly.earth/about
cardbackground: '#000000'
cardheaderimage: /images/Contim_card.png
cardthumbimage: /images/Contim_card.png
cardtitlecolor: white #optional: can be changed to make text visible over card image
categories:
- project
- research
date: 2018-03-01
tags:
- Ocean mass
- Sea level
- Low Earth Orbiters
- Orbit Determination
- CONTIM
title: Consistent Ocean Mass Time Series from LEO Potential Field Missions (CONTIM)
web: http://www.spp-dynamicearth.de/projects/gravity-field/
Description: Consistent Ocean Mass Time Series from LEO Potential Field Missions (CONTIM)
tweetshare: Consistent Ocean Mass Time from LEO Potential Field Missions
---

The DFG funded project CONTIM (Consistent Ocean Mass Time Series from LEO Potential Field Missions), is part of the Priority Program [**Dynamic Earth**](http://www.spp-dynamicearth.de), and started in 2015 (initially for 3 years). It's primary goal is to estimate and study ocean mass variations using numerical ocean modelling, precise orbit determination of low earth orbiters (LEO's), and data combination approaches. The project is expected to yield results which are highly relevant for closing the sea level budget, indirectly providing constraints on the ocean warming and the related energy budget of the Earth. Three institutes are direclty involved in the project: Institut für Erdmessung (IfE) Leibniz Universität Hannover, Institut für Geodäsie und Geoinformationi (IGG) in Bonn, and the Alfred Wegener Institut (AWI) in Bremerhaven. 

{{< figure src="/images/CONTIMTeamBanner.jpg" title="Team members of the CONTIM team. From left to right: Le Ren, Steffen Schön, Christina Lück, Alexey Androsov, Sergey Danilov, Jens Schröter, Roelof Rietbroek, Jürgen Kusche">}}

### Global Ocean mass change
The terrestrial water cycle is continuously causing water exchange between the continents and ocean. Melting of the ice sheets shows, besides seasonal variations, the steady melting of the grounded ice sheets, cause a sea level rise due to to the increase of mass of the oceans. Furthermore, changes in precipitation and evaporation patterns, anthropogenic groundwater pumping, irrigation and dam building, all cause fluctuations and long term changes of sea level.

### Regional ocean mass fluctuations 
Although the global mean ocean change is an important climate indicator, internal redistribution of mass is happening on various time scales as well. At the highest frequencies, wind exerts stress on the surface of the ocean which causes water to slosh from one part of the ocean to the other. On longer time scales, density variations, arising from heating and cooling of the ocean water and the mixing of waters with different salt concentration, will induce currents which subsequently transport mass from one region of the ocean to the other. Within CONTIM, ocean bottom pressure variations and density driven sea level changes (steric sea level) are simulated with the [FESOM model](http://www.fesom.de). The model results are compared with in situ ocean bottom pressure recorders, and are used to study the ocean dynamics at different time scales and spatial scales. Furthermore, the model output is used to construct parameterizations for ocean bottom pressure and steric sea level changes, which are needed in the data combination process.

{{< figure src="/images/FESOMOBP.png" title="Standard deviations of monthly modelled ocean bottom pressure (FESOM model). Ocean bottom pressure fluctuations are responsible for a large part of the sea level fluctuations in the continental shelf regions and the Southern Ocean." attr="AWI (Alexey Androsov)">}}

### Ocean mass redistribution and ionospheric fluctuations are visible in the orbits of Low Earth Orbiters (LEO)
The time variable changes in the ocean mass will induce anomalies in the gravity field of the Earth. This will cause satellites, in particular those which are flying at low altitudes, to be affected by different gravity forces. The corresponding orbit changes will therefore contain information on the ocean mass provided they are measured with a high enough accuracy.

To avoid contamination by force models, a purely kinematic orbit derived from GNSS (e.g. GPS) tracking of the satellites provide a truly independent observation of the Earth's gravity field.

Interestingly, since the GNSS signals will travel through the Earth's ionosphere, they will be sensitive to the fluctuating electron content in it. The activity in the ionosphere, is therefore related to the geomagnetic field and solar activity. For example, the GNSS signals clearly show anomalies when passing over the magnetic equator. A close cooperation with magnetic field experts available within the dynamic Earth program, thus opens up interesting possiblities to observe such ionospheric fluctuations and potentially improve the accuracy of the orbits.

### Combining CHAMP, GRACE and Swarm with altimetry to resolve for the sea level budget
Several low Earth orbiters provide information on the gravity field, the CHAMP and GRACE missions have ended in the meanwhile, and although a GRACE follow on mission is planned for launch in april 2018, there is now, since the end of 2017, a GRACE gap. An alternative is therefore to [use the existing Swarm mission to fill this gap](/post/mindthegap). 

Another method, which is explored in CONTIM, is to combine satellite gravity field data with radar altimetry, which allows the separation of mass driven sea level from the volumetric sea level. The use of multiple datasets at once and the use of advanced parameterizations for ocean bottom pressure signals, non-regional ocean responses to ice sheet melting and contintental water storage changes, and glacial isostatic adjustment. Such combination approaches are a promising alternative to more conventional techniques, because the estimation is guided by geophysical assumptions.

 
{{< figure src="/images/GMSL_smoothed.png" title="Combination of satellite altimetry and GRACE data allows the estimation of the components which make up the sea level budget." attr="Data from Rietbroek et al. 2016" attrlink="http://www.pnas.org/content/113/6/1504">}}


