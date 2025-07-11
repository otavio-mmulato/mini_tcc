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
        'brand-brown': '#A8701A',
        'brand-green': '#2C641E',
        'brand-bg': '#eee4d5',
      }
    },
  },
  plugins: [],
}