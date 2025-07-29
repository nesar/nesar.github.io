---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The mysteries of dark matter and the universe's large-scale structure stand at the forefront of modern cosmology. Despite the remarkable success of the Lambda Cold Dark Matter (ΛCDM) model in explaining a vast array of cosmological observations, the fundamental nature of dark matter and dark energy remains unknown. Furthermore, understanding the formation and evolution of structures, from the largest cosmic voids and filaments down to individual galaxy haloes, requires both precise theoretical frameworks and robust observational constraints. This intricate pursuit involves analyzing subtle gravitational effects like cosmic shear, meticulously mapping the distribution of galaxies and stars, and probing the complex dynamics of the cosmic web.

Contemporary research in this field employs a diverse array of observational techniques, ranging from precision cosmological surveys to detailed stellar population studies within our own galaxy. Observations of the large-scale distribution of matter, such as through weak gravitational lensing (cosmic shear), provide crucial insights into the growth of structure and can test alternative gravitational theories beyond General Relativity. Concurrently, the study of the cosmic web, composed of vast filaments, clusters, and voids, necessitates advanced analytical tools to characterize its complex topology and geometry. Probing the dynamics of dark matter on smaller scales, within halos and along caustics, also offers a unique window into its properties, while the distribution and kinematics of stars in our Milky Way provide crucial local insights into its dark matter halo.

My research directly addresses these challenges by developing and applying novel methodologies to large-scale astrophysical datasets. For instance, I have utilized a k-cut cosmic shear analysis of Hyper Suprime-Cam data to place stringent constraints on modified gravity theories, specifically f(R) gravity, thereby testing alternatives to ΛCDM. To better understand the distribution of baryonic matter within the Milky Way and provide context for its dark matter halo, I developed a photometric sample of 2.6 million Red Clump Stars from Gaia data, enabling detailed mapping from the inner to outer galaxy. Furthermore, my work has significantly advanced our understanding of the non-linear dark matter distribution through the development and application of a multi-stream formalism. This approach has allowed me to meticulously characterize the caustic design, topology, and geometry of dark matter haloes and the cosmic web, providing a comprehensive multi-stream portrait of its intricate structure.

Beyond probing the dark matter distribution, my contributions extend to identifying and characterizing significant astrophysical objects for cosmological and stellar archaeology studies. I have participated in the SPTpol Extended Cluster Survey, contributing to the identification of galaxy clusters that serve as powerful cosmological probes. Additionally, I have employed BP/RP spectra from Gaia DR3 to identify Carbon-Enhanced Metal-Poor (CEMP) star candidates. These rare stars are relics from the early universe, providing invaluable insights into primordial nucleosynthesis and the conditions of the very first stellar generations, offering indirect clues about the early universe's dark matter distribution. Collectively, my research leverages a broad spectrum of techniques—from large-scale statistical analysis of cosmic shear and galaxy cluster properties to high-resolution mapping of stellar populations and the detailed multi-stream analysis of dark matter dynamics—to contribute to a more complete picture of our universe's composition and evolution.

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
