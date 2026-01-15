---
title: "Dark Matter & Cosmology"
excerpt: "Research in dark matter & cosmology"
collection: portfolio
---

The universe at its grandest scales is structured by an invisible scaffolding known as the cosmic web, composed predominantly of dark matter. This mysterious substance, which does not interact with light, is inferred solely through its gravitational effects, dictating the formation and evolution of galaxies and galaxy clusters. Understanding the nature of dark matter and its intricate distribution is a central challenge in modern cosmology, profoundly impacting our models of the universe's origin, expansion, and ultimate fate. Researchers employ a diverse toolkit, ranging from sophisticated cosmological simulations to analyses of vast astronomical survey data, to unravel the properties of dark matter and test fundamental theories of gravity.

Cosmology seeks to explain the universe's large-scale structure, from the distribution of matter to the dynamics of its expansion. This pursuit involves analyzing observational probes such as weak gravitational lensing (cosmic shear), galaxy surveys, and mapping the cosmic microwave background, alongside developing theoretical models that incorporate dark matter and dark energy. The field also investigates alternative theories of gravity, which propose modifications to Einstein's General Relativity on cosmic scales, offering potential explanations for observed phenomena without invoking exotic dark components. These efforts are crucial for refining the standard model of cosmology, known as Lambda-CDM, or for paving the way for new physical paradigms.

My research contributions have centered on developing a deeper understanding of dark matter's structure and its cosmological implications, utilizing both theoretical modeling and cutting-edge observational data. A significant portion of my work has focused on characterizing the complex, multi-stream nature of dark matter within haloes and the cosmic web. By analyzing simulations, I have developed methods to identify and quantify the distinct streams of dark matter that converge to form these structures, revealing their intricate caustic designs and mapping their topology and geometry. This multi-stream view provides a more granular and dynamic portrait of the cosmic web than traditional density-field analyses, offering new insights into how dark matter aggregates and influences galaxy formation.

Furthermore, I have actively contributed to constraining cosmological models and theories of gravity through the analysis of large-scale observational datasets. This includes applying a k-cut cosmic shear analysis to Hyper Suprime-Cam (HSC) first-year data, a powerful technique to test modified gravity theories like f(R) gravity, thereby probing deviations from General Relativity on cosmic scales. My work also extends to developing and utilizing advanced cosmological simulations, such as CRK-HACC, to model the intricacies of galaxy formation within the evolving cosmic web. Complementing these theoretical and numerical efforts, I have been involved in major observational initiatives, contributing to the SPTpol Extended Cluster Survey and analyzing large photometric samples of stars, such as 2.6 million Red Clump stars across the Milky Way, to trace galactic structure and mass distribution. I am also contributing to future missions like SPHEREx, which promise to deliver unprecedented cosmological data, further solidifying our understanding of the universe's fundamental constituents and its grand evolutionary narrative.

<div class="research-figures">
  <div class="figure-item">
    <img src="/images/research/figures/from-the-inner-to-outer-milky-way-a-photometric-sa_plot_1_2e56b6d6.png" alt="Figure from From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/the-caustic-design-of-the-dark-matter-web_plot_1_1a1bb482.png" alt="Figure from The Caustic Design of the Dark Matter Web" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: The Caustic Design of the Dark Matter Web</div>
  </div>
  <div class="figure-item">
    <img src="/images/research/figures/dark-matter-haloes-a-multistream-view_plot_1_bb77684a.png" alt="Figure from Dark matter haloes: a multistream view" onclick="openModal(this)" loading="lazy" />
    <div class="figure-caption">From: Dark matter haloes: a multistream view</div>
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
