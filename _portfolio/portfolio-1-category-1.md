---
title: "Cosmic Structure & Dynamics"
excerpt: "Research in cosmic structure & dynamics"
collection: portfolio
---

The large-scale structure of the universe, known as the Cosmic Web, is an intricate network of vast empty voids, sheet-like walls, elongated filaments, and dense galaxy clusters. This grand structure arises from the gravitational collapse of primordial density fluctuations, predominantly driven by invisible dark matter. Understanding the formation and evolution of the Cosmic Web is crucial for deciphering the universe's past, present, and future, as it dictates the environments in which galaxies form and evolve.

A fundamental aspect of dark matter dynamics, given its collisionless nature, is the phenomenon of "multistreaming." As dark matter particles orbit within gravitational potential wells, their trajectories often cross, leading to regions where multiple distinct streams of particles coexist. These regions of stream overlap are the physical building blocks of dark matter structures, from the dense cores of dark matter haloes to the extended tendrils of the cosmic web. The convergence of these streams can lead to the formation of caustic surfaces, which are sharp enhancements in dark matter density, analogous to light caustics, and are key to understanding the internal structure and dynamics of these cosmic scaffolds.

My research delves into providing a detailed "multistream portrait" of the Cosmic Web, moving beyond simplified density field analyses to directly characterize the phase-space structure of dark matter. In "The Caustic Design of the Dark Matter Web," I have developed methods to identify and analyze these caustic surfaces, demonstrating how they form a fundamental skeleton underlying the dark matter web. This framework reveals how caustics not only delineate the boundaries of virialized structures but also trace out the intricate internal architecture of filaments and sheets.

Furthermore, my work in "Dark matter haloes: a multistream view" and "Topology and geometry of the dark matter web: a multistream view" focuses on the internal structure of dark matter haloes and the quantitative characterization of the multistream web. I have shown that dark matter haloes are complex, multistream environments, and understanding this internal kinematic structure is vital for predicting their observational signatures. To precisely quantify the complex nature of the multistream cosmic web, I have employed advanced topological and geometric analysis techniques, such as persistent homology and Minkowski functionals. These methods allow for a rigorous, scale-independent description of the web's connectivity and morphology, revealing how the number of dark matter streams correlates with the topological features and geometric properties of voids, walls, filaments, and clusters. This comprehensive approach provides a more complete and physically motivated understanding of how dark matter structures are built and evolve.

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
