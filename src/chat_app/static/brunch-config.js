module.exports = {
    files: {
        javascripts: {
            joinTo: 'scripts/main.js'
        },
        stylesheets: {
            joinTo: 'styles/main.css'
        }
    },
    paths: {
        public: 'dist'
    },
    npm: {
        aliases: {
            vue: "vue/dist/vue.js"
        }
    },
    plugins: {
        babel: {
            presets: ['env']
        },
        postcss: {
            processors: [
                require('autoprefixer')(['last 8 versions']),
                require('csswring')()
            ]
        },
        sass: {
            mode: 'native',
            sourceMapEmbed: true,
            includePaths: [
                "node_modules/tachyons-sass/"
            ]
        },
        copycat: {
            "images": ["app/images"],
            // "fonts": ["app/fonts"]
        }
    }
};