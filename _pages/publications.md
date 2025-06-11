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
    <a href="https://scholar.google.com/citations?user=gI4dQOgAAAAJ&hl=en" target="_blank" class="scholar-link">
      <i class="fas fa-graduation-cap"></i> Google Scholar profile
    </a>
  </p>
  <p class="publications-instruction">Click on any paper title to view the full abstract on the right</p>
</div>

<div class="publications-layout">
  <div class="publications-list">
    {% assign publications_by_year = site.publications | group_by_exp:"publication", "publication.date | date: '%Y'" | sort: "name" | reverse %}
    
    {% for year in publications_by_year %}
      <div class="year-section">
        <h2 class="year-header" id="{{ year.name }}">{{ year.name }}</h2>
        <div class="publications-grid">
          {% for post in year.items %}
            <div class="publication-item" data-abstract="{{ post.title | slugify }}">
              <div class="publication-content">
                <h3 class="publication-title" onclick="showAbstract('{{ post.title | slugify }}', this)">
                  {{ post.title }}
                  <i class="fas fa-chevron-right expand-icon"></i>
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
                
                <!-- Hidden abstract content -->
                <div id="abstract-{{ post.title | slugify }}" class="abstract-data" style="display: none;">
                  <div class="abstract-title">{{ post.title }}</div>
                  <div class="abstract-text">{{ post.content | strip_html | strip_newlines }}</div>
                </div>
              </div>
            </div>
          {% endfor %}
        </div>
      </div>
    {% endfor %}
  </div>
  
  <div class="abstract-panel">
    <div class="abstract-panel-header">
      <h3><i class="fas fa-file-alt"></i> Abstract</h3>
    </div>
    <div class="abstract-panel-content">
      <div id="abstract-display" class="abstract-display">
        <div class="abstract-placeholder">
          <i class="fas fa-mouse-pointer"></i>
          <p>Click on any paper title to view its abstract here</p>
        </div>
      </div>
    </div>
  </div>
</div>

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
  margin-bottom: 0.5rem;
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

.publications-instruction {
  font-size: 0.9em;
  color: #718096;
  font-style: italic;
  margin: 0;
}

.publications-layout {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 2rem;
  min-height: 70vh;
}

.publications-list {
  overflow-y: auto;
}

.year-section {
  margin-bottom: 2rem;
}

.year-header {
  font-size: 1.8em;
  font-weight: 700;
  color: #2d3748;
  border-bottom: 3px solid #4299e1;
  padding-bottom: 0.5rem;
  margin-bottom: 1.5rem;
}

.publications-grid {
  display: grid;
  gap: 1rem;
}

.publication-item {
  background: white;
  border-radius: 8px;
  padding: 1.2rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: all 0.2s ease;
  border-left: 4px solid #e2e8f0;
  cursor: pointer;
}

.publication-item:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
  border-left-color: #4299e1;
}

.publication-item.selected {
  border-left-color: #4299e1;
  background: #f7fafc;
}

.publication-title {
  font-size: 1.1em;
  font-weight: 600;
  color: #2d3748;
  margin: 0 0 0.8rem 0;
  cursor: pointer;
  transition: color 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
  line-height: 1.3;
}

.publication-title:hover {
  color: #4299e1;
}

.expand-icon {
  font-size: 0.7em;
  opacity: 0.6;
  transition: all 0.2s ease;
}

.publication-title:hover .expand-icon {
  opacity: 1;
  transform: translateX(2px);
}

