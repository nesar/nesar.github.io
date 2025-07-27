---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative paradigm across numerous scientific disciplines, offering unprecedented capabilities for extracting insights from vast and complex datasets. From astrophysics and high-energy physics to materials science and engineering, AI-driven approaches are accelerating discovery by automating analysis, identifying subtle patterns, and modeling intricate phenomena that defy traditional methods. Key challenges addressed include the management of high-dimensional data, the identification of anomalies, the reconstruction of physical fields from sparse measurements, and the critical need for interpretable and trustworthy predictions in high-stakes scientific contexts.

Within this rapidly evolving landscape, research often focuses on developing bespoke machine learning architectures and methodologies tailored to the unique characteristics of scientific data. This includes leveraging deep learning for image analysis, employing generative models for data synthesis and anomaly detection, and applying unsupervised learning to uncover novel classifications or relationships. A significant emphasis is placed on ensuring that these AI systems not only deliver high performance but also provide quantifiable uncertainties and offer transparent explanations of their decision-making processes, thereby fostering scientific trust and enabling deeper understanding.

My research stands at the intersection of advanced machine learning and various scientific domains, primarily focusing on developing robust and interpretable AI solutions for complex data challenges. A significant part of my work involves advancing generative modeling techniques, such as Generative Adversarial Networks (GANs) and Variational Autoencoders (VAEs). For instance, I have developed methods to enhance interpretability in generative models by guiding the disentanglement of latent spaces with generative factors, crucial for understanding underlying physical processes in scientific datasets. This approach has been instrumental in applications ranging from the physical benchmarking of AI-generated cosmic web structures to the detection of subtle anomalies in large astronomical surveys like Hyper Suprime-Cam galaxy images. Furthermore, I have focused on building trust in AI systems by developing frameworks for interpretable uncertainty quantification in high-energy physics applications.

Beyond generative models, my contributions extend to specialized applications in astronomical data analysis and broader scientific data challenges. I have engineered neural network-based solutions for precise point spread function deconvolution, vital for enhancing image clarity in astronomy. My work also includes the development of modular deep learning pipelines for the robust detection and modeling of galaxy-scale strong gravitational lenses, which are critical for cosmology. In the realm of galaxy morphology, I have explored unsupervised machine learning techniques to move "Beyond the Hubble Sequence," enabling novel classifications and insights into galaxy evolution. Moreover, I have tackled high-dimensional data challenges by applying probabilistic modeling and automated machine learning frameworks for stress field analysis, and developed a unique Voronoi tessellation-assisted deep learning approach for global field reconstruction from sparse sensor data, showcasing the versatility of these techniques across diverse scientific problems.

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
