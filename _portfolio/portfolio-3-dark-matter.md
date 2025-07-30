---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe's large-scale structure, dominated by enigmatic dark matter and dark energy, dictates the formation and evolution of galaxies and galaxy clusters. Understanding the distribution and dynamics of dark matter is central to modern cosmology, providing insights into the fundamental laws of gravity and the universe's ultimate fate. Researchers explore this cosmic architecture, often referred to as the "cosmic web," through diverse observational probes and theoretical frameworks, seeking to unravel the universe's composition and evolution.

Key observational techniques include gravitational lensing, such as cosmic shear, which measures the subtle distortions of background galaxy images by foreground dark matter. Surveys of galaxy clusters, the universe's most massive gravitationally bound structures, offer another avenue to probe the growth of structure. Furthermore, studying individual stars within our own galaxy provides crucial information on the local dark matter distribution and the Milky Way's formation history. These empirical measurements are then compared with predictions from N-body simulations and modified gravity theories, such as f(R) gravity, to test and refine our cosmological models.

My research significantly contributes to this endeavor by bridging theoretical modeling with cutting-edge observational data analysis. I have extensively developed and applied the "multi-stream view" of dark matter, offering a granular understanding of the internal structure of dark matter haloes and the intricate "caustic design" of the cosmic web. This multi-stream approach, detailed in my work on the "topology and geometry of the dark matter web," provides critical insights into the phase-space structure of dark matter and its implications for direct and indirect dark matter detection experiments.

In parallel, I have engaged in observational cosmology to directly test cosmological models. I performed a "k-cut cosmic shear analysis" using Hyper Suprime-Cam First-Year data to constrain f(R) gravity, pushing the boundaries of modified gravity tests. My work also leverages large photometric samples, such as the 2.6 million Red Clump stars observed by Gaia DR3, to map the distribution of visible and dark matter within the Milky Way, extending from the inner to the outer galaxy. Additionally, I have identified Carbon-Enhanced Metal-Poor star candidates using Gaia DR3 spectra to probe the earliest epochs of star formation and chemical evolution, and contributed to the SPTpol Extended Cluster Survey, enhancing our understanding of high-mass dark matter haloes and the large-scale structure. These diverse approaches collectively advance our comprehension of the universe's composition, evolution, and underlying physical laws.

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
