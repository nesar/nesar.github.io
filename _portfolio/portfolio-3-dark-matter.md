---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The study of dark matter and cosmology represents a foundational pillar of modern astrophysics, seeking to unravel the universe's ultimate composition, evolution, and large-scale structure. A significant fraction of the cosmos remains enigmatic, dominated by dark matter and dark energy, which dictate the gravitational assembly of galaxies and galaxy clusters. Dark matter, an unseen substance interacting solely via gravity, forms the cosmic scaffold, giving rise to the intricate "cosmic web" of filaments, voids, and dense nodes where galaxies reside.

Investigating these profound mysteries necessitates a sophisticated, multi-faceted approach. This involves developing advanced theoretical frameworks, conducting high-resolution cosmological simulations, and meticulously analyzing vast amounts of observational data. Key methodologies include cosmic shear analysis, which probes dark matter distribution and tests alternative theories of gravity, alongside extensive surveys of astronomical objects spanning individual stars to massive galaxy clusters. Understanding the complex substructures within dark matter haloes and the overarching topology of the cosmic web is crucial for reconstructing the universe's history and predicting its future.

My research substantially contributes to this critical field through the development and application of innovative techniques across theoretical, computational, and observational domains. I have leveraged $k$-cut cosmic shear analysis of Hyper Suprime-Cam data to constrain modified gravity theories, specifically $f(R)$ gravity, thereby advancing our understanding of gravitation and its role in structure formation. A core focus of my work involves detailing the intricate nature of dark matter structures, from the "caustic design" of the cosmic web to the internal dynamics of dark matter haloes. Through a "multistream view," I have explored the detailed topology, geometry, and phase-space properties of the cosmic web and its haloes, revealing their complex substructure and evolutionary pathways.

Furthermore, I have developed cutting-edge computational tools, including auxiliary-variable-guided generative models, to uncover the physical drivers behind dark matter halo structures, enhancing our ability to simulate and predict their characteristics. My work also includes improving cosmological simulations of galaxy formation using codes like CRK-HACC, providing a more accurate framework for understanding how galaxies emerge within the dark matter framework. On the observational front, I have utilized large photometric samples of red clump stars to map the Milky Way’s internal structure and identified carbon-enhanced metal-poor star candidates from $Gaia$ DR3 spectra, contributing to stellar archaeology and our understanding of the early universe. My involvement in missions like SPHEREx and surveys such as SPTpol underscores my commitment to advancing observational cosmology, providing essential data to test and refine dark matter and cosmic models.

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
