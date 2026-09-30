---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The vast universe is profoundly shaped by dark matter, an enigmatic substance accounting for approximately 85% of its total matter content. While invisible, its gravitational influence is paramount, driving the formation of the large-scale structure of the cosmos, often described as a "cosmic web" of filaments, sheets, and dense halos. These dark matter halos serve as gravitational potential wells where ordinary baryonic matter accumulates, eventually leading to the birth and evolution of galaxies and galaxy clusters. Understanding the distribution, properties, and dynamics of dark matter is central to modern cosmology, particularly in validating and refining the prevailing Lambda-CDM model.

The study of dark matter and cosmology employs a diverse array of methodologies, from large-scale observational surveys to sophisticated numerical simulations. Weak gravitational lensing, the subtle distortion of distant galaxy images by intervening mass, provides a powerful tool to map the distribution of dark matter directly. Cosmological simulations are crucial for modeling the growth of structure from the early universe to the present day, allowing researchers to test theoretical predictions and interpret observational data. Furthermore, investigating alternative gravitational theories, such as $f(R)$ gravity, offers pathways to address persistent cosmological puzzles, including the nature of dark energy, which drives the accelerated expansion of the universe.

My research extensively explores the fundamental properties of dark matter and its role in shaping the cosmic tapestry. I have focused on characterizing the intricate substructure within dark matter halos and the wider cosmic web, employing novel techniques such as a "multistream view" and the "caustic design" to delineate the intricate phase-space structure of dark matter. To deepen our understanding of these structures, I have developed "auxiliary-variable-guided generative models," which uncover the physical drivers behind the formation and evolution of dark matter halo structures. This work integrates closely with advanced cosmological simulations, including "CRK-HACC," to accurately model galaxy formation within these complex dark matter environments.

My work also involves rigorous cosmological tests and the analysis of large-scale astronomical data. I have contributed to "constraining $f(R)$ gravity" through a meticulous "k-cut cosmic shear analysis" of "Hyper Suprime-Cam First-Year Data," advancing precision cosmology. My observational contributions span diverse fields, from creating a "photometric sample of 2.6 million Red Clump stars" to map the "Milky Way's structure," to identifying "Carbon-Enhanced Metal-Poor star candidates from Gaia DR3," shedding light on the early universe's stellar populations. Furthermore, I have optimized survey strategies for "weak lensing cluster mass estimation" by "reducing model error using optimised galaxy selection," and am an active contributor to major projects like "The SPHEREx Satellite Mission" and "The SPTpol Extended Cluster Survey," demonstrating a comprehensive approach to unraveling the universe's dark mysteries.

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
