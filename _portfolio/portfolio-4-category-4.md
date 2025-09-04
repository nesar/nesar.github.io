---
title: "Stellar & Galactic Astrophysics"
excerpt: "Research in stellar & galactic astrophysics"
collection: portfolio
---

Stellar and galactic astrophysics seeks to unravel the formation, evolution, and structure of galaxies, particularly our own Milky Way, by studying its constituent stellar populations. Large-scale astrometric and photometric surveys, such as those from the Gaia mission, provide unprecedented datasets essential for this endeavor. These data enable the identification of specific stellar tracers, like Red Clump (RC) giants, which act as standard candles for mapping galactic structure due to their well-understood intrinsic luminosity. Similarly, Carbon-Enhanced Metal-Poor (CEMP) stars, ancient stellar relics with unusual chemical compositions, offer unique insights into the early universe and the chemical enrichment history of galaxies. Understanding these diverse stellar populations and their distributions is key to reconstructing the Milky Way's past and predicting its future.

My research leverages these cutting-edge datasets and methodologies to address key questions in stellar and galactic evolution. I have undertaken a comprehensive study to characterize the Milky Way's structure using a massive sample of Red Clump stars. This work involved creating a photometric sample of 2.6 million Red Clump stars, meticulously identified and characterized, enabling a detailed mapping from the inner to the outer regions of the Milky Way. By exploiting their well-defined intrinsic luminosity, this research provides robust distance estimates and illuminates the three-dimensional distribution and properties of stellar populations across a significant span of our Galaxy, offering insights into disk structure, warps, and flares.

Concurrently, my work delves into the realm of Galactic archaeology by identifying and studying Carbon-Enhanced Metal-Poor star candidates. Using BP/RP spectra from Gaia DR3, I have developed methods to effectively identify these rare and ancient stellar relics. CEMP stars are crucial tracers for understanding the chemical enrichment of the early universe and the formation mechanisms of the very first stars. The identification of these candidates represents a significant step towards building larger, more comprehensive catalogs of these chemically pristine objects, essential for constraining models of early stellar nucleosynthesis and the assembly history of the Milky Way's halo.

Together, these research strands provide a multifaceted approach to understanding the Milky Way. By combining detailed studies of large-scale galactic structure mapped by Red Clump stars with the chemical fingerprints left by the most ancient CEMP stars, my work offers a more complete picture of our Galaxy's evolution. This dual focus on both the present-day architecture and the primordial history of the Milky Way significantly contributes to the broader field of stellar and galactic astrophysics, pushing the boundaries of our understanding of stellar populations, chemical evolution, and galactic formation processes.

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
