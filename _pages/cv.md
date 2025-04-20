---
layout: archive
title: "Curriculum Vitae"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<div class="cv-actions">
  <div class="cv-download">
    <h3>Download Options</h3>
    <a href="https://nesar.github.io/files/CV_NesarRamachandra.pdf" class="btn btn--primary" target="_blank">Download Full CV</a>
    <a href="https://nesar.github.io/files/Resume_NesarRamachandra.pdf" class="btn" target="_blank">Download Resume</a>
  </div>
  
  <div class="cv-display-options">
    <h3>Display Options</h3>
    <div class="toggle-container">
      <label for="cv-view-toggle">View Mode:</label>
      <select id="cv-view-toggle" onchange="toggleCVView()">
        <option value="embedded">Embedded PDF</option>
        <option value="text">Text Version</option>
      </select>
    </div>
  </div>
</div>

<div id="cv-embedded" class="cv-section">
  <iframe src="https://nesar.github.io/files/CV_NesarRamachandra.pdf" width="100%" height="800"></iframe>
</div>

<div id="cv-text" class="cv-section" style="display: none;">
  <h2>Education</h2>
  <ul>
    <li>
      <strong>Ph.D. in Physics and Astronomy</strong>, 2018<br>
      University of Kansas<br>
      Thesis: <em>Structure of the Dark Matter Web: A Multi-Stream Analysis</em><br>
      Advisor: Prof. Sergei Shandarin
    </li>
    <li>
      <strong>Integrated M.Sc. in Physics</strong>, 2012<br>
      Birla Institute of Technology and Science (BITS), Pilani<br>
      Thesis at Indian Institute of Astrophysics, Bangalore
    </li>
  </ul>

  <h2>Professional Experience</h2>
  <ul>
    <li>
      <strong>Computational Scientist</strong>, 2020-Present<br>
      Argonne National Laboratory, Chicago, IL
    </li>
    <li>
      <strong>Postdoctoral Fellow</strong>, 2018-2020<br>
      High Energy Physics Division, Argonne National Laboratory<br>
      Kavli Institute for Cosmological Physics (KICP), University of Chicago
    </li>
  </ul>

  <h2>Research Interests</h2>
  <ul>
    <li>Machine Learning for Computational Science</li>
    <li>Uncertainty Quantification in Deep Learning</li>
    <li>Computational Cosmology</li>
    <li>Gravitational Lensing</li>
    <li>High-Performance Computing</li>
  </ul>

  <h2>Selected Publications</h2>
  <ul>
    {% for post in site.publications reversed limit:5 %}
      <li>
        {{ post.citation }}
      </li>
    {% endfor %}
    <li><a href="/publications/">See all publications...</a></li>
  </ul>

  <h2>Skills</h2>
  <ul>
    <li>
      <strong>Programming Languages</strong>: Python, C/C++, SQL, R, JavaScript, MATLAB
    </li>
    <li>
      <strong>Frameworks & Tools</strong>: PyTorch, TensorFlow, Scikit-learn, NumPy, SciPy, Pandas, MPI, OpenMP
    </li>
    <li>
      <strong>HPC</strong>: Experience with supercomputing environments and parallel computing
    </li>
  </ul>
</div>

<script>
  function toggleCVView() {
    const viewMode = document.getElementById('cv-view-toggle').value;
    const embeddedView = document.getElementById('cv-embedded');
    const textView = document.getElementById('cv-text');
    
    if (viewMode === 'embedded') {
      embeddedView.style.display = 'block';
      textView.style.display = 'none';
    } else {
      embeddedView.style.display = 'none';
      textView.style.display = 'block';
    }
  }
</script>

<style>
  .cv-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 2em;
    margin-bottom: 2em;
  }
  
  .cv-download, .cv-display-options {
    flex: 1;
    min-width: 250px;
  }
  
  .cv-download h3, .cv-display-options h3 {
    margin-top: 0;
    margin-bottom: 1em;
  }
  
  .cv-download .btn {
    margin-right: 0.5em;
    margin-bottom: 0.5em;
  }
  
  .toggle-container {
    display: flex;
    flex-direction: column;
  }
  
  .toggle-container label {
    margin-bottom: 0.5em;
  }
  
  .toggle-container select {
    padding: 0.5em;
    border-radius: 4px;
    border: 1px solid #ddd;
    max-width: 200px;
  }
  
  .cv-section {
    margin-top: 1em;
  }
  
  #cv-text h2 {
    color: #2c3e50;
    border-bottom: 1px solid #eee;
    padding-bottom: 0.5em;
    margin-top: 1.5em;
  }
  
  #cv-text ul {
    padding-left: 1.5em;
  }
  
  #cv-text li {
    margin-bottom: 0.8em;
  }
</style>
