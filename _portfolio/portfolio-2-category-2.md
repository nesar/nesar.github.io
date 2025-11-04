---
title: "AI for Cosmological Simulations"
excerpt: "Research in ai for cosmological simulations"
collection: portfolio
---

Cosmological simulations are indispensable tools for unraveling the universe's evolution, from the formation of galaxies and the cosmic web to the distribution of dark matter. These simulations, often involving billions of particles and complex physical processes, are computationally intensive, requiring immense supercomputing resources and time. Traditional N-body and hydrodynamic simulations, while providing invaluable insights, often face limitations in terms of resolution, parameter space exploration, and the incorporation of intricate astrophysical feedback mechanisms. This computational bottleneck poses a significant challenge to fully leveraging upcoming large-scale astronomical survey data.

The advent of Artificial Intelligence (AI) and Machine Learning (ML) offers a transformative paradigm shift in this domain. By developing intelligent algorithms, researchers can significantly accelerate simulation workflows, emulate complex physical processes that are prohibitively expensive to simulate directly, and generate vast quantities of synthetic cosmological data. This approach enables a more efficient exploration of cosmological parameter spaces, facilitates the robust interpretation of observational data, and ultimately pushes the boundaries of our understanding of cosmic structure formation.

My research focuses on leveraging cutting-edge AI techniques to address these critical challenges in cosmological simulations. I have developed multi-modal foundation models specifically designed to process and synthesize diverse types of cosmological simulation data, offering a unified framework for understanding complex cosmic phenomena. A key aspect of this work involves robustly benchmarking AI-evolved cosmological structure formation and conducting physical benchmarking for AI-generated cosmic web outputs, ensuring that our AI models not only generate data efficiently but also adhere to fundamental physical principles and statistical properties of the universe.

Furthermore, my contributions include the development of SHAMNet, a novel framework for differentiable predictions of Large Scale Structure. This methodology allows for end-to-end differentiable forward modeling, which is crucial for inverse inference problems, enabling the robust and rapid estimation of cosmological parameters from observational data. By pioneering these advanced AI-driven methodologies, my work significantly accelerates the scientific discovery pipeline in cosmology, providing powerful new tools for interpreting data from current and future astronomical surveys and deepening our understanding of the universe's evolution.

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
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png" alt="Figure from Physical Benchmarking for AI-Generated Cosmic Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Physical Benchmarking for AI-Generated Cosmic Web</div>
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
