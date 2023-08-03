define((function(){return function(e){var r={};function t(n){if(r[n])return r[n].exports;var o=r[n]={i:n,l:!1,exports:{}};return e[n].call(o.exports,o,o.exports,t),o.l=!0,o.exports}return t.m=e,t.c=r,t.d=function(e,r,n){t.o(e,r)||Object.defineProperty(e,r,{enumerable:!0,get:n})},t.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},t.t=function(e,r){if(1&r&&(e=t(e)),8&r)return e;if(4&r&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(t.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&r&&"string"!=typeof e)for(var o in e)t.d(n,o,function(r){return e[r]}.bind(null,o));return n},t.n=function(e){var r=e&&e.__esModule?function(){return e.default}:function(){return e};return t.d(r,"a",r),r},t.o=function(e,r){return Object.prototype.hasOwnProperty.call(e,r)},t.p="",t(t.s=0)}([function(e,r,t){var n=t(1),o=t(4)(n);t.p=document.querySelector("body").getAttribute("data-base-url")+"nbextensions/arcgis-map-ipywidget";var i;window.require&&(i=n.CdnUrl,new Promise((e,r)=>{fetch(i,{mode:"cors"}).then(t=>{t.status>=200&&t.status<300?t.text().then(r=>{e(r)}).catch(e=>{r(e)}):r("HTTP request on "+i+" returned code "+status)}).catch(e=>{r(e)})})).then(e=>{o.setRequireJSConfig(n.BaseRequireJSConfig),console.log("Initializing esriLoader for quicker load times..."),o.loadModules(["esri/Map","esri/views/MapView","esri/views/SceneView","esri/layers/Layer"],n.EsriLoaderOptions).then(([e,r,t,n])=>{console.log("esriLoader initialization completed successfully!")}).catch(e=>{console.log("esriLoader initialization ran into an error:"),console.log(e)})}).catch(e=>{console.log("Cannot reach "+n.CdnUrl+": Not pre-loading, waiting for user to specify the proper CDN path")}),e.exports={load_ipython_extension:function(){}}},function(e,r,t){var n=t(2),o=t(3),i="/";if(/\/[0-9A-Fa-f]{32}\/notebooks\//.test(location.pathname))try{i=location.pathname.match(/.*\/[0-9A-Fa-f]{32}\/(?=notebooks\/)/)[0]}catch(e){}var a=i+"nbextensions/arcgis/";console.log("nbextension path = "+a),n.JSOutputContext="default",n.JupyterTarget="notebook",n.BaseRequireJSConfig={map:{"*":{"arcgis-map-ipywidget":a+"arcgis-map-ipywidget.js","legacy-mapview":a+"legacy-mapview.js"}},config:{has:{"esri-featurelayer-webgl":1},geotext:{useXhr:function(e){return!0},openXhr:!1,onXhr:function(e,r){var t="undefined"!=typeof XMLHttpRequest&&"withCredentials"in new XMLHttpRequest;e.open("GET",t?r:proxyUrl+"?"+r,!0)}}}},o(n,n.CdnUrl),e.exports=n},function(e,r){var t="https://js.arcgis.com/4.19/",n={CdnUrl:t,CdnMainCssUrl:"https://js.arcgis.com/4.19/esri/css/main.css",EsriLoaderOptions:{url:t,dojoConfig:{has:{"esri-featurelayer-webgl":1}}},minJSAPIVersion:"4.19"};e.exports=n},function(e,r){e.exports=function(e,r){if(e.CdnUrl=r,e.EsriLoaderOptions.url=e.CdnUrl,"notebook"===e.JupyterTarget)e.BaseRequireJSConfig.packages=[{name:"esri",location:e.CdnUrl+"esri"},{name:"dojo",location:e.CdnUrl+"dojo"},{name:"dojox",location:e.CdnUrl+"dojox"},{name:"dijit",location:e.CdnUrl+"dijit"},{name:"dstore",location:e.CdnUrl+"dstore"},{name:"moment",location:e.CdnUrl+"moment"},{name:"@dojo",location:e.CdnUrl+"@dojo"},{name:"cldrjs",location:e.CdnUrl+"cldrjs",main:"dist/cldr"},{name:"globalize",location:e.CdnUrl+"globalize",main:"dist/globalize"},{name:"maquette",location:e.CdnUrl+"maquette",main:"dist/maquette.umd"},{name:"maquette-css-transitions",location:e.CdnUrl+"maquette-css-transitions",main:"dist/maquette-css-transitions.umd"},{name:"maquette-jsx",location:e.CdnUrl+"maquette-jsx",main:"dist/maquette-jsx.umd"},{name:"tslib",location:e.CdnUrl+"tslib",main:"tslib"}],window.require&&(window.customRequire=window.require.config(e.BaseRequireJSConfig));else if("lab"===e.JupyterTarget){var t=document.querySelector("script[data-esri-loader]");null!=t&&t.parentNode.removeChild(t)}}},function(e,r,t){var n=t(5),o=t(6);e.exports=function(e){if(e.JupyterTarget){if("lab"===e.JupyterTarget)return n;if("notebook"===e.JupyterTarget)return o;throw"Misconfigured config file! Failing"}throw"config does not specify 'JupyterTarget'! Failing"}},function(e,r,t){!function(e){"use strict";function r(e){if("next"===e.toLowerCase())return"next";var r=e&&e.match(/^(\d)\.(\d+)/);return r&&{major:parseInt(r[1],10),minor:parseInt(r[2],10)}}function t(e){return void 0===e&&(e="4.17"),"https://js.arcgis.com/"+e+"/"}function n(e){return!e||r(e)?function(e){void 0===e&&(e="4.17");var n=t(e),o=r(e);return"next"!==o&&3===o.major?n+(o.minor<=10?"js/":"")+"esri/css/esri.css":n+"esri/themes/light/main.css"}(e):e}function o(e,r){var t=n(e),o=function(e){return document.querySelector('link[href*="'+e+'"]')}(t);return o||function(e,r){if(r){var t=document.querySelector(r);t.parentNode.insertBefore(e,t)}else document.head.appendChild(e)}(o=function(e){var r=document.createElement("link");return r.rel="stylesheet",r.href=e,r}(t),r),o}var i={Promise:"undefined"!=typeof window?window.Promise:void 0},a={};function s(e,r,t){var n;t&&(n=function(e,r){var t=function(n){r(n.error||new Error("There was an error attempting to load "+e.src)),e.removeEventListener("error",t,!1)};return e.addEventListener("error",t,!1),t}(e,t));var o=function(){r(e),e.removeEventListener("load",o,!1),n&&e.removeEventListener("error",n,!1)};e.addEventListener("load",o,!1)}function u(e){void 0===e&&(e={}),a=e}function d(){return document.querySelector("script[data-esri-loader]")}function c(){var e=window.require;return e&&e.on}function l(e){void 0===e&&(e={});var r={};[a,e].forEach((function(e){for(var t in e)Object.prototype.hasOwnProperty.call(e,t)&&(r[t]=e[t])}));var n=r.version,u=r.url||t(n);return new i.Promise((function(e,t){var i=d();if(i){var a=i.getAttribute("src");a!==u?t(new Error("The ArcGIS API for JavaScript is already loaded ("+a+").")):c()?e(i):s(i,e,t)}else if(c())t(new Error("The ArcGIS API for JavaScript is already loaded."));else{var l=r.css;l&&o(!0===l?n:l,r.insertCssBefore),r.dojoConfig&&(window.dojoConfig=r.dojoConfig),s(i=function(e){var r=document.createElement("script");return r.type="text/javascript",r.src=e,r.setAttribute("data-esri-loader","loading"),r}(u),(function(){i.setAttribute("data-esri-loader","loaded"),e(i)}),t),document.body.appendChild(i)}}))}function f(e){return new i.Promise((function(r,t){var n=window.require.on("error",t);window.require(e,(function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t];n.remove(),r(e)}))}))}function p(e,r){if(void 0===r&&(r={}),c())return f(e);var t=d(),n=t&&t.getAttribute("src");return!r.url&&n&&(r.url=n),l(r).then((function(){return f(e)}))}var m={getScript:d,isLoaded:c,loadModules:p,loadScript:l,loadCss:o,setDefaultOptions:u,utils:i};e.getScript=d,e.isLoaded=c,e.loadModules=p,e.loadScript=l,e.loadCss=o,e.setDefaultOptions=u,e.utils=i,e.default=m,Object.defineProperty(e,"__esModule",{value:!0})}(r)},function(e,r,t){"use strict";r.__esModule=!0,r.setRequireJSConfig=r.loadModules=r.loadScript=r.isLoaded=r.getScript=r.utils=r.loadCss=void 0;function n(e){var r=function(e){return document.querySelector('link[href*="'+e+'"]')}(e);return r||(r=function(e){var r=document.createElement("link");return r.rel="stylesheet",r.href=e,r}(e),document.head.appendChild(r)),r}r.loadCss=n;var o="undefined"!=typeof window;function i(e,r,t){var n;t&&(n=function(e,r){var t=function(n){r(n.error||new Error("There was an error attempting to load "+e.src)),e.removeEventListener("error",t,!1)};return e.addEventListener("error",t,!1),t}(e,t));var o=function(){r(e),e.removeEventListener("load",o,!1),n&&e.removeEventListener("error",n,!1)};e.addEventListener("load",o,!1)}function a(){return document.querySelector("script[data-esri-loader]")}function s(){return window.require&&window.requirejs}function u(e){return void 0===e&&(e={}),e.url||(e.url="https://js.arcgis.com/4.7/"),new r.utils.Promise((function(r,t){var o=a();if(o){var u=o.getAttribute("src");u!==e.url?t(new Error("The ArcGIS API for JavaScript is already loaded ("+u+").")):s()?r(o):i(o,r,t)}else s()?t(new Error("The ArcGIS API for JavaScript is already loaded.")):(e.css&&n(e.css),e.requirejsConfig&&window.require.config(e.requirejsConfig),o=function(e){var r=document.createElement("script");return r.type="text/javascript",r.src=e,r.setAttribute("data-esri-loader","loading"),r}(e.url),e.url,i(o,(function(){o.setAttribute("data-esri-loader","loaded"),r(o)}),t),document.body.appendChild(o))}))}function d(e,t){return void 0===t&&(t={}),function(e){return new r.utils.Promise((function(r,t){null==window.activeRequireFunction?t("esriLoader.setRequireJSConfig() has not been called: You MUST call this function before using esriLoader"):window.activeRequireFunction(["require"],(function(n){n(e,(function(){for(var e=[],t=0;t<arguments.length;t++)e[t]=arguments[t];r(e)}),t)}))}))}(e)}function c(e){console.log("Setting requirejs-esri-loader's config:"),console.log(e),window.activeRequireFunction=window.require.config(e)}r.utils={Promise:o?window.Promise:void 0},r.getScript=a,r.isLoaded=s,r.loadScript=u,r.loadModules=d,r.setRequireJSConfig=c,r.default={setRequireJSConfig:c,getScript:a,isLoaded:s,loadModules:d,loadScript:u,loadCss:n,utils:r.utils}}])}));
//# sourceMappingURL=extension.js.map