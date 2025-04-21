---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<p>Up-to-date publication list and citations can be found here: <a href="https://scholar.google.com/citations?user=YOUR_SCHOLAR_ID" target="_blank"><u><span style="color:blue">Google Scholar</span></u></a></p>

{% assign publications_by_year = site.publications | group_by_exp:"publication", "publication.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in publications_by_year %}
  <h2 id="{{ year.name }}">{{ year.name }}</h2>
  {% for post in year.items %}
    {% include custom/archive-single-publication.html %}
  {% endfor %}
{% endfor %}
