---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The intersection of machine learning and scientific research has become a critical frontier, empowering researchers to tackle unprecedented data volumes and complexity across diverse disciplines. From unraveling the mysteries of the cosmos to optimizing engineering processes, artificial intelligence offers transformative capabilities for accelerating discovery and enhancing our understanding of fundamental phenomena. This field is characterized by the development of sophisticated algorithms designed to identify subtle patterns, predict outcomes, and automate laborious tasks, thereby pushing the boundaries of what is scientifically achievable.

In astronomy, machine learning is essential for processing vast datasets from modern telescopes, enabling automated classification, detection of rare phenomena, and improved cosmological parameter estimation. Similarly, in high-energy physics and engineering, these techniques are crucial for data analysis, simulation acceleration, and real-time system monitoring. A common thread across these applications is the imperative for models to not only be accurate but also interpretable, robust to uncertainties, and capable of operating effectively with sparse or noisy scientific data, ensuring reliable insights and trustworthy scientific advancements.

My work extensively leverages advanced machine learning to address pressing challenges across astronomy, cosmology, and engineering. I have developed modular deep learning pipelines for detecting and modeling galaxy-scale strong gravitational lenses, and employed unsupervised methods to explore galaxy morphology beyond traditional classifications. In cosmology, my research includes benchmarking AI-evolved and generated cosmic web structures, and utilizing deep neural networks for peculiar velocity estimation from the kinetic Sunyaev-Zel'dovich effect. I have also contributed to probabilistic redshift estimation (SYTH-Z), identified Carbon-Enhanced Metal-Poor star candidates from Gaia DR3 spectra, and applied generative adversarial networks for anomaly detection in astronomical images, alongside predicting concept-object associations by mining literature.

A core aspect of my contributions lies in enhancing the interpretability and reliability of AI models for scientific discovery. This includes developing interpretable uncertainty quantification in AI for High Energy Physics, and enhancing interpretability in generative modeling through statistically disentangled latent spaces. For engineering and general scientific applications, I have explored multi-task modeling for sparse data, applied probabilistic and automated machine learning for high-dimensional stress fields, and innovated global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning. My research further encompasses optimizing galaxy selection for weak lensing cluster mass estimation to reduce model error, and contributing to the strategic roadmap for AI/ML opportunities within large collaborations like the Rubin LSST Dark Energy Science Collaboration, driving both methodological innovation and direct scientific impact.

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
