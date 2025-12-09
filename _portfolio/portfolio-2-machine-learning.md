---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning (ML) has emerged as a transformative paradigm across numerous scientific disciplines, offering powerful tools to extract knowledge from complex, high-dimensional datasets. In fields like astrophysics and cosmology, where observations generate petabytes of data from telescopes and simulations model intricate physical processes, ML accelerates discovery by automating complex analyses, identifying subtle patterns, and predicting physical phenomena with unprecedented accuracy. This paradigm shift enables scientists to overcome traditional computational bottlenecks, push the boundaries of data interpretation, and develop novel approaches to long-standing scientific challenges.

A key focus within this interdisciplinary area involves leveraging advanced deep learning architectures to model fundamental cosmic structures, characterize celestial objects, and interpret observational data more effectively. This includes developing robust methods for astronomical image analysis, such as Point Spread Function deconvolution and anomaly detection, which are crucial for extracting faint signals and identifying rare events in large-scale surveys. Furthermore, ML is increasingly applied to reconstruct underlying physical fields from sparse measurements and to enhance the interpretability of complex generative models, ensuring that AI-driven insights are not only accurate but also physically meaningful and verifiable.

My research specifically focuses on developing and applying innovative machine learning techniques to address critical problems in astrophysics and cosmology, aiming to improve current analytical capabilities and unlock new avenues for scientific inquiry. I have developed sophisticated deep neural networks for tasks ranging from the precise Point Spread Function deconvolution in astronomical images to the estimation of peculiar velocities from the kinetic Sunyaev-Zel'dovich effect, significantly enhancing observational precision. Furthermore, I have pioneered the use of generative adversarial networks (GANs) for anomaly detection in large astronomical surveys like Hyper Suprime-Cam, enabling the discovery of unusual galaxy morphologies and other rare cosmic phenomena.

A core aspect of my work involves pushing the boundaries of interpretability and physical grounding in AI models. I have contributed to benchmarking AI-evolved cosmological structure formation and developed methods for physical benchmarking of AI-generated cosmic webs, ensuring that synthetic data adheres to known physical laws. My contributions also include enhancing interpretability in generative modeling through statistically disentangled latent spaces, guided by specific generative factors relevant to scientific datasets. Beyond image analysis, I have developed a modular deep learning pipeline for galaxy-scale strong gravitational lens detection and modeling, as well as a novel Voronoi tessellation-assisted deep learning approach for global field reconstruction from sparse sensor data. My research also explores galaxy morphology "beyond the Hubble Sequence" using unsupervised machine learning, offering new perspectives on galactic evolution. These diverse applications underscore my commitment to developing robust, interpretable, and scientifically impactful machine learning solutions.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/benchmarking-ai-evolved-cosmological-structure-for_plot_1_e309ff7d.png" alt="Figure from Benchmarking AI-evolved cosmological structure formation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Benchmarking AI-evolved cosmological structure formation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png" alt="Figure from Physical Benchmarking for AI-Generated Cosmic Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Physical Benchmarking for AI-Generated Cosmic Web</div>
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
