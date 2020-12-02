module.exports = {
    title: 'PARCEL B SEASONAL CHANGES',
    plugins: [],
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
  