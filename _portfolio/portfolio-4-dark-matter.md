---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The field of dark matter and cosmology seeks to understand the invisible substance comprising over 80% of the universe's matter, which dictates the formation and evolution of cosmic structures. Standard cosmological models, such as Lambda-CDM, posit that dark matter forms a vast, interconnected network known as the Cosmic Web. This intricate scaffolding consists of dense dark matter haloes, where galaxies reside, interconnected by vast filaments, separated by sheet-like walls, and enclosing immense voids. Understanding the precise distribution and dynamics of dark matter within this web is crucial for unravelling the universe's large-scale structure and addressing fundamental questions about galaxy formation and the nature of dark matter itself.

Traditional N-body simulations, while invaluable for mapping the overall density distribution of the cosmic web, often struggle to resolve the fine-grained substructure and the complex, multi-component nature of dark matter flows. These simulations typically represent dark matter as a collisionless fluid, but the actual phase-space distribution of dark matter particles can be far more intricate, especially in virialized structures like haloes and along the filaments. A deeper understanding requires moving beyond simple density fields to explore the detailed kinematics and the multi-stream nature of dark matter at various scales, offering insights into features not captured by coarse-grained approaches.

My research delves into the fine-grained structure of the dark matter web, moving beyond traditional density-based analyses to adopt a sophisticated multi-stream view. I have developed and applied methodologies to track the individual streams of dark matter particles that merge and overlap, revealing a far richer and more complex architecture than previously understood. A central focus of this work has been the identification and characterization of "caustics"—regions in phase space where multiple dark matter streams converge and cross. These caustic features are not merely statistical artifacts but represent fundamental, physically significant structures that arise from the gravitational collapse and mixing of dark matter.

Through this multi-stream lens, I have investigated the intricate "caustic design of the dark matter web," mapping how these singularities form and interconnect across filaments, walls, and particularly within dark matter haloes. My work provides a detailed "multi-stream portrait of the Cosmic web," offering a new perspective on its underlying skeletal framework. Furthermore, I have applied these techniques to rigorously analyze the "topology and geometry of the dark matter web," showing how the multi-stream nature profoundly influences the shape and connectivity of cosmic structures. This detailed view is then extended to "dark matter haloes," providing a more precise understanding of their internal structure, which has significant implications for understanding dark matter annihilation signals and direct detection experiments.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/multi-stream-portrait-of-the-cosmic-web_plot_1_6096c149.png" alt="Figure from Multi-stream portrait of the Cosmic web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Multi-stream portrait of the Cosmic web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Topology and geometry of the dark matter web: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Topology and geometry of the dark matter web: a multistream view</div>
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
