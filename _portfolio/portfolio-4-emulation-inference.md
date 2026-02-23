---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Scientific inquiry often relies on computationally intensive simulations to model complex phenomena, ranging from the evolution of the universe to intricate fluid dynamics. These simulations, while powerful, can be prohibitively expensive, hindering extensive parameter space exploration, inverse problem solving, and robust uncertainty quantification. This challenge necessitates innovative approaches to accelerate prediction and analysis without sacrificing accuracy.

The fields of emulation and inference address these limitations by developing surrogate models and advanced statistical techniques. Emulators, often built using machine learning and deep learning, learn the input-output mapping of complex simulators, enabling rapid predictions across vast parameter spaces. Concurrently, advancements in inference methodologies, including Bayesian techniques and probabilistic machine learning, allow for robust quantification of uncertainties inherent in both models and observational data. Together, these tools are transforming the scientific discovery process by making high-fidelity simulations more accessible for real-time analysis, experimental design, and deeper understanding of underlying physical principles.

My research significantly contributes to this evolving landscape by developing novel machine learning and probabilistic AI frameworks for emulation and inference across diverse scientific domains. I have developed high-fidelity emulators for critical cosmological quantities, such as the "Matter Power Spectrum for f(R) Modified Gravity Cosmologies" and for "Cosmological Subgrid Models," enabling efficient exploration of theoretical physics beyond standard models. A key focus has been on "Differentiable Predictions for Large Scale Structure with SHAMNet," which not only provides accurate forecasts but also allows for gradient-based inference, and "Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks," demonstrating the power of deep learning in extracting subtle signals from complex astrophysical data.

Furthermore, my work places a strong emphasis on "Interpretable Uncertainty Quantification in AI," recognizing that robust scientific conclusions require understanding model confidence. I have pioneered the use of "Probabilistic neural networks for fluid flow surrogate modeling and data recovery," and "Probabilistic neural network-based reduced-order surrogates for fluid flows," improving the reliability of predictions and enabling data-driven discovery in complex systems. This commitment to probabilistic modeling extends to "Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z," providing full posterior distributions for critical astronomical parameters. Additionally, I have explored "Latent-space time evolution of non-intrusive reduced-order models using Gaussian process emulation," demonstrating advanced techniques for capturing dynamic system behavior efficiently. Collectively, my contributions accelerate scientific discovery, enhance the interpretability of AI models, and provide robust, uncertainty-aware tools for complex scientific inference.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/emulator-based-inference-of-cosmological-subgrid-m_plot_1_9c094db3.png" alt="Figure from Emulator-Based Inference of Cosmological Subgrid Models" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Emulator-Based Inference of Cosmological Subgrid Models</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/differentiable-predictions-for-large-scale-structu_plot_1_2e3e2c0b.png" alt="Figure from Differentiable Predictions for Large Scale Structure with SHAMNet" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Differentiable Predictions for Large Scale Structure with SHAMNet</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/machine-learning-synthetic-spectra-for-probabilist_plot_1_e2025c80.png" alt="Figure from Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Machine learning synthetic spectra for probabilistic redshift estimation: SYTH-Z</div>
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
