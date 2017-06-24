---
layout: post
title:  "Getting things started! #TeamEquity"
date:   2017-06-23
author: Jacob Kovacs
---
 
*\#TeamEquity is [Gundula Proksch,](http://realestate.washington.edu/about/people/fellows/gundula-proksch/) associate professor of architecture; [Rachel Berney,](http://realestate.washington.edu/about/people/fellows/rachel-berney/) assistant professor of urban design and planning; [Bernease Herman](http://escience.washington.edu/people/bernease-herman/) and [Amanda Tan,](http://escience.washington.edu/people/amanda-tan/) DSSG data scientists; and DSSG fellows [Hillary Dawkins,](https://uwescience.github.io/DSSG2017//2017/06/16/Hillary_Dawkins.html) [Yahui Ma,](https://uwescience.github.io/DSSG2017//2017/06/16/maya-post.html) [Jacob Kovacs,](https://uwescience.github.io/DSSG2017//2017/06/16/jtkovacs-intro.html) and [Jacob Rich.](https://uwescience.github.io/DSSG2017//2017/06/16/jrich.html)*

## What we’re doing

This summer, building on work by [DC Action for Children,](http://datatools.dcactionforchildren.org/) \#TeamEquity will be developing an interactive online tool for investigating urban equity and gentrification in Seattle. Our hope is to bring some clarity and direction to an important and impassioned public discussion, and to help various actors see and understand the potential impact of different actions. We want to provide:

- **Decision-making** support for city leaders
- **Education** for the public
- **Planning** support for built environment professionals
- **Research** support for academics
- **Support** for social service/non-profit organizations

## Unique challenges

As we looked around the WRF Data Science Studio the second week of the DSSG program, it seemed like other fellows were already up to their elbows in data. Not us! In sharing our alarm with each other, we came to realized that our team’s project is fundamentally different from the other 2017 DSSG projects, and that our process this summer will reflect that difference. 

The other DSSG teams are tackling three major data analysis projects, trying to determine the impact of a new light rail station on transit traffic; to extract policy implications from a multi-country collection of agriculturally-relevant datasets; and to identify patterns in downtown Seattle traffic cruising data. Their challenge is to take existing datasets—either single datasets or data collections that have been thoughtfully assembled—and mine them for insights.

Our challenge is much different. Before we start working with data, we have to determine what data is needed and available. This is a conceptual problem first: what is ‘gentrification’? What is ‘urban equity’? What combination of indicators can best stand in for these concepts? Finding satisfactory answers to these questions requires a lot of subject matter knowledge, for which we’ll need to engage significantly with scholarly literature.

## Infrastructure for collaboration

In order to collaborate on refinement of concepts, we spent this week creating shared artifacts and workspaces to help us coordinate our work, build efficiently on each other’s efforts, and improve the reproducibility of our final project:

- **Research questions:** We created a document for capturing literature-oriented research questions, like “What’s the role of businesses in gentrification?”.
- **Bibliography:** We created a bibliography and started adding sources and annotations. In addition to helping us read efficiently as a team, a bibliography has value in its own right and will likely be published alongside the final tool.
- **Glossary:** We created a document to record definitions of key terms as we extract and synthesize them from the literature.
- **Metrics:** Project leads Gundula and Rachel provided a preliminary list of indicators grouped into six major themes with additional subthemes. We translated this into a spreadsheet to use as a shared workspace for listing, grouping, and choosing indicators. The first tab (fig 1) provides a dynamically-populated overview of all indicators, arranged by major theme; the remaining tabs each deal with a major theme (fig 2 provides an example), with individual team members taking ownership of specific themes and responsible for identifying indicators that best illuminate their theme. 
- **Data dictionary:** We created a document for tracking datasets—their contents, origin, spatial unit, and any notes of interest. 
- **User research:** Building on a stakeholder analysis workshop conducted by [DSSG’s resident ethnographers,](http://escience.washington.edu/research-project/ethnography-of-data-science-collaborations/) we created a document for resarching the functionality and UI that various target user groups may expect.
- **Wishlist:** We created a catch-all document to complement the user research document, where we can capture our own ideas about potential tool features and useful site content to accompany the tool.

[Fig. 1: Indicators overview tab]({{ site.url }}assets/images/equity-blog1-fig1.png)

[Fig. 2: Example major theme tab]({{ site.url }}assets/images/equity-blog1-fig2.png)

# Next steps

In addition to these documents on Google Drive, moving forward we’ll be storing data in AWS and sharing our code via GitHub. Once data is obtained and cleaned, we expect to use structural equation modeling to enable interactive exploration of policy impacts. Stay tuned!
