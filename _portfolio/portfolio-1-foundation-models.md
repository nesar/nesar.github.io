---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation models represent a transformative paradigm in artificial intelligence, demonstrating remarkable capabilities across a wide array of general-purpose tasks. However, their direct application to highly specialized scientific domains, such as astrophysics, often encounters limitations. These general models may struggle with the nuanced terminology, complex reasoning patterns, and vast, evolving knowledge bases inherent to scientific research, necessitating domain-specific adaptations and rigorous evaluation.

The effective integration of AI into scientific workflows demands not only models with deep domain understanding but also robust methodologies to assess their reliability, accuracy, and utility as genuine research tools. The challenge lies in moving beyond simple fact retrieval to enable AI systems to perform complex scientific reasoning, synthesize novel insights, and function as collaborative assistants in the discovery process.

My research directly addresses these challenges by developing and rigorously evaluating specialized large language models tailored for the field of astronomy. In "AstroMLab 3," I demonstrated that a specialized 8B-parameter language model could achieve performance levels comparable to significantly larger, general-purpose models like GPT-4o on complex astronomy tasks, highlighting the efficiency and power of domain adaptation. Building on this foundation, "AstroMLab 4" introduced a 70B-parameter domain-specialized reasoning model that set new benchmarks for astronomy Q&A, showcasing advanced reasoning capabilities crucial for scientific inquiry. My earlier work in "AstroMLab 1" explored initial benchmarks for AI performance in astronomy knowledge.

A core contribution of my work extends beyond model development to the establishment of comprehensive evaluation frameworks. In "EAIRA," I developed a novel methodology for systematically evaluating AI models as scientific research assistants. This framework goes beyond traditional accuracy metrics, assessing an AI's capacity for complex scientific reasoning, information synthesis, and overall utility in accelerating research. This rigorous, multi-faceted approach ensures that the foundation models I develop are not only powerful and efficient but also reliable and trustworthy collaborators in the advancement of scientific discovery.

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
