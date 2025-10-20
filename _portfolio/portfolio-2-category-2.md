---
title: "Machine Learning for Astrophysics & Cosmology"
excerpt: "Research in machine learning for astrophysics & cosmology"
collection: portfolio
---

The convergence of vast astronomical datasets from cutting-edge observatories and rapid advancements in machine learning (ML) has ushered in a transformative era for astrophysics and cosmology. This synergy empowers researchers to tackle complex challenges, ranging from understanding the universe's large-scale structure to precisely characterizing individual galaxies. Machine learning models offer unprecedented capabilities for pattern recognition, anomaly detection, data synthesis, and the acceleration of computationally intensive simulations, extracting deeper insights from cosmic data. Within this dynamic landscape, a primary focus lies on developing robust ML methodologies to address fundamental questions about cosmic evolution, including the emulation of complex physical processes, the identification of subtle astrophysical signals, and the robust classification and characterization of astronomical objects. Specific applications encompass the analysis of large-scale structure formation, the detection and modeling of strong gravitational lenses, galaxy property estimation, and the exploration of modified gravity theories through high-fidelity data analysis.

My research applies innovative machine learning techniques to these critical problems, developing advanced ML models to accelerate discovery and enhance cosmic understanding. A significant portion of my work focuses on building multi-modal foundation models for cosmological simulation data, rigorously benchmarking AI-evolved cosmic structures and foundation models. I developed SHAMNet for differentiable predictions of large-scale structure, offering a robust approach to cosmological parameter inference, and created matter power spectrum emulators for f(R) modified gravity cosmologies, enabling rapid exploration of alternative theories. In observational astronomy, I pioneered anomaly detection in astronomical images using generative adversarial networks (GANs) and developed a modular deep learning pipeline for strong gravitational lens detection and modeling, alongside optimizing galaxy selection to reduce model error in weak lensing cluster mass estimation.

Beyond imaging and simulations, my research extends to spectroscopic data, exploring methods for teaching large language models (LLMs) to "speak spectroscopy," and developing SYTH-Z for probabilistic redshift estimation from synthetic spectra. I also addressed peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect using deep neural networks. Collectively, these efforts demonstrate my commitment to developing robust, scalable, and physically informed machine learning solutions, pushing the boundaries of astrophysical and cosmological research and providing novel insights into the universe's fundamental properties.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/multi-modal-foundation-model-for-cosmological-simu_plot_1_204705ca.png" alt="Figure from Multi-modal Foundation Model for Cosmological Simulation Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-modal Foundation Model for Cosmological Simulation Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
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
