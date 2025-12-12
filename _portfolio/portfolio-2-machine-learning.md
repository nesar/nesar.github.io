---
title: "Machine Learning for Scientific Applications"
excerpt: "Research in machine learning for scientific applications"
collection: portfolio
---

Machine learning stands as a transformative paradigm in contemporary scientific discovery, offering unprecedented capabilities to analyze vast, complex datasets, discern intricate patterns, and accelerate computationally intensive simulations. Its application spans diverse scientific domains, from fundamental physics and cosmology to materials science and engineering, significantly enhancing our ability to extract knowledge and make predictions from experimental and observational data. The inherent power of machine learning lies in its capacity to automate hypothesis generation, optimize model parameters, and uncover relationships that might be intractable through traditional analytical methods, thereby pushing the frontiers of scientific understanding.

In particular, machine learning is proving indispensable for addressing some of the most challenging problems in astrophysics and cosmology, where data volumes are enormous and physical phenomena are highly non-linear. This includes tasks such as the characterization of cosmic structures, the classification and morphological analysis of galaxies, anomaly detection in observational surveys, and the reconstruction of physical fields from sparse measurements. By leveraging advanced algorithms, scientists are now able to process petabytes of telescope data, identify rare events, and refine models of the universe with greater precision and efficiency than ever before.

My research focuses on developing and applying innovative machine learning methodologies to tackle critical challenges across various scientific disciplines, primarily in astrophysics and cosmology, but also extending to general scientific data analysis. I have developed robust frameworks utilizing deep learning, generative adversarial networks (GANs), probabilistic modeling, and unsupervised learning to unlock insights from complex datasets. A significant methodological contribution includes enhancing interpretability in generative models through statistically disentangled latent spaces, guided by physically meaningful generative factors, to provide more transparent and actionable scientific insights. I have also designed modular deep learning pipelines, for example, to streamline complex tasks like strong gravitational lens detection and modeling, ensuring scalability and adaptability.

I have applied these advanced techniques to a diverse range of scientific problems, making specific contributions to cosmological structure formation by benchmarking AI-evolved models and performing physical benchmarking of AI-generated cosmic web simulations. In astrophysics, my work includes pioneering anomaly detection in Hyper Suprime-Cam galaxy images using GANs, exploring galaxy morphology beyond the traditional Hubble sequence with unsupervised machine learning, and employing neural networks for precise Point Spread Function deconvolution and peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect. Beyond cosmology, I have also developed probabilistic modeling and automated machine learning frameworks for high-dimensional stress fields and innovated global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning. These applications collectively demonstrate the profound impact of tailored machine learning solutions in accelerating scientific discovery and improving data analysis pipelines.

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
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
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