.publication-venue {
  color: #718096;
  font-size: 0.85em;
  margin: 0 0 0.8rem 0;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.publication-links {
  display: flex;
  gap: 0.8rem;
  flex-wrap: wrap;
}

.pub-link {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.4rem 0.8rem;
  border-radius: 4px;
  text-decoration: none;
  font-size: 0.8em;
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

/* Abstract Panel Styles */
.abstract-panel {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  position: sticky;
  top: 2rem;
  height: fit-content;
  max-height: 80vh;
}

.abstract-panel-header {
  background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
  color: white;
  padding: 1.2rem;
  border-bottom: 1px solid #e2e8f0;
}

.abstract-panel-header h3 {
  margin: 0;
  font-size: 1.2em;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.abstract-panel-content {
  height: 100%;
}

.abstract-display {
  padding: 1.5rem;
  max-height: 70vh;
  overflow-y: auto;
}

.abstract-placeholder {
  text-align: center;
  color: #a0aec0;
  padding: 3rem 1rem;
}

.abstract-placeholder i {
  font-size: 3em;
  margin-bottom: 1rem;
  display: block;
}

.abstract-placeholder p {
  font-size: 1.1em;
  margin: 0;
  line-height: 1.5;
}

.abstract-content-display {
  animation: fadeIn 0.3s ease;
}

.abstract-title-display {
  font-size: 1.1em;
  font-weight: 600;
  color: #2d3748;
  margin-bottom: 1rem;
  line-height: 1.4;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 0.8rem;
}

.abstract-text-display {
  font-size: 1em;
  line-height: 1.7;
  color: #4a5568;
  text-align: justify;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Responsive Design */
@media (max-width: 1200px) {
  .publications-layout {
    grid-template-columns: 1fr 350px;
  }
}

@media (max-width: 968px) {
  .publications-layout {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .abstract-panel {
    position: relative;
    top: 0;
    max-height: 400px;
  }
  
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
    font-size: 1em;
  }
  
  .abstract-display {
    max-height: 300px;
  }
}

/* Hide abstract data - this is just for storing content */
.abstract-data {
  display: none !important;
}
</style>

<script>
function showAbstract(titleSlug, element) {
  // Remove selected class from all items
  document.querySelectorAll('.publication-item').forEach(item => {
    item.classList.remove('selected');
  });
  
  // Add selected class to clicked item
  const publicationItem = element.closest('.publication-item');
  if (publicationItem) {
    publicationItem.classList.add('selected');
  }
  
  // Get the abstract data
  const abstractData = document.getElementById('abstract-' + titleSlug);
  const abstractDisplay = document.getElementById('abstract-display');
  
  if (abstractData) {
    // Get title and text from the hidden data
    const titleElement = abstractData.querySelector('.abstract-title');
    const textElement = abstractData.querySelector('.abstract-text');
    
    const title = titleElement ? titleElement.textContent : 'Publication Abstract';
    let abstractText = textElement ? textElement.textContent : '';
    
    // Clean up the text
    abstractText = abstractText
      .replace(/\s+/g, ' ') // Replace multiple spaces with single space
      .trim();
    
    // Remove "Summary:" prefix if it exists
    abstractText = abstractText.replace(/^Summary:\s*/i, '');
    
    // If still empty or very short, provide fallback
    if (!abstractText || abstractText.length < 10) {
      abstractText = 'Full abstract not available in the current format. Please visit the paper link or arXiv link for complete details including the full abstract and paper content.';
    }
    
    // Update the abstract panel
    abstractDisplay.innerHTML = `
      <div class="abstract-content-display">
        <div class="abstract-title-display">${title}</div>
        <div class="abstract-text-display">${abstractText}</div>
      </div>
    `;
    
    // Scroll abstract panel to top
    abstractDisplay.scrollTop = 0;
    
  } else {
    // Fallback display
    abstractDisplay.innerHTML = `
      <div class="abstract-content-display">
        <div class="abstract-title-display">Abstract Not Available</div>
        <div class="abstract-text-display">Unable to load abstract content. Please visit the paper link or arXiv link for full details.</div>
      </div>
    `;
  }
}

// Optional: Auto-select first publication on page load
document.addEventListener('DOMContentLoaded', function() {
  // You can uncomment this if you want the first paper to be auto-selected
  // const firstPublication = document.querySelector('.publication-title');
  // if (firstPublication) {
  //   firstPublication.click();
  // }
});
</script>
