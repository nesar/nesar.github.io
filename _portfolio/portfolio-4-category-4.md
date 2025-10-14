---
title: "Galactic & Stellar Astrophysics"
excerpt: "Research in galactic & stellar astrophysics"
collection: portfolio
---

The field of Galactic and Stellar Astrophysics is dedicated to understanding the fundamental processes that govern the formation, evolution, and interactions of stars and galaxies. A primary goal is to decipher the structure, dynamics, and chemical history of our own Milky Way galaxy, from its central bulge to its extended halo and disk. This involves meticulous characterization of stellar populations, which serve as crucial tracers of galactic evolution, providing insights into the distribution of mass, stellar birth rates, and the chemical enrichment of the interstellar medium over cosmic time.

Advancements in large-scale astrometric and photometric surveys have revolutionized our ability to conduct these studies. These surveys provide unprecedented catalogs of stellar positions, motions, and spectral properties, enabling researchers to identify and analyze specific stellar types that act as powerful probes. For instance, certain evolutionary phases of stars, like Red Clump stars, exhibit remarkably stable intrinsic luminosities, making them excellent standard candles for mapping galactic distances. Similarly, the identification of chemically peculiar stars, such as Carbon-Enhanced Metal-Poor (CEMP) stars, offers a unique window into the early universe, preserving the chemical signatures of the first generations of stars.

My work focuses on leveraging these extensive astronomical datasets to address key questions in galactic structure and stellar archaeology. I have developed a comprehensive photometric sample of 2.6 million Red Clump stars, meticulously selected to span from the inner to the outer regions of the Milky Way. By exploiting the well-calibrated intrinsic luminosity of these stars, this sample serves as a robust foundation for mapping the detailed density distribution and three-dimensional structure of the Galactic disk and bulge, providing critical constraints on models of galactic formation and evolution.

Furthermore, my research extends into stellar archaeology, utilizing the rich spectral information from the Gaia DR3 mission. I have applied sophisticated analysis techniques to BP/RP spectra to identify a significant number of Carbon-Enhanced Metal-Poor (CEMP) star candidates. These extremely ancient stars are considered stellar fossils, bearing the chemical imprints of the earliest nucleosynthesis events in the universe. Their study is crucial for understanding the properties of the first stars, the mechanisms of chemical enrichment in the nascent Milky Way, and the evolutionary pathways of very low-metallicity stellar populations.

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
