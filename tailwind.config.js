/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html"
  ],
  theme: {
    extend: {
      
      colors: {
        'primario': '#1E3A8A',
        'primario-hover': '#3061e680',
        'secundario': '#FBBF24',
        'rojo-logo': '#EF4444',
        'verde-claro': '#C6F6D5',
        'amarillo-claro': '#FEF9C3',

        /* --- 🔹 NUEVOS COLORES PARA EL FORMULARIO 🔹 --- */
        'gray-form': '#f5f5f5',      // Fondo de la página
        'blue-accent': '#2f80ed',    // Azul brillante para botones/foco
        'dark-text': '#333333',      // Texto principal
        'light-text': '#666666',     // Texto de etiquetas (labels)
      },

      /* --- 🔹 NUEVA FAMILIA DE FUENTES 🔹 --- */
      fontFamily: {
        sans: ['Nunito', 'sans-serif'], // Fuente principal
      },

      spacing: {
        'md': '1rem', 
        'lg': '2rem'
      },

      borderRadius: {
        'md': '0.5rem',
        /* --- 🔹 NUEVOS BORDES REDONDEADOS 🔹 --- */
        'lg': '1rem',
        'xl': '1.5rem',
        '2xl': '2rem',
      },

      boxShadow: {
        'base': '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
        'media': '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
        /* --- 🔹 NUEVAS SOMBRAS 🔹 --- */
        'input': '0 2px 4px rgba(0,0,0,0.05)',
        'card': '0 4px 12px rgba(0,0,0,0.08)',
      },

      keyframes: {
        'pulse-subtle': {
          '0%, 100%': { transform: 'scale(1)', boxShadow: '0 0 0 0 rgba(251, 191, 36, 0.4)' },
          '50%': { transform: 'scale(1.05)', boxShadow: '0 0 0 10px rgba(251, 191, 36, 0)' }
        },
        'slide-x': {
          '0%, 100%': { transform: 'translateX(0)' },
          '33%': { transform: 'translateX(-100%)' },
          '66%': { transform: 'translateX(-200%)' }
        },
        'slide-x-4': {
          '0%, 100%': { transform: 'translateX(0)' },
          '25%': { transform: 'translateX(-100%)' },
          '50%': { transform: 'translateX(-200%)' },
          '75%': { transform: 'translateX(-300%)' }
        },
        'jiggle': { 
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' }
        }
      },
      
      animation: {
        'pulse-subtle': 'pulse-subtle 2.5s infinite',
        'slide-x': 'slide-x 9s ease-in-out infinite',
        'slide-x-4': 'slide-x-4 12s ease-in-out infinite',
        'jiggle': 'jiggle 0.4s ease-in-out'
      }
    },
  },
  plugins: [],
}