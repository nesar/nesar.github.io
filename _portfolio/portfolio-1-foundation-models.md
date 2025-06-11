---
title: "Foundation Models"
excerpt: "Research in foundation models <br/><img src='/images/research_foundation-models.png'>"
collection: portfolio
---

Developing large language models and foundation models specialized for astronomy, including domain-specific LLMs for scientific research and education.

## Research Figures

<div class="research-figures-grid">
</div>

<style>
.research-figures-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

.research-figure {
  text-align: center;
  background: #f8f9fa;
  border-radius: 8px;
  padding: 1rem;
  transition: transform 0.2s ease;
}

.research-figure:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}

.research-figure img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.research-figure img:hover {
  opacity: 0.9;
}

.figure-caption {
  font-size: 0.85em;
  color: #6c757d;
  margin-top: 0.5rem;
  line-height: 1.3;
}

/* Modal styles */
.modal {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0,0,0,0.9);
}

.modal-content {
  margin: auto;
  display: block;
  width: 80%;
  max-width: 700px;
  padding-top: 5%;
}

.close {
  position: absolute;
  top: 15px;
  right: 35px;
  color: #f1f1f1;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}
</style>

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

// Close modal when clicking outside the image
window.onclick = function(event) {
  var modal = document.getElementById('imageModal');
  if (event.target == modal) {
    modal.style.display = 'none';
  }
}
</script>

## Related Publications:

- **AstroMLab 4: Benchmark-Topping Performance in Astronomy Q&A with a
  70B-Parameter Domain-Specialized Reasoning Model** (2025) - Preprint
- **EAIRA: Establishing a Methodology for Evaluating AI Models as Scientific
  Research Assistants** (2025) - Preprint
- **AstroMLab 1: Who wins astronomy jeopardy!?** (2025) - Astronomy and Computing
- **Snowmass2021-Letter of Interest Scientific AI Approaches in Computational Cosmology** (2025) - Preprint
- **AstroMLab 3: Achieving GPT-4o Level Performance in Astronomy with a
  Specialized 8B-Parameter Large Language Model** (2024) - Preprint
- **Constructing impactful machine learning research for astronomy: Best practices for researchers and reviewers** (2023) - arXiv preprint arXiv:2310.12528
