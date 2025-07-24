---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative paradigm across various scientific disciplines, offering unprecedented capabilities for data analysis, discovery, and simulation. In an era characterized by increasingly vast and complex datasets, fields such as astrophysics, high-energy physics, and materials science face challenges ranging from extracting subtle signals from noise and identifying rare anomalies to modeling intricate physical phenomena and accelerating computationally intensive simulations. Machine learning techniques provide powerful tools to address these challenges, enabling researchers to uncover hidden patterns, make data-driven predictions, and gain deeper insights into the fundamental laws governing our universe.

The application of machine learning in scientific research particularly excels in handling high-dimensional data, automating complex analyses, and enhancing the efficiency of traditional scientific workflows. Key areas of focus include the development of sophisticated deep learning architectures for image and signal processing, advanced generative models for data synthesis and anomaly detection, and robust probabilistic frameworks for uncertainty quantification. There is also a strong emphasis on developing interpretable and physically informed AI models, ensuring that machine learning insights are not only accurate but also explainable and consistent with known scientific principles, thereby accelerating discovery and pushing the boundaries of what is possible in data-intensive research.

My research extensively explores the innovative application of machine learning, particularly deep learning and generative models, to tackle pressing challenges across astrophysics, cosmology, and high-energy physics. A significant portion of my work focuses on developing and applying generative adversarial networks (GANs) for tasks such as robust anomaly detection in astronomical images, including data from Hyper Suprime-Cam, and for the synthesis of physically consistent cosmic structures. A core emphasis in this area has been enhancing the interpretability of these complex models; I have developed methods for statistically disentangling latent spaces in generative models, guided by domain-specific physical factors. Complementary to this, I have also contributed to providing interpretable uncertainty quantification in AI applications for high-energy physics, critical for robust scientific conclusions.

Beyond generative approaches, my work encompasses a broad spectrum of advanced machine learning techniques applied to diverse scientific problems, significantly advancing data analysis and predictive modeling. I have designed and implemented neural network-based solutions for challenging image processing tasks, such as Point Spread Function deconvolution in astronomy, which improves image clarity, and for exploring galaxy morphology beyond the traditional Hubble Sequence using unsupervised machine learning. I developed a modular deep learning pipeline for efficient detection and modeling of galaxy-scale strong gravitational lenses, a crucial tool for cosmology. My contributions also include probabilistic redshift estimation from synthetic spectra (SYTH-Z), global field reconstruction from sparse sensor data leveraging Voronoi tessellation-assisted deep learning, and the application of differentiable predictions for large-scale structure with SHAMNet. Furthermore, I have applied probabilistic modeling and automated machine learning frameworks to analyze high-dimensional stress fields, demonstrating the versatility and broad applicability of these ML approaches across various scientific domains to accelerate discovery and enhance understanding.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from machine learning synthetic spectra for probabilist" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: machine learning synthetic spectra for probabilist</div>
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
