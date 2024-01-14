#!/usr/bin/node

const dict = require('./101-data').dict;

const ret = {};
for (const key in dict) {
  if (!(dict[key] in ret)) {
    ret[dict[key]] = [];
  }
  ret[dict[key]].push(key);
}
console.log(ret);
