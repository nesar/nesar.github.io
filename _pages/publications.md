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
  
  <div class="publication-filters">
    <div class="filter-container">
      <label for="pub-filter">Filter by research area:</label>
      <select id="pub-filter" onchange="filterPublications()">
        <option value="all">All Publications</option>
        <option value="cosmic">Cosmic Web & Dark Matter</option>
        <option value="ml">Machine Learning</option>
        <option value="lens">Gravitational Lensing</option>
        <option value="uncertainty">Uncertainty Quantification</option>
      </select>
    </div>
    
    <div class="filter-container">
      <label for="year-filter">Filter by year:</label>
      <select id="year-filter" onchange="filterPublications()">
        <option value="all">All Years</option>
        <option value="2023">2023+</option>
        <option value="2022">2022</option>
        <option value="2021">2021</option>
        <option value="2020">2020</option>
        <option value="2019">2019</option>
        <option value="older">2018 and earlier</option>
      </select>
    </div>
  </div>
</div>

<div id="publication-container">
  {% for post in site.publications reversed %}
    <div class="publication-item" 
         data-year="{{ post.date | date: '%Y' }}" 
         data-tags="{{ post.tags | join: ' ' }}">
      {% include archive-single.html %}
    </div>
  {% endfor %}
</div>

<script>
  function filterPublications() {
    const topicFilter = document.getElementById('pub-filter').value;
    const yearFilter = document.getElementById('year-filter').value;
    const publications = document.querySelectorAll('.publication-item');
    
    publications.forEach(pub => {
      const pubYear = pub.getAttribute('data-year');
      const pubTags = pub.getAttribute('data-tags');
      let showByTopic = false;
      let showByYear = false;
      
      // Topic filtering
      if (topicFilter === 'all') {
        showByTopic = true;
      } else if (topicFilter === 'cosmic' && pubTags.includes('cosmic') || pubTags.includes('dark matter')) {
        showByTopic = true;
      } else if (topicFilter === 'ml' && pubTags.includes('machine learning') || pubTags.includes('deep learning')) {
        showByTopic = true;
      } else if (topicFilter === 'lens' && pubTags.includes('lensing')) {
        showByTopic = true;
      } else if (topicFilter === 'uncertainty' && pubTags.includes('uncertainty')) {
        showByTopic = true;
      }
      
      // Year filtering
      if (yearFilter === 'all') {
        showByYear = true;
      } else if (yearFilter === '2023' && parseInt(pubYear) >= 2023) {
        showByYear = true;
      } else if (yearFilter === pubYear) {
        showByYear = true;
      } else if (yearFilter === 'older' && parseInt(pubYear) <= 2018) {
        showByYear = true;
      }
      
      // Show publication if it passes both filters
      if (showByTopic && showByYear) {
        pub.style.display = 'block';
      } else {
        pub.style.display = 'none';
      }
    });
  }
  
  // Initialize tags for publications
  document.addEventListener('DOMContentLoaded', function() {
    const publications = document.querySelectorAll('.publication-item');
    
    publications.forEach(pub => {
      const title = pub.querySelector('.archive__item-title').textContent.toLowerCase();
      const excerpt = pub.querySelector('.archive__item-excerpt') ? 
                     pub.querySelector('.archive__item-excerpt').textContent.toLowerCase() : '';
      const content = title + ' ' + excerpt;
      let tags = [];
      
      // Assign tags based on content
      if (content.includes('cosmic') || content.includes('dark matter') || 
          content.includes('halo') || content.includes('filament') || 
          content.includes('void') || content.includes('multistream')) {
        tags.push('cosmic', 'dark matter');
      }
      
      if (content.includes('machine learning') || content.includes('deep learning') || 
          content.includes('neural network') || content.includes('ai') || 
          content.includes('cnn')) {
        tags.push('machine learning', 'deep learning');
      }
      
      if (content.includes('lens') || content.includes('gravitational lens')) {
        tags.push('lensing');
      }
      
      if (content.includes('uncertainty') || content.includes('probabilistic') || 
          content.includes('bayesian')) {
        tags.push('uncertainty');
      }
      
      pub.setAttribute('data-tags', tags.join(' '));
    });
  });
</script>

<style>
  .publications-header {
    margin-bottom: 2em;
  }
  
  .publication-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 1em;
    margin: 1.5em 0;
  }
  
  .filter-container {
    display: flex;
    flex-direction: column;
    min-width: 200px;
  }
  
  .filter-container label {
    margin-bottom: 0.5em;
    font-weight: bold;
  }
  
  .filter-container select {
    padding: 0.5em;
    border-radius: 4px;
    border: 1px solid #ddd;
  }
  
  .publication-item {
    margin-bottom: 2.5em;
    padding-bottom: 1.5em;
    border-bottom: 1px solid #eee;
  }
  
  @media (max-width: 768px) {
    .publication-filters {
      flex-direction: column;
    }
  }
</style>
