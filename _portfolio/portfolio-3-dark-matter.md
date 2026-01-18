---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter, an elusive component constituting approximately 27% of the universe's mass-energy budget, remains one of the most profound mysteries in modern cosmology. While its particle nature is yet to be directly detected, its gravitational influence is undeniably crucial for explaining the observed dynamics of galaxies and galaxy clusters, as well as the formation of large-scale structure. The standard cosmological model, Lambda-CDM, posits that dark matter acts as the gravitational scaffolding upon which the visible Cosmic Web – a vast network of filaments, sheets, and dense haloes – is built, hosting galaxies and galaxy clusters.

Understanding the distribution and evolution of dark matter is therefore paramount for constraining cosmological parameters, testing fundamental theories of gravity beyond General Relativity, and modeling galaxy formation processes. Researchers employ a combination of observational techniques, such as gravitational lensing, galaxy surveys, and cosmic microwave background measurements, alongside large-scale cosmological simulations to probe the properties of dark matter and the Cosmic Web. These investigations aim to characterize the statistical properties of structure, map its complex geometry, and identify signatures that could distinguish between different dark matter candidates or alternative gravitational theories.

My research extensively explores the fundamental properties of dark matter and the Cosmic Web through both theoretical modeling and empirical data analysis. I have focused on characterizing the complex phase-space structure of dark matter haloes, developing a "Multi-stream portrait of the Cosmic web" and analyzing the "Topology and geometry of the dark matter web" and "The Caustic Design of the Dark Matter Web." These efforts provide a deeper understanding of dark matter substructure and its role in galaxy formation, complemented by my contributions to "Modeling Galaxy Formation in Cosmological Simulations with CRK-HACC." This work traces the non-linear evolution of structure, from its initial conditions to the complex "Tracing the cosmic web" we observe today.

On the observational front, I apply cutting-edge techniques to large datasets to test cosmological models and probe theories of gravity. This includes "Constraining $f(R)$ Gravity with a $k$-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data," utilizing weak gravitational lensing to search for deviations from Einstein’s General Relativity. I have also been involved in major surveys that map the large-scale distribution of matter and galaxies, such as "The SPTpol Extended Cluster Survey," and contributed to the scientific objectives of future missions like "The SPHEREx Satellite Mission." Furthermore, my work extends to analyzing stellar populations, as demonstrated by "From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars," which provides crucial baryonic tracers for understanding the galactic environments within their encompassing dark matter haloes.

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
