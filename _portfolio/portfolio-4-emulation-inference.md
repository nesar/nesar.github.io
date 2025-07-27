---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The fields of scientific emulation and inference are at the forefront of modern computational science, addressing the challenges posed by complex, data-rich systems across diverse disciplines. Emulation involves creating fast, accurate surrogate models of computationally expensive simulations, enabling rapid exploration of parameter spaces, uncertainty quantification, and real-time decision-making that would otherwise be intractable. Inference, on the other hand, focuses on extracting meaningful insights, predictions, and underlying physical parameters from noisy, incomplete, or high-dimensional observational data, often necessitating robust statistical and machine learning methodologies.

These research areas increasingly leverage advanced machine learning techniques, including deep learning, neural networks, and Gaussian processes, to build sophisticated models capable of capturing intricate non-linear relationships. A critical aspect of this work is the rigorous quantification of uncertainty, providing not just point estimates but also a reliable measure of confidence in predictions, essential for scientific discovery and high-stakes engineering applications. Key challenges include developing interpretable models, handling sparse or high-dimensional data effectively, and ensuring generalizability across diverse physical regimes. Applications span from fundamental physics and cosmology to engineering design and environmental modeling.

My research extensively contributes to this domain by developing and applying novel machine learning and probabilistic modeling frameworks for both emulation and inference tasks. I have developed probabilistic neural network-based reduced-order surrogates for complex fluid flows, enabling efficient simulation and data recovery while robustly quantifying prediction uncertainties. My work also includes leveraging Gaussian process emulation for the latent-space time evolution of reduced-order models and constructing fast and accurate matter power spectrum emulators for modified gravity cosmologies, significantly accelerating cosmological parameter inference.

Furthermore, I have focused on enhancing inference capabilities across various scientific datasets. This includes applying deep neural networks for peculiar velocity estimation from kinetic Sunyaev-Zel'dovich effect, developing machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z), and creating neural network-based point spread function deconvolution methods for astronomical imaging. Addressing data sparsity, I have also contributed to global field reconstruction using Voronoi tessellation-assisted deep learning and explored interpretable uncertainty quantification in AI for high-energy physics. My contributions aim to overcome computational bottlenecks, provide robust predictions with clear uncertainty estimates, and accelerate scientific discovery in fields ranging from astrophysics and cosmology to fluid dynamics and high-dimensional stress analysis.

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
