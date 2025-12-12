---
title: "Dark Matter, Cosmology & Astrophysics"
excerpt: "Research in dark matter, cosmology & astrophysics"
collection: portfolio
---

The study of dark matter and the large-scale structure of the universe is central to modern cosmology and astrophysics. Understanding the nature of dark matter, which constitutes approximately 27% of the universe's mass-energy budget, is crucial for unraveling the formation and evolution of cosmic structures, from individual galaxies to the vast network of filaments, walls, and voids known as the cosmic web. This research area also delves into testing the fundamental laws of gravity on cosmological scales, exploring alternatives to General Relativity, and developing sophisticated numerical simulations to model the complex interplay of dark matter, baryonic matter, and gravity over cosmic time.

Researchers employ a diverse array of methodologies, including weak gravitational lensing analyses, which measure subtle distortions in galaxy shapes caused by foreground mass distributions, to map the dark matter distribution. Large-scale photometric and spectroscopic surveys of galaxies and stars provide crucial observational data for tracing cosmic structures, identifying unique stellar populations, and characterizing galactic environments. Complementing these observations are high-resolution N-body and hydrodynamic simulations, essential for predicting the emergence of the cosmic web and galaxy formation within theoretical frameworks. Furthermore, specialized astronomical missions are designed to gather precise data across various wavelengths, enabling detailed studies of distant galaxy clusters, the cosmic microwave background, and the distribution of matter.

My work significantly contributes to these efforts by advancing both our theoretical understanding and observational capabilities. I have focused on exploring the intricate structure of the dark matter web through a "multistream view," which analyzes the phase-space characteristics of dark matter particles to reveal the complex substructures within halos and filaments. This includes developing the "caustic design" concept, which provides a robust method for delineating boundaries and identifying accreted structures within dark matter halos, thereby offering new insights into their formation history and dynamics. Furthermore, I have investigated the topology and geometry of the dark matter web using these multistream techniques, providing a more comprehensive portrait of how the universe's backbone is formed.

On the observational and simulation fronts, I have applied sophisticated techniques to constrain fundamental cosmological models and improve our modeling capabilities. This includes performing a "k-cut cosmic shear analysis" using Hyper Suprime-Cam data to test "f(R) gravity" models, thereby probing deviations from General Relativity on cosmological scales. My research also extends to the realm of galaxy formation, where I have contributed to "modeling galaxy formation in cosmological simulations with CRK-HACC," enhancing our ability to simulate realistic galaxy populations. Additionally, I have been involved in analyzing large astronomical datasets, such as identifying "Carbon-Enhanced Metal-Poor star candidates from BP/RP Spectra in Gaia DR3" to shed light on the early universe, and contributing to major survey efforts like the "SPTpol Extended Cluster Survey" and the design of future missions such as "The SPHEREx Satellite Mission." These contributions collectively aim to refine our understanding of dark matter, the cosmic web, and the processes that govern the evolution of the universe.

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
