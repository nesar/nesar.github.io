---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine Learning (ML) is rapidly transforming scientific research by offering powerful tools to analyze complex, high-dimensional, and often sparse datasets. This paradigm shift enables scientists to extract meaningful insights, automate discovery, and build predictive models across diverse disciplines. Fundamental challenges in scientific data analysis, such as identifying subtle anomalies, reconstructing incomplete information, understanding intricate patterns, and accelerating computationally intensive simulations, are increasingly addressed through sophisticated ML methodologies.

Within fields like astronomy and engineering, ML applications are particularly impactful. In astronomy, ML facilitates the classification and characterization of celestial objects, from galaxies to transient phenomena, often operating on vast imaging and spectroscopic datasets. It also aids in overcoming observational limitations, such as atmospheric blurring or incomplete spatial coverage. For engineering applications, ML can optimize design processes, predict material behavior, and manage complex systems, especially when dealing with high-dimensional parameter spaces and limited experimental data. The focus extends to developing robust, interpretable, and scalable ML solutions tailored to the unique demands of scientific inquiry.

My research specifically targets these challenges, developing and applying advanced machine learning techniques to address critical problems in astrophysics and engineering. I have developed multi-task modeling approaches to handle sparse data in engineering applications and utilized probabilistic modeling and automated machine learning (AutoML) frameworks for high-dimensional stress field analysis. In astronomy, my work spans several areas: I have explored natural language processing techniques to predict novel concept-object associations by mining scientific literature and contributed to the strategic planning for AI/ML opportunities within large collaborations like the Rubin LSST Dark Energy Science Collaboration.

A significant portion of my work involves deep learning and generative models. I have developed neural network-based methods for point spread function deconvolution, crucial for precise astronomical measurements, and engineered modular deep learning pipelines for the detection and modeling of strong gravitational lenses. My research also utilizes Generative Adversarial Networks (GANs) for anomaly detection in astronomical images, including Hyper Suprime-Cam galaxy images, to identify unusual objects in large surveys. Furthermore, I have applied deep neural networks for peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect and employed unsupervised machine learning to explore galaxy morphology beyond traditional classification schemes. A key theme in my generative modeling work is enhancing interpretability by creating statistically disentangled latent spaces, guided by generative factors, for clearer scientific understanding. Additionally, I have developed innovative global field reconstruction methods from sparse sensors using Voronoi tessellation-assisted deep learning, demonstrating versatility across diverse scientific data types.

<div class="research-figures">
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
