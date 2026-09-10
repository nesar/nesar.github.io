---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The study of Dark Matter is central to modern cosmology, addressing one of the most significant mysteries in our understanding of the universe. Observations across a vast range of scales, from the rotation curves of galaxies to the large-scale structure of the cosmos, indicate that approximately 85% of the universe's matter content is composed of a mysterious, non-luminous substance that interacts only gravitationally. This invisible component, known as dark matter, provides the gravitational scaffolding necessary for the formation and evolution of galaxies and the intricate cosmic web.

The standard cosmological model, Lambda-CDM, posits that dark matter, alongside dark energy and baryonic matter, dictates the universe's expansion history and the growth of structures. However, the precise nature of dark matter remains unknown, prompting active research into its fundamental properties and its role in shaping the cosmos. Researchers employ diverse methodologies, including gravitational lensing, large-scale galaxy surveys, high-resolution cosmological simulations, and tests of alternative theories of gravity, to unravel the enigma of dark matter and refine our cosmological models. A key focus is to characterize the dark matter distribution, particularly the formation and properties of dark matter halos, which host galaxies, and the large-scale structure of the Cosmic Web.

My research significantly contributes to understanding the intricate architecture and dynamics of the Dark Matter Web. I have developed and applied advanced techniques, including multi-stream analysis and topological methods, to precisely characterize the complex structures of dark matter halos and the large-scale distribution of matter. Specifically, my work explores the "caustic design" of the dark matter web and provides a "multistream portrait" to illuminate its density and velocity substructures, tracing the cosmic web at various scales. Furthermore, I have leveraged auxiliary-variable-guided generative models to uncover the physical drivers governing dark matter halo structures and have contributed to improving galaxy formation models within cosmological simulations like CRK-HACC, providing a more robust framework for interpreting observational data.

In addition to studying dark matter dynamics, I have actively contributed to testing alternative theories of gravity, such as $f(R)$ gravity, using cutting-edge "k-cut cosmic shear analysis" of data from major surveys like the Hyper Suprime-Cam First-Year Data. My research also refines weak gravitational lensing techniques for more accurate cluster mass estimation by optimizing galaxy selection, thereby reducing model error. Furthermore, I engage with large observational datasets from missions like SPHEREx and surveys like the SPTpol Extended Cluster Survey to constrain cosmological parameters. I also utilize stellar populations, such as Red Clump stars and Carbon-Enhanced Metal-Poor star candidates from Gaia DR3, to trace the Milky Way's dark matter halo and probe galactic structure from the inner to outer regions.

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
