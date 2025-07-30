---
title: "Emulation & Inference"
excerpt: "Research in emulation & inference"
collection: portfolio
---

The intersection of complex scientific and engineering problems with high-fidelity simulations often creates significant computational bottlenecks. Emulation and inference, powered by advanced machine learning and artificial intelligence techniques, offer a powerful paradigm to overcome these challenges. This field focuses on creating computationally efficient surrogate models, or emulators, that accurately mimic the behavior of complex systems, thereby enabling rapid exploration of vast parameter spaces, efficient inverse problem solving, and robust uncertainty quantification.

Research in this area spans diverse domains, including astrophysics and cosmology, where tasks like estimating galaxy cluster masses from weak lensing, understanding large-scale structure formation, and determining probabilistic redshifts from synthetic spectra are computationally intensive. It also extends to engineering disciplines, particularly fluid dynamics and materials science, for applications such as reconstructing high-dimensional stress fields from limited data, simulating complex fluid flows, and developing reduced-order models for real-time analysis or data recovery from sparse sensors.

Methodologically, the work leverages state-of-the-art techniques including deep neural networks, Gaussian processes, and novel probabilistic modeling frameworks. These advanced techniques are employed to build high-fidelity emulators for phenomena like the matter power spectrum in modified gravity theories, to estimate peculiar velocities from kinetic SZ effects, and to develop non-intrusive reduced-order models for fluid flows. A recurring theme across these applications is the emphasis on not just accurate prediction, but also interpretable uncertainty quantification and the ability to perform differentiable predictions, allowing for efficient gradient-based optimization and robust inference.

My work has specifically focused on developing and applying these advanced machine learning methodologies to accelerate scientific discovery and engineering design. I have pioneered the use of probabilistic neural networks (PNNs) for robust fluid flow surrogate modeling and data recovery, and for constructing reduced-order models capable of latent-space time evolution using Gaussian process emulation. In cosmology, I developed SHAMNet for differentiable predictions of large-scale structure and SYTH-Z for machine learning synthetic spectra to enable probabilistic redshift estimation, alongside an emulator for the matter power spectrum in f(R) modified gravity cosmologies. Furthermore, I have addressed practical challenges such as reducing model error in weak lensing cluster mass estimation through optimized galaxy selection and reconstructing global fields from sparse sensor data using Voronoi tessellation-assisted deep learning.

A core contribution across these projects is the rigorous integration of interpretable uncertainty quantification into AI models, ensuring that predictions are not only accurate but also provide reliable confidence estimates crucial for high-stakes scientific and engineering applications. By developing these computationally efficient and robust AI-driven emulation and inference frameworks, my research significantly reduces the time and computational resources required for complex simulations and data analysis, thereby accelerating hypothesis testing, model validation, and the discovery of new physical insights.

<div class="research-figures"><div class="no-figures"><p>Representative figures will be added soon.</p></div></div>

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
