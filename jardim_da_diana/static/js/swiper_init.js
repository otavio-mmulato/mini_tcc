document.addEventListener('DOMContentLoaded', () => {
    // Inicialização do carrossel de Banners (Hero)
    const heroSwiper = new Swiper('.hero-swiper', {
        loop: true,
        effect: 'fade',
        fadeEffect: { crossFade: true },
        pagination: { el: '.swiper-pagination', clickable: true },
        navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
        autoplay: { delay: 4000, disableOnInteraction: false },
    });

    // Inicialização do carrossel de produtos (ATUALIZADO)
    const productSwiper = new Swiper('.product-swiper', {
        loop: true,
        spaceBetween: 24,

        slidesPerView: 1,
        centeredSlides: true,

        navigation: {
            nextEl: '.product-carousel-container .swiper-button-next',
            prevEl: '.product-carousel-container .swiper-button-prev',
        },

        // ADICIONE O BLOCO ABAIXO DE VOLTA
        pagination: {
            el: '.product-swiper .swiper-pagination', // Usamos um seletor mais específico
            clickable: true,
        },

        breakpoints: {
            768: {
                slidesPerView: 3,
                centeredSlides: false,
            },
            1024: {
                slidesPerView: 5,
                centeredSlides: false,
            }
        }
    });
});
