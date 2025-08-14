---
title: "Early Universe Astrophysics & Galaxy Formation"
excerpt: "Research in early universe astrophysics & galaxy formation"
collection: portfolio
---

The study of the Early Universe and Galaxy Formation delves into the period following the Big Bang, a transformative epoch known as the "Cosmic Dawn." During this time, the first stars, often referred to as Population III stars, formed within small dark matter structures called minihalos, bringing an end to the cosmic "Dark Ages." These pioneering stars were crucial as they synthesized the first heavy elements through nuclear fusion, and their explosive deaths as supernovae scattered these elements into the pristine primordial gas. This initial metal enrichment was a pivotal event, fundamentally altering the physical conditions of the intergalactic medium and laying the groundwork for the formation of subsequent generations of stars and the first galaxies. Understanding these processes – from the infall of gas into dark matter halos to the subsequent cooling, virialization, and the impact of early supernovae – is key to unraveling how the cosmos evolved from a uniform state into the complex, structured universe we observe today.

A primary challenge in this field is to accurately model the multi-scale physics involved, from the collapse of individual gas clouds to the gravitational growth of large dark matter halos, while simultaneously tracking the non-uniform distribution of elements forged in the first stars. These early galaxies, though small by present-day standards, were the building blocks of larger structures and played a critical role in the reionization of the universe, providing the first sources of ultraviolet light that stripped electrons from neutral hydrogen atoms. Comprehensive theoretical and numerical approaches are therefore essential to reconstruct the environment and conditions that governed the birth of the first luminous objects and the subsequent assembly of galactic structures.

My research focuses precisely on these critical early cosmic processes, employing advanced numerical simulations to bridge the gap between primordial star formation and the emergence of the first galaxies. I have specifically investigated the "External Enrichment of Minihalos by the First Supernovae," demonstrating how the energetic outflows from these explosions can spread heavy elements far beyond their immediate vicinity, influencing future star formation in neighboring minihalos. Building on this, my work in "Galaxies and Their Environment at z >= 10" explores the intricate interplay of primordial chemical enrichment, gas accretion, cooling, and virialization within dark matter halos at very high redshifts, providing a comprehensive picture of the conditions conducive to the earliest galaxy formation.

Furthermore, I have elucidated "The First Galaxies and the Effect of Heterogeneous Enrichment from Primordial Stars," highlighting how the non-uniform distribution of metals from early supernovae creates diverse environments for subsequent star formation, leading to variations in the properties of the first galaxies. A cornerstone of my methodology involves high-resolution hydrodynamical simulations, as demonstrated in "Connecting Primordial Star Forming Regions and Second Generation Star Formation in the Phoenix Simulations." This work directly links the specific sites of Population III star formation to the subsequent formation of second-generation stars within nascent galaxies, providing crucial insights into the feedback mechanisms and legacy of the universe's first luminous objects. Through these contributions, my research provides a deeper understanding of the initial chemical evolution of the universe and the fundamental processes that govern the assembly of the very first galaxies.

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
