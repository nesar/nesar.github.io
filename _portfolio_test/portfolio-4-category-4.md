---
title: "Machine Learning for Astrophysical Prediction and Analysis"
excerpt: "Research in machine learning for astrophysical prediction and analysis"
collection: portfolio
---

The field of astrophysics is increasingly leveraging the power of machine learning to tackle complex problems that are computationally intensive or analytically intractable. From discovering exoplanets to classifying galaxies and simulating cosmic evolution, machine learning algorithms offer novel approaches to extract insights from vast astronomical datasets and high-fidelity simulations. This interdisciplinary convergence is crucial for advancing our understanding of the universe, enabling faster predictions, identifying subtle patterns, and developing new analytical tools that complement traditional theoretical and observational methods.

One particularly challenging area within astrophysics is understanding the formation of the first stars, known as Population III (Pop III) or primordial stars. These stars are theorized to have formed from pristine hydrogen and helium following the Big Bang, profoundly influencing the reionization of the early universe and seeding the formation of subsequent stellar generations. Accurately modeling their formation, especially identifying the precise locations and conditions conducive to their birth within the complex, evolving cosmic web, requires sophisticated numerical simulations that are often computationally prohibitive and difficult to generalize.

My research focuses on addressing these computational and analytical challenges by developing advanced machine learning methodologies. I have specifically concentrated on the application of deep learning techniques to predict the emergence and localization of primordial star formation, thereby significantly accelerating our ability to explore the early universe.

In my work, I have developed and deployed Deep Convolutional Neural Networks (CNNs) to predict localized primordial star formation. These CNNs are meticulously designed to process complex three-dimensional simulation data, learning intricate relationships between initial gas properties, dark matter distribution, and the ultimate sites where primordial stars are most likely to form. This approach not only provides highly accurate predictions for star-forming regions but also offers unprecedented insights into the underlying physical conditions that drive primordial collapse. By leveraging the pattern recognition capabilities of CNNs, I have created a powerful predictive tool that can significantly reduce the computational burden of traditional cosmological simulations, allowing for more extensive parameter space exploration and a deeper understanding of the early universe's stellar genesis. The impact of this work is in providing a rapid, robust method for identifying critical regions in vast cosmic datasets, thus enabling more efficient and targeted follow-up studies and advancing our knowledge of cosmic reionization and the universe's formative epochs.

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
