---
layout: archive
title: "Miscellaneous"
permalink: /miscellaneous/
author_profile: true
---

## Teaching Experience
{% include base_path %}
{% for post in site.teaching reversed %}
  {% include archive-single.html %}
{% endfor %}

## Selected Talks
{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
