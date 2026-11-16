/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        tsplrb: {
          navy: "#0f172a",
          gold: "#d97706",
          blue: "#2563eb",
          green: "#16a34a",
          red: "#dc2626",
          purple: "#7c3aed",
        }
      }
    },
  },
  plugins: [],
}
