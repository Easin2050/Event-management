/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
  "./templates/**/*.html",//template at the project lavel
  "./**/templates/**/*.html"//templates inside application
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

