---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference <br/><img src='/images/research_emulation-inference.png'>"
collection: portfolio
---

Developing statistical emulators, surrogate models, and uncertainty quantification methods for cosmological simulations and scientific inference.

## Research Figures

<div class="research-figures-grid">
  <div class="research-figure">
    <img src="/images/research/figures/probabilistic_neural_network-based_reduced-order_s_page5_fig1_68f5e3f1.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)">
    <p class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</p>
  </div>
</div>

<style>
.research-figures-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.research-figure {
  text-align: center;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  transition: transform 0.2s ease;
}

.research-figure:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.research-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.research-figure img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.85em;
  color: #6c757d;
  margin-top: 0.5rem;
  line-height: 1.3;
}

/* Modal styles */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  padding-top: 5%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}
</style>

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

// Close modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}
</script>

## Related Publications:

- **MGemu: An emulator for cosmological models beyond general relativity** (2025) - Zenodo
- **Constraining Early Dark Energy Models with Power Spectra Emulators** (2025) - Bulletin of the American Physical Society
- **Data-Efficient Dimensionality Reduction and Surrogate Modeling of High-Dimensional Stress Fields** (2025) - Journal of Mechanical Design
- **High-dimensional Surrogate Modeling for Image Data with Nonlinear Dimension Reduction** (2024) - Preprint
- **Application of probabilistic modeling and automated machine learning
  framework for high-dimensional stress field** (2023) - Preprint
- **Interpretable Uncertainty Quantification in AI for HEP** (2022) - Preprint
- **AI for High Energy Physics: Interpretable Uncertainty Quantification** (2022) - Bulletin of the American Physical Society
- **Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation** (2021) - Physica D: Nonlinear Phenomena
- **Global field reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning** (2021) - Nature Machine Intelligence
- **Matter power spectrum emulator for  modified gravity cosmologies** (2021) - Physical Review D
- **Probabilistic neural networks for fluid flow surrogate modeling and data recovery** (2020) - Phys. Rev. Fluids 5, 104401 (2020)
- **Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies** (2020) - Phys. Rev. D 103, 123525 (2020)
- **Probabilistic neural network-based reduced-order surrogate for fluid flows** (2020) - arXiv preprint arXiv:2012.08719
- **Probabilistic neural networks for fluid flow model-order reduction and data recovery** (2020) - arXiv preprint arXiv:2005.04271
