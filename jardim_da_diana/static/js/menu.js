// js/menu.js

document.addEventListener('DOMContentLoaded', () => {
    // Seleciona os elementos do DOM
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const closeMenuBtn = document.getElementById('close-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    // Função para abrir o menu
    const openMenu = () => {
        mobileMenu.classList.add('open');
    };

    // Função para fechar o menu
    const closeMenu = () => {
        mobileMenu.classList.remove('open');
    };

    // Adiciona evento de clique ao botão hambúrguer para abrir o menu
    if (hamburgerBtn) {
        hamburgerBtn.addEventListener('click', openMenu);
    }

    // Adiciona evento de clique ao botão de fechar para fechar o menu
    if (closeMenuBtn) {
        closeMenuBtn.addEventListener('click', closeMenu);
    }
});