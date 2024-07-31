/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["*.{html,js},",
    './index.html',
    './admin/**/*.html',
    './dashboard/**/*.html',
    './garage/**/*.html',
  ],
  theme: {
    extend: {
      opacity: ['group-hover'],
      animation: {
        'gradient': 'gradient 8s linear infinite',
      },
      keyframes: {
        'gradient': {
          to: { 'background-position': '200% center' },
        }
      },
      colors: {
        "primary": "#FF8236",
        "secondary": {
          100: "#C1F1DD",
          200: "#888883",
        },
        "warning": "#FF8236",
      },
    },
    fontFamily: {
      "body": ["Mokoto", "sans-serif"],
    },
  },
  plugins: [require("daisyui")],
}

