---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Emulation and inference represent a critical frontier in modern computational science, addressing the inherent challenges of simulating complex physical systems and extracting meaningful insights from observational data. High-fidelity simulations, ranging from cosmological structure formation to turbulent fluid dynamics, are often computationally prohibitive, making extensive parameter space exploration or real-time analysis impractical. Emulators, also known as surrogate models, leverage advanced machine learning and statistical techniques to construct fast, accurate approximations of these expensive simulations. These surrogates enable rapid predictions, facilitating the robust inference of underlying physical parameters from noisy, sparse, or incomplete observational data, while critically quantifying the associated uncertainties.

The core objective within this domain is to develop computationally efficient and reliable tools that bridge the gap between theoretical models and real-world observations. This involves mastering techniques such as reduced-order modeling, which compresses high-dimensional system dynamics into lower-dimensional representations, and integrating probabilistic approaches to quantify the uncertainty inherent in both the models and the data. Successful emulation and inference strategies are transformative, allowing scientists and engineers to accelerate design cycles, explore novel physics, and make data-driven decisions with greater confidence across diverse fields.

My research focuses on developing and applying cutting-edge emulation and inference methodologies to tackle grand challenges in scientific computing, particularly in cosmology and fluid dynamics. I have developed probabilistic neural network-based reduced-order surrogates for fluid flows, enabling efficient and uncertainty-aware prediction of complex flow dynamics and facilitating data recovery from sparse sensor measurements. These models provide not only accurate predictions but also robust quantification of the predictive uncertainty, which is crucial for real-world applications.

Furthermore, I have contributed to the field of cosmology by developing a Matter Power Spectrum Emulator for f(R) modified gravity cosmologies. This emulator significantly accelerates the exploration of alternative gravity theories, allowing for rapid comparison with cosmological observations and robust inference of model parameters. My work also includes enhancing weak lensing cluster mass estimation through optimized galaxy selection, a key inference problem that reduces model error and improves the precision of cosmological parameter constraints. Additionally, I have advanced non-intrusive reduced-order models by utilizing Gaussian process emulation for latent-space time evolution, a technique that efficiently captures the temporal dynamics of complex systems with rigorous uncertainty quantification, further strengthening the capabilities of robust emulation and inference.

<div class="no-figures"><p>Representative figures will be added soon.</p></div>

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
