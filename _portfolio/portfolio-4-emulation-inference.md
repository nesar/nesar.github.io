---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The fields of scientific emulation and inference are critical for advancing our understanding of complex systems across diverse disciplines, from astrophysics and cosmology to fluid dynamics and high-energy physics. In an era of increasingly large datasets and computationally intensive simulations, emulation provides a powerful solution by creating fast, accurate surrogate models. These emulators learn the intricate relationships between input parameters and system outputs, enabling rapid exploration of vast parameter spaces, facilitating efficient uncertainty quantification, and accelerating scientific discovery by sidestepping the prohibitive cost of running full-fidelity simulations.

Complementing emulation, robust inference methodologies are essential for extracting meaningful insights and knowledge from observational data and simulation outputs. This involves not only estimating physical parameters but also rigorously quantifying the associated uncertainties. Accurate uncertainty quantification is paramount for building reliable scientific models, distinguishing between true signals and noise, and ensuring the trustworthiness of predictions. The synergistic integration of emulation and inference techniques allows for a comprehensive approach to data analysis and model validation, providing a foundation for data-driven discovery and robust scientific conclusions.

My research extensively explores the intersection of machine learning, emulation, and inference, with a strong focus on developing novel methodologies to tackle computationally intensive problems in scientific domains. I have developed and applied advanced machine learning techniques, including probabilistic neural networks and Gaussian process emulation, to create high-fidelity, reduced-order surrogates for complex fluid flows, enabling their latent-space time evolution and data recovery. This work provides significant speed-ups over traditional methods, crucial for real-time applications and extensive parameter sweeps.

Furthermore, my contributions extend to diverse areas of cosmology and astrophysics. I have built a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, allowing for efficient exploration of alternative gravity theories. I have also focused on improving inference capabilities, developing methods for interpretable uncertainty quantification in AI for high-energy physics and optimizing galaxy selection to reduce model error in weak lensing cluster mass estimation. My work on differentiable predictions for large-scale structure with SHAMNet and machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z) demonstrates a commitment to robust, uncertainty-aware inference. Moreover, I have applied deep neural networks for peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect, showcasing the power of deep learning for complex astrophysical inferences. These efforts collectively aim to accelerate scientific discovery, enhance the reliability of predictions, and provide interpretable insights with well-quantified uncertainties.

<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>

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
