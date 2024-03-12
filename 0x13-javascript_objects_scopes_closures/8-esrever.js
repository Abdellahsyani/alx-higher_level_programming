#!/sur/bin/node

exports.esrever = function (list, searchElement) {
  return list.reduceRight((final, item) => {
    final.push(item);
    return final;
  }, []);
};
