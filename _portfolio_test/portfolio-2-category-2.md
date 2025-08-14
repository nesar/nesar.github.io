---
title: "Early Universe and Galaxy Formation"
excerpt: "Research in early universe and galaxy formation"
collection: portfolio
---

The early universe, following the cosmic Dark Ages, represents a pivotal epoch in cosmic history, characterized by the formation of the first stars, galaxies, and the reionization of the intergalactic medium. Understanding this era is fundamental to comprehending the origins of all structures observed today, from dwarf galaxies to massive galaxy clusters. Key challenges in this field include modeling the gravitational collapse of dark matter halos, the complex interplay of gas accretion, cooling, and feedback processes, and the propagation of the first heavy elements synthesized in the earliest stars.

These initial stars, known as Population III (Pop III) stars, were metal-free and significantly more massive and short-lived than stars forming today. Their explosive deaths as supernovae were the universe's first factories for heavy elements, or metals, which were then dispersed into the pristine cosmic gas. This primordial chemical enrichment fundamentally altered the conditions for subsequent star formation, transitioning from metal-free Population III stars to the metal-enriched Population II and I stars that constitute most of the stars we see in galaxies today. The spatial and temporal distribution of these first metals dictates where and when the first galaxies could assemble and grow.

My research extensively investigates the intricate physical processes that governed the formation of the first stars and galaxies in the nascent universe. I have developed and utilized sophisticated high-resolution cosmological simulations to model the dynamics of gas and dark matter at redshifts greater than ten, a critical epoch before significant cosmic reionization. My work on "External Enrichment of Minihalos by the First Supernovae" demonstrated that the outflows from the very first stellar explosions could enrich neighboring minihalos, driving the formation of second-generation stars in previously unpolluted environments. This finding highlights the crucial role of long-range metal dispersal in seeding star formation beyond the immediate vicinity of primordial supernovae.

Further, my studies detailed in "Galaxies and Their Environment at $z \gtrsim 10$ -- I: Primordial Chemical Enrichment, Accretion, Cooling, and Virialization of Gas in Dark Matter Halos" provided a comprehensive analysis of the fundamental processes shaping the very first galactic systems, including gas accretion, cooling mechanisms, and virialization within dark matter potential wells. Building on this, "The First Galaxies and the Effect of Heterogeneous Enrichment from Primordial Stars" elucidated how the highly heterogeneous (non-uniform) distribution of primordial metals profoundly influenced the formation pathways of the first galaxies, leading to diverse star formation modes. Finally, "Connecting Primordial Star Forming Regions and Second Generation Star Formation in the Phoenix Simulations" explicitly linked the formation sites of the first stars to the subsequent emergence of enriched stellar populations within emerging galaxies, leveraging the high-fidelity Phoenix simulation suite to trace these evolutionary connections. This body of work provides a detailed framework for understanding the pivotal role of primordial stars and their remnants in chemically enriching the early universe, thereby enabling the formation and evolution of the first galaxies.

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
