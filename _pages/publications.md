---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<div class="publications-header">
  <p>Up-to-date publication list and citations can be found here: 
    <a href="https://arxiv.org/search/?query=Ramachandra%2C+N&searchtype=author&abstracts=show&order=-announced_date_first&size=50" target="_blank"><span style="color:blue">arXiv</span></a> 
    and 
    <a href="https://ui.adsabs.harvard.edu/#/public-libraries/y2_59cmZQ2iC2mUPSYSXtQ" target="_blank"><span style="color:blue">SAO/NASA Astrophysics Data System (ADS)</span></a>
  </p>
</div>

<div class="publication-list">
  <h2>Recent Publications</h2>
  {% assign recent_publications = site.publications | sort: "date" | reverse | slice: 0, 10 %}
  {% for post in recent_publications %}
    <div class="publication-item">
      {% include archive-single.html %}
    </div>
  {% endfor %}
  
  <h2>All Publications</h2>
  <div id="publication-container">
    {% assign older_publications = site.publications | sort: "date" | reverse | slice: 10, 1000 %}
    {% for post in older_publications %}
      <div class="publication-item">
        {% include archive-single.html %}
      </div>
    {% endfor %}
  </div>
</div>

<style>
  .publication-item {
    margin-bottom: 2em;
    padding-bottom: 1em;
    border-bottom: 1px solid #eee;
  }
  
  .publications-header {
    margin-bottom: 2em;
  }
</style>
