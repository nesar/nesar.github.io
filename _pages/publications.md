---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

You can also find my publications on [<u><span style="color:blue"> SAO/NASA Astrophysics Data System (ADS) </span></u>](https://ui.adsabs.harvard.edu/#/public-libraries/y2_59cmZQ2iC2mUPSYSXtQ) or [<u><span style="color:blue"> arXiv </span></u>](https://arxiv.org/find/astro-ph/1/au:+Ramachandra_N/0/1/0/all/0/1)


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
