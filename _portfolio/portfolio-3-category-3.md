---
title: "Machine Learning for Astronomical Observations"
excerpt: "Research in machine learning for astronomical observations"
collection: portfolio
---

The field of astronomical observations is undergoing a profound transformation driven by an unprecedented deluge of data from modern telescopes. Analyzing terabytes of complex imaging and spectroscopic information presents significant challenges, far exceeding the capabilities of traditional manual analysis or rule-based algorithms. Machine learning (ML) has emerged as an indispensable tool, offering powerful solutions to automate data processing, extract subtle patterns, and accelerate discovery across various scales and phenomena in the universe.

Machine learning techniques are particularly adept at identifying intricate features within both spectroscopic and imaging datasets. In spectroscopy, ML enables the precise characterization of celestial objects, from stars to distant galaxies, by interpreting their unique light signatures and deriving fundamental properties such as composition, temperature, and redshift. Concurrently, deep learning and generative models have revolutionized image analysis in large-scale astronomical surveys, facilitating efficient object detection, classification, and the identification of rare or anomalous events, thereby pushing the frontiers of astrophysical research.

My research extensively leverages these cutting-edge machine learning methodologies to address critical challenges in astronomical observation and interpretation. A significant focus has been on enhancing spectroscopic analysis, where I have pioneered methods like "Teaching LLMs to Speak Spectroscopy." This work explores how large language models can be trained to interpret and articulate complex spectroscopic features, thereby facilitating more intuitive scientific communication and insight generation from spectral data. Complementing this, I have developed "Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z," which employs sophisticated ML models to accurately predict galaxy redshifts while providing robust uncertainty estimates, crucial for precision cosmology.

Furthermore, my contributions extend to advanced image analysis and anomaly detection. I have developed and applied generative adversarial networks (GANs) for "Anomaly detection in Hyper Suprime-Cam galaxy images" and more broadly for "Anomaly Detection in Astronomical Images with Generative Adversarial Networks." This allows for the automated identification of unusual or novel astrophysical phenomena in vast image surveys that might otherwise be overlooked. Another key contribution is "A Modular Deep Learning Pipeline for Galaxy-Scale Strong Gravitational Lens Detection and Modeling," which utilizes deep learning architectures to efficiently detect these rare cosmological probes and model their properties, providing invaluable tools for studying dark matter and the expansion of the universe. My work collectively demonstrates a comprehensive approach to applying machine learning from fundamental data interpretation to the automated discovery and characterization of complex astrophysical objects.

<div class="research-figures">
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
