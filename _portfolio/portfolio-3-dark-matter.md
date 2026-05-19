---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Research in cosmology and dark matter seeks to unravel the fundamental constituents and evolutionary history of our universe. A cornerstone of modern cosmology is the $\Lambda$CDM model, which postulates that the universe is predominantly composed of dark energy and dark matter, with baryonic matter making up only a small fraction. Dark matter, an enigmatic substance that interacts gravitationally but not electromagnetically, is crucial for understanding the formation and growth of cosmic structures, from galaxies to vast galaxy clusters, and serves as the scaffolding upon which visible matter aggregates.

A key focus within this field is the study of the "cosmic web," a vast network of dark matter filaments, sheets, and dense halos that permeate the universe. These structures are the sites of galaxy formation and provide critical probes for testing cosmological models and theories of gravity. Precision measurements from large-scale astronomical surveys are essential for constraining cosmological parameters and investigating potential deviations from the $\Lambda$CDM paradigm, such as those proposed by alternative theories of gravity like $f(R)$ models. Understanding the intricate dynamics and morphology of the cosmic web and its constituent dark matter halos is therefore paramount for a complete picture of cosmic evolution.

My research extensively explores the nature of dark matter and its role in shaping the universe, employing both advanced cosmological simulations and sophisticated analytical techniques. I have contributed to constraining alternative theories of gravity, such as $f(R)$ gravity, by developing and applying a $k$-cut cosmic shear analysis to observational data from the Hyper Suprime-Cam First-Year Survey. Furthermore, my work delves into the intricate internal structures of dark matter halos and the cosmic web, characterizing their dynamics through a "multistream view" that accounts for the complex velocity flows within these structures. I have investigated the "caustic design" and the "topology and geometry" of the dark matter web, providing a deeper understanding of its formation and morphology.

To further unravel the physical drivers of dark matter halo structures, I have pioneered the application of auxiliary-variable-guided generative models, leveraging machine learning to identify key influences on halo properties. This work, alongside developing tools like CRK-HACC for modeling galaxy formation within cosmological simulations and advanced methods for tracing the cosmic web, collectively advances our capability to simulate, analyze, and interpret the universe’s large-scale structure. My contributions provide critical insights into dark matter's behavior, the formation of galaxies, and robustly test our current cosmological framework against both theoretical predictions and observational evidence.

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
