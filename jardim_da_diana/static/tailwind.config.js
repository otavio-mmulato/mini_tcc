/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './*.{html,js}',
    './css/base.css',
  ],
  theme: {
    extend: {
      fontFamily: {
          serif: ['Times New Roman', 'Times', 'serif'],
      },
      colors: {
        'brand-yellow': '#F2B11D',
        'brand-brown': '#A07855',
        'brand-green': '#2C641E',
        'brand-bg': '#F8F5EF',
        'card-bg': '#FFFFFF',
        'header-text': '#3B2116', // <-- COR MAIS ESCURA APLICADA
      }
    },
  },
  plugins: [],
}