---
title: "Cosmic Structure & Dark Matter Dynamics"
excerpt: "Research in cosmic structure & dark matter dynamics"
collection: portfolio
---

The formation and evolution of the universe's large-scale structure (LSS) is a cornerstone of modern cosmology, driven primarily by the gravitational collapse of dark matter. This intricate cosmic web, characterized by a hierarchical network of voids, sheets, filaments, and massive dark matter halos, serves as the scaffolding upon which galaxies form and evolve. Understanding its detailed architecture and dynamics is crucial for unraveling the mysteries of dark energy, the nature of dark matter, and the fundamental laws governing cosmic evolution.

Accurately modeling the dark matter distribution presents significant challenges, especially at nonlinear scales where the simplifying assumptions of linear perturbation theory break down. The dynamics of dark matter become particularly complex after shell crossing, leading to a multi-stream flow where particles traverse the same spatial point multiple times. Traditional N-body simulations, while powerful, are computationally expensive, necessitating the development of advanced analytical and computational techniques to explore the vast parameter space of cosmological models and probe the fine-grained structure of the dark matter web.

My research significantly advances our understanding of the fine-grained structure and dynamics of the dark matter web, moving beyond simplified single-stream approximations. Through detailed phase space analysis, I have explored the "multistream view" of dark matter halos and the cosmic web, elucidating their intricate topology and geometry. This work has revealed the "caustic design" of these structures, identifying regions of high dark matter density and velocity dispersion arising from gravitational collapse and shell crossing. By mapping these caustic structures, my contributions provide a deeper insight into the physical processes shaping the dark matter distribution, directly addressing the complexities of its highly nonlinear evolution.

Furthermore, I have pioneered the application of machine learning and artificial intelligence to accelerate and refine predictions for large-scale structure. I have developed "SHAMNet," a differentiable framework for predicting large-scale structure properties, and created methodologies for "Physical Benchmarking" of AI-generated cosmic web simulations, ensuring their fidelity and physical consistency. This includes developing "Matter Power Spectrum Emulators" specifically for f(R) Modified Gravity Cosmologies, allowing for rapid and accurate exploration of alternative gravitational theories. These AI-driven approaches offer unprecedented speed and precision, enabling the robust comparison of theoretical models with observational data and opening new avenues for cosmological parameter inference and model testing.

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
