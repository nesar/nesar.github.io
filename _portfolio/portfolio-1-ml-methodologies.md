---
title: "Machine Learning Methodologies & General Algorithms"
excerpt: "Research in machine learning methodologies & general algorithms"
collection: portfolio
---

Modeling complex physical phenomena and high-dimensional datasets often presents significant computational challenges. Fields such as fluid dynamics, astrophysics, and engineering design frequently grapple with simulations that are computationally prohibitive, data that is noisy or incomplete, and systems characterized by inherent uncertainties. Traditional analytical and numerical methods, while foundational, can be slow, resource-intensive, or struggle to adequately quantify the uncertainty associated with their predictions, limiting their utility in real-time applications or iterative design processes.

Machine learning methodologies have emerged as a powerful paradigm to address these formidable challenges. By learning intricate patterns and relationships from data, these techniques enable the creation of highly efficient surrogate models, reduced-order representations, and robust data processing pipelines. Approaches like neural networks, particularly those incorporating probabilistic frameworks, are instrumental in accelerating scientific discovery and engineering design by providing rapid, accurate predictions, quantifying uncertainty, and extracting meaningful insights from vast or complex datasets, thereby transforming the landscape of computational science.

My research extensively explores the application and development of advanced machine learning techniques, with a particular focus on Probabilistic Neural Networks (PNNs), to tackle these complex scientific and engineering problems. I have developed novel PNN-based reduced-order models that significantly reduce the computational burden of simulating high-dimensional systems, allowing for real-time analysis and design optimization. This work emphasizes not only efficiency but also the crucial ability of PNNs to inherently quantify predictive uncertainty, offering a more complete and reliable understanding of the system behavior.

Furthermore, my contributions extend to specialized applications in astrophysics and fluid dynamics. I have pioneered the development of machine learning techniques for generating synthetic spectra, which is vital for astronomical data analysis and understanding stellar and galactic evolution. Concurrently, I have advanced neural network-based Point Spread Function (PSF) deconvolution methods to enhance the clarity and interpretability of observational data by correcting optical distortions. In the realm of fluid dynamics, I have developed sophisticated PNN-based surrogate models for complex fluid flows, enabling rapid and accurate predictions of flow characteristics, which is critical for aerospace design, weather forecasting, and various engineering applications, ultimately accelerating discovery and decision-making in computationally intensive domains.

<div class="no-figures"><p>Representative figures will be added soon.</p></div>

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
