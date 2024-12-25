const slides = document.querySelector('.slides');
const slide = document.querySelectorAll('.slide');

const slides_mini = document.querySelector('.slides_mini');
const mini_slide = document.querySelectorAll('.mini_slide');

const nextBtn = document.getElementById('nextBtn');
const prevBtn = document.getElementById('prevBtn');

let index = 0;
let index_mini = 0;
nextBtn.addEventListener('click', () => {
  index++;
  index_mini++;
  if (index >= slide.length - 2) {
    index = 0; // Сброс индекса для бесконечного слайдера
    index_mini = 0;
  } 
  updateSlider();
});

prevBtn.addEventListener('click', () => {
  index--;
  index_mini--;
  if (index < 0) {
    index = slide.length - 3; // Сброс индекса для бесконечного слайдера
    index_mini = slide.length - 3;
  }
  updateSlider();
});

function updateSlider() {
  const offset = -index * 455; // 300 - ширина одного слайда
  const offset_mini = index_mini * 50; // 200 - ширина mini слайда
  slides.style.transform = `translateX(${offset}px)`;
  slides_mini.style.transform = `translateX(${offset_mini}px)`;
}
