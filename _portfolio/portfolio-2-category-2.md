---
title: "Stellar & Galaxy Astronomy"
excerpt: "Research in stellar & galaxy astronomy"
collection: portfolio
---

Stellar and galaxy astronomy encompasses the study of the fundamental building blocks of the universe, from individual stars and their populations to the grand architectures of galaxies and the large-scale cosmic web. This field seeks to understand the formation, evolution, and dynamics of these celestial objects, providing insights into the origin and future of the cosmos. Key areas of investigation include mapping the structure and composition of the Milky Way, characterizing the diverse morphologies and evolutionary pathways of external galaxies, and unraveling the nature of dark matter and dark energy through gravitational lensing phenomena.

Advancements in observational capabilities, such as those provided by large-scale surveys and space-based missions, have led to an unprecedented deluge of astronomical data. Extracting meaningful scientific insights from these massive datasets presents significant computational and analytical challenges. Consequently, modern astronomical research increasingly leverages sophisticated data science techniques, including machine learning, deep learning, and advanced statistical modeling, to classify objects, infer properties, and test theoretical predictions with greater precision and efficiency. These methodologies are crucial for pushing the boundaries of our understanding of cosmic structures and processes.

My research contributes to these endeavors by developing and applying cutting-edge techniques across various scales of stellar and galaxy astronomy. In stellar populations, I have utilized large photometric datasets to map the Milky Way's structure and identify rare stellar types. For instance, my work involved creating a comprehensive photometric sample of 2.6 million Red Clump stars to trace the inner to outer regions of our galaxy, providing vital constraints on Galactic disk properties. Furthermore, I have focused on identifying Carbon-Enhanced Metal-Poor star candidates from BP/RP spectra within Gaia DR3, leveraging the precise spectroscopic information to pinpoint these ancient stars crucial for understanding early stellar nucleosynthesis and galactic chemical evolution.

At the galactic and cosmological scales, my contributions include enhancing our ability to characterize galaxies and estimate cosmic parameters. I have developed methods to explore galaxy morphology beyond the traditional Hubble Sequence by employing unsupervised machine learning techniques, revealing new classifications and evolutionary pathways that are not captured by conventional approaches. To improve the precision of cosmological measurements, I contributed to reducing model error in weak lensing cluster mass estimation through optimized galaxy selection, ensuring more robust and accurate inferences about dark matter halos. Addressing the challenge of vast spectral data, I have developed SYTH-Z, a framework that uses machine learning to generate synthetic spectra for probabilistic redshift estimation, offering a powerful tool for large-scale spectroscopic surveys. Moreover, I designed and implemented a modular deep learning pipeline for both the detection and detailed modeling of galaxy-scale strong gravitational lenses, which are invaluable probes of dark matter distribution and galaxy mass profiles.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/carbon-enhanced-metal-poor-star-candidates-from-bp_plot_1_17c64dee.png" alt="Figure from Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in $Gaia$ DR3</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
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
