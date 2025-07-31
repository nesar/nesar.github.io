---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Emulation and inference are cornerstone methodologies in modern scientific computing and engineering, offering critical advancements in fields ranging from computational fluid dynamics to astrophysics and materials science. These techniques address the challenge of computationally expensive simulations and complex data analysis by developing fast, accurate surrogate models (emulators) that can mimic the behavior of high-fidelity simulations. This allows for rapid exploration of vast parameter spaces, efficient uncertainty quantification, and expedited inverse problem solving, which are often intractable with direct simulation approaches. Furthermore, inference methods provide robust frameworks for extracting meaningful insights and quantifying confidence from observational data and model outputs, enabling data-driven discovery and decision-making under uncertainty.

The development of sophisticated machine learning algorithms and probabilistic frameworks has significantly advanced the capabilities of emulation and inference. By leveraging neural networks, Gaussian processes, and other statistical models, researchers can construct high-fidelity emulators that capture complex non-linear relationships and high-dimensional dependencies inherent in scientific phenomena. These advancements not only accelerate research workflows but also democratize access to complex models, facilitating interdisciplinary collaboration and innovation across scientific and engineering domains.

My research extensively explores the application and development of advanced machine learning and probabilistic modeling techniques for emulation and inference across diverse scientific and engineering disciplines. I have developed probabilistic neural networks (PNNs) and Gaussian Process (GP) emulators to create reduced-order surrogate models for complex fluid flows, enabling faster simulations and efficient data recovery, including novel approaches for latent-space time evolution. This work significantly accelerates the analysis of dynamic systems where traditional simulations are prohibitively expensive.

My contributions also extend to high-energy physics (HEP) and cosmology, where I have focused on interpretable uncertainty quantification in AI models, a crucial aspect for high-stakes scientific discovery. I developed a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, providing a rapid and accurate tool for exploring alternative gravitational theories. Furthermore, I have applied probabilistic modeling and automated machine learning (AutoML) frameworks to analyze high-dimensional stress fields, enhancing predictive capabilities and managing complex engineering data. In astrophysics, I developed SYTH-Z, a machine learning approach using synthetic spectra for probabilistic redshift estimation, a vital tool for large-scale structure surveys. A central theme across my work is the emphasis on robust uncertainty quantification and model interpretability, paramount for building trust and reliability in AI-driven scientific discovery and engineering solutions.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/application-of-probabilistic-modeling-and-automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automated machine learning framework for high-dimensional stress field</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
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
