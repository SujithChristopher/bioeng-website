/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        navy: {
          900: '#0f2645',
          800: '#1a3a5c',
          700: '#1e4976',
          600: '#2563a8',
          100: '#dce8f5',
          50: '#f0f5fb',
        },
        gold: {
          500: '#b8941f',
        },
      },
      fontFamily: {
        serif: ['Playfair Display', 'Georgia', 'serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
