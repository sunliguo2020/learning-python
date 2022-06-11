function get_first_t(e) {
return Math.ceil(e).toString(16).toUpperCase()
}

function a() {
var e = 8;
for (var t = "",
n = 0; n < e; n++) t += o(16 * Math.random());
return s(t, e)
}

o = function(e) {
return Math.ceil(e).toString(16).toUpperCase()
}

s = function(e, t) {
var n = "";
if (e.length < t) for (var r = 0; r < t - e.length; r++) n += "0";
return n + e
}

function get_final_t(e) {
var t = get_first_t(e);
result = a();
return "".concat(result, "_").concat(t);
}