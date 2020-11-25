# PyQGIS Tutorial

This tutorial serves as an introduction to both QGIS and the use of Python scripting within the QGIS platform. It was developed as a final project for IDCE 30274 Computer Programming for GIS taught by Professor Shadrock Roberts at Clark University in Fall 2020. Questions, comments, and suggestions should be directed to Jess Strzempko either at JeStrzempko@clarku.edu or JessStrzempko@gmail.com. Her GitHub profile can be found [here](https://github.com/jstrzempko). 

### Objectives

* To introduce users to the use of Python scripting in QGIS
* To promote the use of open source software through a demonstration of its capabilities
* To explore the ACLED US Crisis Monitor dataset

### Data

Data for this tutorial is sourced from [ACLED](acleddata.com), the Armed Conflict Location & Event Data Project. ACLED is a registered non-profit organization with 501(c)(3) status operating in the United States that compiles spatial and attribute data on worldwide crises. These include political violence, civil and communal conflicts, violence against civilians, remote violence, rioting, and protesting. ACLED has [teams of research analysts](https://acleddata.com/about-acled/) that collect, analyze, and map events in these regions: Africa, East Asia, South Asia, Southeast Asia, the Middle East, Central Asia and the Caucasus, Latin America and the Caribbean, and Southeastern and Eastern Europe and the Balkans. 

In addition to location data, disaggregated information on the dates, actors, fatalities, and types of conflict is gathered and verified through media outlets. Decisionmaking and documentation behind the methodology can be found [here](https://acleddata.com/resources/methodology/). This tutorial will specifically be using data from the [US Crisis Monitor](https://acleddata.com/special-projects/us-crisis-monitor/), a new project begun by ACLED in 2020 in response to increased domestic civil unrest following the murder of [George Floyd](https://en.wikipedia.org/wiki/George_Floyd) by Minneapolis police. In collaboration with the Bridging Divides Initiative (BDI) at Princeton University, ACLED launched the US Crisis Monitor to support and empower local communities through access to real-time evidence of demonstrations, protesting and violence. Nowadays, Americans are faced with an insidious combination of [white supremacist extremism](https://www.theguardian.com/australia-news/audio/2020/nov/03/us-election-2020-trump-and-the-rise-of-white-supremacist-extremism) and [political partisanship](https://www.cbsnews.com/news/second-stimulus-check-status-update-2020-11-24/) exacerbated by a global pandemic and fascist president. The US data ACLED gathers and shares aims to provide communities with useful information on risks, conflict hotspots, and resources needed to keep community members safe and healthy. 

Both the data and analysis performed by ACLED is free for use, which is why we will be employing it in this tutorial. The outputs are merely educational and exploratory and should not be treated as academically rigorous results. Use of ACLED data for research should involve a [critical examination of the quality and methodology](https://journals.sagepub.com/doi/abs/10.1177/0010836711434463) behind the data collection and analysis, with an eye toward biased findings and reliance on media sources. Comments and questions about the ACLED dataset should be directed toward admin@acleddata.com. 

![](images/download_acled.PNG)

Data should be downloaded from [the US Crisis Monitor site](https://acleddata.com/special-projects/us-crisis-monitor/). It should then be opened in Excel and saved as a CSV UTF-8 (Comma Delimited) (`.csv`) file for ease of use with QGIS (and other software). Should problems arise, a back-up version of the `.csv` file is provided in the data folder within this repository. 

## Tutorial Steps

### Downloading QGIS 

QGIS can be downloaded for free from the [QGIS website](download.qgis.org). This tutorial will explain some points of confusion surrounding the process, but assumes users have previous experience downloading programs to their personal computers. QGIS can be downloaded for Windows, MacOS X, Linux, BDS, and Android. This tutorial will focus on a Windows downloads. Assistance with other operating systems can be found on the [QGIS Installers page](https://qgis.org/en/site/forusers/alldownloads.html). 

![](images/download_qgis.PNG)

The first question that arises when downloading QGIS is - what is OSGeo4W? A [nice and quick explanation](https://gis.stackexchange.com/questions/164976/what-is-osgeo4w) of OSGeo and OSGeo4W can be found by StackExchange user HeikkiVesanto. To paraphrase, OSGeo, [The Open Source Geospatial Foundation](https://www.osgeo.org/) supports open source GIS projects like QGIS, GeoServer, and OpenLayers, offering legitimacy and quality assurance. OSGeo4W is a Windows installer for Open Source GIS projects. It keeps track of the dependencies (reliance of one piece of software on another) of Open Source GIS packages, ensuring that one install of programs like Python, GDAL, or GRASS can be shared among softwares. It also maintains software versions so you can easily upgrade programs. 

I would recommend downloading using OSGeo4W if you intend to perform further GIS/programming work on your personal computer. Having dependencies already installed can be incredibly useful in the future and save time and energy (and prevent frustration). However, if you feel that your foray into GIS will be limited or you are inexperienced, I would suggest downloading using the QGIS Standalone Installer. Choice of 32 vs 64 bit depends on [what processor](https://www.techsoup.org/Support/articles-and-how-tos/do-i-need-the-32bit-or-64bit) your personal computer has. More and more often, personal computers have 64-bit processors, but if you are concerned you should verify this information. 

![](images/osgeo4w_setup.PNG)
![](images/osgeo4w_setup2.PNG)
![](images/osgeo4w_setup3.PNG)
![](images/osgeo4w_setup4.PNG)
![](images/osgeo4w_setup5.PNG)
![](images/osgeo4w_setup6.PNG)
![](images/osgeo4w_setup7.PNG)
![](images/osgeo4w_setup8.PNG)

Don’t blindly do a full install of OSGeo4W. Only install QGIS and maybe other components you like. Dependencies will be included automatically. A full install pulls in components that require third party additions, which need to be installed manually. These components render the installation unusable without those additions.

### PyQGIS

work with the data (in qgis in the python console)
