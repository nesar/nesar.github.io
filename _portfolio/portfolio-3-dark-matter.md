---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter, an enigmatic component of the universe, constitutes approximately 85% of its total matter content and plays a pivotal role in the formation and evolution of cosmic structures. Within the standard Lambda-CDM cosmological model, dark matter provides the gravitational scaffolding upon which galaxies and galaxy clusters assemble, forming an intricate network known as the cosmic web. This vast, filamentary structure, composed of dense halos, connecting filaments, sheet-like walls, and expansive voids, dictates the large-scale distribution of luminous matter and serves as a fundamental framework for understanding the universe's large-scale organization.

Understanding the precise distribution, dynamics, and internal structure of dark matter is crucial for probing its fundamental nature, testing cosmological models, and informing experimental searches for dark matter particles. Traditional approaches often focus on the smoothed density field, but the detailed fine-grained structure, including the coherent flows of dark matter particles, holds essential information about the early universe and the non-linear processes of gravitational collapse. Investigating this intricate substructure, particularly the multi-stream nature of dark matter flows, offers a unique avenue to decipher the complex physics governing structure formation.

My research delves into the fine-grained structure and dynamics of the dark matter web and its constituent halos, moving beyond density-based analyses to explore the underlying multi-stream nature of dark matter flows. I have developed and applied novel methodologies to characterize the topology and geometry of the dark matter web from a multi-stream perspective, revealing the intricate patterns of caustics – regions where dark matter streams cross and accumulate. This approach, as detailed in "The Caustic Design of the Dark Matter Web," highlights how these caustic structures are not merely theoretical constructs but represent fundamental building blocks of the dark matter distribution, arising from the non-linear gravitational collapse of primordial density fluctuations.

My work further extends this multi-stream paradigm to provide a comprehensive "Multi-stream portrait of the Cosmic web," demonstrating how the cosmic web, including filaments and walls, is fundamentally shaped by the coherent convergence and divergence of dark matter streams. Through investigations into the "Topology and geometry of the dark matter web: a multistream view," I have shown that the topological features of the cosmic web are profoundly influenced by these multi-stream flows, offering new insights into the hierarchical formation of structure. Furthermore, in "Dark matter haloes: a multistream view," I have applied this framework to dark matter halos, revealing that their internal structure is characterized by a complex superposition of streams, providing a deeper understanding of halo density profiles, substructure, and their potential implications for indirect dark matter detection experiments. These contributions offer a more complete and dynamically rich picture of the dark matter distribution, vital for refining cosmological models and informing future dark matter searches.

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
