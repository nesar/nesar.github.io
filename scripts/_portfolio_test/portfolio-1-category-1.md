---
title: "Early Universe Cosmology & Galaxy Formation"
excerpt: "Research in early universe cosmology & galaxy formation"
collection: portfolio
---

The study of the early Universe, particularly the "Cosmic Dawn" era, focuses on the formation of the first stars and galaxies, and their profound impact on the reionization of the intergalactic medium. This foundational period, occurring hundreds of millions of years after the Big Bang, marks the transition from a neutral, dark cosmos to the ionized, structured Universe we observe today. Understanding these primordial objects requires sophisticated theoretical models and high-resolution numerical simulations, as direct observation remains challenging. Key questions revolve around the role of dark matter halos in gathering primordial gas, the processes of gas cooling and collapse, and the conditions under which the very first, metal-free (Population III) stars could form.

Following the birth and death of these first stars, the cosmos began to be enriched with the first heavy elements, synthesized in supernova explosions. This "chemical enrichment" fundamentally altered the conditions for subsequent star formation, paving the way for the formation of the first galaxies and more complex stellar populations. The distribution and impact of these early metals, especially their heterogeneous spread throughout nascent cosmic structures, are crucial for tracing the evolutionary path from the pristine early Universe to the complex galaxies observed at later times. Addressing these challenges involves intricate simulations tracking gas dynamics, chemical mixing, and stellar feedback processes across vast cosmological scales.

My research significantly contributes to unraveling these mysteries of the early Universe and the genesis of galaxies. Through my work, I have investigated the critical mechanisms driving early cosmic evolution, particularly focusing on the interplay between gas physics, dark matter halos, and the chemical feedback from the first stars. For instance, in "External Enrichment of Minihalos by the First Supernovae," I explored how the ejecta from primordial supernovae externally enriches neighboring minihalos, demonstrating a crucial pathway for the spread of metals and the initiation of second-generation star formation in previously unenriched environments. Concurrently, in "Galaxies and Their Environment at $z \gtrsim 10$ -- I: Primordial Chemical Enrichment, Accretion, Cooling, and Virialization of Gas in Dark Matter Halos," I detailed the fundamental processes of gas accretion, cooling, and virialization within dark matter halos at very high redshifts, highlighting their role in regulating the supply of pristine gas for star formation and the impact of primordial chemical enrichment.

Furthermore, my work has illuminated the intricate processes governing the formation of the earliest galaxies. In "The First Galaxies and the Effect of Heterogeneous Enrichment from Primordial Stars," I specifically examined how the non-uniform distribution of metals from early stars fundamentally shaped the properties and star formation efficiency of the very first galaxies, emphasizing the critical role of chemical inhomogeneity in the Population III to Population II transition. Utilizing advanced hydrodynamical simulations, including the cutting-edge "Phoenix Simulations" as detailed in "Connecting Primordial Star Forming Regions and Second Generation Star Formation in the Phoenix Simulations," I have developed robust numerical models to track the complex pathways of metal distribution and its influence on subsequent stellar generations. My technical contributions involve developing sophisticated methods to resolve gas dynamics and chemical mixing at the high resolutions required to model the earliest stellar populations, advancing our predictive capabilities for future Cosmic Dawn observations.

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
