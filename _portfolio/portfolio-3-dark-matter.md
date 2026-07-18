---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe's large-scale structure is predominantly shaped by dark matter, an enigmatic substance that constitutes about 27% of the cosmos's mass-energy density but interacts only gravitationally. Its elusive nature presents a profound challenge in modern astrophysics and cosmology. Understanding the distribution, properties, and evolution of dark matter is central to refining the Lambda-CDM model, which describes the universe's expansion and the formation of cosmic structures like galaxies and galaxy clusters. Research in this field aims to probe the fundamental nature of dark matter particles, test gravitational theories beyond General Relativity, and accurately model the complex interplay between dark matter and baryonic matter.

Key areas of investigation include the characterization of the "cosmic web" – a vast network of dark matter filaments, sheets, and voids – and the dark matter haloes in which galaxies reside. Scientists employ a diverse array of methodologies, ranging from advanced N-body simulations that trace the gravitational evolution of dark matter over cosmic time to sophisticated analyses of observational data from wide-field surveys. These studies seek to map the dark matter distribution across various scales, uncover its intricate substructure, and constrain cosmological parameters and alternative theories of gravity.

My research significantly contributes to these efforts by developing novel techniques to map and characterize the cosmic web and dark matter haloes. I have pioneered methods for analyzing the multistream nature of dark matter flows within haloes and the cosmic web, revealing their intricate topology, geometry, and caustic features. This work provides a detailed "multi-stream portrait" of how dark matter structures form and evolve. Furthermore, I have applied state-of-the-art machine learning, specifically auxiliary-variable-guided generative models, to uncover the underlying physical drivers dictating dark matter halo structures, enhancing our predictive capabilities in cosmological simulations.

My contributions also extend to rigorous tests of cosmological models and gravity theories. I have been involved in using cosmic shear analysis, particularly the k-cut technique applied to Hyper Suprime-Cam data, to place stringent constraints on alternative gravity models like f(R) gravity. In parallel, I have actively participated in major observational endeavors such as the SPHEREx Satellite Mission and the SPTpol Extended Cluster Survey, which provide crucial data for testing theoretical predictions. My work also includes developing improved galaxy formation models within cosmological simulations like CRK-HACC and contributing to large photometric surveys of stars in the Milky Way, bridging the gap between dark matter theory and observable galactic properties.

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
