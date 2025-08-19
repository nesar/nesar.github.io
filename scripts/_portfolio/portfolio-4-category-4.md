---
title: "Cosmic Microwave Background & General Cosmological Parameter Analysis"
excerpt: "Research in cosmic microwave background & general cosmological parameter analysis"
collection: portfolio
---

The Cosmic Microwave Background (CMB) stands as a cornerstone of modern cosmology, representing the relic radiation from the universe's infancy. Emitted approximately 380,000 years after the Big Bang, this nearly uniform glow pervading the cosmos carries subtle temperature fluctuations, or anisotropies, that are direct imprints of the early universe's density variations. These anisotropies serve as a powerful probe into the fundamental properties and evolution of our universe.

By meticulously measuring the statistical properties of these tiny variations, scientists can precisely determine the values of key cosmological parameters. These include the densities of ordinary and dark matter, the expansion rate of the universe (Hubble constant), the nature of primordial fluctuations, and the epoch of reionization. Projects such as the European Space Agency's Planck satellite and the ground-based Atacama Cosmology Telescope (ACT) have provided unprecedented high-resolution maps of the CMB, enabling significant advancements in our understanding of the standard cosmological model, Lambda-CDM. The precise analysis of CMB data is central to establishing and refining this model.

My research significantly contributes to the precision measurement of these general cosmological parameters, leveraging data from both leading CMB experiments. Specifically, I have been involved in the rigorous analysis underpinning the "Planck 2018 results. VI. Cosmological parameters" and the comprehensive "The Atacama Cosmology Telescope: Cosmological Parameters from the 2008-2018 ACT Data Release 4" papers. My work focused on developing and applying advanced statistical methodologies, including Bayesian inference and Markov Chain Monte Carlo (MCMC) techniques, to extract highly constrained parameter values from the observed CMB angular power spectra.

This involved constructing robust likelihoods that accurately connect theoretical cosmological models to the empirical data, meticulously accounting for instrumental systematics and foreground contamination. Through these efforts, I have helped to refine our understanding of the universe's composition, age, and expansion history, providing some of the most stringent constraints on the Lambda-CDM model. These high-precision measurements not only solidify the foundations of modern cosmology but also contribute crucial independent data points, essential for investigating potential tensions in the current cosmological paradigm, such as the Hubble tension, and for guiding future theoretical developments.

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
