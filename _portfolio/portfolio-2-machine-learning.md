---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative paradigm across diverse scientific disciplines, offering powerful tools to navigate and extract insights from increasingly complex and voluminous datasets. Its applications span from fundamental physics and astronomy to materials science and biology, enabling advancements in data analysis, pattern recognition, predictive modeling, and the generation of synthetic data. Researchers leverage machine learning to tackle challenges such as high-dimensional feature spaces, the need for robust anomaly detection, the interpretation of intricate physical phenomena, and the efficient processing of large-scale scientific simulations and observational data.

A core focus in this domain involves the development of robust and interpretable AI systems that not only provide accurate predictions but also offer insights into the underlying scientific processes. This includes addressing crucial aspects like uncertainty quantification, ensuring models can express their confidence in predictions, and enhancing model explainability to foster trust and facilitate new scientific discoveries. Furthermore, machine learning models are becoming indispensable for tasks like automated data curation, real-time analysis, and the accelerated exploration of parameter spaces in complex scientific simulations.

My research focuses on developing and applying advanced machine learning techniques to address challenging problems in astrophysics, high-energy physics, and broader scientific data analysis. I have pioneered methods for enhancing interpretability in generative models by guiding latent spaces with known scientific factors, and developed a probabilistic modeling and automated machine learning framework for analyzing high-dimensional stress fields. My work also encompasses the crucial area of uncertainty quantification in AI for high-energy physics, ensuring that machine learning predictions are not only accurate but also provide reliable confidence estimates.

A significant portion of my contributions lies in astronomical applications, where I have developed neural network-based methods for point spread function deconvolution, crucial for sharpening astronomical images. I have also advanced anomaly detection in galaxy images using Generative Adversarial Networks (GANs), and explored galaxy morphology beyond traditional classification using unsupervised learning. Furthermore, I have developed a modular deep learning pipeline for strong gravitational lens detection and modeling, and employed deep neural networks for peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect. My research also includes the creation of machine learning synthetic spectra for probabilistic redshift estimation (SYTH-Z), the physical benchmarking of AI-generated cosmic web simulations, and global field reconstruction from sparse sensor data using Voronoi tessellation-assisted deep learning. These efforts collectively aim to push the boundaries of scientific discovery by providing more accurate, efficient, and interpretable analytical tools.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_2_4e0250f1.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_3_4f111230.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
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
