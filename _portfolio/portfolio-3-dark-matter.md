---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe at large scales is profoundly shaped by dark matter, an enigmatic substance whose gravitational influence orchestrates the formation and evolution of cosmic structures. This influence manifests as the "Cosmic Web," an intricate network comprising vast voids, filamentary structures, sheet-like walls, and dense dark matter haloes where galaxies reside. Understanding the precise distribution and dynamics of dark matter within this web is paramount for constraining cosmological parameters, testing theories of gravity beyond General Relativity, and unraveling the complex mechanisms of galaxy formation and evolution.

Researchers in this domain employ a diverse array of sophisticated techniques. These include observational probes like weak gravitational lensing, which maps mass distributions, and the kinematic Sunyaev-Zel'dovich (kSZ) effect, which probes peculiar velocities of galaxy clusters. Such observations are complemented by advanced theoretical and computational methodologies, notably N-body and hydrodynamical simulations that model dark matter collapse and its baryonic interactions, serving as essential testbeds for cosmological models and advanced analysis pipelines.

My research significantly contributes to this field by developing advanced theoretical frameworks, innovative analysis techniques, and computational tools to map and characterize the dark matter distribution across cosmic scales. I have explored the fundamental properties of dark matter structures by characterizing the "caustic design" of the dark matter web and developing a "multistream view" to understand the fine-grained dynamics and topology of dark matter haloes. This work provides a more granular perspective on how dark matter streams coalesce to form structures, offering critical insights into the underlying gravitational processes. I have also leveraged auxiliary-variable-guided generative models, using machine learning to uncover the physical drivers of dark matter halo structures.

Furthermore, my work applies these insights to constrain cosmological models and improve observational analyses. I have conducted a $k$-cut cosmic shear analysis of Hyper Suprime-Cam data to constrain alternative gravity theories like $f(R)$ models. My contributions include enhancing weak lensing cluster mass estimations through "optimised galaxy selection" and developing deep neural networks for "peculiar velocity estimation from the kinetic SZ effect" using data from missions like SPTpol. I have also been involved in mapping the Milky Way's dark matter distribution with "2.6 million Red Clump stars" and modeling galaxy formation in cosmological simulations using CRK-HACC. These efforts advance our ability to extract robust cosmological information from current and future datasets, including those from upcoming missions like SPHEREx.

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
