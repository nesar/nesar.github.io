---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The rapidly advancing frontier of scientific discovery often relies on complex numerical simulations and sophisticated models to interpret observational data and predict phenomena. However, many state-of-the-art simulations, particularly in fields such as astrophysics, cosmology, and planetary science, are computationally prohibitive, requiring vast amounts of time and resources to explore large parameter spaces or perform robust statistical analyses. This computational bottleneck severely limits the ability of researchers to conduct comprehensive uncertainty quantification, perform detailed parameter inference, or iterate quickly on model development.

To overcome these challenges, the field of scientific machine learning has increasingly focused on the development of "emulators" or "surrogate models." An emulator is a fast, data-driven approximation of a more complex, computationally expensive simulation or model. By training machine learning algorithms, such as neural networks or Gaussian processes, on a smaller set of meticulously generated simulation outputs, these emulators can learn the underlying relationships and provide predictions orders of magnitude faster than the original model. This acceleration is crucial for enabling efficient "inference," where observational data are used to determine the most probable parameters of a physical model, often through techniques like Bayesian inference.

The application of emulators has revolutionized various research domains, allowing for deeper exploration of scientific hypotheses. For instance, in cosmology, emulators enable the rapid generation of cosmological observables needed for comparing theoretical models with observational data from galaxy surveys. Similarly, in exoplanetary science, emulators facilitate the swift computation of atmospheric spectra, a key step in characterizing the compositions and properties of distant planetary atmospheres. By bridging the gap between intricate theoretical models and the imperative for rapid, reliable analysis of observational data, emulation and inference techniques are essential tools for accelerating scientific progress.

My research directly addresses these computational barriers by developing and applying advanced machine learning techniques to construct efficient emulators for complex scientific models. I have specifically focused on leveraging the power of neural networks and Gaussian processes to create high-fidelity surrogate models that drastically reduce computational time while maintaining the necessary accuracy for scientific discovery. For instance, I have developed neural network emulators for accelerating cosmological N-body simulations, which are foundational for understanding the large-scale structure of the universe. These emulators accurately predict key cosmological observables, such as the non-linear matter power spectrum, enabling faster exploration of cosmological parameter space and more robust comparisons with observational data from current and future galaxy surveys.

Furthermore, my work has extended to the characterization of exoplanet atmospheres, where I have developed a Gaussian process emulator to facilitate Bayesian inference of exoplanet atmospheric compositions. Atmospheric models are inherently complex and computationally intensive, making traditional Bayesian sampling methods prohibitively slow. By replacing the full atmospheric model with a highly accurate Gaussian process emulator, I significantly accelerate the likelihood evaluations, allowing for efficient and comprehensive exploration of the posterior distribution for atmospheric parameters. This technical contribution enables the rapid and precise characterization of exoplanet atmospheres, providing crucial insights into planetary formation, evolution, and habitability.

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
