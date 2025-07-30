---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative discipline in various scientific domains, offering powerful tools to tackle complex challenges posed by increasingly large and intricate datasets. In fields like astrophysics and cosmology, where observations span vast scales and simulations generate immense volumes of data, traditional analytical methods often fall short in extracting subtle patterns, identifying rare phenomena, or efficiently processing information. Deep learning, in particular, provides robust frameworks for tasks such as image analysis, anomaly detection, and the synthesis of physically consistent data, accelerating discovery and enabling new avenues of research.

A critical area of application involves leveraging generative models to understand underlying data distributions, synthesize new samples, and enhance interpretability. Simultaneously, machine learning plays a pivotal role in refining observational data through advanced signal processing techniques and in extending the capabilities of human expert analysis through automated classification and anomaly identification. The development of robust, physically-informed machine learning models and pipelines is therefore essential for pushing the boundaries of scientific inquiry, allowing researchers to explore novel hypotheses and unlock insights previously obscured by data complexity.

My research focuses on developing and applying cutting-edge machine learning methodologies to address fundamental problems in astronomy and astrophysics. A significant portion of my work centers on generative models, where I have pioneered methods for enhancing interpretability in generative modeling by developing statistically disentangled latent spaces guided by known generative factors in scientific datasets. This approach provides a clearer understanding of the underlying physical parameters driving data generation. I have also extensively utilized Generative Adversarial Networks (GANs) for anomaly detection in large astronomical image surveys, such as the Hyper Suprime-Cam, enabling the identification of rare or unusual celestial objects that could represent new classes of astrophysical phenomena.

Furthermore, my contributions extend to developing a modular deep learning pipeline for the efficient detection and modeling of galaxy-scale strong gravitational lenses, a crucial tool for probing the distribution of dark matter. I have explored new frontiers in galaxy morphology by applying unsupervised machine learning techniques to move beyond traditional classification schemes like the Hubble Sequence, revealing novel morphological insights. My work also includes developing neural network based Point Spread Function (PSF) deconvolution techniques to improve the quality of astronomical images, and conducting physical benchmarking for AI-generated cosmic web simulations to ensure their scientific validity. Collectively, these efforts demonstrate the power of advanced machine learning techniques to accelerate scientific discovery, improve data analysis workflows, and provide novel insights into the universe's most complex phenomena.

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
