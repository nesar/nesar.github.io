---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Cosmology seeks to understand the origin, evolution, and large-scale structure of the universe. A cornerstone of the current standard model of cosmology, Lambda-CDM, is the existence of dark matter – an enigmatic substance that does not interact with light but accounts for approximately 27% of the universe's mass-energy content. Dark matter is crucial for explaining the formation of galaxies, galaxy clusters, and the large-scale cosmic web structure we observe today, acting as the gravitational scaffold upon which baryonic matter collects. Despite its profound gravitational influence, the fundamental nature of dark matter remains one of the most significant unsolved mysteries in physics.

Investigating dark matter and its role in cosmic evolution involves a multifaceted approach, combining observational cosmology with theoretical modeling and numerical simulations. Researchers employ techniques such as cosmic shear analysis, which probes the subtle distortions of distant galaxy shapes due to foreground dark matter distributions, and studies of the large-scale distribution of galaxies and galaxy clusters, which trace the underlying dark matter web. Understanding the fine-grained structure of the cosmic web – including the formation of dark matter haloes and the intricate filamentary network – is paramount to testing cosmological models and even alternative theories of gravity that aim to explain cosmic acceleration or modify general relativity on vast scales.

The distribution of dark matter extends from the largest cosmic structures down to the smallest scales, influencing the dynamics of individual galaxies like our own Milky Way. By studying the kinematics and distribution of stars within galaxies, particularly in the halo regions, scientists can infer the properties and extent of their dark matter content. Furthermore, insights into the early universe and the formation of the first stars and galaxies can be gleaned from examining the most pristine, metal-poor stars, whose chemical compositions carry imprints of the earliest stellar generations and the conditions of the nascent galactic halo where dark matter began to clump.

My research program is dedicated to unraveling the mysteries of dark matter and its profound impact on the universe's structure and evolution, employing a diverse array of advanced analytical and observational techniques. I have conducted extensive studies on the intricate architecture of the cosmic web, developing innovative methodologies, including "multistream views" and "caustic design" analysis, to depict the complex topological and geometrical properties of dark matter distributions arising from N-body simulations. This work provides a highly detailed portrait of the dark matter web, revealing its hierarchical formation and internal dynamics from simulations to tracing the cosmic web in observations.

Furthermore, my contributions extend to rigorously testing cosmological models and alternative theories of gravity. I have applied a "k-cut cosmic shear analysis" to Hyper Suprime-Cam first-year data, for example, to place robust constraints on $f(R)$ modified gravity models, which propose deviations from Einstein's General Relativity on cosmological scales. Beyond large-scale structure, I have delved into understanding the dark matter halo of our own Milky Way, utilizing vast photometric samples of stars such as 2.6 million Red Clump stars and Carbon-Enhanced Metal-Poor candidates from *Gaia* DR3. This work allows for precise mapping of stellar populations from the inner to outer Milky Way, providing crucial observational constraints on the distribution and properties of its dark matter halo. My involvement in projects like the SPTpol Extended Cluster Survey has further contributed to characterizing galaxy clusters and their role as powerful cosmological probes, enhancing our understanding of the universe's large-scale structure and evolution.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from topology and geometry of the dark matter web a mul" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: topology and geometry of the dark matter web a mul</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from the caustic design of the dark matter web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: the caustic design of the dark matter web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_2_ec781175.png" alt="Figure from topology and geometry of the dark matter web a mul" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: topology and geometry of the dark matter web a mul</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_3_a3b0a1c0.png" alt="Figure from the caustic design of the dark matter web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: the caustic design of the dark matter web</div>
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
