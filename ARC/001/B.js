function how_many(from, to) {
  var diff = to - from;
  var cnt = 0;
  while (diff != 0) {
    if (diff < 0)  sign = 1;
    else sign = -1;

    d10 =  Math.abs(diff + sign * 10);
    d5 = Math.abs(diff + sign * 5);
    d1 = Math.abs(diff + sign * 1);
    m = Math.min(d10, d5, d1);
    if (m == d10) to += sign * 10;
    else if (m == d5) to += sign * 5;
    else to += sign * 1;
    cnt += 1;
    diff = to - from;
  }
  return cnt;
}

var rl = require('readline');
i = rl.createInterface(process.stdin, process.stdout);
i.on('line', function(line) {
  var ary = line.trim().split(' ').map(function (x) { return parseInt(x) });
  var from = ary[0]
  var to = ary[1]
  console.log(how_many(from, to));
  process.exit(0);
});
