// Entry point for the notebook bundle containing custom model definitions.
//
// Setup notebook base URL
//
// Some static assets may be required by the custom widget javascript. The base
// url for the notebook is not known at build time and is therefore computed
// dynamically.
var __webpack_public_path__ = document.querySelector("body").getAttribute("data-base-url") + "nbextensions/jupyter-exawidgets/";

// Export widget models and views, and the npm package version number.
var _ = require("underscore");
module.exports = _.extend(
    {},
    require("./base.js"),
    require("./base-three.js"),
    require("./utility.js"),
    require("./app3d.js"),
    require("./field.js"),
    require("./test.js"),
    require("./num.js")
);
module.exports["version"] = require("../package.json").version;
