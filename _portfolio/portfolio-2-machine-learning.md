---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning applications in scientific research have revolutionized data analysis across multiple domains, particularly in astronomy, cosmology, and fluid dynamics. This research encompasses diverse methodologies including generative adversarial networks for anomaly detection in astronomical surveys, deep neural networks for point spread function deconvolution, and probabilistic approaches for surrogate modeling in complex physical systems. The work spans from fundamental image processing challenges to sophisticated pattern recognition tasks in large-scale scientific datasets.

Advanced techniques in this area include modular deep learning pipelines for gravitational lensing analysis, neural network-based approaches for synthetic sky image generation, and novel architectures for handling high-dimensional scientific data. The research emphasizes both computational efficiency and scientific accuracy, developing methods that can handle the scale and complexity of modern astronomical surveys while maintaining rigorous uncertainty quantification.

My contributions to this field focus on developing interpretable and efficient machine learning methods for astronomical applications. I have worked extensively on creating modular pipelines that can be adapted across different scientific problems, with particular emphasis on maintaining scientific rigor while leveraging the power of modern deep learning architectures. This work has enabled more accurate and efficient analysis of complex astronomical phenomena, from galaxy morphology classification to cosmological parameter estimation.

## Representative Research Figures

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/Neural_Network_Based_Point_Spread_Function_Deconvo_plot_1_96427c88.png" alt="Figure from Neural Network Based Point Spread Function Deconvo" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvo</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/Neural_Network_Based_Point_Spread_Function_Deconvo_plot_2_ad6f7fae.png" alt="Figure from Neural Network Based Point Spread Function Deconvo" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvo</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/Neural_Network_Based_Point_Spread_Function_Deconvo_plot_3_4f111230.png" alt="Figure from Neural Network Based Point Spread Function Deconvo" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Neural Network Based Point Spread Function Deconvo</div>
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
