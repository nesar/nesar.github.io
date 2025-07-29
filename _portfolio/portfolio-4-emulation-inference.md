---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The fields of scientific emulation and inference are at the forefront of tackling complex computational challenges across various domains, including physics, engineering, and astrophysics. As simulations become increasingly sophisticated and data grows exponentially, traditional analytical or brute-force numerical methods often become computationally prohibitive. Emulation addresses this by developing highly accurate yet computationally inexpensive surrogate models that can mimic the behavior of complex systems, significantly accelerating prediction and analysis.

Inference, on the other hand, focuses on extracting meaningful insights, quantifying uncertainties, and making predictions from observed data, often high-dimensional or incomplete. These interdisciplinary approaches leverage advanced statistical techniques, machine learning algorithms, and reduced-order modeling principles to enable rapid exploration of parameter spaces, real-time decision-making, and a deeper understanding of underlying physical phenomena, moving beyond static data analysis to dynamic, predictive capabilities.

My research extensively contributes to these areas, developing novel methodologies for emulation and inference in challenging scientific and engineering contexts. I have specifically focused on creating efficient data-driven surrogates for computationally expensive simulations and developing robust techniques for reconstructing complex fields from limited data. For instance, I developed a Matter Power Spectrum Emulator using neural networks, enabling rapid exploration of f(R) modified gravity cosmologies, which previously required time-consuming N-body simulations. This significantly accelerates cosmological parameter inference and theoretical model validation.

Furthermore, I have innovated in the realm of fluid dynamics by developing a probabilistic neural network-based reduced-order surrogate for fluid flows, providing not just predictions but also crucial uncertainty quantification. Addressing data sparsity, my work on global field reconstruction from sparse sensors with Voronoi tessellation offers a powerful method to infer complete spatial fields from limited measurement points, crucial for real-time monitoring and control. Additionally, I have applied probabilistic modeling and an automated machine learning framework for high-dimensional stress field analysis, demonstrating enhanced efficiency and reliability in material science applications by automatically selecting optimal models and quantifying uncertainties in complex stress states. These contributions collectively advance the capabilities of scientific machine learning, enabling faster discovery, better design, and more reliable decision-making in high-impact research areas.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/matter-power-spectrum-emulator-for-fr-modified-gra_plot_1_d6154d54.png" alt="Figure from Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/probabilistic-neural-network-based-reduced-order-s_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network-based reduced-order surrogate for fluid flows" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network-based reduced-order surrogate for fluid flows</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/global-field-reconstruction-from-sparse-sensors-wi_plot_1_93ef286c.png" alt="Figure from Global field reconstruction from sparse sensors with Voronoi tessellation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Global field reconstruction from sparse sensors with Voronoi tessellation</div>
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
