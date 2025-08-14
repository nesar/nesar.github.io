---
title: "AI Applications in Computational Astrophysics"
excerpt: "Research in ai applications in computational astrophysics"
collection: portfolio
---

Computational astrophysics plays a pivotal role in unraveling the mysteries of the universe, employing advanced numerical simulations to model complex phenomena ranging from galaxy formation to the evolution of stars. This field is essential for exploring regimes inaccessible to direct observation, such as the early universe or the interiors of compact objects. Researchers leverage supercomputers to simulate the interplay of gravity, hydrodynamics, radiative transfer, and chemical processes, generating vast datasets that capture the evolution of cosmic structures over billions of years. The immense complexity and scale of these simulations present significant challenges in data analysis and the identification of crucial physical processes.

One particularly challenging area within this domain is the study of primordial star formation, which concerns the birth of the very first stars, known as Population III stars. These stars, formed from the pristine, metal-free gas left over from the Big Bang, are thought to have profoundly influenced the early universe by reionizing hydrogen and synthesizing the first heavy elements. Identifying the precise conditions and locations where these stars form within vast cosmological simulations requires sophisticated techniques, as it involves detecting small-scale gravitational collapses embedded within evolving cosmic webs. The burgeoning field of artificial intelligence (AI), particularly machine learning, offers powerful new paradigms to address these challenges, enabling rapid pattern recognition, prediction, and the extraction of subtle features from astrophysical data.

My research stands at the intersection of computational astrophysics and advanced machine learning, specifically focusing on applying deep learning techniques to accelerate and enhance our understanding of primordial star formation. In particular, I have developed and implemented Deep Convolutional Neural Networks (DCNNs) to predict localized primordial star formation within cosmological simulations. This work addresses the critical need for efficient methods to identify the precise sites of gravitational collapse that lead to the birth of the first stars. By training DCNNs on simulated cosmic gas density fields, I have demonstrated their exceptional capability to learn and generalize the complex, non-linear relationships that govern the onset of star formation, effectively bypassing computationally expensive traditional analytical criteria or detailed follow-up simulations.

The methodology I developed leverages the inherent strength of DCNNs in learning hierarchical spatial features, making them particularly well-suited for analyzing three-dimensional astrophysical data cubes and discerning subtle density fluctuations that signify impending collapse. This approach not only provides a highly accurate predictive tool but also significantly reduces the computational resources required to pinpoint star-forming regions. My contributions offer a significant step forward in our ability to rapidly identify and characterize the progenitors of Population III stars, paving the way for more targeted and efficient high-resolution simulations of these pivotal cosmic events, and thereby enabling deeper insight into the foundational processes that shaped the universe we observe today.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/predicting-localized-primordial-star-formation-wit_plot_1_20ccb55a.png" alt="Figure from Predicting Localized Primordial Star Formation with Deep Convolutional Neural Networks" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Predicting Localized Primordial Star Formation with Deep Convolutional Neural Networks</div>
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
