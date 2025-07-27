---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Cosmology fundamentally seeks to unravel the Universe's composition, origin, and evolution. A cornerstone of this endeavor is understanding dark matter, an enigmatic substance that, despite its elusive nature, accounts for approximately 27% of the Universe's mass-energy budget. Its gravitational dominance is indispensable for explaining observed galactic rotation curves, galaxy cluster dynamics, and the formation of large-scale structures, which coalesce into an intricate network known as the cosmic web. This cosmic web, comprised of dense nodes, filaments, and vast voids, serves as the scaffolding upon which visible matter aggregates to form galaxies and clusters.

Investigating dark matter and the cosmic web relies on sophisticated observational probes. Weak gravitational lensing, which measures the subtle distortion of light from distant galaxies by intervening mass, provides a direct avenue for mapping the underlying dark matter distribution. Large-scale galaxy surveys and catalogs of galaxy clusters further constrain the distribution of baryonic matter, acting as tracers for the invisible dark matter skeleton. Additionally, precise measurements of stellar kinematics and populations within galaxies can illuminate the properties of the dark matter halos in which they reside. While the Cold Dark Matter (CDM) model currently stands as the leading paradigm, alternative gravitational theories, such as f(R) gravity, offer different explanations for cosmological phenomena without invoking exotic dark matter particles, necessitating rigorous observational tests.

My research extensively delves into characterizing the fundamental nature and intricate distribution of dark matter and the cosmic web. I have pioneered and applied methodologies like the "multi-stream" view to comprehensively characterize the "topology and geometry of the dark matter web" and dark matter haloes, providing a detailed "multi-stream portrait of the Cosmic web." This innovative approach helps dissect how different streams of matter converge and contribute to the formation of structures. Furthermore, I have explored the "caustic design of the dark matter web," utilizing unique features in the dark matter phase space to delineate structure, and employed stellar populations, such as a "photometric sample of 2.6 million Red Clump stars" from the inner to outer Milky Way, to "trace the cosmic web" and map the gravitational potential within our own galaxy.

A significant portion of my work is dedicated to robustly constraining cosmological models and testing alternative gravity theories through cutting-edge observational data analysis. I have contributed to "constraining f(R) Gravity with a k-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data," a technique specifically designed to enhance precision in weak lensing measurements. Through involvement in projects like "The SPTpol Extended Cluster Survey," I have refined weak lensing methods for "reducing model error using optimised galaxy selection" to achieve more accurate "weak lensing cluster mass estimation," which is crucial for cosmological parameter inference. My research also extends to using "Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in Gaia DR3" as unique chemical tracers, providing insights into early galaxy formation and chemical evolution, which are intimately tied to the formation history of dark matter halos in the early Universe.

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
