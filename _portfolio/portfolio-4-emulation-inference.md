---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The field of Emulation and Inference is dedicated to developing advanced computational methods that address the challenges of complex scientific and engineering systems. These systems often involve high-fidelity simulations that are computationally prohibitive, or require analysis of vast, high-dimensional datasets. Emulation, also known as surrogate modeling, involves creating fast, data-driven approximations of these expensive simulations. These emulators can rapidly predict system behavior across a wide parameter space, significantly accelerating design, optimization, and uncertainty quantification tasks.

Inference, on the other hand, focuses on extracting meaningful insights and knowledge from data, often involving statistical and machine learning techniques to understand underlying processes, reconstruct unobserved phenomena, or quantify uncertainties in model parameters and predictions. Together, emulation and inference empower researchers to navigate complex problem spaces more efficiently, enabling real-time decision-making, exploring larger parameter spaces, and making robust predictions with quantified uncertainties. This paradigm shift is critical for fields ranging from cosmology and fluid dynamics to materials science and climate modeling, where traditional approaches are often limited by computational cost or data sparsity.

My work in Emulation and Inference has focused on developing novel machine learning and probabilistic modeling techniques to tackle these challenges across diverse scientific domains. I have developed a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, which utilizes advanced machine learning architectures to rapidly predict the cosmological matter power spectrum. This emulator significantly accelerates parameter inference via Markov Chain Monte Carlo (MCMC) simulations, enabling efficient exploration of complex cosmological models.

Furthermore, I have contributed to the development of a Probabilistic Neural Network-based reduced-order surrogate for fluid flows. This method creates a highly efficient, data-driven model that not only predicts complex fluid dynamics but also quantifies the inherent uncertainties in these predictions. My research also includes a method for Global Field Reconstruction from Sparse Sensors using Voronoi Tessellation, demonstrating robust techniques for inferring complete spatial fields from limited measurement points. This is complemented by my work on the Application of Probabilistic Modeling and Automated Machine Learning Framework for High-Dimensional Stress Fields, where I have applied advanced statistical and AutoML techniques to efficiently analyze and interpret complex, high-dimensional stress data, providing critical insights for material characterization and structural integrity assessments.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png" alt="Figure from Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/global-field-reconstruction-from-sparse-sensors-wi_plot_1_93ef286c.png" alt="Figure from Global field reconstruction from sparse sensors with Voronoi tessellation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Global field reconstruction from sparse sensors with Voronoi tessellation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
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
