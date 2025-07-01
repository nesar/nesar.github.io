---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

<div class="publications-header">
  <p class="publications-note">
    Up-to-date publication list and citations can be found on my 
    <a href="https://scholar.google.com/citations?hl=en&user=dCe3MK0AAAAJ&view_op=list_works&sortby=pubdate" target="_blank" class="scholar-link">
      Google Scholar profile
    </a>
  </p>
  <p class="disclaimer"><strong>Disclaimer:</strong> This section is automatically updated by Reasoning Language Models. Google Gemini is utilized to periodically go over my recent publications, talks and activities to update the content. While the information is monitored, at times incorrect information may appear.</p>
</div>

{% assign publications_by_year = site.publications | group_by_exp:"publication", "publication.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in publications_by_year %}
  <div class="year-section">
    <h2 class="year-header" id="{{ year.name }}">{{ year.name }}</h2>
    <div class="publications-grid">
      {% for post in year.items %}
        <div class="publication-item">
          <div class="publication-content">
            <h3 class="publication-title">
              {{ post.title }}
            </h3>
            
            {% if post.venue %}
              <p class="publication-venue">
                {{ post.venue }}, {{ post.date | date: "%Y" }}
              </p>
            {% endif %}
            
            <div class="publication-links">
              {% if post.paperurl %}
                <a href="{{ post.paperurl }}" target="_blank" class="pub-link paper-link">
                  📄 Paper
                </a>
              {% elsif post.excerpt and post.excerpt contains 'arXiv' %}
                {% assign arxiv_match = post.excerpt | split: '](http://arxiv.org/abs/' %}
                {% if arxiv_match.size > 1 %}
                  {% assign arxiv_id = arxiv_match[1] | split: ')' | first %}
                  <a href="http://arxiv.org/abs/{{ arxiv_id }}" target="_blank" class="pub-link paper-link">
                    📄 Paper
                  </a>
                {% endif %}
              {% endif %}
            </div>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
{% endfor %}

<style>
.publications-header {
  background: linear-gradient(135deg, #1a1c1e 0%, #2a2d30 100%);
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
  text-align: center;
  border: 1px solid #2a2d30;
}

.publications-note {
  font-size: 1.1em;
  margin: 0;
  color: #e8e8e8;
}

.scholar-link {
  color: #ffffff;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.scholar-link:hover {
  color: #cccccc;
  text-decoration: underline;
}

.disclaimer {
  font-size: 0.9em;
  color: #aaaaaa;
  font-style: italic;
  margin-top: 1.5rem;
  border-top: 1px solid #2a2d30;
  padding-top: 1rem;
}

.year-section {
  margin-bottom: 3rem;
}

.year-header {
  font-size: 2em;
  font-weight: 400;
  color: #ffffff;
  border-bottom: 2px solid #ffffff;
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
}

.publications-grid {
  display: grid;
  gap: 1.5rem;
}

.publication-item {
  background: #1a1c1e;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(255, 255, 255, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  border: 1px solid #2a2d30;
  border-left: 4px solid #ffffff;
}

.publication-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(255, 255, 255, 0.15);
}

.publication-title {
  font-size: 1.2em;
  font-weight: 400;
  color: #ffffff;
  margin: 0 0 1rem 0;
  line-height: 1.4;
}

.publication-venue {
  color: #aaaaaa;
  font-size: 0.95em;
  margin: 0 0 1rem 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.publication-links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.pub-link {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem 1.2rem;
  border-radius: 8px;
  text-decoration: none !important;
  font-size: 0.95em;
  font-weight: 600;
  transition: all 0.2s ease;
  margin: 0.25rem;
}

.paper-link {
  background: linear-gradient(135deg, #ffffff, #f0f0f0);
  color: #000000 !important;
  border: 2px solid #ffffff;
  font-weight: 600;
  text-shadow: none;
  box-shadow: 0 2px 8px rgba(255, 255, 255, 0.3);
}

.paper-link:hover {
  background: linear-gradient(135deg, #e0e0e0, #d0d0d0);
  color: #000000 !important;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(255, 255, 255, 0.4);
}

/* Responsive Design */
@media (max-width: 768px) {
  .publications-header {
    padding: 1.5rem;
  }
  
  .year-header {
    font-size: 1.5em;
  }
  
  .publication-item {
    padding: 1rem;
  }
  
  .publication-title {
    font-size: 1.1em;
  }
  
  .publication-links {
    gap: 0.5rem;
  }
  
  .pub-link {
    font-size: 0.8em;
    padding: 0.4rem 0.8rem;
  }
}
</style>

