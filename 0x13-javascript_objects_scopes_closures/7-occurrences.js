#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((total, current) => {
    if (searchElement === current) total++;
    return total;
  }, 0);
};
