---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

Emulation and statistical inference represent critical methodologies for enabling efficient analysis of complex scientific models and extracting reliable information from high-dimensional datasets. This research area focuses on developing surrogate models that can approximate computationally expensive simulations, advanced uncertainty quantification techniques, and probabilistic frameworks for parameter estimation in scientific applications. The work spans multiple domains including cosmology, high-energy physics, and engineering applications, emphasizing the development of robust, scalable methods for scientific inference.

The research encompasses sophisticated approaches including Gaussian process-based emulation, neural network surrogate modeling, and automated machine learning frameworks for handling high-dimensional problems. Key contributions include developing methods for nonlinear dimensionality reduction in scientific datasets, creating efficient emulators for power spectrum analysis in cosmological models, and establishing frameworks for interpretable uncertainty quantification in AI applications for scientific research.

My work in this area has centered on developing probabilistic modeling frameworks that can handle the computational challenges of modern scientific research. I have contributed to creating automated machine learning pipelines that maintain scientific rigor while providing computational efficiency gains. Through this research, I have helped enable more sophisticated analyses of complex models and provided tools that allow researchers to extract reliable inferences from increasingly large and complex scientific datasets.



<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/Application_of_probabilistic_modeling_and_automate_plot_1_8f87fb28.png" alt="Figure from Application of probabilistic modeling and automate" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automate</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/Application_of_probabilistic_modeling_and_automate_plot_2_23b6d91f.png" alt="Figure from Application of probabilistic modeling and automate" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automate</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/Application_of_probabilistic_modeling_and_automate_plot_3_f865475d.png" alt="Figure from Application of probabilistic modeling and automate" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Application of probabilistic modeling and automate</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/Probabilistic_neural_network_reduced_order_plot_1_0ea468f8.png" alt="Figure from Probabilistic neural network reduced order" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Probabilistic neural network reduced order</div>
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

/* Modal styles */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 90%;
  max-width: 1000px;
  max-height: 90vh;
  object-fit: contain;
  margin-top: 2%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
  transition: color 0.3s ease;
}

.close:hover {
  color: #bbb;
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

// Close modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}

// Close modal with escape key
document.addEventListener('keydown', function(event) {
  if (event.key === 'Escape') {
    closeModal();
  }
});
</script>
