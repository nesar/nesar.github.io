---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Research in dark matter and cosmology aims to comprehensively understand the universe's fundamental constituents, its evolutionary history, and the formation of the large-scale structures that define its cosmic web. This intricate network of dark matter haloes, filaments, and voids provides the gravitational scaffolding for galaxy formation. Cosmological simulations, particularly N-body and hydrodynamical models, are indispensable tools for predicting the evolution of these structures, offering theoretical frameworks to be rigorously tested against observational data.

Observational cosmology employs diverse techniques to probe the cosmic web and constrain cosmological models. Gravitational lensing, encompassing both weak and strong regimes, directly maps mass distribution, while extensive surveys of galaxy clusters and the cosmic microwave background illuminate large-scale structure and fundamental cosmological parameters. These efforts are crucial for testing General Relativity, exploring alternative theories like $f(R)$ gravity, and characterizing dark matter halo properties. The integration of advanced data science and artificial intelligence, including deep learning, is increasingly vital for analyzing complex datasets and accelerating discovery in this data-rich era.

My research significantly advances these areas through the development and application of cutting-edge computational and analytical techniques. I have extensively utilized N-body simulations to characterize the intricate multi-stream nature, topology, and geometry of the dark matter cosmic web, including its detailed caustic design (papers 3, 4, 5, 6). Leveraging advanced machine learning, including generative models, my work uncovers physical drivers of dark matter halo structures and benchmarks AI-evolved cosmological structure formation (papers 7, 10, 13). I also contributed to the CRK-HACC hydrodynamical simulation code, instrumental for modeling galaxy formation within these evolving cosmic structures (paper 8).

In observational cosmology, my work focuses on robustly constraining cosmological models and enhancing the precision of various probes. I performed $k$-cut cosmic shear analyses using Hyper Suprime-Cam data to constrain alternative gravity theories like $f(R)$ gravity, providing stringent tests of cosmic acceleration (paper 1). I optimized galaxy selection for reduced model error in weak lensing cluster mass estimations (paper 11) and developed modular deep learning pipelines for efficient galaxy-scale strong gravitational lens detection and modeling (paper 15). I also applied deep neural networks for peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect (paper 14), enabling more precise cosmological measurements from large surveys (papers 9, 16). Collectively, my research bridges theoretical modeling, advanced simulations, and state-of-the-art data analysis to shed new light on the dark universe.

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
