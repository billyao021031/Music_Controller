const path = require("path");
const webpack = require("webpack");

module.exports = {
    entry: "./src/index.js",
    output: {
        path:path.resolve(__dirname, "./static/frontend"),
        filename: "[name].js",
    },
    module: {
        rules: [
            {
                test:/\.js$/,
                exclude: /node_modules/,
                use:{
                    loader:"babel-loader"
                },
            },
        ],
    },
    optimization:{
        minimize:true,
    },
    plugins:[
        new webpack.DefinePlugin({
            "process.env":{
                //this has effect on react lib size
                NODE_NEV: JSON.stringify("production"),
            },
        }),
    ],
}