---
title: "Cosmic Web & Structure Formation"
excerpt: "Research in cosmic web & structure formation"
collection: portfolio
---

The universe's large-scale structure is characterized by the "Cosmic Web," a vast network of interconnected filaments, sheets, and dense dark matter haloes, separated by immense voids. This intricate cosmic architecture is believed to have formed through the gravitational collapse of primordial density fluctuations, predominantly driven by dark matter. Understanding the formation and evolution of this web is fundamental to modern cosmology, as it dictates the distribution of galaxies and provides crucial insights into the nature of dark matter and dark energy.

The standard model of structure formation posits that dark matter, an invisible and non-baryonic component of the universe, constitutes the gravitational backbone of the Cosmic Web. As dark matter particles move under gravity, they develop complex trajectories, leading to regions of high density and stream crossings. These dynamics are challenging to model and observe directly, requiring sophisticated N-body simulations and advanced analytical techniques to unravel the underlying physics. A key aspect of this research involves understanding the multi-stream nature of dark matter flows within these structures, particularly at the caustic surfaces where streams converge.

My research focuses on dissecting the intricate architecture of the dark matter web through a unique "multistream view," which provides an unparalleled understanding of its fine-grained structure. I have developed and applied methodologies to explicitly trace the multiple dark matter streams that converge to form haloes, filaments, and sheets, thereby revealing the phase-space origins of these structures. This approach allows for a direct characterization of the dark matter distribution beyond simple density fields, providing insights into the kinematic substructure crucial for understanding dark matter annihilation signals and galaxy formation processes.

Specifically, my work has elucidated the "caustic design of the dark matter web," mapping out the intricate network of caustics – regions of infinite density in phase space – that are fundamental to the gravitational collapse process. By analyzing the "topology and geometry of the dark matter web" from a multistream perspective, I have uncovered new insights into the connectivity and morphological characteristics of these cosmic structures. This detailed "multi-stream portrait of the Cosmic web" extends to understanding "dark matter haloes," the hosts of galaxies, by precisely quantifying the number and properties of streams that constitute them. These contributions provide a robust framework for interpreting dark matter simulations and have significant implications for indirect dark matter detection experiments, as the local velocity distribution of dark matter streams directly impacts expected signals.

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
