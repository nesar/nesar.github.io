---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The integration of Machine Learning (ML) and Artificial Intelligence (AI) is rapidly transforming the landscape of scientific discovery, offering powerful tools to address complex challenges across diverse domains. From unraveling the mysteries of the cosmos to optimizing engineering processes, ML methodologies enable scientists to extract nuanced insights from massive, high-dimensional datasets, accelerate computationally intensive simulations, and automate intricate analytical tasks. Key areas of application include large-scale astronomical surveys that generate petabytes of data, demanding sophisticated methods for object detection, classification, and physical parameter estimation, as well as in materials science and engineering where predictive modeling can inform design and material development.

This revolution is driven by advances in deep learning, generative models, and probabilistic frameworks, which provide robust solutions for problems ranging from anomaly detection and feature extraction to causal inference and uncertainty quantification. These techniques are crucial for navigating the inherent noise and incompleteness often present in scientific data, fostering a new era of data-driven science where observational and simulated data can be fully leveraged to push the boundaries of current understanding.

My research focuses on developing and applying advanced machine learning techniques to address critical challenges in astrophysics, cosmology, and engineering. I have developed innovative methodologies that span a wide spectrum of AI paradigms, including generative modeling, probabilistic inference, and interpretable deep learning. For instance, my work includes pioneering the use of Generative Adversarial Networks (GANs) for anomaly detection in astronomical images, such as those from Hyper Suprime-Cam, and for generating synthetic spectra (SYTH-Z) to improve probabilistic redshift estimation. I have also explored the physical benchmarking of AI-evolved cosmological structure formation and generative models of the cosmic web, aiming to ensure scientific validity while leveraging AI's accelerative power.

Furthermore, I have significantly contributed to enhancing interpretability and uncertainty quantification in AI models, crucial for scientific trust and discovery. This includes developing methods for statistically disentangled latent spaces in generative models guided by physical factors, and frameworks for interpretable uncertainty quantification in high energy physics (HEP). My work also extends to practical applications such as multi-task modeling for sparse engineering data, reducing model error in weak lensing cluster mass estimation through optimized galaxy selection, and developing neural network-based Point Spread Function deconvolution for astronomical applications. I have applied deep learning to map the Milky Way using millions of Red Clump stars, detect Carbon-Enhanced Metal-Poor stars from Gaia data, and explore galaxy morphology "Beyond the Hubble Sequence" using unsupervised methods, thereby providing robust, scalable, and interpretable solutions to complex scientific problems.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
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
