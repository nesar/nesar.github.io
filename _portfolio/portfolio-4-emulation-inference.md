---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Emulation and inference represent a rapidly evolving frontier in computational science, addressing the inherent challenges of highly complex and computationally intensive simulations. In fields ranging from astrophysics and cosmology to fluid dynamics and materials science, researchers frequently encounter systems governed by intricate physics, requiring vast computational resources to model accurately. Emulators, or surrogate models, provide a powerful solution by learning the input-output relationships of these complex systems, enabling rapid and accurate predictions without the need for full-scale simulations. This capability is crucial for accelerating design optimization, exploring vast parameter spaces, and performing robust scientific inference.

The development of sophisticated emulation techniques often leverages advanced machine learning methodologies, including neural networks, Gaussian processes, and various forms of reduced-order modeling. These approaches not only aim to replicate simulation outputs but also to quantify uncertainties inherent in their predictions, providing a probabilistic understanding of system behavior. By compressing high-dimensional data into low-dimensional latent spaces, or by constructing non-intrusive surrogates, these methods significantly reduce the computational burden, allowing for real-time analysis, inverse problem solving, and the efficient analysis of large datasets where traditional methods would be intractable.

My research significantly contributes to this landscape by developing cutting-edge emulation and inference tools for diverse scientific domains. In cosmology, for instance, I have developed innovative methodologies to refine critical measurements, such as weak lensing cluster mass estimation. This includes reducing model error through optimized galaxy selection strategies, enhancing the precision of cosmological parameters. Furthermore, I have engineered a Matter Power Spectrum Emulator specifically for f(R) modified gravity cosmologies, which dramatically accelerates the exploration of alternative gravity theories, enabling robust constraints on cosmological models against observational data.

Extending these capabilities to complex physical systems, my work also encompasses the development of advanced surrogate models for fluid flows. I have pioneered the use of probabilistic neural networks (PNNs) for fluid flow surrogate modeling, providing not only efficient predictions but also crucial uncertainty quantification and data recovery capabilities for sparse or noisy datasets. Additionally, I have explored the latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation for accurate and efficient prediction of dynamic system behavior. Collectively, these contributions provide powerful, data-driven frameworks for accelerating scientific discovery, enabling the design of more efficient systems, and extracting deeper insights from complex scientific data across multiple disciplines.

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
