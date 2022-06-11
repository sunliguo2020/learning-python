a = function(e) {
for (var t = "",
n = 0; n < e; n++) t += o(16 * Math.random());
return s(t, e)
},
s = function(e, t) {
var n = "";
if (e.length < t) for (var r = 0; r < t - e.length; r++) n += "0";
return n + e
},
o = function(e) {
return Math.ceil(e).toString(16).toUpperCase()
}
function get_uuid() {
var e = a(8),
t = a(4),
n = a(4),
r = a(4),
o = a(12),
i = (new Date).getTime();
return e + "-" + t + "-" + n + "-" + r + "-" + o + s((i % 1e5).toString(), 5) + "infoc"
}