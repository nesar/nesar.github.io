---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The field of machine learning for science is rapidly transforming how researchers approach complex problems across various disciplines, particularly in astronomy and engineering. By leveraging advanced computational techniques, scientists can extract unprecedented insights from vast and intricate datasets, accelerate discovery, and push the boundaries of knowledge. This area focuses on developing and applying sophisticated algorithms to tackle challenges such as the analysis of large-scale survey data, the identification of subtle patterns, and the creation of accurate predictive models that would be intractable through traditional methods.

Core to this endeavor is the deployment of diverse machine learning methodologies, including deep learning architectures, generative adversarial networks, probabilistic modeling, and unsupervised learning, tailored to scientific contexts. These techniques are crucial for tasks like deconvolution of noisy images, anomaly detection in observational data, precise estimation of physical parameters, and robust classification of celestial objects. Furthermore, the emphasis extends to enhancing the interpretability of models, ensuring that the insights gained are not only accurate but also physically meaningful and verifiable, thereby fostering trust and deeper scientific understanding.

My research significantly contributes to this landscape by developing and applying cutting-edge machine learning techniques to address pressing challenges in astrophysics and broader engineering applications. I have developed multi-task modeling approaches to efficiently handle sparse engineering data and introduced probabilistic frameworks for high-dimensional stress field analysis, as well as global field reconstruction from sparse sensors using Voronoi tessellation-assisted deep learning. In astrophysics, my work includes pioneering applications of neural networks for tasks like Point Spread Function deconvolution and novel anomaly detection in Hyper Suprime-Cam galaxy images using generative adversarial networks. I have also explored the rich potential of unsupervised machine learning to move "Beyond the Hubble Sequence" in classifying galaxy morphologies, and created modular deep learning pipelines for strong gravitational lens detection and modeling.

A major thrust of my contributions lies in leveraging machine learning for large-scale astronomical surveys and physical parameter inference. This includes utilizing deep neural networks for peculiar velocity estimation from the Kinetic Sunyaev-Zel'dovich effect, and developing the SYTH-Z framework for machine learning synthetic spectra to enable probabilistic redshift estimation. I have also focused on enhancing interpretability in generative models by guiding disentangled latent spaces with physical factors to uncover the drivers of dark matter halo structures. Furthermore, my research extends to improving the reliability of weak lensing cluster mass estimation through optimized galaxy selection, identifying Carbon-Enhanced Metal-Poor star candidates from Gaia DR3 spectra, and predicting new concept-object associations in astronomy by mining the literature, ultimately supporting missions like SPHEREx and the Rubin LSST Dark Energy Science Collaboration. These efforts aim to not only accelerate data analysis but also to reveal fundamental physical processes and enable new scientific discoveries.

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
