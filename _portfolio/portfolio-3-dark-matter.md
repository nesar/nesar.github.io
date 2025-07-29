---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter, an elusive substance comprising approximately 27% of the universe's mass-energy content, plays a pivotal role in the standard cosmological model. Its gravitational influence is essential for explaining the formation and evolution of large-scale structures, from individual galaxies to vast galaxy clusters. Without dark matter, current cosmological simulations fail to reproduce the observed rotational curves of galaxies, the gravitational lensing of distant objects, or the distribution of temperature anisotropies in the Cosmic Microwave Background. Therefore, understanding dark matter's properties and distribution is fundamental to a complete picture of the cosmos.

The universe's large-scale structure is often described as a "cosmic web," a vast network of gravitationally bound dark matter haloes, connected by filaments, and interspersed with immense voids. This intricate web is the scaffolding upon which baryonic matter collects, forming galaxies and clusters. Investigating the morphology, topology, and dynamics of this cosmic web provides crucial insights into the underlying nature of dark matter and gravity. Furthermore, some cosmological models explore modifications to General Relativity, such as f(R) gravity, as alternative explanations for cosmic acceleration or as ways to reconcile discrepancies without invoking exotic dark matter particles, necessitating precise observational constraints on these theories.

My research delves into these critical areas of dark matter and cosmology, employing cutting-edge analytical and observational techniques. I have significantly contributed to constraining alternative gravity theories like f(R) gravity through a novel k-cut cosmic shear analysis of data from the Hyper Suprime-Cam, providing stringent limits on deviations from General Relativity. My work also focuses on detailed mapping of the Milky Way's stellar distribution using photometric samples of 2.6 million Red Clump stars, enabling a better understanding of our galaxy's potential and its inner-to-outer structure.

Furthermore, I have developed and applied advanced methods to characterize the dark matter distribution and the cosmic web. This includes the "caustic design" of dark matter haloes, providing a unique multistream view that reveals the complex substructures arising from gravitational collapse. Through topological and geometrical analyses, I have extensively mapped the multi-stream portrait of the cosmic web, highlighting its intricate filamentary and void network. My contributions extend to utilizing large datasets like the SPTpol Extended Cluster Survey to trace the cosmic web, demonstrating how clusters serve as key nodes in this vast cosmic architecture, and providing a comprehensive understanding of the universe's large-scale structure from both theoretical and observational perspectives.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
  </div>
</div>


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
