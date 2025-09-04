---
title: "Cosmic Structure & Cosmology"
excerpt: "Research in cosmic structure & cosmology"
collection: portfolio
---

Cosmic structure formation is a cornerstone of modern cosmology, investigating how the universe evolved from a nearly uniform state to the complex tapestry of galaxies, clusters, and voids observed today. This evolution is primarily governed by the interplay of dark matter, dark energy, and ordinary baryonic matter. Understanding the distribution and dynamics of the cosmic web – the filamentary network of dark matter and galaxies – provides crucial insights into the universe's fundamental constituents and its expansion history.

Probing these cosmic structures requires sophisticated observational techniques and robust theoretical modeling. Weak gravitational lensing, which measures the subtle distortions of background galaxy shapes due to foreground mass, is a powerful tool for mapping dark matter distribution and constraining cosmological parameters. Galaxy clusters, as the largest gravitationally bound structures, serve as invaluable probes of structure growth. Furthermore, the kinetic Sunyaev-Zel'dovich (kSZ) effect offers a unique window into the peculiar velocities of galaxy clusters, shedding light on the underlying large-scale flow of matter.

My research focuses on developing and applying advanced analytical and computational techniques to understand the cosmic web and constrain cosmological models, particularly those involving modifications to general relativity. I have contributed to constraining alternative gravity theories, such as $f(R)$ gravity, by employing novel methodologies like a $k$-cut cosmic shear analysis applied to large datasets, including the Hyper Suprime-Cam data, and developing matter power spectrum emulators for these modified cosmologies. A significant part of my work involves characterizing the intricate nature of the dark matter web, exploring its "caustic design," and offering a "multistream view" to understand its topology and geometry, thereby providing a more complete picture of how dark matter structures evolve.

Furthermore, I have pioneered the application of machine learning and artificial intelligence to enhance predictions and reduce model errors in large-scale structure analysis. This includes developing "differentiable predictions for large-scale structure with SHAMNet" and establishing "physical benchmarking for AI-generated cosmic web" to ensure the astrophysical validity of these new models. I have also developed deep neural network approaches for "peculiar velocity estimation from the kinetic SZ effect," significantly improving the accuracy of these measurements. In observational cosmology, I have been involved in major surveys like "The SPTpol Extended Cluster Survey" and refined cluster mass estimation techniques by "reducing model error using optimised galaxy selection" for weak lensing analyses, leading to more robust cosmological inferences. My work ultimately aims to provide more precise constraints on cosmological parameters and a deeper understanding of the universe's large-scale structure.

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
