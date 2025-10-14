---
title: "Astronomical Data Analysis with AI/ML"
excerpt: "Research in astronomical data analysis with ai/ml"
collection: portfolio
---

The burgeoning volume and complexity of data from modern astronomical surveys and observatories present both immense opportunities and significant computational challenges. Traditional data analysis methods often struggle to cope with the sheer scale, high dimensionality, and inherent noise of these datasets, necessitating the development of advanced analytical tools. Artificial Intelligence and Machine Learning (AI/ML) have emerged as powerful paradigms for extracting profound scientific insights, enabling unprecedented efficiency and accuracy in processing, interpreting, and understanding the universe.

Within this rapidly evolving landscape, deep learning techniques, including neural networks, generative adversarial networks (GANs), and unsupervised learning algorithms, are transforming various facets of astronomical research. These methods are adept at tasks ranging from enhancing the quality of observational data and automating the detection and classification of celestial objects to identifying subtle anomalies and modeling complex astrophysical phenomena. By moving beyond human-intensive manual inspection, AI/ML enables astronomers to unlock new discoveries and explore previously intractable problems.

My research leverages these cutting-edge AI/ML methodologies to address critical challenges across diverse astronomical domains. I have developed a neural network-based point spread function deconvolution method, significantly improving image quality and resolution for astronomical applications by effectively removing instrumental blurring. For spectral analysis, my work on SYTH-Z introduced machine learning synthetic spectra for probabilistic redshift estimation, enhancing the accuracy and robustness of this fundamental cosmological measurement. Furthermore, I have applied generative adversarial networks (GANs) for robust anomaly detection in vast imaging datasets, successfully identifying unusual and potentially novel objects within Hyper Suprime-Cam galaxy images, pushing the boundaries of discovery beyond predefined classifications.

Beyond individual object analysis, my contributions extend to understanding large-scale cosmic structures and phenomena. I have explored galaxy morphology "Beyond the Hubble Sequence" using unsupervised machine learning, uncovering new, data-driven classifications that offer deeper insights into galaxy evolution than traditional schemes. A significant aspect of my work also includes the development of a modular deep learning pipeline for galaxy-scale strong gravitational lens detection and modeling. This pipeline automates and accelerates the identification and characterization of these crucial cosmic lenses, which are invaluable probes for studying dark matter, dark energy, and the expansion history of the universe. Collectively, my work demonstrates the transformative potential of AI/ML in accelerating discovery, enhancing precision, and enabling entirely new avenues of research in astronomy.

<div class="research-figures">
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
  <div class="figure-item">
    <img src="/images/research/figures/anomaly-detection-in-astronomical-images-with-gene_plot_1_6d84e8fe.png" alt="Figure from Anomaly Detection in Astronomical Images with Generative Adversarial Networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Anomaly Detection in Astronomical Images with Generative Adversarial Networks</div>
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
