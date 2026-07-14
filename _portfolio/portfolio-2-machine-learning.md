---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning and artificial intelligence are rapidly transforming scientific research, offering powerful new tools to analyze vast and complex datasets, accelerate discovery, and tackle problems intractable with traditional methods. These advancements are particularly impactful in fields dealing with high-dimensional data, sparse observations, or the need for rapid, automated analysis. Key challenges include developing robust models that can generalize well, providing interpretable insights into complex phenomena, accurately quantifying uncertainties, and efficiently processing the deluge of data from modern scientific instruments and simulations. Techniques such as deep learning, generative modeling, and probabilistic frameworks are being harnessed to push the boundaries of what is possible in scientific data analysis.

Across various scientific domains, machine learning is enabling significant progress. In astrophysics and cosmology, these methods are crucial for handling petabytes of data from surveys like the Rubin LSST and Gaia, facilitating tasks such as the photometric identification of millions of red clump stars, the discovery of rare stellar populations like Carbon-Enhanced Metal-Poor stars, and detailed galaxy morphology studies through unsupervised learning. Advanced deep learning pipelines are also instrumental in detecting and modeling galaxy-scale strong gravitational lenses, reconstructing point spread functions for precise astronomical measurements, and estimating cosmological parameters like peculiar velocities from the kinetic Sunyaev-Zel'dovich effect. Beyond cataloging and classification, generative adversarial networks (GANs) are proving invaluable for anomaly detection in astronomical images, pinpointing unusual or novel phenomena that warrant further investigation.

The scope of machine learning in science also extends to engineering applications and high energy physics. In engineering, machine learning addresses the challenge of sparse or high-dimensional data, for instance, in multi-task modeling for complex systems or reconstructing global fields from limited sensor measurements using Voronoi tessellation-assisted deep learning. For high energy physics and other domains where model reliability is paramount, a strong focus is placed on enhancing interpretability and quantifying uncertainty in AI models. This involves developing methodologies for statistically disentangled latent spaces guided by generative factors, ensuring that models provide transparent and trustworthy predictions crucial for scientific validation and discovery.

My work specifically focuses on developing and deploying cutting-edge machine learning and AI methodologies to address critical challenges across a broad spectrum of scientific disciplines. I have pioneered the application of deep learning, generative models, and probabilistic frameworks to extract profound insights from complex scientific data. This includes developing novel techniques for enhancing interpretability in generative models, creating statistically disentangled latent spaces that reveal underlying generative factors, and integrating interpretable uncertainty quantification into AI models for High Energy Physics. I have also designed and implemented automated machine learning frameworks for high-dimensional problems, such as stress field analysis, and multi-task learning approaches for engineering applications with sparse data.

A significant portion of my research is dedicated to advancing astronomical data analysis, where I have developed deep learning pipelines for detecting and modeling strong gravitational lenses, created neural network-based point spread function deconvolution methods, and applied generative adversarial networks for robust anomaly detection in galaxy images from surveys like Hyper Suprime-Cam. Furthermore, I have contributed to large-scale data products, such as the photometric sample of 2.6 million red clump stars, and explored new methods for probabilistic redshift estimation using machine learning synthetic spectra (SYTH-Z). My contributions also extend to strategic discussions on AI/ML opportunities for collaborations like the Rubin LSST Dark Energy Science Collaboration, aiming to leverage these technologies for future groundbreaking discoveries in cosmology and astrophysics.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
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
