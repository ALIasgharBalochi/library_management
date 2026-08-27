/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./book/templates/**/*.html",
    "./book/**/*.py",
  ],
  theme: {
    extend: {
      colors: {
        ink: "#0A0A0B",
        electric: "#A3FF12",
      },
      boxShadow: {
        glow: "0 0 40px rgba(163,255,18,.16)",
      },
    },
  },
  plugins: [],
}
