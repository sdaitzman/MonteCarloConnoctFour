module.exports = {
    title: 'Monte Carlo Tree Search Connect Four',
    plugins: [
      [
        'vuepress-plugin-mathjax',
        {
          target: 'svg',
          macros: {
            '*': '\\times'
          }
        }
      ]
    ],
    markdown: {
      anchor: {
        permalink: false,
        permalinkBefore: true,
        permalinkSymbol: '#'
      },
      extendMarkdown: md => {
        md.use(require('@centerforopenscience/markdown-it-imsize'))
      }
      // lineNumbers: true
    }
  }
  