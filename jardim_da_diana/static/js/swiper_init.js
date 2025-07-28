document.addEventListener('DOMContentLoaded', function () {
  const heroSwiper = new Swiper('.hero-swiper', {
    direction: 'horizontal',
    loop: true,
    effect: 'fade',
    pagination: { el: '.swiper-pagination', clickable: true, },
    navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev', },
    autoplay: { delay: 5000, disableOnInteraction: false, }
  });
});