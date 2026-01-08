---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe is largely composed of dark matter, a mysterious substance that does not interact with light but exerts profound gravitational influence, forming the foundational scaffolding upon which galaxies and larger cosmic structures are built. Understanding dark matter's properties and its distribution is central to modern cosmology, as it dictates the evolution of the cosmos from the Big Bang to the present day. Its gravitational clustering leads to the formation of the intricate "cosmic web," a vast network of voids, sheets, filaments, and dense haloes that defines the large-scale structure of the universe and shapes galaxy formation.

Probing dark matter and the cosmic web requires a multifaceted approach, combining sophisticated observational techniques with advanced theoretical modeling and numerical simulations. Weak gravitational lensing, which measures the subtle distortions of background galaxy shapes by foreground mass distributions, serves as a crucial tool for mapping dark matter directly. Simultaneously, extensive stellar surveys provide kinematic and photometric data to infer dark matter's presence and distribution within galaxies, while cosmological simulations model the growth of structure under various dark matter and gravitational theories, including alternatives like f(R) gravity, which modify Einstein's general relativity at cosmological scales.

My research significantly contributes to these efforts by developing and applying cutting-edge techniques to unravel the mysteries of dark matter and cosmic evolution. I have advanced methods for constraining modified gravity theories, such as f(R) gravity, through the application of a k-cut cosmic shear analysis to large datasets like the Hyper Suprime-Cam first-year data. This work, alongside improving weak lensing cluster mass estimation by optimizing galaxy selection, reduces model errors and yields more precise cosmological parameters. A core area of my focus has been to meticulously characterize the dark matter web itself, exploring its topology, geometry, and multi-stream nature using detailed analyses that reveal its intricate caustic design and the complex flow of dark matter. I have also contributed to the development and application of cosmological simulations, such as CRK-HACC, to model galaxy formation within these evolving dark matter structures.

Furthermore, my work extends to mapping the distribution of dark matter within the Milky Way and other galaxies by analyzing large stellar samples. I have utilized extensive photometric samples of millions of Red Clump stars to trace galactic structure from the inner to outer Milky Way, providing crucial insights into the halo's properties and evolution. Complementary to this, I have leveraged data from missions like Gaia DR3 to identify rare stellar populations, such as Carbon-Enhanced Metal-Poor star candidates from BP/RP spectra, which act as invaluable probes of early galactic formation and chemical enrichment histories. My involvement in major observational initiatives like the SPHEREx Satellite Mission and the SPTpol Extended Cluster Survey also underscores my commitment to driving advancements in observational cosmology. Collectively, my contributions provide robust constraints on cosmological models, enhance our understanding of the cosmic web's formation and evolution, and refine our picture of galaxy assembly within a dark matter dominated universe.

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
