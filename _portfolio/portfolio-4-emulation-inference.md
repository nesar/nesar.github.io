---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The rapidly expanding frontiers of scientific and engineering research are increasingly reliant on complex computational models and vast datasets. Many high-fidelity simulations, while crucial for accurate representation, are computationally expensive and time-consuming, hindering thorough exploration of parameter spaces or real-time decision-making. This challenge necessitates the development of advanced techniques for "emulation," which involves creating fast, surrogate models that mimic the behavior of complex systems, enabling rapid predictions without the need for full simulations. Concurrently, extracting reliable insights from noisy, high-dimensional data requires robust "inference" methods that can quantify uncertainties, account for model errors, and provide statistically sound conclusions, from astrophysical observations to material properties.

Emulation and inference, often powered by cutting-edge machine learning and statistical methodologies, are therefore foundational to accelerating scientific discovery and engineering innovation. Emulators, ranging from Gaussian Process models to deep neural networks, allow researchers to explore complex system behaviors across a broad range of inputs, facilitating sensitivity analysis, optimization, and uncertainty propagation. Probabilistic inference frameworks, on the other hand, provide a rigorous lens through which to interpret observational data or simulation outputs, allowing for the estimation of physical parameters, the identification of patterns, and the quantification of confidence in predictions, which is paramount for drawing meaningful and trustworthy conclusions.

My work primarily focuses on the development and application of advanced computational and statistical methods at the intersection of emulation and probabilistic inference across diverse scientific domains. I have developed sophisticated emulators, such as a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, to rapidly predict complex astrophysical phenomena, and leveraged probabilistic neural network-based reduced-order surrogates for high-fidelity fluid flows, enabling efficient design and analysis without resorting to prohibitively expensive simulations. My contributions extend to novel approaches for modeling the latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation, tackling dynamic systems effectively.

A core aspect of my research involves robust probabilistic inference, evident in methods for reducing model error in weak lensing cluster mass estimation through optimized galaxy selection, and identifying unique stellar populations like Carbon-Enhanced Metal-Poor stars from vast astronomical datasets. Furthermore, I have applied probabilistic modeling and automated machine learning frameworks to complex, high-dimensional problems such as stress field analysis and fluid flow data recovery, ensuring reliable predictions and rigorous uncertainty quantification. These methodologies consistently integrate uncertainty quantification, a critical element for generating trustworthy predictions and informed decision-making across diverse scientific and engineering disciplines, from cosmology and astrophysics to fluid dynamics and materials science.

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
