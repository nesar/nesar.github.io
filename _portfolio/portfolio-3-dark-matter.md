---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The current cosmological paradigm, the Lambda-Cold Dark Matter (ΛCDM) model, posits that the vast majority of the universe's mass-energy content comprises enigmatic components: dark matter and dark energy. Dark matter, accounting for approximately 27% of the universe's mass-energy, is crucial for explaining the formation and evolution of large-scale structures, from galaxies to galaxy clusters and the intricate cosmic web. Despite its gravitational influence, dark matter does not interact with light, making its direct detection and precise characterization one of the most significant challenges in modern astrophysics. Dark energy, composing about 68%, is responsible for the universe's accelerated expansion, further deepening the mysteries surrounding cosmic evolution.

Understanding the nature and distribution of dark matter necessitates sophisticated observational techniques and theoretical models. Weak gravitational lensing, the subtle distortion of distant galaxy images by intervening mass, provides a powerful tool to map the distribution of dark matter across vast cosmic scales. Galaxy surveys, mapping millions of galaxies, allow for the reconstruction of the cosmic web – the filamentary network of dark matter and baryonic matter that permeates the universe. Furthermore, studying the kinematics of stars within galaxies offers crucial insights into the gravitational potential, and thus the dark matter halo, of our own Milky Way and other galaxies, bridging galactic scales with cosmological ones.

My research significantly contributes to addressing these fundamental questions by developing and applying advanced methodologies across multiple observational domains. I have focused on leveraging weak gravitational lensing techniques, including k-cut cosmic shear analysis of Hyper Suprime-Cam (HSC) data, to constrain cosmological models such as f(R) gravity, which offers an alternative to dark energy. My work also encompasses optimizing galaxy selection strategies for weak lensing cluster mass estimation, reducing model error and enhancing the precision of cluster surveys like the SPTpol Extended Cluster Survey. These efforts are crucial for accurately probing the mass distribution of dark matter in galaxy clusters, key cosmological probes.

Beyond large-scale structures, I have deeply investigated the intricate geometry and topology of the dark matter web using a multi-stream view, developing techniques like the "caustic design" to characterize the complex flow of dark matter. This approach provides a granular understanding of dark matter haloes and their evolution within the cosmic web. Additionally, my research extends to understanding our own Milky Way's dark matter distribution through the precise photometric analysis of 2.6 million Red Clump stars, mapping the stellar population from the inner to outer galaxy. I have also explored Carbon-Enhanced Metal-Poor star candidates from Gaia DR3 spectra, which serve as ancient tracers, offering unique insights into the earliest phases of galactic formation and the dark matter halo assembly in the context of the cosmic web. Collectively, my work advances our understanding of dark matter's fundamental properties and its role in shaping the universe.

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
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_3_75c6be1f.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
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
