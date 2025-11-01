---
title: "AI/ML for Observational Astrophysics"
excerpt: "Research in ai/ml for observational astrophysics"
collection: portfolio
---

Observational astrophysics is currently experiencing a transformative era, driven by the proliferation of increasingly large and complex datasets from cutting-edge telescopes and surveys. This unprecedented influx of information presents both immense opportunities for discovery and significant analytical challenges for traditional methods. Artificial Intelligence and Machine Learning (AI/ML) have emerged as indispensable tools to navigate this data-rich landscape, enabling automated analysis, enhanced precision, and deeper insights into the fundamental properties and evolution of cosmic phenomena. These advanced methodologies are fundamentally reshaping how astronomers process, interpret, and extract scientific value from observational data, from our own Milky Way to the distant reaches of the universe.

The application of AI/ML extends across a broad spectrum of observational astrophysics, proving crucial for tasks such as the efficient identification and characterization of celestial objects in vast surveys, the precise estimation of cosmological parameters, and the detection of rare or anomalous events that might otherwise elude human inspection. Techniques spanning deep learning, generative models, and sophisticated statistical algorithms are being deployed to address challenges ranging from accurate redshift estimation and the comprehensive analysis of gravitational lensing to mapping stellar distributions and understanding the intricate dynamics of galaxy clusters through phenomena like the kinetic Sunyaev-Zel'dovich (kSZ) effect. These innovations are vital for pushing the boundaries of our understanding of galaxy evolution, the distribution of dark matter, and the overarching structure of the cosmos.

My research extensively utilizes and develops AI/ML techniques to tackle some of the most pressing challenges in observational astrophysics. I have employed data-driven approaches to characterize stellar populations, exemplified by the creation of a photometric sample of 2.6 million Red Clump stars across the Milky Way, providing a robust dataset for galactic structure studies. In the realm of cosmology, I have contributed to improving weak lensing cluster mass estimations by reducing model error through optimized galaxy selection strategies, thereby enhancing the precision of dark matter distribution measurements. Furthermore, I have developed machine learning models, including SYTH-Z, which generate synthetic spectra for probabilistic redshift estimation, significantly improving the accuracy and reliability of distance measurements for galaxies.

My work also extends to applying advanced deep learning techniques for complex image analysis. I have pioneered the use of Generative Adversarial Networks (GANs) for anomaly detection in Hyper Suprime-Cam galaxy images, providing a powerful method to identify unusual astronomical objects that could represent new phenomena. Additionally, I developed deep neural networks for peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect, offering new insights into the kinematics of galaxy clusters. Furthermore, I designed a modular deep learning pipeline for the detection and modeling of galaxy-scale strong gravitational lenses, automating this complex task and enabling efficient discovery. These contributions collectively advance our ability to extract detailed scientific insights from massive astronomical datasets, driving new discoveries and refining our understanding of the cosmos.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/anomaly-detection-in-hyper-suprime-cam-galaxy-imag_plot_1_58355288.png" alt="Figure from Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks</div>
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
