---
title: "Stellar & Galactic Astrophysics"
excerpt: "Research in stellar & galactic astrophysics"
collection: portfolio
---

The field of Stellar and Galactic Astrophysics is dedicated to unraveling the fundamental properties and evolutionary history of stars and their collective arrangement within galaxies, particularly our own Milky Way. Understanding the spatial distribution, kinematics, and chemical compositions of different stellar populations provides crucial insights into the formation processes of the Milky Way, from its innermost bulge to its outermost halo. This endeavor relies heavily on precise observational data from large-scale astronomical surveys, enabling astronomers to trace the assembly history of our galaxy and characterize the diverse stellar components that comprise it.

Key to these studies are specific classes of stars that serve as powerful diagnostic tools. Red Clump (RC) stars, for instance, are evolved, helium-core burning stars that exhibit remarkably uniform absolute magnitudes, making them excellent "standard candles" for precise distance measurements across vast Galactic distances. Conversely, Carbon-Enhanced Metal-Poor (CEMP) stars are ancient, chemically peculiar stars characterized by extremely low iron abundances but unexpectedly high carbon content. These rare objects are thought to be direct descendants of the earliest stellar generations, offering unique fossil records of nucleosynthesis in the early universe and providing invaluable clues about the nature of the first stars and the chemical enrichment history of galaxies.

My research extensively utilizes cutting-edge observational datasets, particularly from the Gaia mission, to address critical questions about Galactic structure and stellar evolution. In one significant contribution, I have developed a robust methodology for identifying and characterizing a vast photometric sample of Red Clump stars. This work resulted in a catalog of 2.6 million RC stars, meticulously covering regions from the innermost bulge to the outer reaches of the Milky Way disk and halo. By precisely measuring their distances and spatial distribution, this large-scale sample provides an unprecedented detailed map of the Milky Way’s three-dimensional structure, enabling a more accurate understanding of its global morphology and substructures.

Furthermore, my work extends to the challenging realm of stellar archaeology, specifically targeting the identification of Carbon-Enhanced Metal-Poor star candidates. Leveraging the low-resolution BP/RP spectra from Gaia DR3, I have developed innovative techniques to identify these extremely rare and faint objects. This research is crucial for understanding the chemical fingerprints of the early universe, tracing the origins of elements, and shedding light on the properties of the very first stars. The identification of such candidates significantly contributes to our understanding of the formation and early chemical enrichment of the Milky Way, linking the observed properties of individual stars to the broader picture of Galactic evolution.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/carbon-enhanced-metal-poor-star-candidates-from-bp_plot_1_17c64dee.png" alt="Figure from Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3</div>
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
