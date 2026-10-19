---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

Dark matter and cosmology represent fundamental pillars of modern astrophysical research, seeking to unravel the composition, evolution, and large-scale structure of the universe. Dark matter, an enigmatic substance that interacts only gravitationally, constitutes approximately 27% of the cosmos and plays a crucial role in the formation and growth of galaxies and cosmic structures. Its precise nature remains unknown, driving extensive theoretical and observational efforts to detect it directly, characterize its properties, and understand its impact on cosmic evolution.

Cosmology explores the universe from its earliest moments to its present-day state, investigating phenomena such as the cosmic microwave background, the expansion of space, and the formation of the vast cosmic web. This intricate network of voids, sheets, filaments, and massive dark matter haloes provides the scaffolding upon which galaxies form and evolve. Researchers leverage advanced numerical simulations, sophisticated statistical analyses of astronomical surveys, and novel computational techniques, including machine learning, to probe these mysteries, test cosmological models, and constrain alternative theories of gravity.

My research significantly contributes to this field by advancing our understanding of dark matter distribution and the cosmic web. I have developed and applied multi-stream analyses to characterize the topology, geometry, and caustic design of dark matter haloes and the cosmic web, providing a detailed portrait of these fundamental structures. Through innovative applications of auxiliary-variable-guided generative models and deep learning, I have uncovered physical drivers influencing dark matter halo structures and benchmarked AI-generated cosmic web simulations against physical expectations. Furthermore, I have contributed to sophisticated cosmological simulations, such as CRK-HACC, to model galaxy formation within these dark matter environments, bridging the gap between dark matter dynamics and observable galaxy populations.

My work also focuses on utilizing gravitational lensing as a powerful probe of cosmology and dark matter. I have contributed to constraining alternative theories of gravity, such as $f(R)$ gravity, using k-cut cosmic shear analysis applied to large datasets like the Hyper Suprime-Cam first-year data. In weak lensing, I have developed methods to reduce model error in cluster mass estimation via optimized galaxy selection. Moreover, I have designed modular deep learning pipelines for efficient detection and modeling of galaxy-scale strong gravitational lenses. Beyond lensing, my contributions include developing differentiable predictions for large-scale structure with SHAMNet and analyzing observational data from missions like SPHEREx and surveys like SPTpol. This includes identifying new stellar populations (e.g., Red Clump and Carbon-Enhanced Metal-Poor stars from Gaia DR3) to characterize galactic substructures, which serve as crucial tracers of the dark matter halo.

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
