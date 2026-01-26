---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Cosmology endeavors to understand the origin, evolution, and large-scale structure of the universe. A cornerstone of the current standard model, Lambda-CDM, posits the existence of dark matter and dark energy, which together constitute over 95% of the cosmos's mass-energy budget. Dark matter, a mysterious non-baryonic substance, dictates the formation and growth of cosmic structures, from galaxies to vast galaxy clusters, by providing the gravitational scaffolding upon which luminous matter collapses. Unraveling its nature and distribution is paramount to understanding the universe we observe.

Research in this field often involves large-scale astronomical surveys, advanced N-body and hydrodynamical simulations, and sophisticated statistical analysis techniques to probe the distribution of dark matter and its influence. Key areas of investigation include characterizing the dark matter halo population, mapping the intricate filamentary network known as the "cosmic web" where galaxies reside, and testing alternative theories of gravity, such as f(R) gravity, that might explain cosmic acceleration. These efforts aim to precisely constrain cosmological parameters and scrutinize the foundations of our understanding of gravity on cosmic scales.

My research significantly contributes to these frontiers by developing and applying innovative methodologies to probe the dark universe. I have utilized cosmic shear analysis, specifically a k-cut technique applied to Hyper Suprime-Cam First-Year data, to place stringent constraints on f(R) modified gravity models, testing fundamental physics at cosmological scales. A substantial portion of my work focuses on elucidating the structure and dynamics of dark matter, employing multi-stream analysis to reveal the intricate caustic design of dark matter haloes and the topology and geometry of the cosmic web. This multi-stream perspective provides an unprecedented view into the fine-grained structure of dark matter, tracing its complex flows and identifying coherent substructures.

Beyond theoretical aspects of dark matter distribution, my work extends to modeling galaxy formation within these structures using cosmological simulations like CRK-HACC, bridging the gap between dark matter dynamics and observable galaxies. I have also leveraged large astronomical datasets to trace and understand cosmic structures, from identifying a photometric sample of 2.6 million Red Clump stars across the Milky Way as precise distance indicators, to searching for Carbon-Enhanced Metal-Poor (CEMP) star candidates from Gaia DR3 BP/RP spectra, which serve as relics of early star formation within dark matter haloes. Furthermore, I contribute to major observational missions such as the SPHEREx satellite and the SPTpol Extended Cluster Survey, poised to deliver crucial data for future cosmological analyses and deepen our understanding of dark matter, galaxy evolution, and the large-scale structure of the universe.

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
