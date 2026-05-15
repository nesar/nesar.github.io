---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe's large-scale structure, from galaxy clusters to the vast cosmic web, is primarily governed by the distribution and evolution of dark matter. This enigmatic substance, making up about 27% of the universe's energy density, dictates the gravitational scaffolding upon which luminous matter assembles. Understanding its fundamental nature and how it interacts on cosmological scales is central to modern astrophysics and cosmology, often involving the testing of current cosmological models like Lambda-CDM against alternative theories, including modified gravity.

The intricate network of voids, sheets, filaments, and massive clusters, known as the cosmic web, is a direct consequence of dark matter's gravitational collapse, providing a powerful probe of cosmological parameters. Researchers employ sophisticated N-body and hydrodynamic simulations to model these structures, while vast observational surveys, utilizing weak gravitational lensing and galaxy cluster detection, provide crucial data for testing theoretical predictions. A key challenge lies in precisely characterizing the fine-grained, multi-stream structure of dark matter within haloes and the cosmic web, which requires advanced analytical tools, phase-space information, and cutting-edge machine learning and high-fidelity numerical simulations.

My research significantly contributes to these efforts by developing and applying novel methodologies to uncover the intricate structure and dynamics of the dark matter universe. I have focused on understanding the dark matter web and halo formation through a "multistream view," analyzing the phase-space of dark matter particles to reveal the underlying caustic design and the topological and geometric properties of these structures. This approach provides a more complete picture beyond simple density fields. Furthermore, I have leveraged auxiliary-variable-guided generative models to uncover the physical drivers governing dark matter halo structures, offering new insights into the interplay of various physical parameters on halo formation.

Beyond structural analysis, my work extends to constraining cosmological models and improving simulation capabilities. I have applied advanced techniques like $k$-cut cosmic shear analysis to Hyper Suprime-Cam (HSC) data, providing robust constraints on modified gravity theories such as $f(R)$ gravity. I have also been involved in large-scale observational efforts, including the SPTpol Extended Cluster Survey, which probes cosmology through galaxy cluster abundances. On the simulation front, I contributed to modeling galaxy formation in cosmological simulations using CRK-HACC, a high-fidelity hydrodynamic code. This comprehensive approach, blending theoretical development, advanced data analysis, and high-performance computing, aims to deepen our understanding of dark matter and the fundamental laws governing our universe.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Topology and geometry of the dark matter web: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Topology and geometry of the dark matter web: a multistream view</div>
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
