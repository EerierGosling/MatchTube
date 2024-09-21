/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    colors: {
      'tinderPink': '#FD297B',
      'tinderOrange': '#FF655B',
      'tinderRed': '#FF5864',
      'white': '#FFFFFF',
      'grey': '#CCCCCC'
    },
    extend: {},
  },
  plugins: [
    require("tailwindcss-animate"),
  ],
}

