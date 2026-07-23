---
title: "Machine Learning for Science"
excerpt: "Research in machine learning for science"
collection: portfolio
---

The confluence of machine learning and scientific discovery is rapidly transforming traditional research paradigms across diverse disciplines. By leveraging advanced computational algorithms, researchers can now tackle complex problems that were previously intractable due to computational expense or experimental limitations. This integration offers unprecedented opportunities to accelerate discovery, deepen understanding, and engineer novel solutions in fields ranging from materials science to molecular biology.

One critical application area lies in enhancing atomistic simulations, such as Molecular Dynamics (MD), which are fundamental for understanding the behavior of molecules and materials at atomic resolution but are notoriously computationally intensive. Simultaneously, the design and discovery of novel materials with targeted properties remains a formidable challenge, often relying on extensive experimental synthesis and characterization or computationally demanding *ab initio* calculations. Machine learning approaches are emerging as powerful tools to address these bottlenecks, providing efficient predictive models and accelerating the exploration of vast chemical and material spaces.

My research significantly contributes to this exciting frontier by developing and applying cutting-edge machine learning methodologies to critical scientific challenges. Specifically, I have focused on leveraging deep learning to dramatically accelerate molecular dynamics simulations. My work involves designing sophisticated neural network architectures capable of accurately learning complex interatomic force fields or predicting system evolution, thereby enabling simulations to run orders of magnitude faster than conventional methods. This advancement allows for the exploration of larger systems and longer timescales, previously inaccessible, providing deeper insights into molecular mechanisms and material dynamics.

Furthermore, I have developed innovative graph neural network (GNN) models for predicting the properties of novel materials. By representing molecules and periodic solids as graphs, where atoms are nodes and bonds are edges, GNNs can effectively learn structure-property relationships directly from atomic configurations. This approach facilitates high-throughput screening and accurate prediction of various material characteristics, from electronic band gaps to mechanical strength, significantly accelerating the discovery process and guiding the synthesis of materials with desired functionalities. Together, my contributions demonstrate the transformative power of deep learning and GNNs in computational science, offering robust tools for fundamental discovery and practical engineering applications.

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
