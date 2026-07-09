---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

Machine learning has emerged as a transformative paradigm across diverse scientific domains, offering powerful tools to extract knowledge from complex and high-dimensional datasets. In fields ranging from astrophysics and cosmology to materials science and engineering, ML techniques are enabling unprecedented rates of discovery, enhancing data analysis pipelines, and providing novel insights into underlying physical processes. Researchers are leveraging advanced algorithms to tackle challenges such as the analysis of vast astronomical surveys, the detection of rare or anomalous phenomena, the interpretation of intricate simulations, and the robust prediction of physical properties, often under conditions of sparse or uncertain data.

The application of machine learning in scientific contexts frequently involves developing methodologies tailored to specific domain characteristics, such as the need for physical interpretability, accurate uncertainty quantification, and the ability to handle inherent data sparsity or noise. Deep learning architectures, generative models, multi-task learning frameworks, and probabilistic modeling are at the forefront of these efforts. These techniques are employed to perform tasks such as automated classification of astronomical objects, reconstruction of complex physical fields from limited sensor data, identification of subtle patterns in observational data, and the generation of synthetic data to augment simulations or improve understanding. The impact spans from accelerating the processing of petabytes of data from observatories like Rubin LSST to enabling the design of novel materials and systems in engineering.

My research extensively explores and contributes to this rapidly evolving landscape, focusing on developing and applying cutting-edge machine learning methodologies to address pressing challenges in both fundamental science and engineering. I have developed multi-task modeling approaches specifically for engineering applications characterized by sparse data, demonstrating robust performance in scenarios where traditional methods struggle. A significant portion of my work centers on enhancing the interpretability and reliability of AI systems through techniques such as statistically disentangled latent spaces in generative models, ensuring that insights gleaned are physically meaningful. Furthermore, I have advanced probabilistic modeling and automated machine learning frameworks to handle high-dimensional stress fields and improve interpretable uncertainty quantification in AI for high-energy physics.

I have applied these advanced methodologies to a broad spectrum of scientific problems. In astrophysics, my contributions span from creating comprehensive photometric samples of stars in the Milky Way and predicting new concept-object associations in literature to developing modular deep learning pipelines for galaxy morphology classification, strong gravitational lens detection and modeling, and point spread function deconvolution. My work includes leveraging generative adversarial networks (GANs) for anomaly detection in Hyper Suprime-Cam galaxy images, benchmarking AI-evolved cosmological structure formation, and estimating peculiar velocities and probabilistic redshifts from synthetic spectra (SYTH-Z). These efforts are crucial for understanding galaxy evolution, probing dark energy (e.g., for Rubin LSST Dark Energy Science Collaboration), exploring the cosmic web, and identifying exotic stars like Carbon-Enhanced Metal-Poor candidates, while also extending to global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
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
