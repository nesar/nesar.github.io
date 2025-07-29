---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine Learning (ML) has emerged as a profoundly transformative discipline, offering unprecedented capabilities for accelerating discovery and tackling complex analytical challenges across diverse scientific domains. In fields such as astrophysics, cosmology, and high-energy physics, researchers contend with an ever-increasing deluge of data from sophisticated instruments and simulations. Here, ML provides powerful computational frameworks for extracting subtle patterns, making accurate predictions, and synthesizing information in ways that extend beyond traditional analytical methods.

Key applications of ML in scientific research include the automated classification and identification of objects, the reconstruction of underlying physical processes from noisy or sparse observations, and the detection of rare or anomalous phenomena that could signal groundbreaking discoveries. Furthermore, a critical focus within scientific AI is on ensuring the trustworthiness and transparency of these advanced models. This necessitates the development of novel approaches for interpretability and robust uncertainty quantification, guaranteeing that scientific conclusions drawn from ML systems are both reliable and scientifically justifiable. This paradigm shift in data-driven discovery is enabling scientists to gain deeper insights into fundamental physical laws.

My research at the intersection of Machine Learning and science, particularly within astrophysics and cosmology, is dedicated to developing innovative methodologies that not only enhance analytical capabilities but also foster greater interpretability and reliability in AI-driven scientific discovery. I have developed and applied advanced deep learning techniques, including Generative Adversarial Networks (GANs) and other unsupervised learning methods, to address challenging problems such as anomaly detection in Hyper Suprime-Cam galaxy images and broader astronomical datasets. This work extends to exploring galaxy morphology beyond the traditional Hubble Sequence, utilizing unsupervised machine learning to uncover hidden patterns and classify diverse galaxy types.

A core theme across my contributions involves improving both the fidelity and the understanding of AI models for scientific applications. For instance, I have addressed the critical task of Neural Network Based Point Spread Function Deconvolution for astronomical images and developed a Modular Deep Learning Pipeline for the efficient detection and modeling of galaxy-scale strong gravitational lenses. My work also emphasizes creating more interpretable and robust AI systems; I have advanced methods for enhancing interpretability in generative modeling by developing statistically disentangled latent spaces guided by generative factors in scientific datasets, and introduced techniques for Interpretable Uncertainty Quantification in AI for High Energy Physics (HEP). Furthermore, I have contributed to Physical Benchmarking for AI-Generated Cosmic Web simulations and investigated Global Field Reconstruction from sparse sensors with Voronoi tessellation-assisted deep learning, demonstrating a broad commitment to pushing the boundaries of machine learning for rigorous and impactful scientific application.

<div class="research-figures">
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
