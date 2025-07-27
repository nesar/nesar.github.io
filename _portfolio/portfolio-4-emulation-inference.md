---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The fields of emulation and inference are at the forefront of modern scientific discovery and engineering, offering powerful tools to navigate the complexities of high-dimensional systems and vast datasets. Emulation involves creating fast, accurate surrogate models that mimic the behavior of computationally expensive simulations, enabling rapid exploration of parameter spaces and real-time predictions. Inference, conversely, leverages these models, often in conjunction with observed data, to deduce fundamental physical parameters, underlying processes, or reconstruct missing information. Together, these disciplines accelerate research by replacing prohibitive computational costs with efficient machine learning approximations, thereby democratizing access to sophisticated modeling capabilities.

At the heart of many advanced emulation and inference techniques lies the integration of machine learning, particularly deep learning and Gaussian processes. These methodologies are adept at learning complex, non-linear relationships directly from data, making them ideal for constructing robust surrogates for phenomena ranging from cosmological structure formation to intricate fluid dynamics. A critical aspect of this research area is the emphasis on uncertainty quantification, ensuring that predictions and inferences are not only efficient but also accompanied by reliable estimates of their precision, which is crucial for scientific rigor and trustworthy decision-making.

My research extensively contributes to this rapidly evolving landscape, focusing on the development and application of novel machine learning frameworks for addressing grand challenges in astrophysics, cosmology, and computational fluid dynamics. I have consistently aimed to bridge the gap between cutting-edge data science techniques and complex scientific problems, delivering solutions that accelerate understanding, enable precise parameter estimation, and offer robust predictive capabilities with quantified uncertainties.

My research extensively focuses on developing differentiable and probabilistic models for scientific applications. In cosmology, I spearheaded the creation of SHAMNet for differentiable predictions of large-scale structure, facilitating efficient parameter inference, and developed a matter power spectrum emulator for f(R) modified gravity cosmologies. My work also includes SYTH-Z for machine learning synthetic spectra and probabilistic redshift estimation, and deep neural networks for peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect. For scientific computing and fluid dynamics, I pioneered the use of probabilistic neural networks for robust reduced-order surrogate modeling and data recovery, and explored Gaussian process emulation for latent-space time evolution of non-intrusive reduced-order models. This body of work underscores my commitment to advancing scientific discovery through innovative, uncertainty-aware, and computationally efficient machine learning methodologies.

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
