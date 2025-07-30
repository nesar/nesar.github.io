---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter, an elusive component that makes up approximately 27% of the universe's mass-energy budget, plays a pivotal role in the formation and evolution of cosmic structures. Its gravitational influence is evident from galactic rotation curves to the largest scales of the universe, yet its fundamental nature remains one of the most significant unsolved problems in modern physics and cosmology. Understanding dark matter's distribution, dynamics, and interaction is crucial for a complete picture of the cosmos.

The universe's large-scale structure, often referred to as the Cosmic Web, is a vast network of gravitationally bound dark matter haloes, connected by filaments, interspersed with walls, and enclosing large voids. This intricate architecture, predicted by cosmological simulations and observed through galaxy surveys, provides a powerful laboratory for testing cosmological models, including the standard Lambda-CDM paradigm and alternative theories of gravity like f(R) gravity. Probing this web requires sophisticated observational techniques and advanced analytical methods to extract its underlying physical properties.

My research focuses on unraveling the mysteries of dark matter and the Cosmic Web through a combination of theoretical insights and advanced observational data analysis. I have developed and applied novel multi-stream techniques to dissect the intricate phase-space structure of dark matter, revealing the "caustic design" and multi-stream nature of dark matter haloes and the broader Cosmic Web. This approach provides a detailed kinematic portrait of dark matter, moving beyond simple density profiles to understand the formation history and dynamics of these structures. My work involves tracing the cosmic web and identifying its components through the analysis of kinematic features, offering a unique perspective on cosmic structure formation.

Furthermore, I have contributed to constraining fundamental cosmological parameters and alternative theories of gravity by performing advanced cosmic shear analyses. Specifically, I have utilized the k-cut cosmic shear method on large datasets such as the Hyper Suprime-Cam First-Year Data to place robust constraints on f(R) gravity models, providing crucial tests for modifications to General Relativity on cosmological scales. Beyond dark matter dynamics, I have leveraged large photometric surveys, including Red Clump stars and Gaia DR3, to map the Milky Way's structure and identify unique stellar populations like Carbon-Enhanced Metal-Poor stars. These stars serve as invaluable probes for understanding early galactic evolution. I have also participated in extended cluster surveys, such as the SPTpol survey, to identify and characterize large galaxy clusters, which are key cosmological probes. These diverse approaches contribute significantly to our understanding of the universe's composition, evolution, and underlying gravitational laws.

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
