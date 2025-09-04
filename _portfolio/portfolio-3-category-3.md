---
title: "Advanced AI/ML Methods & Scientific Emulation"
excerpt: "Research in advanced ai/ml methods & scientific emulation"
collection: portfolio
---

The intersection of advanced Artificial Intelligence (AI) and Machine Learning (ML) with scientific emulation is rapidly transforming the landscape of scientific discovery and engineering. This field is dedicated to developing sophisticated computational tools that can accurately model, predict, and understand complex physical phenomena, often where traditional simulations are computationally prohibitive or data is scarce. A core objective is to harness the power of AI to accelerate scientific workflows, ranging from analyzing vast datasets in cosmology and high-energy physics to simulating intricate fluid dynamics and materials science.

Key methodological thrusts in this domain include the development of high-fidelity surrogate models and emulators that can quickly reproduce the output of expensive simulations, often leveraging techniques like probabilistic modeling, neural networks, and Gaussian processes. Furthermore, a significant challenge lies in ensuring that these AI-driven tools are not only accurate but also interpretable, robust, and capable of quantifying their own uncertainties, thereby maintaining scientific rigor. Research in this area also explores novel ways to represent complex scientific data, such as disentangled latent spaces for generative models, and to develop frameworks for rigorously evaluating AI models as credible scientific assistants.

My research significantly contributes to this exciting domain by developing cutting-edge AI/ML methodologies specifically tailored for scientific applications. I have focused on enhancing the interpretability and reliability of AI models, for instance, by designing generative models with statistically disentangled latent spaces guided by physical factors, enabling a clearer understanding of the underlying scientific processes. A major emphasis of my work involves robust Uncertainty Quantification (UQ) for AI in critical fields like High-Energy Physics (HEP) and fluid dynamics, utilizing probabilistic neural networks to provide not just predictions but also transparent estimates of their confidence. This ensures that AI-generated insights are trustworthy and scientifically rigorous.

Additionally, I have engineered high-performance scientific emulators, such as a Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies, to rapidly explore vast parameter spaces, and developed non-intrusive reduced-order models with latent-space time evolution using Gaussian process emulation for complex fluid flows. My work also introduces novel techniques like SHAMNet for differentiable predictions of large-scale structure and Voronoi tessellation-assisted deep learning for global field reconstruction from sparse sensors, demonstrating the versatility of these methods across diverse scientific problems, including probabilistic modeling for high-dimensional stress fields. Furthermore, I have established a methodology, EAIRA, for evaluating AI models as scientific research assistants, underscoring my commitment to building scientifically sound and impactful AI solutions that accelerate discovery and advance our understanding of the physical world.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/eaira-establishing-a-methodology-for-evaluating-ai_plot_1_adce1f78.png" alt="Figure from EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific Research Assistants</div>
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
