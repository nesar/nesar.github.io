---
title: "Foundational AI Methods & Astrophysical Data Characterization"
excerpt: "Research in foundational ai methods & astrophysical data characterization"
collection: portfolio
---

Modern scientific research across domains like astrophysics, fluid dynamics, and high-energy physics is increasingly reliant on complex, high-dimensional datasets. Extracting meaningful insights, predicting phenomena, and developing robust models from this deluge of information presents significant computational and methodological challenges. There is a critical need for advanced artificial intelligence and machine learning (AI/ML) techniques that not only process data efficiently but also offer interpretability, quantify uncertainty, and provide actionable scientific understanding, moving beyond opaque "black-box" approaches.

This interdisciplinary challenge drives the development of foundational AI methods tailored for scientific discovery. Key areas of focus include probabilistic modeling to inherently account for uncertainties, generative models capable of synthesizing realistic data and identifying underlying physical factors, and advanced deep learning architectures for tasks such as data recovery, high-dimensional field reconstruction, and reduced-order modeling. These methods aim to transform raw data into knowledge, enabling faster simulations, more accurate predictions, and the characterization of complex systems, from stellar populations to turbulent flows.

My work centers on developing and applying foundational AI methods to address these complex challenges, emphasizing interpretability and robust uncertainty quantification across diverse scientific datasets. I have developed probabilistic neural networks for efficient and uncertainty-aware surrogate modeling of fluid flows, enabling faster simulations and data recovery from sparse measurements. Furthermore, I have contributed to enhancing interpretability in generative modeling by statistically disentangling latent spaces, guiding the models with known generative factors to uncover meaningful physical parameters in scientific datasets. This includes applying automated machine learning frameworks to analyze high-dimensional stress fields, providing robust predictive capabilities.

In astrophysics, my research involves large-scale data characterization and discovery. I have led the creation of a comprehensive photometric sample of 2.6 million Red Clump stars, a crucial step for mapping the structure of the Milky Way, utilizing advanced data analysis techniques on vast astronomical surveys. I have also identified Carbon-Enhanced Metal-Poor star candidates from BP/RP spectra in Gaia DR3, contributing to our understanding of the early universe. Beyond astronomy, I have developed innovative approaches for global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning, and advanced non-intrusive reduced-order models using Gaussian process emulation for latent-space time evolution in fluid dynamics, showcasing the versatility and impact of these AI methodologies across scientific frontiers. My contributions provide tools that enable deeper scientific understanding, more reliable predictions, and accelerate discovery.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
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
