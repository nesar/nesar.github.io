---
title: "Early Universe Astrophysics & Galaxy Formation"
excerpt: "Research in early universe astrophysics & galaxy formation"
collection: portfolio
---

The formation of the first stars and galaxies represents a pivotal epoch in cosmic history, bridging the simplicity of the early universe with the complex, structured cosmos we observe today. Following the Big Bang, the universe was composed primarily of hydrogen and helium, and the first luminous objects, known as Population III (Pop III) stars, formed within small dark matter halos called minihalos. These stars, massive and short-lived, are believed to have begun the process of reionizing the neutral intergalactic medium and initiated the chemical enrichment of the pristine gas, laying the groundwork for subsequent generations of stars and the emergence of the first galaxies.

Understanding the processes by which these initial structures evolved, how gas accreted and cooled within them, and how the explosive deaths of Pop III stars (supernovae) dispersed the first heavy elements, is crucial for comprehending the origins of cosmic structure. This period, often referred to as the Cosmic Dawn, directly influences the properties of galaxies throughout cosmic time, including their metallicity, star formation rates, and morphology. Unraveling these complex interactions requires sophisticated theoretical models and high-resolution numerical simulations that can track the multi-scale physics, from the dynamics of gas in dark matter halos to the intricate effects of stellar feedback.

My research extensively explores these foundational questions, focusing on the interplay between primordial star formation, chemical enrichment, and the genesis of the first galaxies. I have investigated how the first supernovae externally enrich surrounding minihalos, thereby facilitating the conditions for subsequent star formation in regions beyond the immediate vicinity of the Pop III event. My work has also delved into the detailed physical processes occurring at very high redshifts ($z \gtrsim 10$), specifically the primordial chemical enrichment, accretion, cooling, and virialization of gas within nascent dark matter halos, establishing the initial environmental conditions for galactic formation.

Further, I have explored the critical impact of heterogeneous enrichment from primordial stars on the formation of the first galaxies. This heterogeneity, meaning the non-uniform distribution of metals, significantly influences the cooling properties of gas and thus the sites and rates of second-generation star formation. Utilizing high-resolution simulations, notably the Phoenix Simulations, I have developed models that connect the initial primordial star-forming regions directly to the emergence of second-generation star formation, thereby tracing the causal links between the earliest stars and the building blocks of modern galaxies. These contributions advance our understanding of how the universe transitioned from its primordial state to one rich in stars, galaxies, and complex chemical elements.

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
