---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The burgeoning field of machine learning is profoundly transforming scientific discovery across diverse disciplines, from astrophysics to materials science. As experimental facilities and simulations generate unprecedented volumes of complex, high-dimensional data, traditional analytical methods often prove insufficient. Machine learning algorithms offer powerful tools to discern subtle patterns, classify intricate phenomena, automate laborious tasks, and extract meaningful insights that were previously inaccessible, thereby accelerating the pace of scientific understanding and technological innovation.

In astronomy, for instance, machine learning is at the forefront of tackling some of the most challenging data analysis problems. This includes the efficient processing of vast survey data for tasks like galaxy morphology classification, accurate estimation of cosmological parameters such as redshift, and the identification of rare or anomalous celestial events. Beyond astronomy, similar challenges exist in fields dealing with complex, multi-dimensional datasets, such as modeling physical systems with numerous interdependent variables. The development of robust, scalable, and interpretable machine learning solutions tailored to these unique scientific contexts is crucial for maximizing their impact and ensuring reliable scientific conclusions.

My work lies at the intersection of machine learning and scientific discovery, primarily focusing on astrophysical applications but also extending to other scientific domains. I have developed and applied a range of advanced machine learning techniques, including deep learning architectures, generative adversarial networks (GANs), probabilistic modeling, and unsupervised learning, to address critical challenges in data analysis. For instance, I have designed neural network-based methods for point spread function deconvolution to enhance image quality in astronomical observations, and developed robust frameworks for probabilistic redshift estimation using synthetic spectra, known as SYTH-Z. My contributions also include building modular deep learning pipelines for the automatic detection and modeling of galaxy-scale strong gravitational lenses, a crucial tool for studying dark matter and cosmology.

Furthermore, my research explores the power of unsupervised machine learning to move "Beyond the Hubble Sequence," enabling the discovery of novel galaxy morphologies without prior labels. I have also pioneered the use of generative adversarial networks for anomaly detection in Hyper Suprime-Cam galaxy images, providing a powerful means to identify unusual or unexpected astronomical phenomena. Beyond specific applications, I have focused on enhancing the interpretability of generative models by constructing statistically disentangled latent spaces, guided by generative factors inherent in scientific datasets. This effort is critical for ensuring that machine learning models provide not just predictions, but also understandable insights into the underlying physics. Additionally, I have applied probabilistic modeling and automated machine learning frameworks to analyze high-dimensional stress fields in materials science, demonstrating the broader applicability of these methods. My commitment extends to advancing the field through foundational best practices, as evidenced by my work on "Constructing Impactful Machine Learning Research for Astronomy."

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
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
