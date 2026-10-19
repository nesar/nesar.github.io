---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The application of machine learning (ML) and artificial intelligence (AI) is rapidly transforming scientific research, enabling unprecedented capabilities for data analysis, discovery, and simulation across diverse fields. Scientific datasets often present unique challenges, characterized by their high dimensionality, sparsity, and the critical need for robust interpretability and uncertainty quantification to ensure trustworthiness and scientific rigor. This necessitates the development of specialized AI/ML methodologies that can not only extract patterns but also adhere to physical laws and provide actionable insights in domains ranging from astrophysics and cosmology to materials science and high energy physics.

A significant frontier in this interdisciplinary space involves leveraging advanced ML paradigms to address complex scientific problems. Generative models, for instance, offer powerful tools for data synthesis, anomaly detection, and understanding underlying data distributions. Multi-task learning can improve efficiency by simultaneously addressing related problems, while probabilistic modeling provides frameworks for quantifying uncertainty inherent in measurements and predictions. Deep learning techniques are being tailored to solve specific scientific tasks such as deconvolution, field reconstruction from sparse measurements, and unsupervised exploration of complex datasets, pushing the boundaries of what is discoverable from increasingly large and intricate scientific data streams.

My research broadly focuses on developing and applying innovative machine learning and artificial intelligence techniques to tackle some of the most pressing challenges in scientific data analysis and discovery. I have developed multi-task modeling approaches specifically for engineering applications characterized by sparse data, enhancing predictive capabilities under limited information. My work also extends to mining scientific literature to predict new concept-object associations in astronomy, a critical task for identifying novel phenomena and optimizing observations for collaborations such as the Rubin LSST Dark Energy Science Collaboration, where I have actively identified opportunities for AI/ML integration. Furthermore, I have contributed to benchmarking AI-evolved cosmological structure formation simulations, ensuring the reliability and scientific validity of AI-accelerated discoveries.

A core focus of my contributions lies in enhancing the interpretability and robustness of AI models for scientific applications. I have developed methods to enhance interpretability in generative modeling by creating statistically disentangled latent spaces, guided by generative factors in scientific datasets. This advancement is crucial for understanding the underlying physical processes that drive data generation. Complementing this, I have extensively utilized Generative Adversarial Networks (GANs) for robust anomaly detection in various astronomical images, including those from Hyper Suprime-Cam, helping scientists identify unusual events and objects. My work also encompasses the application of probabilistic modeling and automated machine learning frameworks for analyzing high-dimensional stress fields and the development of neural network-based Point Spread Function deconvolution techniques for improving the clarity of astronomical images. Additionally, I have developed interpretable uncertainty quantification methods for AI in High Energy Physics, and pioneered Voronoi tessellation-assisted deep learning for global field reconstruction from sparse sensor data. To push the boundaries of astronomical discovery, I have employed unsupervised machine learning to explore galaxy morphology "Beyond the Hubble Sequence," uncovering novel classifications and insights without predefined labels, thereby advancing our understanding of cosmic evolution.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
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
