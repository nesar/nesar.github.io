---
title: "Cosmic Structure & Modified Gravity"
excerpt: "Research in cosmic structure & modified gravity"
collection: portfolio
---

The large-scale structure of the Universe, often referred to as the Cosmic Web, is a complex network of dark matter haloes, filaments, and sheets, embedded within vast cosmic voids. Understanding the formation and evolution of this structure is a cornerstone of modern cosmology. Dark matter, comprising approximately 27% of the Universe's mass-energy budget, plays a dominant role in gravitational collapse and structure formation, providing the scaffolding upon which galaxies and galaxy clusters form. Detailed characterization of the dark matter distribution, from its smooth initial state to its highly non-linear final configuration, is essential for testing the standard cosmological model and probing the fundamental properties of dark matter.

The standard Lambda-CDM model has been remarkably successful in explaining a wide range of cosmological observations. However, mysteries such as the nature of dark energy, responsible for the Universe's accelerated expansion, prompt investigations into alternative gravitational theories, known as Modified Gravity. These theories propose deviations from General Relativity on cosmic scales, potentially altering the growth of structure and leaving distinct signatures in the Cosmic Web. Precisely modeling these effects, alongside the complex, multi-stream dynamics of dark matter, presents significant theoretical and computational challenges, requiring sophisticated numerical simulations and analytical tools.

My research extensively explores the intricate multi-stream nature of the dark matter web, moving beyond simplified single-fluid descriptions. I have specifically investigated the "Caustic Design of the Dark Matter Web," tracing particle trajectories to understand how the interweaving of multiple dark matter streams gives rise to the characteristic features of haloes and filaments. This work, detailed in papers such as "Dark matter haloes: a multistream view" and "Topology and geometry of the dark matter web: a multistream view," characterizes the density, velocity, and velocity dispersion fields within these complex environments, revealing the formation of caustics – regions where dark matter streams cross and density peaks are amplified. This "Multi-stream portrait of the Cosmic web" provides a more complete and physically realistic picture of dark matter structures, critical for interpreting observational probes like gravitational lensing.

Furthermore, my research extends to the realm of Modified Gravity, specifically focusing on f(R) theories. To address the computational demands of exploring the parameter space of these alternative gravitational models, I developed a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies." This emulator efficiently and accurately predicts the matter power spectrum – a key statistical measure of cosmic structure – across a wide range of cosmological and f(R) parameters. This technical contribution is vital for efficiently comparing theoretical predictions from modified gravity models with observational data from large-scale structure surveys, allowing for robust constraints on deviations from General Relativity and refining our understanding of cosmic acceleration. The ultimate impact of this work is to provide rigorous tests of fundamental physics through the detailed study of the Cosmic Web.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Topology and geometry of the dark matter web: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Topology and geometry of the dark matter web: a multistream view</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/multi-stream-portrait-of-the-cosmic-web_plot_1_6096c149.png" alt="Figure from Multi-stream portrait of the Cosmic web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-stream portrait of the Cosmic web</div>
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
