---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter remains one of the most significant mysteries in modern astrophysics and cosmology. Constituting approximately 27% of the universe's total mass-energy density, its gravitational influence is essential for explaining the formation and evolution of galaxies and large-scale structures, yet it has not been directly detected. Understanding the nature and distribution of dark matter is crucial for a complete picture of our universe, driving extensive theoretical and observational efforts across the globe.

Cosmological research delves into the universe's fundamental properties, its origin, evolution, and ultimate fate. A key focus is the 'cosmic web' – the filamentary network of dark matter and galaxies that permeates the universe, connecting massive galaxy clusters and separating vast cosmic voids. Investigating the geometry, topology, and internal dynamics of this web, alongside the processes of galaxy formation within dark matter haloes, provides critical insights into the underlying cosmological model and potential deviations from General Relativity, such as modified gravity theories. Advanced techniques, from cosmic shear analysis to detailed simulations and large-scale astronomical surveys, are vital tools in this quest.

My research significantly contributes to unraveling the secrets of dark matter and the cosmic web. I have extensively investigated the intricate architecture of the dark matter web, employing advanced multi-stream and caustic analyses to characterize its topology, geometry, and internal dynamics. This work, detailed in papers like "The Caustic Design of the Dark Matter Web" and "Topology and geometry of the dark matter web: a multistream view," provides a granular view of dark matter's distribution, revealing the complex, interwoven structure that underpins the universe. By "tracing the cosmic web" and exploring the "multi-stream portrait," my aim is to gain a deeper understanding of how these structures evolve and influence galaxy formation. I also map the distribution of dark matter haloes and their internal structure using a multi-stream view.

Furthermore, my work extends to probing alternative gravity theories and refining our observational understanding of cosmic structures. I have contributed to "Constraining f(R) Gravity with a k-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data," applying sophisticated weak lensing techniques to observational data to test modifications to General Relativity. In the realm of galaxy formation, I have worked on "Modeling Galaxy Formation in Cosmological Simulations with CRK-HACC," developing tools to simulate baryonic processes within dark matter haloes. My research also leverages large astronomical surveys, for instance, using "A Photometric Sample of Red Clump Stars" from Gaia DR3 to map the Milky Way's structure, and developing methods for "Reducing Model Error Using Optimised Galaxy Selection" for weak lensing cluster mass estimation. I also identify "Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in Gaia DR3," contributing to galactic archaeology, and contribute to future missions like SPHEREx and analyze data from surveys like SPTpol, ensuring robust and precise cosmological measurements.

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
