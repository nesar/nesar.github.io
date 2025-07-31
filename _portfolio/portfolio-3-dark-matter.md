---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The standard cosmological model, Lambda-Cold Dark Matter (ΛCDM), posits that dark matter, an invisible substance interacting only gravitationally, constitutes approximately 27% of the universe's mass-energy content. Its gravitational influence is crucial for the formation and evolution of large-scale structures, including galaxies, galaxy clusters, and the intricate network known as the cosmic web. This cosmic web, an intricate network of filaments, sheets, and knots, is the scaffolding upon which visible matter aggregates, and understanding its topology, geometry, and evolution is paramount for testing cosmological models and inferring the nature of dark matter.

Beyond ΛCDM, alternative theories of gravity, such as f(R) gravity, are explored to explain observed cosmological phenomena and address potential tensions within the standard model. Observational probes like cosmic shear, which measures the subtle distortions of distant galaxy images due to intervening mass, and extensive galaxy cluster surveys provide powerful constraints on these models. Furthermore, dissecting the internal structure of galaxies, like our own Milky Way, through stellar population studies, offers a unique opportunity to map the local dark matter distribution and probe its interaction with baryonic matter. Studies of the earliest stars, characterized by their metal-poor nature, also provide critical insights into the chemical enrichment history of the universe and the conditions of the primordial cosmos.

My research extensively employs advanced analytical and observational techniques to probe the nature of dark matter and the large-scale structure of the universe. I have developed and applied methods to characterize the dark matter web and its constituent halos, analyzing their complex phase-space structure through a "multistream view" and the "caustic design" of their internal dynamics. This work elucidates the topology and geometry of these structures, providing a more complete "portrait" of the cosmic web. A significant part of my contribution involves using large-scale cosmological surveys: I have applied "k-cut cosmic shear analysis" to Hyper Suprime-Cam first-year data to constrain f(R) gravity models, pushing the boundaries of precision cosmology. Additionally, I have been involved in the "SPTpol Extended Cluster Survey," identifying and characterizing galaxy clusters that serve as vital probes of cosmological parameters.

Within our own galaxy, I have contributed to mapping the Milky Way's structure using a comprehensive "photometric sample of 2.6 million Red Clump stars," which provides unprecedented detail on the distribution of stars from the inner to the outer galaxy. This mapping helps infer the local dark matter halo properties. My work also extends to stellar archaeology, identifying "Carbon-Enhanced Metal-Poor star candidates" from Gaia DR3 BP/RP spectra. These rare stars are relics from the early universe, offering crucial insights into the chemical enrichment history from the first stars and the conditions of the nascent cosmos. Collectively, my research offers a multifaceted approach to understanding dark matter, from its distribution on cosmological scales to its local imprint within galaxies, leveraging diverse datasets and innovative analytical frameworks.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from Constraining f(R) Gravity with a k-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Constraining f(R) Gravity with a k-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
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
