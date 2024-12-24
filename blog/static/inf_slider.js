const slides = document.querySelector('.slides');
const slide = document.querySelectorAll('.slide');
const nextBtn = document.getElementById('nextBtn');
const prevBtn = document.getElementById('prevBtn');

let index = 0;

nextBtn.addEventListener('click', () => {
  index++;
  if (index >= slide.length-2) {
    index = 0; // Сброс индекса для бесконечного слайдера
  }
  updateSlider();
});

prevBtn.addEventListener('click', () => {
  index--;
  if (index < 0) {
    index = slide.length - 1; // Сброс индекса для бесконечного слайдера
  }
  updateSlider();
});

function updateSlider() {
  const offset = -index * 300; // 300 - ширина одного слайда
  slides.style.transform = `translateX(${offset}px)`;
}
