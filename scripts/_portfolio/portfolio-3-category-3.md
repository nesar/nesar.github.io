---
title: "High-Redshift Extragalactic Source Characterization"
excerpt: "Research in high-redshift extragalactic source characterization"
collection: portfolio
---

High-redshift extragalactic sources, observed as they existed billions of years ago, offer a unique window into the early universe, revealing the fundamental processes of galaxy formation and evolution. Characterizing these distant objects is crucial for understanding how the first galaxies assembled, how star formation proceeded in the cosmic dawn, and the role of dark matter and baryonic matter in structuring the universe. However, their extreme distances mean that their emitted light is significantly redshifted and intrinsically faint, posing substantial observational challenges.

Millimeter-wave telescopes, such as the South Pole Telescope (SPT) and the Atacama Cosmology Telescope (ACT), are powerful tools for identifying these elusive sources. They are particularly effective at detecting distant, dusty, star-forming galaxies, whose peak emission is redshifted into the millimeter regime due to the "negative K-correction" effect. Additionally, gravitational lensing, where foreground massive structures magnify the light from background high-redshift galaxies, provides a crucial mechanism to overcome faintness limitations, enabling the detailed study of sources that would otherwise be undetectable.

My research has focused on surmounting these observational challenges to characterize high-redshift extragalactic sources, providing critical insights into early galaxy evolution. A significant portion of my work involved the search for and characterization of gravitationally lensed galaxies using data from the South Pole Telescope. This technical contribution leveraged the magnification power of strong gravitational lensing to detect inherently faint, distant submillimeter galaxies, allowing for their detailed study and contributing to our understanding of the most vigorously star-forming systems in the early universe.

Furthermore, I have developed and applied methodologies for determining photometric redshifts of millimeter-selected galaxies using data from the Atacama Cosmology Telescope. This technical contribution is vital for efficiently estimating the distances to a large number of these sources, circumventing the resource-intensive process of spectroscopic follow-up. By deriving these photometric redshifts, I contributed to building large, statistically significant samples of high-redshift galaxies, enabling comprehensive analyses of their spatial distribution, evolution, and their contribution to the cosmic star formation history. This work significantly advances our ability to map and understand the properties of the early universe's galaxy population.

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
