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
  <p class="publications-instruction">Click on any paper title to view the full abstract</p>
</div>

{% assign publications_by_year = site.publications | group_by_exp:"publication", "publication.date | date: '%Y'" | sort: "name" | reverse %}

{% for year in publications_by_year %}
  <div class="year-section">
    <h2 class="year-header" id="{{ year.name }}">{{ year.name }}</h2>
    <div class="publications-grid">
      {% for post in year.items %}
        <div class="publication-item">
          <div class="publication-content">
            <h3 class="publication-title" onclick="openAbstract('{{ post.title | slugify }}')">
              {{ post.title }}
              <i class="fas fa-expand-alt expand-icon"></i>
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
            <div id="abstract-{{ post.title | slugify }}" class="abstract-content" style="display: none;">{{ post.content }}</div>
          </div>
        </div>
      {% endfor %}
    </div>
  </div>
{% endfor %}

<!-- Abstract Modal -->
<div id="abstractModal" class="abstract-modal">
  <div class="modal-content">
    <div class="modal-header">
      <h3 id="modalTitle" class="modal-title"></h3>
      <span class="close-modal" onclick="closeAbstract()">&times;</span>
    </div>
    <div class="modal-body">
      <div id="modalAbstract" class="modal-abstract"></div>
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
  cursor: pointer;
  transition: color 0.2s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.publication-title:hover {
  color: #4299e1;
}

.expand-icon {
  font-size: 0.8em;
  opacity: 0.6;
  transition: opacity 0.2s ease;
}

.publication-title:hover .expand-icon {
  opacity: 1;
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

/* Modal Styles */
.abstract-modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  animation: fadeIn 0.3s ease;
}

.modal-content {
  background: white;
  margin: 5% auto;
  width: 90%;
  max-width: 800px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  animation: slideIn 0.3s ease;
}

.modal-header {
  background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
  color: white;
  padding: 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.modal-title {
  margin: 0;
  font-size: 1.3em;
  font-weight: 600;
  line-height: 1.4;
  flex: 1;
  padding-right: 1rem;
}

.close-modal {
  background: none;
  border: none;
  color: white;
  font-size: 2em;
  cursor: pointer;
  padding: 0;
  width: 2rem;
  height: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: background-color 0.2s ease;
  flex-shrink: 0;
}

.close-modal:hover {
  background-color: rgba(255, 255, 255, 0.2);
}

.modal-body {
  padding: 2rem;
  max-height: 60vh;
  overflow-y: auto;
}

.modal-abstract {
  font-size: 1.05em;
  line-height: 1.7;
  color: #4a5568;
  text-align: justify;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes slideIn {
  from { 
    opacity: 0;
    transform: translateY(-50px);
  }
  to { 
    opacity: 1;
    transform: translateY(0);
  }
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
  
  .modal-content {
    width: 95%;
    margin: 10% auto;
  }
  
  .modal-header {
    padding: 1rem;
  }
  
  .modal-title {
    font-size: 1.1em;
  }
  
  .modal-body {
    padding: 1.5rem;
  }
}
</style>

<script>
function openAbstract(titleSlug) {
  const abstractContent = document.getElementById('abstract-' + titleSlug);
  const modal = document.getElementById('abstractModal');
  const modalTitle = document.getElementById('modalTitle');
  const modalAbstract = document.getElementById('modalAbstract');
  
  if (abstractContent) {
    // Get the title from the clicked element
    const titleElement = document.querySelector('[onclick*="' + titleSlug + '"]');
    const title = titleElement ? titleElement.textContent.replace(/\s*$/, '').trim() : 'Publication Abstract';
    
    // Get abstract text and clean it up
    let abstractText = abstractContent.innerHTML || abstractContent.textContent || '';
    
    // Clean up HTML tags and formatting
    abstractText = abstractText
      .replace(/<[^>]*>/g, '') // Remove HTML tags
      .replace(/&nbsp;/g, ' ') // Replace non-breaking spaces
      .replace(/&amp;/g, '&') // Replace HTML entities
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>')
      .replace(/&quot;/g, '"')
      .replace(/&#39;/g, "'")
      .replace(/\s+/g, ' ') // Replace multiple spaces with single space
      .trim();
    
    // Remove "Summary:" prefix if it exists
    abstractText = abstractText.replace(/^Summary:\s*/i, '');
    
    // If still empty or very short, provide fallback
    if (!abstractText || abstractText === '' || abstractText.length < 10) {
      abstractText = 'Full abstract not available in the current format. Please visit the paper link or arXiv link above for complete details including the full abstract and paper content.';
    }
    
    modalTitle.textContent = title;
    modalAbstract.textContent = abstractText; // Use textContent to avoid HTML interpretation issues
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  } else {
    console.log('No abstract content found for:', titleSlug);
    // Fallback - show modal anyway with error message
    const modal = document.getElementById('abstractModal');
    const modalTitle = document.getElementById('modalTitle');
    const modalAbstract = document.getElementById('modalAbstract');
    
    modalTitle.textContent = 'Abstract Not Available';
    modalAbstract.textContent = 'Unable to load abstract content. Please visit the paper link or arXiv link for full details.';
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function closeAbstract() {
  const modal = document.getElementById('abstractModal');
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}

// Close modal when clicking outside
window.onclick = function(event) {
  const modal = document.getElementById('abstractModal');
  if (event.target === modal) {
    closeAbstract();
  }
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeAbstract();
  }
});
</script>
