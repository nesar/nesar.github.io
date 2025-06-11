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
      <i class="fas fa-graduation-cap"></i> Google Scholar profile
    </a>
  </p>
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
                <i class="fas fa-journal-whills"></i> {{ post.venue }}, {{ post.date | date: "%Y" }}
              </p>
            {% endif %}
            
            <div class="publication-links">
              {% if post.paperurl %}
                <a href="{{ post.paperurl }}" target="_blank" class="pub-link paper-link">
                  <i class="fas fa-file-pdf"></i> Paper
                </a>
              {% endif %}
              
              {% if post.excerpt and post.excerpt contains 'arXiv' %}
                {% assign arxiv_match = post.excerpt | split: '](http://arxiv.org/abs/' %}
                {% if arxiv_match.size > 1 %}
                  {% assign arxiv_id = arxiv_match[1] | split: ')' | first %}
                  <a href="http://arxiv.org/abs/{{ arxiv_id }}" target="_blank" class="pub-link arxiv-link">
                    <i class="fas fa-external-link-alt"></i> arXiv
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
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  padding: 2rem;
  border-radius: 12px;
  margin-bottom: 2rem;
  text-align: center;
}

.publications-note {
  font-size: 1.1em;
  margin: 0;
  color: #4a5568;
}

.scholar-link {
  color: #4285f4;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.2s ease;
}

.scholar-link:hover {
  color: #1a73e8;
  text-decoration: underline;
}

.year-section {
  margin-bottom: 3rem;
}

.year-header {
  font-size: 2em;
  font-weight: 700;
  color: #2d3748;
  border-bottom: 3px solid #4299e1;
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
}

.publications-grid {
  display: grid;
  gap: 1.5rem;
}

.publication-item {
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  border-left: 4px solid #4299e1;
}

.publication-item:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.publication-title {
  font-size: 1.2em;
  font-weight: 600;
  color: #2d3748;
  margin: 0 0 1rem 0;
  line-height: 1.4;
}

.publication-venue {
  color: #718096;
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
  padding: 0.5rem 1rem;
  border-radius: 6px;
  text-decoration: none;
  font-size: 0.9em;
  font-weight: 500;
  transition: all 0.2s ease;
}

.paper-link {
  background: #e53e3e;
  color: white;
}

.paper-link:hover {
  background: #c53030;
  color: white;
}

.arxiv-link {
  background: #48bb78;
  color: white;
}

.arxiv-link:hover {
  background: #38a169;
  color: white;
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

