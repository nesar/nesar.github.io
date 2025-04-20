---
layout: archive
title: "Miscellaneous"
permalink: /misc/
author_profile: true
---

## Teaching Experience

{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}

## Selected Talks

{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
