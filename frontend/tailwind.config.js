/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      backgroundImage:{
        "pesasImg": "url('/src/pages/auth/pesas.jpg')",
      },
      backgroundColor:{
        'gris-oscuro': '#2c2c2c',
      }
    },
  },
  plugins: [
    function ({ addUtilities }) {
      const newUtilities = {
        '.clip-path-poly-trapezium': {
          clipPath: 'polygon(0% 0%, 100% 0%, 80% 100%, 0% 100%)',
        },
        '.clip-t':{
          clipPath: 'polygon(68% 0, 100% 0, 100% 100%, 51% 100%)',
        },
        '.clip-path-poly-trapezium-bg-black': {
          '@apply clip-path-poly-trapezium': {},
          backgroundColor: 'black',
        },
      };
      addUtilities(newUtilities, ['responsive', 'hover']);
    },
  ],
}