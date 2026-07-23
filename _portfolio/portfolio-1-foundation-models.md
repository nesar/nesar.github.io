---
title: "Foundation Models"
excerpt: "Research in foundation models"
collection: portfolio
---

Foundation Models represent a pivotal paradigm shift in artificial intelligence, characterized by their immense scale, pre-training on vast and diverse datasets, and remarkable adaptability to a wide array of downstream tasks. These models serve as powerful general-purpose systems, capable of performing complex operations ranging from natural language understanding and generation to advanced image recognition and scientific discovery. Their ability to generalize across tasks and domains with minimal fine-tuning has positioned them as a cornerstone for future AI development, driving innovation across numerous industries and research fields.

Within this transformative landscape, two critical areas of inquiry stand out: the fundamental principles governing the behavior of Large Language Models (LLMs) and the development of multimodal foundation models. Research into LLMs explores the intricate relationship between model scale, computational resources, and performance, seeking to uncover universal scaling laws that predict how capabilities evolve. Concurrently, the exploration of emergent abilities investigates the qualitative shifts in intelligence that arise unexpectedly as models increase in size and training data. Complementing this, multimodal foundation models aim to bridge the gap between disparate data types, such as images, text, and numerical data, particularly critical for applications demanding holistic understanding in complex domains like scientific analysis.

My research significantly contributes to both of these foundational pillars of artificial intelligence. In investigating "Scaling Laws for Large Language Models and Emergent Abilities," I have systematically analyzed the quantitative relationships that govern LLM performance, demonstrating how increasing computational budget, model parameters, and dataset size lead to predictable improvements. Crucially, my work identifies and characterizes emergent abilities—novel capabilities that manifest non-linearly at certain scales, such as advanced reasoning or problem-solving skills—providing critical insights into the qualitative leaps in AI intelligence and informing the design principles for more efficient and powerful next-generation models.

Furthermore, my efforts extend into the development of "Multimodal Foundation Models for Scientific Image Analysis." Recognizing the limitations of unimodal approaches in complex scientific contexts, I have designed and implemented innovative architectures that integrate diverse data modalities, including high-resolution images, associated metadata, and textual descriptions. This approach addresses the unique challenges of scientific data, enabling more accurate and interpretable analyses in critical fields such as material science, biology, and medicine. By leveraging rich, heterogeneous information, my models enhance the discovery process, offering deeper insights into intricate scientific phenomena that were previously inaccessible to purely visual or textual AI systems.

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
