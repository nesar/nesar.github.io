---
title: "Cosmology & Large-Scale Structure Dynamics"
excerpt: "Research in cosmology & large-scale structure dynamics"
collection: portfolio
---

Cosmology and the study of large-scale structure dynamics aim to unravel the universe's evolution from its earliest moments to its current complex configuration. This field investigates how gravitational instability, driven by dark matter and dark energy, shapes the cosmic web—an intricate network of voids, sheets, filaments, and massive dark matter halos. Understanding the formation and evolution of these structures is crucial for testing fundamental physics, including the nature of gravity and the properties of dark matter. Researchers in this domain employ sophisticated theoretical models and analyze vast observational datasets to probe the universe's constituents and governing laws.

Key observational probes include cosmic shear from weak gravitational lensing, which maps the distribution of dark matter; galaxy clusters, which represent the most massive gravitationally bound structures; and the kinetic Sunyaev-Zel'dovich (kSZ) effect, offering insights into the peculiar velocities of galaxy groups and clusters. The precise analysis of these data, often at the limits of detector capabilities, necessitates advanced statistical and computational techniques. Furthermore, exploring alternative gravity theories, such as f(R) gravity, requires developing specific methodologies to constrain their parameters and distinguish them from standard cosmological models.

My research extensively explores the fundamental dynamics and structure of the cosmic web, leveraging both theoretical insights and advanced computational techniques. I have pioneered the "multistream view" of dark matter dynamics, elucidating the intricate substructure within dark matter halos and the surrounding cosmic web, as detailed in my work on "Dark matter haloes: a multistream view" and "Multi-stream portrait of the Cosmic web." This approach, along with investigations into "The Caustic Design of the Dark Matter Web" and "Topology and geometry of the dark matter web," provides novel ways to characterize the phase-space structure, classify cosmic web elements, and trace its formation, contributing significantly to our understanding of structure formation beyond simplified models.

A major thrust of my work involves developing and applying advanced machine learning and artificial intelligence methodologies to tackle complex problems in cosmology. I have developed high-fidelity emulators, such as the "Matter Power Spectrum Emulator for f(R) Modified Gravity Cosmologies," which efficiently predict cosmological observables under alternative gravity theories, enabling robust constraints from data like the "k-cut Cosmic Shear Analysis" of Hyper Suprime-Cam data. Furthermore, I have contributed to "Benchmarking AI-evolved cosmological structure formation" and creating "Multi-modal Foundation Models" for simulation data, pushing the boundaries of AI in simulating and analyzing the universe. My contributions also include developing "Differentiable Predictions for Large Scale Structure with SHAMNet" and novel methods for "Peculiar Velocity Estimation from Kinetic SZ Effect using Deep Neural Networks," alongside strategies for "Reducing Model Error Using Optimised Galaxy Selection" for weak lensing cluster mass estimation. These innovations enhance the precision and efficiency of cosmological analyses, paving the way for more accurate inferences from next-generation surveys.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/topology-and-geometry-of-the-dark-matter-web-a-mul_plot_1_b9734473.png" alt="Figure from Topology and geometry of the dark matter web: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Topology and geometry of the dark matter web: a multistream view</div>
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
