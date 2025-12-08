---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The advent of increasingly complex scientific datasets across fields like astrophysics and materials science has necessitated innovative computational approaches to extract meaningful insights. Machine learning, particularly deep learning, has emerged as a transformative paradigm, offering powerful tools for automating data analysis, accelerating simulations, and discovering hidden patterns that traditional methods often miss. In astronomy and cosmology, where surveys generate petabytes of images and spectra, these techniques are crucial for tackling challenges such as classifying celestial objects, detecting rare phenomena, and modeling the universe's evolution.

The application of machine learning in scientific discovery extends from simulating the large-scale structure of the cosmos to dissecting the properties of individual stars and galaxies. Advanced methodologies like generative adversarial networks (GANs) and deep neural networks are employed to identify anomalies in vast image datasets, enhance the resolution of astronomical observations through deconvolution, and build robust pipelines for object detection and characterization. Furthermore, unsupervised machine learning offers new avenues for exploring complex morphological spaces without prior assumptions, while rigorous benchmarking ensures the physical fidelity and reliability of AI-generated scientific models. A concurrent focus remains on developing interpretable AI models to foster trust and facilitate deeper scientific understanding.

My research centers on developing and applying cutting-edge machine learning methodologies to address fundamental questions in astrophysics, cosmology, and broader scientific domains. I have contributed significantly to benchmarking AI-evolved models for cosmological structure formation, ensuring that AI-generated cosmic web simulations maintain physical consistency with established theory. Furthermore, I have explored the application of probabilistic modeling and automated machine learning frameworks for high-dimensional scientific data, demonstrating the versatility of these approaches beyond traditional astronomical applications.

I have developed and deployed sophisticated deep learning pipelines for a range of astronomical tasks, including the efficient detection and modeling of galaxy-scale strong gravitational lenses, a crucial step for probing dark matter and cosmology. My work also involved pioneering the use of generative adversarial networks for anomaly detection in large astronomical image surveys, enabling the discovery of unusual galaxies. In stellar astrophysics, I have leveraged neural networks for point spread function deconvolution to improve image quality and contributed to identifying carbon-enhanced metal-poor star candidates and mapping red clump stars using vast photometric datasets from missions like Gaia. Additionally, I have focused on enhancing interpretability in generative models through statistically disentangled latent spaces and provided guidance on best practices for impactful machine learning research in astronomy, contributing to the responsible advancement of the field.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
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
