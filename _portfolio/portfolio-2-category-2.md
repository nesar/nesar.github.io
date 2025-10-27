---
title: "Machine Learning for Cosmology"
excerpt: "Research in machine learning for cosmology"
collection: portfolio
---

The advent of large-scale cosmological surveys and complex numerical simulations has generated an unprecedented volume of data, posing significant challenges for traditional analytical and computational methods. Machine learning (ML) has emerged as a transformative paradigm, offering powerful tools to extract knowledge, accelerate simulations, and bridge the gap between theoretical models and observational data. This interdisciplinary field focuses on developing novel AI techniques to analyze cosmic microwave background data, map the cosmic web, infer cosmological parameters, and explore alternative theories of gravity, thereby pushing the boundaries of our understanding of the universe's origin and evolution.

The application of machine learning in cosmology is particularly impactful in areas requiring high-fidelity predictions or rapid exploration of parameter spaces. This includes emulating computationally expensive N-body simulations, identifying cosmic structures like galaxy clusters and voids, and interpreting subtle observational signatures such as peculiar velocities from the kinetic Sunyaev-Zel'dovich effect. By developing intelligent algorithms, researchers can significantly reduce the computational cost associated with exploring vast cosmological model spaces, validate complex theoretical predictions, and gain deeper insights into the fundamental physics governing the large-scale structure of the universe, even under modified gravity scenarios.

My research extensively explores the application of advanced machine learning techniques to tackle some of the most challenging problems in modern cosmology. I have developed a multi-modal foundation model specifically designed for cosmological simulation data, enabling robust and versatile analysis across diverse data types and scales. This foundational work underpins efforts to not only predict but also to understand the complex interplay of cosmic structures.

Furthermore, my work has focused on ensuring the physical integrity of AI-generated cosmological insights. This includes physically benchmarking AI-evolved cosmological structure formation and the AI-generated cosmic web, ensuring that our models accurately reflect the underlying gravitational dynamics. I have also contributed to specific applications, such as developing Differentiable Predictions for Large Scale Structure with SHAMNet, enhancing the interpretability and utility of structure formation models. Additionally, my research includes developing deep neural networks for peculiar velocity estimation from the Kinetic SZ Effect and creating an efficient Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, significantly accelerating the exploration of alternative gravitational theories. These contributions collectively advance our ability to analyze vast cosmological datasets, refine theoretical models, and make new discoveries about the universe's fundamental properties.

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
