---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The prevailing cosmological model posits that approximately 85% of the universe's matter content is composed of dark matter, a mysterious substance that does not interact with light but exerts gravitational influence. Dark matter is indispensable for explaining the formation and evolution of large-scale structures, such as galaxies and galaxy clusters, within the observed universe. Its gravitational pull acts as the cosmic scaffolding, dictating how ordinary baryonic matter collapses and forms the luminous structures we observe today. Understanding the nature and distribution of dark matter is therefore central to modern astrophysics and cosmology.

Research in cosmology extends beyond the direct detection of dark matter to investigating the intricate network it forms—the "cosmic web"—which comprises haloes, filaments, sheets, and voids. This cosmic web serves as the arena for galaxy formation and evolution, making its characterization crucial. Furthermore, the standard cosmological model, Lambda-CDM, is continuously tested against a wealth of observational data, including probes of alternative theories of gravity, the dynamics of galaxy formation, and the precise mapping of stellar populations in galactic environments. These investigations often rely on cutting-edge numerical simulations, sophisticated data analysis techniques, and next-generation observational surveys to unravel the universe's fundamental properties.

My research delves into the fundamental nature and intricate architecture of dark matter, particularly focusing on its fine-grained structure within haloes and the cosmic web. I have developed and applied multi-stream views to characterize the phase-space structure of dark matter haloes, revealing the complex caustic design that underlies these gravitational wells. My work explores the topology and geometry of the dark matter web, providing a detailed portrait of its interconnected filaments and nodes. Utilizing advanced methodologies, I have employed auxiliary-variable-guided generative models to uncover the physical drivers behind dark matter halo structures, thereby advancing our theoretical understanding through sophisticated machine learning techniques.

Beyond the intrinsic properties of dark matter, my contributions extend to constraining cosmological models and understanding galaxy formation. I have performed k-cut cosmic shear analyses using Hyper Suprime-Cam data to constrain alternative theories of gravity, specifically $f(R)$ gravity, pushing the boundaries of precision cosmology. My work also includes involvement in large-scale cluster surveys, such as the SPTpol Extended Cluster Survey, and developing robust methodologies for modeling galaxy formation within cosmological simulations like CRK-HACC. Furthermore, I have contributed to large-scale observational efforts, including building photometric samples of millions of red clump stars for Galactic structure studies, identifying carbon-enhanced metal-poor star candidates from Gaia DR3 spectra, and participating in future missions like SPHEREx, all of which provide crucial data for testing and refining our cosmological framework.

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
