---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter constitutes approximately 27% of the universe's mass-energy content, playing a crucial role in the formation and evolution of cosmic structures, from individual galaxies to the vast network known as the cosmic web. This invisible substance interacts gravitationally, providing the scaffolding upon which baryonic matter collapses and forms stars and galaxies. Understanding its properties and distribution is paramount to developing a complete picture of the universe, complementing insights derived from the standard Lambda-CDM cosmological model and probing alternative theories of gravity.

The cosmic web, characterized by a hierarchical structure of dense galaxy clusters, filamentary connections, sheet-like walls, and vast voids, represents the largest-scale organization of matter in the universe. Its intricate topology and geometry are direct consequences of dark matter's gravitational influence. Researchers leverage a diverse array of observational techniques, including cosmic shear analyses of distant galaxies, large-scale surveys of galaxy clusters, and precise measurements of stellar populations within our own Milky Way, to map this structure and infer the underlying dark matter distribution. These observational probes are essential for testing theoretical predictions and refining our cosmological models.

My research contributes significantly to unraveling the mysteries of dark matter and the cosmic web, employing cutting-edge methodologies across multiple scales. I have developed and applied advanced techniques such as k-cut cosmic shear analysis to the Hyper Suprime-Cam First-Year data, providing robust constraints on modified gravity theories like f(R) gravity, which propose alternatives to dark energy. Furthermore, my work extends to the fine-grained structure of dark matter, utilizing a multi-stream view to characterize the caustic design, topology, and geometry of dark matter haloes and the cosmic web itself. This involves analyzing the paths of dark matter particles to reconstruct the complex, interwoven nature of these structures.

Beyond theoretical and simulation-based studies, I have directly engaged with large observational datasets to trace cosmic structures. This includes leveraging the SPTpol Extended Cluster Survey to study galaxy clusters, which are crucial probes of the cosmic web's densest nodes. Within the Milky Way, I have used a photometric sample of 2.6 million Red Clump stars to map galactic structure from the inner to outer regions, providing insights into the distribution of dark matter locally. Additionally, I have analyzed BP/RP spectra from Gaia DR3 to identify Carbon-Enhanced Metal-Poor star candidates, which serve as excellent tracers of the Milky Way's oldest stellar populations and, by extension, its early dark matter halo assembly. Collectively, my work advances our understanding of dark matter's nature, its imprint on the cosmic web, and the precise observational techniques required to uncover these fundamental cosmological truths.

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
