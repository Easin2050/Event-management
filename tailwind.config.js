module.exports = {
  content: [
    "./templates/**/*.html",
    "./**/templates/**/*.html"
  ],
  safelist: [
    {
      pattern: /bg-(red|green|blue|yellow|purple|pink|indigo|gray|stone|amber|teal|cyan|lime|emerald|orange|fuchsia|violet|rose)-(100|200|300|400|500|600|700|800|900)/,
    },
    {
      pattern: /text-(red|green|blue|yellow|purple|pink|indigo|gray|stone|amber|teal|cyan|lime|emerald|orange|fuchsia|violet|rose)-(100|200|300|400|500|600|700|800|900)/,
    },
    {
      pattern: /border-(red|green|blue|yellow|purple|pink|indigo|gray|stone|amber|teal|cyan|lime|emerald|orange|fuchsia|violet|rose)-(100|200|300|400|500|600|700|800|900)/,
    },
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
