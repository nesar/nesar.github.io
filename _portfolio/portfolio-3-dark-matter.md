---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe's composition and evolution are governed by enigmatic components, notably dark matter and dark energy, which together constitute approximately 95% of its mass-energy budget. Understanding their nature and influence is central to modern cosmology. Dark matter, invisible yet gravitationally dominant, orchestrates the formation of large-scale structures, from galaxy halos to the intricate cosmic web. However, its fundamental particle nature remains unknown, prompting investigations into both its standard cold dark matter (CDM) paradigm and alternative theories, such as modified gravity, which propose deviations from General Relativity on cosmological scales.

Cosmological research employs a diverse toolkit to probe these mysteries, ranging from precision measurements of the cosmic microwave background to large-scale structure surveys. Techniques like cosmic shear, which analyzes distortions in distant galaxy shapes caused by intervening mass, provide crucial constraints on cosmological parameters and tests of gravitational theories like f(R) gravity. Similarly, identifying and characterizing massive galaxy clusters through surveys offers insights into the growth of structure over cosmic time. Unraveling the substructure within dark matter halos and the filamentary cosmic web, a complex network of galaxies and dark matter, requires advanced analytical and computational methods to trace its topology and dynamics.

My research extensively contributes to these areas, developing and applying novel methodologies to address fundamental questions in dark matter and cosmology. I have, for instance, employed a k-cut cosmic shear analysis of Hyper Suprime-Cam first-year data to derive stringent constraints on f(R) gravity models, pushing the boundaries of modified gravity tests. Recognizing the importance of stellar tracers, I have constructed a large photometric sample of 2.6 million Red Clump stars across the Milky Way, providing a robust dataset for mapping our galaxy's structure and dynamics, which are intimately linked to its dark matter halo. Furthermore, I have pioneered the application of the caustic technique and multi-stream analysis to unravel the intricate design, topology, and geometry of the dark matter web and dark matter haloes, revealing their complex substructure and dynamic evolution.

My work also encompasses analysis of large-scale observational datasets and the identification of unique stellar populations. I have participated in the SPTpol Extended Cluster Survey, contributing to the characterization of massive galaxy clusters, critical probes of cosmological growth. In stellar archaeology, I have identified Carbon-Enhanced Metal-Poor (CEMP) star candidates using BP/RP spectra from Gaia DR3, providing invaluable insight into the early universe's chemical enrichment and the formation of the first stars, which influence the early dark matter distribution. By tracing the cosmic web through various methods, my research collectively enhances our understanding of the universe's large-scale architecture, the nature of dark matter, and the validity of gravitational theories on cosmic scales.

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
