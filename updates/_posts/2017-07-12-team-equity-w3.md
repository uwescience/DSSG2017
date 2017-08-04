---
layout: post
title: "Buffets & menus #TeamEquity"
date: 2017-06-30
author: Jacob Kovacs, Jacob Rich
---

*\#TeamEquity is [Gundula Proksch,](http://realestate.washington.edu/about/people/fellows/gundula-proksch/) associate professor of architecture; [Rachel Berney,](http://realestate.washington.edu/about/people/fellows/rachel-berney/) assistant professor of urban design and planning; [Bernease Herman](http://escience.washington.edu/people/bernease-herman/) and [Amanda Tan,](http://escience.washington.edu/people/amanda-tan/) DSSG data scientists; and DSSG fellows [Hillary Dawkins,](https://uwescience.github.io/DSSG2017//2017/06/16/Hillary_Dawkins.html) [Yahui Ma,](https://uwescience.github.io/DSSG2017//2017/06/16/maya-post.html) [Jacob Kovacs,](https://uwescience.github.io/DSSG2017//2017/06/16/jtkovacs-intro.html) and [Jacob Rich.](https://uwescience.github.io/DSSG2017//2017/06/16/jrich.html)*

# Where we’re at

Last week *#TeamEquity* dug into [DC Action’s interactive mapping tool](http://datatools.dcactionforchildren.org/). We managed to shift the map from the DC area to the Seattle area, to pull data from the [ACS 5 year Census API](https://www.census.gov/data/developers/data-sets/acs-5year.html), to visualize it at the Census block level, and to crosswalking the data so we can show it at the level of [Seattle neighborhoods](http://seattle.findwell.com/seattle-neighborhoods/) that our users will recognize. 

We also spent some time thinking about how users should be able to interact with the tool. The DC Action tool’s default is to present a ‘buffet’ of indicators that users can switch on or off—like a made-to-order restaurant. Some indicators can be visualized simultaneously, because they’re simply points on the map showing the location of a specific building; other indicators shade an area according to the percentage or number of resources within it, and can therefore be viewed only one at a time.

# Buffets: the pros & cons

The buffet approach to indicators gives users a lot of control and freedom, although they’re obviously still restricted to the datasets that our team has loaded into the tool. This freedom to play around with the data is not completely harmless. One concern that emerged from an recent ethics workshop is that our tool might make it easier for people without significant data skills to discover and then endorse actions on the basis of spurious correlations. This danger already exists with the DC Action tool, which is purely descriptive; it’s exacerbated in our modified tool because we hope to build in predictive capacity, which introduces additional uncertainty. Skilled users would know to account for this uncertainty in their interpretation of the model, but to perform its social good mission our tool needs to be accessible to a much broader range of affected and interested audiences.

# Menus: the pros & cons

In response to this danger, our solution is to give users a ‘menu’ of thematic indexes. We’re performing an extensive literature review to identify relevant concepts and indicators, then using [structural equation modeling](https://m-clark.github.io/docs/sem/) (SEM) to construct indexes that combine indicators into statistically and conceptually meaningful groups.

Life being life, there are drawbacks to the menu approach as well. The first is an artifact of our team’s constraints. Although some members of our team have domain expertise, the reality of our short timeline and our interdisciplinarity means that the ‘menu’ isn’t being built solely by seasoned ‘chefs’, but also by people working to cultivate their own understanding of new material. Obviously more time and greater domain expertise across the team would help us assemble a more complete and revealing set of indexes, but we face real deadlines and limitations.

The second drawback is more fundamental. Restricting users to predefined menu items limits their freedom to explore novel questions with the tool. While some audiences may welcome limitations that reduce the tool’s cognitive burden, there are good reasons for different users to want more flexibility—either because they have data expertise of their own, or because they have healthy skepticism towards the tendency of external experts to impose inappropriate solutions on communities and situations that they don’t deeply understand.

# Buffets & menus: our path forward

After thinking through these challenges as a group, we decided to attempt some combination of menu and buffet in our map navigation elements. The idea is to make some map layers indexes defined by our model, but let users also explore individual datasets that have been aggregated into the indexes. This should provide enough freedom in the tool so that people can ask the questions they want in their own way, but not so much that it’s a free-for-all. In restaurant terms, we’re going to spell out our understanding of the general structure and workflow that makes the best burrito.

# Bonus: a Chipotle pro tip

It turns out one of our team members has developed significant domain expertise in the arena of ordering from Chipotle. With his endorsement here is a guide to [optimizing your Chipotle order.](https://www.apartmentlist.com/rentonomics/6-techniques-to-get-more-chipotle-burrito-for-free/)  
