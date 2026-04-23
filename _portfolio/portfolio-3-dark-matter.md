---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter and dark energy constitute the vast majority of the Universe's mass-energy budget, yet their fundamental nature remains one of the most profound mysteries in modern physics. The Lambda-CDM cosmological model, while highly successful in explaining cosmic evolution, critically relies on these enigmatic components. Understanding their properties is paramount to unraveling the Universe's history, predicting its future, and testing the limits of general relativity and our understanding of gravity.

A key avenue for investigating dark matter and cosmological models involves studying the large-scale structure of the Universe – the intricate 'cosmic web' of halos, filaments, sheets, and voids formed through gravitational instability. This research area combines theoretical modeling, sophisticated N-body and hydrodynamical simulations, and rigorous analysis of observational data from wide-field astronomical surveys. Such studies aim to map the distribution of dark matter, characterize its substructures, constrain cosmological parameters, and probe alternative theories of gravity that might explain the Universe's accelerated expansion without recourse to dark energy.

My research significantly contributes to this field by developing and applying advanced computational and analytical techniques to understand the nature of dark matter and the evolution of the cosmic web. I have extensively investigated the multi-stream nature of dark matter halos and the cosmic web itself, analyzing their complex topology and geometry. This work, highlighted in papers like "The Caustic Design of the Dark Matter Web," "Dark matter haloes: a multistream view," and "Topology and geometry of the dark matter web: a multistream view," provides fundamental insights into the fine-grained substructure that governs dark matter distribution and its gravitational effects. Furthermore, I leverage and develop advanced cosmological simulations, such as CRK-HACC, to model galaxy formation within these dark matter structures, tracing the cosmic web with high fidelity to understand its physical drivers.

A crucial aspect of my recent contributions involves pioneering the application and rigorous benchmarking of artificial intelligence and machine learning in cosmological research. I have developed auxiliary-variable-guided generative models to uncover physical drivers of dark matter halo structures and performed comprehensive physical benchmarking for both AI-evolved cosmological structure formation and AI-generated cosmic web models. This innovative approach, detailed in papers like "Uncovering Physical Drivers of Dark Matter Halo Structures with Auxiliary-Variable-Guided Generative Models" and "Benchmarking AI-evolved cosmological structure formation," enhances our ability to analyze and predict cosmic evolution with unprecedented efficiency and precision. Beyond dark matter structure, my work extends to constraining alternative theories of gravity, such as $f(R)$ gravity, using cutting-edge observational techniques like $k$-cut cosmic shear analysis of Hyper Suprime-Cam data. Additionally, I contribute to major astronomical missions and surveys, including the SPHEREx satellite mission and the SPTpol Extended Cluster Survey, and utilize data from Gaia DR3 to trace stellar populations and infer the distribution of dark matter within galaxies, thereby connecting theoretical predictions with empirical observations across cosmic scales.

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
