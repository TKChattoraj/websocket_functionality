const path = require('path');

module.exports = {
  entry: './chat/assets/asset.js',  // path to our input file
  output: {
    filename: 'asset-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './chat/static/chat'),  // path to our Django static directory
  },
  module: {
    rules: [
        {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: { presets: ["@babel/preset-env", "@babel/preset-react"] }
        },
    ]
    }
};