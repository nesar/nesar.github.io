---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The field of astronomy and cosmology is undergoing a profound transformation driven by an unprecedented surge in data from advanced telescopes and sophisticated simulations. This deluge of information presents both immense opportunities for groundbreaking discoveries and significant computational challenges related to data processing, analysis, and interpretation. Machine learning (ML) has emerged as a crucial paradigm in this era, offering powerful tools to extract complex patterns, identify rare events, enhance data quality, and accelerate scientific inquiry beyond the capabilities of traditional methods.

Machine learning applications in astrophysics span a broad spectrum, encompassing tasks from the automated detection and classification of celestial objects to the precise deconvolution of instrumental artifacts and the generation of physically consistent cosmological simulations. Deep learning models, in particular, are proving invaluable due to their ability to learn intricate, non-linear relationships directly from vast datasets. This capability addresses many historically challenging problems, such as improving the fidelity of astronomical images, discovering anomalous phenomena, and rigorously validating synthetic universes that represent our understanding of cosmic evolution.

My research focuses on developing and deploying cutting-edge machine learning techniques to tackle some of the most pressing challenges in astrophysics and cosmology. I have spearheaded initiatives aimed at enhancing the quality and reliability of observational data, as well as establishing rigorous methodologies for validating complex theoretical models. For instance, I have developed innovative solutions such as those presented in "Anomaly Detection in Astronomical Images with Generative Adversarial Networks," which leverages Generative Adversarial Networks (GANs) to identify unusual or potentially novel phenomena within extensive image datasets by learning the underlying distribution of normal observations. Furthermore, I have significantly contributed to improving image fidelity through "Neural Network Based Point Spread Function Deconvolution For Astronomical Applications," utilizing deep neural networks to effectively remove instrumental blurring and enhance the clarity and precision of astronomical data.

Beyond data enhancement, my work extends into the realm of cosmological simulations and large-scale sky surveys. I have investigated the physical consistency and reliability of AI-generated cosmic structures, as detailed in "Physical Benchmarking for AI-Generated Cosmic Web," establishing robust methods to ensure that synthetic data accurately reflects known physical laws and observational constraints. Moreover, to accelerate the discovery of one of nature's most powerful cosmic probes, I designed and implemented "A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection." This pipeline streamlines the challenging task of identifying strong gravitational lenses in vast astronomical surveys, which is critical for mapping dark matter distributions and understanding the universe's expansion history. Collectively, my contributions highlight a commitment to leveraging state-of-the-art ML methodologies to advance astronomical research, from precise data refinement to large-scale automated discovery and validation.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/anomaly-detection-in-astronomical-images-with-gene_plot_1_6d84e8fe.png" alt="Figure from Anomaly Detection in Astronomical Images with Generative Adversarial Networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Anomaly Detection in Astronomical Images with Generative Adversarial Networks</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/neural-network-based-point-spread-function-deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvolution For Astronomical Applications" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvolution For Astronomical Applications</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/physical-benchmarking-for-ai-generated-cosmic-web_plot_1_11f44910.png" alt="Figure from Physical Benchmarking for AI-Generated Cosmic Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Physical Benchmarking for AI-Generated Cosmic Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/a-modular-deep-learning-pipeline-for-galaxy-scale-_plot_1_a983de9a.png" alt="Figure from A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection</div>
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
