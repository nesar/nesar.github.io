---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Modern scientific research across fields such as astrophysics, materials science, and engineering is increasingly characterized by an explosion of complex and high-dimensional datasets. From panoramic sky surveys capturing billions of galaxies to intricate simulations modeling fundamental physical processes, these data volumes often exceed the capacity of traditional analytical methods. Extracting meaningful patterns, identifying subtle anomalies, and accelerating computationally expensive simulations are critical challenges that demand innovative computational approaches. The sheer scale and inherent noise in scientific data necessitate methodologies capable of robust feature extraction, noise reduction, and efficient knowledge discovery.

Machine learning (ML) has emerged as a powerful paradigm to address these formidable challenges, offering transformative capabilities for scientific discovery. Deep learning architectures, generative models, and advanced probabilistic frameworks are particularly adept at processing vast datasets, learning intricate relationships, and uncovering hidden structures that may elude human observation or conventional statistical techniques. These methods enable automated classification, regression, and pattern recognition, significantly accelerating scientific workflows and fostering new avenues of inquiry.

The application of ML in science extends beyond mere data processing, enabling critical advancements such as enhancing interpretability in complex models, synthesizing realistic data for simulation acceleration, and performing anomaly detection in diverse datasets. By developing domain-specific ML solutions, researchers can improve the fidelity of scientific instruments, streamline the analysis of experimental and simulated data, and ultimately gain deeper insights into fundamental phenomena, from the evolution of the cosmos to the properties of novel materials.

My research focuses on developing and deploying cutting-edge machine learning and artificial intelligence methodologies to tackle pressing challenges in scientific discovery, primarily within astrophysics and engineering. I have developed modular deep learning pipelines for critical tasks such as galaxy-scale strong gravitational lens detection and modeling, significantly advancing our ability to map dark matter and probe cosmic expansion. In cosmology, my work includes benchmarking AI-evolved cosmological structure formation and physically benchmarking AI-generated cosmic web simulations, ensuring the scientific fidelity of these advanced models. I have also contributed to predicting new concept-object associations in astronomy by mining the literature and designed InferA, a smart assistant for cosmological ensemble data, to streamline complex data analysis. My contributions extend to applying neural networks for point spread function deconvolution in astronomical images and developing SYTH-Z for machine learning synthetic spectra, crucial for probabilistic redshift estimation.

Furthermore, I have innovated in the area of anomaly detection, employing generative adversarial networks (GANs) to identify unusual features in astronomical images, including those from the Hyper Suprime-Cam survey, thereby uncovering novel astrophysical phenomena. My work also addresses the challenges of sparse and high-dimensional data in engineering, through multi-task modeling and the application of probabilistic modeling and automated machine learning for high-dimensional stress fields. To enhance the utility of generative models, I have focused on enhancing interpretability by creating statistically disentangled latent spaces guided by generative factors in scientific datasets. Additionally, I developed a Voronoi tessellation-assisted deep learning approach for global field reconstruction from sparse sensors and contributed to peculiar velocity estimation from the Kinetic SZ effect using deep neural networks. This comprehensive portfolio underscores my commitment to leveraging advanced ML techniques to accelerate scientific discovery and address complex data challenges across various scientific domains.

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
