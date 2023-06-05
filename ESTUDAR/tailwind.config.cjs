/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [ "./index.html",
  "./src/**/*.{js,ts,jsx,tsx}",
],
  theme: {
    extend: {
      colors: {
        'blue-gradient': '#442DB3',
        'purple-gradient': '#BE00FF',

      },
      screens: {
        'md': {'max': '900px'},
        'md2': {'max': '450px'},
        
      }
    },
  },
  plugins: [],
}
