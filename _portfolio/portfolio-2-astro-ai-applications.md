---
title: "AI for Astrophysical Data Analysis & Simulation"
excerpt: "Research in ai for astrophysical data analysis & simulation"
collection: portfolio
---

The field of astrophysics is currently experiencing an unprecedented era of data abundance, driven by next-generation telescopes and sophisticated numerical simulations. These instruments generate vast, high-dimensional datasets, presenting significant computational and analytical challenges for extracting scientific insights. Traditional methods often struggle with the sheer volume, inherent non-linearity, and complex relationships within astronomical data, particularly when analyzing phenomena ranging from galaxy evolution to the large-scale structure of the Universe and cosmological parameters. The demand for efficient, robust, and scalable analysis techniques is therefore paramount for accelerating scientific discovery and fully leveraging these invaluable datasets.

Artificial intelligence (AI) and machine learning (ML) offer powerful solutions to these challenges, providing innovative tools for data processing, feature extraction, pattern recognition, and simulation emulation. These techniques enable researchers to rapidly identify subtle signals, detect anomalies, classify astronomical objects with high precision, and predict complex astrophysical phenomena. By applying AI, it becomes possible to circumvent computationally intensive simulations, explore vast parameter spaces efficiently, and unlock insights previously unattainable, thereby revolutionizing the way astrophysical research is conducted and interpreted.

My research portfolio is dedicated to advancing the application of AI and deep learning methodologies for astrophysical data analysis and simulation. I have developed generative models, such as those demonstrated in "Generative networks synthetic sky images" and "Anomaly detection in astronomical images with generative networks," to create realistic synthetic astronomical data and to identify unusual objects or events in observational imagery, which could signify new discoveries. Furthermore, I have focused on optimizing galaxy analysis through "A Modular Deep Learning Pipeline for Galaxy-Scale" analysis and "Reducing Model Error Using Optimised Galaxy Selection," which enhance the accuracy and efficiency of galaxy classification and parameter estimation, crucial for understanding galaxy formation and evolution.

A significant portion of my work also addresses cosmological challenges. I have explored "Differentiable Predictions for Large Scale Structure," enabling more direct and optimizable links between theoretical models and observations. In "Peculiar Velocity Estimation from Kinetic SZ Effect," I applied AI to extract cosmological information from cosmic microwave background data, aiding our understanding of cosmic flows. Critically, my work on "Matter Power Spectrum Emulator for fR Modified Gravity" showcases the development of machine learning emulators to rapidly predict outcomes of computationally expensive simulations for complex cosmological models, dramatically accelerating the exploration of modified gravity theories and their comparison with observational data. These contributions collectively empower faster, more accurate, and more comprehensive astrophysical research.

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
