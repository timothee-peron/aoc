import { readFileSync } from "fs";
import { resolve } from "path";
import * as nj from "numjs";

let inputFileName = "sample.txt";
// inputFileName = "input.txt"

const readInputFile = () => {
  const data = readFileSync(resolve(__dirname, inputFileName), "utf-8");
  const lines = data.split(/\r?\n/);
  return lines;
};

const makeInputMap = (lines: Array<String>) => {
  const _map = [];
  for (let line of lines) {
    line.split("");
  }
};

const a = nj.array([
  [0, 1, 2, 3],
  [4, 5, 6, 7],
  [8, 9, 10, 11],
]);
console.log(a.reshape());
