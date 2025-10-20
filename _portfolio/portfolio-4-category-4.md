---
title: "Galactic Structure & Stellar Populations"
excerpt: "Research in galactic structure & stellar populations"
collection: portfolio
---

The study of Galactic structure and stellar populations is crucial for understanding the formation and evolutionary history of the Milky Way, our home galaxy. By examining the distribution, kinematics, and chemical compositions of different stellar groups, astronomers can reconstruct the processes that built the disk, bulge, and halo, shed light on the nature of dark matter, and trace the galaxy's interactions with its satellite companions. This research area often grapples with challenges such as interstellar dust extinction, which obscures distant regions, and the accurate determination of stellar distances, which is fundamental to mapping the galaxy's three-dimensional structure.

To overcome these challenges, researchers frequently employ standard candles – stars with well-defined intrinsic luminosities – whose observed brightness can then be used to infer their distances. Red Clump (RC) stars, post-main sequence stars undergoing helium core burning, are particularly valuable standard candles due to their remarkably consistent absolute magnitudes across a wide range of metallicities and ages. This characteristic makes them ideal tracers for mapping the large-scale structure of the Milky Way, allowing for accurate distance measurements even in dust-enshrouded or distant regions.

Large-scale photometric surveys, which systematically observe vast swathes of the sky in multiple wavelength bands, have revolutionized this field by providing the necessary data to identify and characterize millions of these stellar tracers. The accurate identification and precise distance determination of Red Clump stars from these surveys are essential for constructing detailed maps of the Galactic disk, revealing its scale height, warp, and any underlying substructures. These comprehensive catalogs enable unprecedented insights into the Milky Way's stellar density distribution and its dynamic properties.

My research focuses on leveraging these massive photometric datasets to unravel the Milky Way's intricate structure. In a significant contribution, I developed a robust methodology to identify and characterize an unprecedented sample of 2.6 million Red Clump stars across the entire Galactic disk, from its innermost regions to its distant outskirts. This work, detailed in "From the Inner to Outer Milky Way: A Photometric Sample of 2.6 Million Red Clump Stars," involved meticulous selection criteria based on precise photometric data, enabling accurate distance measurements for each star.

The resulting catalog provides a powerful new tool for mapping the Milky Way's stellar density distribution, identifying subtle substructures such as stellar streams and warps, and deriving Galactic parameters with unparalleled precision. By extending the mapping capabilities to both the inner and outer Galaxy, my work offers crucial insights into the formation and evolution of the disk, providing essential observational constraints for theoretical models of galaxy assembly. This extensive sample facilitates studies ranging from the kinematics of the stellar halo to the properties of the Galactic bar, significantly advancing our understanding of our home galaxy's complex architecture.

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
