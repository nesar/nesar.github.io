---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The integration of machine learning (ML) into scientific research has revolutionized the way vast and complex datasets are analyzed, interpreted, and utilized across disciplines like astronomy, cosmology, and materials science. Machine learning algorithms offer unprecedented capabilities for pattern recognition, predictive modeling, and automation, thereby accelerating discovery and deepening our understanding of fundamental phenomena. Key applications include the extraction of subtle features from noisy data, the identification of rare or anomalous events, the reconstruction of physical fields from sparse measurements, and the development of sophisticated simulations.

The challenges addressed by ML in science are diverse, ranging from the need for high-fidelity image processing in astronomical observations to the interpretation of high-dimensional physical parameters. Scientists increasingly leverage advanced ML techniques, such as deep learning, generative models, and probabilistic frameworks, to overcome traditional analytical limitations. These methods enable the exploration of parameter spaces that are intractable for human analysis, facilitate the automated discovery of new structures or classes of objects, and provide tools for validating theoretical models against empirical data.

My research focuses on developing and applying cutting-edge machine learning methodologies to address critical problems in scientific domains, particularly in astronomy and cosmology. I have developed innovative approaches to enhance data interpretability, perform robust anomaly detection, and create efficient pipelines for complex scientific tasks. For instance, I have worked on enhancing interpretability in generative modeling by developing methods for statistically disentangled latent spaces guided by generative factors, which allows for a deeper understanding of underlying data variations. My work also includes applying probabilistic modeling and automated machine learning frameworks to analyze high-dimensional stress fields, providing robust insights into material properties.

I have extensively utilized deep learning techniques for various astronomical applications, including neural network based point spread function deconvolution for clearer astronomical images and a modular deep learning pipeline for the efficient detection and modeling of galaxy-scale strong gravitational lenses. Furthermore, my research explores the power of generative adversarial networks (GANs) for anomaly detection in large astronomical image datasets, such as those from Hyper Suprime-Cam, and for physically benchmarking AI-generated cosmic web simulations. I have also contributed to global field reconstruction from sparse sensors using a novel Voronoi tessellation-assisted deep learning approach, and explored galaxy morphology beyond the traditional Hubble Sequence using unsupervised machine learning, demonstrating the potential of ML to uncover new classifications and insights from complex observational data. These contributions aim to accelerate scientific discovery and provide powerful new tools for researchers.

<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>

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
