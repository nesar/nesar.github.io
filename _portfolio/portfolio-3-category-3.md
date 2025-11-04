---
title: "Observational Astronomy & AI-Driven Analysis"
excerpt: "Research in observational astronomy & ai-driven analysis"
collection: portfolio
---

Modern astronomical research is characterized by an unprecedented deluge of data from ground-based and space-borne observatories, posing significant challenges and opportunities for discovery. This era of "big data" astronomy necessitates advanced computational techniques to extract meaningful scientific insights from vast datasets, ranging from high-resolution imaging surveys to complex spectroscopic measurements. Observational astronomy, which relies on direct data acquisition, is increasingly interwoven with sophisticated analytical methods to push the frontiers of our understanding of the universe.

A key development in addressing these challenges is the integration of Artificial Intelligence (AI) and Machine Learning (ML). These computational paradigms enable astronomers to process, classify, and interpret large volumes of data with unprecedented efficiency and accuracy. Applications span from the identification of subtle signals in noisy data to the automated classification of celestial objects and the detection of rare or anomalous phenomena that might otherwise go unnoticed. AI-driven analysis is thus becoming indispensable for accelerating discoveries across diverse astronomical domains, including cosmology, galaxy evolution, and stellar astrophysics.

The convergence of observational data and AI methodologies facilitates the creation of robust tools for parameter estimation, model validation, and hypothesis generation. Deep Learning, in particular, has emerged as a transformative force, capable of learning intricate patterns and relationships within complex astronomical datasets. This allows for more precise measurements, improved predictive capabilities, and a deeper exploration of the universe's structure and evolution, ultimately enhancing our ability to address fundamental questions in astrophysics.

My research extensively explores the synergy between advanced AI techniques and observational astronomy, developing novel methodologies to tackle complex scientific problems. I have focused on leveraging Machine Learning, Deep Learning, and Generative Adversarial Networks (GANs) to extract crucial information from large-scale astronomical surveys. For instance, I contributed to mapping the Milky Way's structure through a photometric sample of 2.6 million Red Clump stars. My work also introduced innovative applications like teaching Large Language Models (LLMs) to interpret spectroscopic data and developed the SYTH-Z method for probabilistic redshift estimation using machine learning synthetic spectra.

Furthermore, I have developed techniques for reducing model error in weak lensing cluster mass estimation through optimized galaxy selection and applied GANs for anomaly detection in Hyper Suprime-Cam galaxy images, uncovering unusual cosmic phenomena. My contributions extend to cosmological probes, including the estimation of peculiar velocities from the Kinetic Sunyaev-Zel'dovich effect using Deep Neural Networks, and the creation of a modular deep learning pipeline for the detection and precise modeling of galaxy-scale strong gravitational lenses. These efforts collectively enhance our capacity to analyze complex observational data, leading to more accurate measurements, automated discovery, and deeper insights into the fundamental properties and evolution of the universe.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
</div>


<style>
.research-figures {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.figure-item {
  text-align: center;
  background: #f8f9fa;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.figure-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 20px rgba(0,0,0,0.15);
}

.figure-item img {
  max-width: 100%;
  height: auto;
  max-height: 300px;
  object-fit: contain;
  border-radius: 8px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.figure-item img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.9em;
  color: #6c757d;
  margin-top: 1rem;
  line-height: 1.4;
  font-style: italic;
}

@media (max-width: 768px) {
  .research-figures {
    grid-template-columns: 1fr;
    gap: 1rem;
  }
  
  .figure-item {
    padding: 1rem;
  }
}
</style>

<!-- Figure Modal -->
<div id="imageModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <img class="modal-content" id="modalImage">
</div>

<script>
function openModal(img) {
  var modal = document.getElementById('imageModal');
  var modalImg = document.getElementById('modalImage');
  modal.style.display = 'block';
  modalImg.src = img.src;
}

function closeModal() {
  document.getElementById('imageModal').style.display = 'none';
}

window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}

document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeModal();
  }
});
</script>
