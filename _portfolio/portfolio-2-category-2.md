---
title: "Cosmology & Large-Scale Structure"
excerpt: "Research in cosmology & large-scale structure"
collection: portfolio
---

Research in Cosmology and Large-Scale Structure aims to unravel the universe's evolutionary history, from the cosmic microwave background to the formation of galaxies and galaxy clusters. A central focus is understanding the enigmatic nature of dark matter and dark energy, which dictate the growth of cosmic structure and the expansion of the universe. This field leverages sophisticated observational data from powerful telescopes, alongside advanced theoretical models and simulations, to map the distribution of matter across vast cosmic scales.

The study of large-scale structure encompasses the characterization of the "cosmic web"—a vast network of dark matter filaments, sheets, and voids that permeates the universe and dictates where galaxies form. Researchers employ a range of techniques, including gravitational lensing, galaxy surveys, and cluster observations, to probe this structure and test the predictions of General Relativity and alternative cosmological models. Challenges involve distinguishing between different cosmological models, accurately modeling complex astrophysical processes, and managing the increasing complexity of astronomical datasets.

My research extensively investigates the fundamental nature of the cosmic web and its dark matter components. I have pioneered the application of a "multistream view" to characterize the complex "topology and geometry of the dark matter web," revealing its intricate "caustic design" and providing novel insights into the "tracing" of these structures. This approach offers a detailed "multi-stream portrait of the Cosmic web," enhancing our understanding of how "dark matter haloes" form and evolve within the overarching cosmic architecture.

Furthermore, my work contributes to testing alternative cosmological models, specifically "f(R) modified gravity," through rigorous observational analyses. This includes "constraining f(R) gravity with a k-cut Cosmic Shear Analysis of the Hyper Suprime-Cam First-Year Data" and developing a "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" to accelerate theoretical predictions. I also focus on improving the precision of observational probes, exemplified by "reducing Model Error Using Optimised Galaxy Selection" for "Weak Lensing Cluster Mass Estimation" in surveys like "The SPTpol Extended Cluster Survey." In parallel, I have advanced the application of machine learning to cosmology, developing "Differentiable Predictions for Large Scale Structure with SHAMNet" and establishing "Physical Benchmarking for AI-Generated Cosmic Web," paving the way for data-driven discovery and more efficient simulations in the field.

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
