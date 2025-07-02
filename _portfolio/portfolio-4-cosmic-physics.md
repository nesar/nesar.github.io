---
title: "Cosmological Structure & Dark Matter Physics"
excerpt: "Research in cosmological structure & dark matter physics"
collection: portfolio
---

The large-scale structure of the Universe, often referred to as the "Cosmic Web," is a complex network of vast filamentary structures, sheet-like walls, and dense galaxy clusters, all underpinned by the mysterious substance known as dark matter. Understanding the formation, evolution, and internal architecture of this web, particularly its dominant dark matter component, is a central goal in modern cosmology. While N-body simulations provide powerful visualizations of this structure, analytical and theoretical frameworks are essential to fully grasp the underlying physical processes that govern its emergence from initial quantum fluctuations.

Dark matter, constituting about 85% of the Universe's matter content, dictates the gravitational scaffolding upon which luminous baryonic matter condenses to form galaxies. Key to understanding dark matter distribution are dark matter halos, dense concentrations where galaxies reside, and the less dense, but equally vital, filaments and sheets that connect them. Unraveling the precise distribution, velocity fields, and inherent complexities within these structures is critical for both fundamental cosmology and for interpreting experimental searches for dark matter particles.

A significant challenge lies in moving beyond simple density mapping to explore the more fundamental phase-space structure of dark matter. This involves characterizing not just where dark matter is, but also how it moves and how distinct flows of particles interact and overlap. Such an approach can reveal deeper insights into the gravitational collapse process and the fine-grained substructures that are often smoothed out in coarser analyses.

My research has specifically focused on dissecting the intricate architecture of the cosmic web and dark matter halos through a "multi-stream" lens. I have developed and applied novel methodologies to understand how multiple flows of dark matter, originating from different initial conditions, converge and intertwine to form the observed structures. This work, detailed in "Multi-stream portrait of the cosmic web" and "Dark matter haloes a multistream view," moves beyond traditional density-field analysis to explore the rich phase-space information, providing a more complete picture of dark matter dynamics and distribution within these complex systems.

A key contribution of my work, particularly highlighted in "The Caustic Design of the Dark Matter Web," involves the precise identification and characterization of "caustics." These are sharp enhancements in dark matter density that arise naturally from the multi-stream nature of gravitational collapse and serve as fundamental "design" elements of the dark matter web and its halos. Furthermore, I have applied advanced topological and geometrical tools, as explored in "Topology and geometry of the dark matter web a mul," to quantify the intricate connectivity and shape of this multi-stream dark matter web. This topological analysis offers a robust, quantitative means to describe the large-scale structure, providing new metrics to compare theoretical predictions with simulations and observations, and ultimately refining our understanding of how cosmic structure emerges.

<div class="no-figures"><p>Representative figures will be added soon.</p></div>

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
