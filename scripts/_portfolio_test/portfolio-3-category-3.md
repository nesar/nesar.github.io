---
title: "Early Universe Cosmology & Formation"
excerpt: "Research in early universe cosmology & formation"
collection: portfolio
---

Early Universe Cosmology investigates the earliest epochs of cosmic history, from the initial cooling of the universe after the Big Bang to the formation of the very first stars and galaxies. This era, often termed the "Cosmic Dawn," represents a pivotal transition from the dark ages – a period when the universe was neutral and largely opaque – to the reionized and complex cosmos we observe today. Understanding the physical conditions that led to the birth of the first stars (Population III stars) within the smallest dark matter halos is fundamental to explaining the subsequent evolution of cosmic structure, chemical enrichment, and the eventual emergence of large galaxies.

The formation of these pristine structures involved intricate processes, including the gravitational collapse of gas within nascent dark matter potential wells, followed by various cooling mechanisms that allowed the gas to condense sufficiently to form stars. Crucially, the short, violent lives of the first stars culminated in supernovae that dispersed the first heavy elements, forging a chemically enriched environment from the initially pristine hydrogen and helium. Tracing the propagation of these supernova blast waves and the resulting inhomogeneous distribution of metals is essential for accurately modeling the formation of the first galaxies and the transition to subsequent generations of metal-enriched star formation.

My research in early universe cosmology primarily focuses on unraveling the intricate physical processes that governed the formation of the first stars and galaxies. I have developed and applied sophisticated numerical and theoretical models to investigate the *primordial chemical enrichment* of early cosmic structures and the dynamic interplay of *gas accretion, cooling, and virialization within dark matter halos at very high redshifts*, specifically *z* greater than 10. A significant part of this work has been dedicated to understanding the *external enrichment of minihalos by the first supernovae*, detailing how these events rapidly spread the initial heavy elements, thereby influencing the conditions for subsequent star formation.

Furthermore, my investigations have explored the critical impact of *heterogeneous enrichment from primordial stars* on the properties of *the first galaxies*. I have leveraged cutting-edge, large-scale cosmological simulations, including the *Phoenix Simulations*, to meticulously trace the evolution from pristine gas to the emergence of the first galactic systems. This work specifically focuses on *connecting primordial star forming regions and second generation star formation*, providing a comprehensive framework for understanding how the remnants and chemical imprints of the earliest stars directly influenced the birth and characteristics of the subsequent stellar populations and the nascent galaxies they comprised. These efforts aim to bridge the gap between theoretical predictions and future observational capabilities, enhancing our understanding of the Cosmic Dawn.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/external-enrichment-of-minihalos-by-the-first-supe_plot_1_b5b1abaa.png" alt="Figure from External Enrichment of Minihalos by the First Supernovae" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: External Enrichment of Minihalos by the First Supernovae</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/galaxies-and-their-environment-at-z-gtrsim-10----i_plot_1_10d746ce.png" alt="Figure from Galaxies and Their Environment at $z \gtrsim 10$ -- I: Primordial Chemical Enrichment, Accretion, Cooling, and Virialization of Gas in Dark Matter Halos" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Galaxies and Their Environment at $z \gtrsim 10$ -- I: Primordial Chemical Enrichment, Accretion, Cooling, and Virialization of Gas in Dark Matter Halos</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-first-galaxies-and-the-effect-of-heterogeneous_plot_1_001904e0.png" alt="Figure from The First Galaxies and the Effect of Heterogeneous Enrichment from Primordial Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The First Galaxies and the Effect of Heterogeneous Enrichment from Primordial Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/connecting-primordial-star-forming-regions-and-sec_plot_1_40efcdea.png" alt="Figure from Connecting Primordial Star Forming Regions and Second Generation Star Formation in the Phoenix Simulations" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Connecting Primordial Star Forming Regions and Second Generation Star Formation in the Phoenix Simulations</div>
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
