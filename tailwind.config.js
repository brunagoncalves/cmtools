/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
    "./node_modules/flowbite/**/*.js",
  ],
  theme: {
    colors: {
      bgSidebar: "#F5F5F5",
      bgButtonSidebar: "#534FEB",
      textSidebar: "#534FEB",
    },
    extend: {},
  },
  plugins: [require("flowbite/plugin")],
};
