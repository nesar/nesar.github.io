---
title: "Advanced Data Science & Scientific Computation"
excerpt: "Research in advanced data science & scientific computation"
collection: portfolio
---

The field of Advanced Data Science and Scientific Computation plays a pivotal role in accelerating scientific discovery and engineering innovation by tackling complex challenges across diverse domains. It encompasses the development and application of sophisticated computational and statistical techniques to extract meaningful insights from vast, often high-dimensional and noisy datasets, and to build robust predictive models for intricate physical phenomena. Key areas include the creation of efficient surrogate models, the reconstruction of global fields from sparse observations, and the enhancement of model interpretability and reliability through uncertainty quantification.

Researchers in this domain are dedicated to advancing methodologies for addressing the inherent complexities of scientific data, such as non-linearity, sparsity, and the need for statistically sound inference. This involves developing novel machine learning architectures, probabilistic modeling frameworks, and optimization strategies tailored to specific scientific problems, ranging from astrophysical surveys to complex fluid dynamics simulations. The overarching goal is to transform raw data into actionable knowledge, enabling more accurate predictions, deeper understanding, and optimized design and operational processes.

My research significantly contributes to this landscape by developing and applying cutting-edge data science and machine learning techniques to solve complex problems in both fundamental science and engineering. I have focused on enhancing model interpretability and robustness, for instance, by developing methods for generating statistically disentangled latent spaces guided by generative factors in scientific datasets, thereby making complex generative models more transparent and reliable. A core aspect of my work involves probabilistic modeling, where I have designed and applied probabilistic neural networks and Gaussian process emulation to create efficient reduced-order surrogates for fluid flows, enabling robust predictions and data recovery even with limited information. Furthermore, I have explored automated machine learning frameworks for high-dimensional stress field analysis, drastically improving efficiency and accuracy in computational mechanics.

Beyond methodology development, my work directly impacts critical scientific and engineering applications. In astrophysics, I constructed a comprehensive photometric sample of 2.6 million Red Clump stars, pushing the boundaries of our understanding of the Milky Way's inner to outer structure. I also devised optimized galaxy selection techniques to reduce model error in weak lensing cluster mass estimation, crucial for cosmological studies. For real-world engineering challenges, I developed Voronoi tessellation-assisted deep learning approaches for global field reconstruction from sparse sensors, providing efficient and accurate ways to monitor and understand distributed physical phenomena. These contributions highlight my expertise in transforming theoretical advancements into practical tools that accelerate scientific discovery and improve engineering design and analysis.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/enhancing-interpretability-in-generative-modeling-_plot_1_fb007588.png" alt="Figure from Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Enhancing Interpretability in Generative Modeling: Statistically Disentangled Latent Spaces Guided by Generative Factors in Scientific Datasets</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/reducing-model-error-using-optimised-galaxy-select_plot_1_8b13e102.png" alt="Figure from Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Reducing Model Error Using Optimised Galaxy Selection: Weak Lensing Cluster Mass Estimation</div>
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
