#!/usr/bin/node
/* compare two argument */
const all = process.argv.slice(2);

if (all.length < 2) console.log('0');
else {
  let maxi = 0;
  for (const i in all) {
    all[i] = Number(all[i]);
    if (all[i] > all[maxi]) maxi = i;
  }
  all.splice(maxi, 1);
  console.log(Math.max(...all));
}
